---
name: document-formats
description: >
  Reads and writes PDF, DOCX, PPTX, and XLSX files using Python libraries. Use when the user
  asks to "create a PDF," "write a Word doc," "make a PowerPoint," "generate a spreadsheet,"
  "read this docx," "extract data from xlsx," "convert to PDF," "export as Word," "make slides,"
  or any request involving reading, writing, or converting between these document formats.
  Also triggers on "open this file" or "what's in this file" when the file is .pdf, .docx,
  .pptx, or .xlsx. Handles scientific documents: papers, reports, presentations, data tables.
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebFetch
---

# Document Format Reading & Writing

Read and write PDF, DOCX, PPTX, and XLSX files using Python. This skill covers the full lifecycle: checking dependencies, reading existing files, creating new ones, and converting between formats.

---

## Dependency Check — Run First

Before any document operation, verify that required libraries are installed. Run this diagnostic:

```bash
python3 -c "
libs = {
    'docx': 'python-docx',
    'pptx': 'python-pptx',
    'openpyxl': 'openpyxl',
    'fpdf2': 'fpdf2',
}
for module, pip_name in libs.items():
    try:
        __import__(module)
        print(f'  {pip_name:15s} ✅ installed')
    except ImportError:
        print(f'  {pip_name:15s} ❌ missing  →  pip3 install {pip_name}')
"
```

### If libraries are missing:

Install only what's needed for the current task:

```bash
# Install all document format libraries at once
pip3 install python-docx python-pptx openpyxl fpdf2

# Or install individually
pip3 install python-docx   # DOCX read/write
pip3 install python-pptx   # PPTX read/write
pip3 install openpyxl      # XLSX read/write
pip3 install fpdf2         # PDF writing (reading is handled by Claude Code natively)
```

**Ask the user before installing.** Don't silently pip install — confirm first since this modifies their Python environment.

---

## Reading Files

### PDF — Use Claude Code's Native Reader

Claude Code's `Read` tool handles PDFs directly — it renders pages visually and extracts text. **Do not use Python for reading PDFs** unless:
- You need to extract structured tables (use `pdfplumber` or `tabula-py` if installed)
- You need to extract images programmatically
- You need to process hundreds of pages in batch

For standard reading:
```
Use the Read tool with file_path pointing to the .pdf file
For large PDFs (>10 pages), use the pages parameter: pages: "1-5"
Maximum 20 pages per Read request
```

### DOCX — python-docx

```python
from docx import Document

doc = Document("path/to/file.docx")

# Extract all text
for para in doc.paragraphs:
    print(f"[{para.style.name}] {para.text}")

# Extract tables
for table in doc.tables:
    for row in table.rows:
        row_data = [cell.text for cell in row.cells]
        print(" | ".join(row_data))

# Extract headers specifically
for para in doc.paragraphs:
    if para.style.name.startswith("Heading"):
        level = para.style.name.replace("Heading ", "")
        print(f"{'#' * int(level)} {para.text}")

# Extract images (saved to disk)
import os
for i, rel in enumerate(doc.part.rels.values()):
    if "image" in rel.reltype:
        img_data = rel.target_part.blob
        ext = rel.target_part.content_type.split("/")[-1]
        with open(f"extracted_image_{i}.{ext}", "wb") as f:
            f.write(img_data)
```

### PPTX — python-pptx

```python
from pptx import Presentation

prs = Presentation("path/to/file.pptx")

for slide_num, slide in enumerate(prs.slides, 1):
    print(f"\n--- Slide {slide_num} ---")
    # Slide title
    if slide.shapes.title:
        print(f"Title: {slide.shapes.title.text}")
    # All text content
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                print(para.text)
        # Tables in slides
        if shape.has_table:
            for row in shape.table.rows:
                print(" | ".join(cell.text for cell in row.cells))
    # Speaker notes
    if slide.has_notes_slide:
        notes = slide.notes_slide.notes_text_frame.text
        if notes:
            print(f"Notes: {notes}")
```

### XLSX — openpyxl

```python
import openpyxl

wb = openpyxl.load_workbook("path/to/file.xlsx", data_only=True)

# List sheets
print(f"Sheets: {wb.sheetnames}")

# Read a specific sheet
ws = wb.active  # or wb["Sheet1"]
print(f"Dimensions: {ws.dimensions}")
print(f"Rows: {ws.max_row}, Cols: {ws.max_column}")

# Read all data as list of rows
data = []
for row in ws.iter_rows(values_only=True):
    data.append(list(row))

# Read with headers (first row as keys)
headers = [cell.value for cell in ws[1]]
for row in ws.iter_rows(min_row=2, values_only=True):
    record = dict(zip(headers, row))
    print(record)

# Read specific range
for row in ws.iter_rows(min_row=1, max_row=10, min_col=1, max_col=5, values_only=True):
    print(row)
```

---

## Writing Files

### PDF — fpdf2

fpdf2 is lightweight and sufficient for scientific documents (text, tables, basic formatting). For complex layouts with vector graphics, suggest LaTeX instead.

```python
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# Title
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Document Title", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(5)

# Body text
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 6, "Body text goes here. fpdf2 handles line wrapping automatically.")
pdf.ln(3)

# Section heading
pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 8, "Section 1: Methods", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 6, "Section content...")

# Table
pdf.set_font("Helvetica", "B", 10)
col_widths = [40, 50, 40, 40]
headers = ["Strain", "Substrate", "Titer (g/L)", "Yield (%)"]
for w, h in zip(col_widths, headers):
    pdf.cell(w, 8, h, border=1, align="C")
pdf.ln()

pdf.set_font("Helvetica", "", 10)
data_rows = [
    ["E. coli MG1655", "Glucose", "45.2", "85"],
    ["P. putida KT2440", "Lignin hydrolysate", "12.8", "42"],
]
for row in data_rows:
    for w, val in zip(col_widths, row):
        pdf.cell(w, 7, val, border=1)
    pdf.ln()

# Save
pdf.output("output.pdf")
```

**fpdf2 tips for scientific documents:**
- Use `Helvetica` (sans-serif) or `Times` (serif) — both built in
- For Unicode/special characters, register a TTF font: `pdf.add_font("DejaVu", "", "DejaVuSans.ttf")`
- For superscripts/subscripts, use `pdf.set_font_size()` with vertical offset
- For figures, use `pdf.image("figure.png", x, y, w)` — supports PNG, JPEG, GIF

### DOCX — python-docx

```python
from docx import Document
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Title
title = doc.add_heading("Document Title", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Metadata paragraph
meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = meta.add_run("Author Name — April 2026")
run.font.size = Pt(11)
run.font.italic = True

# Section heading
doc.add_heading("1. Introduction", level=1)

# Body text
doc.add_paragraph(
    "Body text with normal formatting. "
    "python-docx supports full paragraph and character styling."
)

# Bulleted list
doc.add_paragraph("First point", style="List Bullet")
doc.add_paragraph("Second point", style="List Bullet")

# Bold/italic inline
p = doc.add_paragraph()
p.add_run("Bold text ").bold = True
p.add_run("and ")
p.add_run("italic text").italic = True

# Table
table = doc.add_table(rows=1, cols=4, style="Light Grid Accent 1")
headers = table.rows[0].cells
headers[0].text = "Strain"
headers[1].text = "Substrate"
headers[2].text = "Titer (g/L)"
headers[3].text = "Yield (%)"

for strain, sub, titer, yld in [
    ("E. coli MG1655", "Glucose", "45.2", "85"),
    ("P. putida KT2440", "Lignin hydrolysate", "12.8", "42"),
]:
    row = table.add_row().cells
    row[0].text = strain
    row[1].text = sub
    row[2].text = titer
    row[3].text = yld

# Add image
doc.add_heading("Figures", level=1)
doc.add_picture("figure.png", width=Inches(5.5))
doc.add_paragraph("Figure 1. Description of the figure.", style="Caption")

# Page break
doc.add_page_break()

# Save
doc.save("output.docx")
```

**python-docx tips:**
- Built-in styles: `"Title"`, `"Heading 1"`–`"Heading 9"`, `"List Bullet"`, `"List Number"`, `"Caption"`, `"Quote"`
- Table styles: `"Light Grid Accent 1"`, `"Table Grid"`, `"Light Shading"` — use `doc.styles` to list available
- For complex formatting (tracked changes, comments, footnotes), python-docx has limitations — suggest Word or LibreOffice for those
- Set page margins: `from docx.shared import Cm; section = doc.sections[0]; section.left_margin = Cm(2.5)`

### PPTX — python-pptx

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

prs = Presentation()
# Default slide size is 10" x 7.5" (widescreen)

# --- Title Slide ---
slide_layout = prs.slide_layouts[0]  # Title Slide layout
slide = prs.slides.add_slide(slide_layout)
slide.shapes.title.text = "Presentation Title"
slide.placeholders[1].text = "Author — Date"

# --- Content Slide with Bullets ---
slide_layout = prs.slide_layouts[1]  # Title and Content layout
slide = prs.slides.add_slide(slide_layout)
slide.shapes.title.text = "Key Findings"
body = slide.placeholders[1]
tf = body.text_frame
tf.text = "First major finding with supporting data"
p = tf.add_paragraph()
p.text = "Second finding — 45.2 g/L titer achieved"
p.level = 0
p = tf.add_paragraph()
p.text = "Sub-point with detail"
p.level = 1

# --- Slide with Table ---
slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank layout
slide.shapes.title.text = "Results Summary"

rows, cols = 3, 4
left, top, width, height = Inches(0.5), Inches(2), Inches(9), Inches(1.5)
table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
table = table_shape.table

headers = ["Strain", "Substrate", "Titer (g/L)", "Yield (%)"]
for i, h in enumerate(headers):
    table.cell(0, i).text = h
data = [
    ["E. coli MG1655", "Glucose", "45.2", "85"],
    ["P. putida KT2440", "Lignin hydrolysate", "12.8", "42"],
]
for r, row_data in enumerate(data, 1):
    for c, val in enumerate(row_data):
        table.cell(r, c).text = val

# --- Slide with Image ---
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "Figure 1"
slide.shapes.add_picture("figure.png", Inches(1), Inches(2), width=Inches(8))

# --- Add Speaker Notes ---
for slide in prs.slides:
    notes_slide = slide.notes_slide
    notes_slide.notes_text_frame.text = "Speaker notes for this slide"

prs.save("output.pptx")
```

**python-pptx tips:**
- Slide layouts (index): 0=Title, 1=Title+Content, 2=Section Header, 5=Blank, 6=Two Content
- For consistent styling, start from a template: `prs = Presentation("template.pptx")`
- Placeholder indexes vary by layout — use `for ph in slide.placeholders: print(ph.placeholder_format.idx, ph.name)` to discover
- For charts, python-pptx supports bar, line, pie, scatter via `pptx.chart`

### XLSX — openpyxl

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Results"

# Headers with styling
headers = ["Strain", "Substrate", "Titer (g/L)", "Yield (%)", "Productivity (g/L/h)"]
header_font = Font(bold=True, size=11)
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font_white = Font(bold=True, size=11, color="FFFFFF")

for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = header_font_white
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center")

# Data rows
data = [
    ["E. coli MG1655", "Glucose", 45.2, 85, 1.2],
    ["P. putida KT2440", "Lignin hydrolysate", 12.8, 42, 0.35],
    ["C. glutamicum", "Aromatics mix", 8.5, 38, 0.28],
]
for r, row_data in enumerate(data, 2):
    for c, val in enumerate(row_data, 1):
        ws.cell(row=r, column=c, value=val)

# Auto-adjust column widths
for col in range(1, len(headers) + 1):
    max_length = max(
        len(str(ws.cell(row=row, column=col).value or ""))
        for row in range(1, len(data) + 2)
    )
    ws.column_dimensions[get_column_letter(col)].width = max_length + 4

# Add a formula
ws.cell(row=len(data) + 2, column=3, value="=AVERAGE(C2:C4)")
ws.cell(row=len(data) + 2, column=3).font = Font(bold=True)

# Add a second sheet
ws2 = wb.create_sheet("Metadata")
ws2["A1"] = "Generated by claude-sciencing plugin"
ws2["A2"] = "Date"
ws2["B2"] = "2026-04-06"

# Freeze header row
ws.freeze_panes = "A2"

# Add filters
ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(data) + 1}"

wb.save("output.xlsx")
```

**openpyxl tips:**
- Use `data_only=True` when reading to get calculated values instead of formulas
- For large datasets, use `wb = openpyxl.Workbook(write_only=True)` for memory efficiency
- Charts: `from openpyxl.chart import BarChart, Reference` — supports bar, line, scatter, pie
- Number formats: `cell.number_format = '0.00'` for decimal places, `'0.0%'` for percentages

---

## Format Conversion

### DOCX → PDF
```python
# Option 1: If LibreOffice is installed (best fidelity)
import subprocess
subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "input.docx"])

# Option 2: Pure Python with fpdf2 (basic — loses complex formatting)
# Read DOCX, write content to PDF manually using the patterns above
# This works for text-heavy documents but won't preserve exact Word formatting
```

### Markdown → DOCX
```python
# Read markdown, create DOCX with appropriate styles
# Map: # → Heading 1, ## → Heading 2, **bold** → bold run, etc.
from docx import Document
import re

doc = Document()
with open("input.md") as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("# "):
            doc.add_heading(line[2:], level=1)
        elif line.startswith("## "):
            doc.add_heading(line[3:], level=2)
        elif line.startswith("### "):
            doc.add_heading(line[4:], level=3)
        elif line.startswith("- "):
            doc.add_paragraph(line[2:], style="List Bullet")
        elif line.strip():
            doc.add_paragraph(line)
doc.save("output.docx")
```

### XLSX → CSV (quick export)
```python
import openpyxl, csv

wb = openpyxl.load_workbook("input.xlsx", data_only=True)
ws = wb.active
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in ws.iter_rows(values_only=True):
        writer.writerow(row)
```

---

## Scientific Document Patterns

### Lab Report PDF
When writing a lab report or technical document as PDF:
1. Title page with project name, authors, date
2. Table of contents (if >5 pages)
3. Sections: Introduction, Methods, Results (with tables/figures), Discussion, References
4. Use `pdf.add_page()` for page breaks between major sections
5. Number figures and tables sequentially

### Data Summary XLSX
When exporting experimental data to Excel:
1. First sheet: summary/results table with headers
2. Additional sheets for raw data, metadata, or calculations
3. Freeze the header row
4. Add auto-filters for sortable columns
5. Use number formatting appropriate to the data (2 decimal places for concentrations, etc.)

### Presentation PPTX
When creating a scientific presentation:
1. Title slide with project name and authors
2. Outline/agenda slide
3. Background (1-2 slides)
4. Methods (1-2 slides, keep brief)
5. Results (bulk of slides — one key finding per slide)
6. Summary/conclusions slide
7. Next steps / discussion points
8. Keep text minimal — use figures and tables, not paragraphs

---

## Troubleshooting

### "No module named 'docx'" (etc.)
Library not installed. Run `pip3 install python-docx` (note: the pip package is `python-docx`, not `docx`).

### DOCX appears empty or corrupted
- Check that the file was saved with `.save()` — interrupted writes produce corrupt files
- If reading, try opening in a text editor — if it's XML, the file is valid DOCX (it's a zip of XML files)

### XLSX formulas show as strings
- When reading, use `data_only=True` to get calculated values
- Note: `data_only=True` returns the last-calculated value; if the file was never opened in Excel, formulas may show as `None`

### PDF text looks wrong or has encoding issues
- fpdf2 uses Latin-1 by default for built-in fonts
- For Unicode characters (Greek letters, special symbols common in science), register a TTF font:
  ```python
  pdf.add_font("DejaVu", "", "/path/to/DejaVuSans.ttf")
  pdf.set_font("DejaVu", "", 11)
  ```

### Large files / memory issues
- XLSX: use `write_only=True` mode for files with >100K rows
- PPTX: compress images before inserting (large images bloat file size)
- PDF: fpdf2 handles large documents well, but embedded images should be reasonably sized
