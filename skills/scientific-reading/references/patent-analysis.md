# Patent Analysis

Patents are legal documents wrapped in technical language. Reading them requires different skills than reading papers — you're extracting legal scope, not scientific insight.

## Patent Anatomy

Understanding the structure is essential because different sections serve fundamentally different purposes:

### Title and Abstract
- Often broad and vague — don't rely on these for understanding scope
- Useful only for initial triage

### Specification (Description)
- The aspirational part — describes everything the inventors could imagine
- Includes embodiments that may never have been reduced to practice
- "In some embodiments..." does not mean "we actually did this"
- Read for technical context, NOT for understanding what the patent actually protects

### Claims
- **This is what the patent actually protects.** Everything else is context.
- Independent claims define the broadest scope of protection
- Dependent claims narrow the scope with additional limitations
- A patent is only infringed if ALL elements of at least one claim are met

### Examples
- The most reliable technical content in a patent
- Actual experimental data (though sometimes prophetic — predicted, not performed)
- "Prophetic examples" are described in present tense; actual examples use past tense
- In biotech, check whether the examples use real or model substrates

### Figures
- Process flow diagrams, experimental schematics, data plots
- Often the fastest way to understand what was actually done

---

## Claims Analysis Protocol

This is the core of patent reading. The claims define what matters.

### Step 1: Find the Independent Claims
Claims that don't reference other claims. Typically Claim 1 (method), sometimes also a composition claim and a system/apparatus claim.

### Step 2: Parse Each Independent Claim Element by Element

Break the claim into its constituent elements and assess each:

**Example claim:**
> "A method for producing 1,3-propanediol comprising:
> (a) contacting a carbon source with a recombinant microorganism of the genus Escherichia;
> (b) wherein the microorganism comprises a heterologous dhaB gene cluster encoding glycerol dehydratase;
> (c) culturing under anaerobic or microaerobic conditions; and
> (d) recovering 1,3-propanediol from the culture medium."

**Element analysis:**

| Element | Scope | Notes |
|---------|-------|-------|
| "a carbon source" | Broad — covers glucose, glycerol, corn syrup, etc. | Not limited to specific substrates |
| "genus Escherichia" | Covers all species in genus | Not limited to K-12 or BL21 |
| "heterologous dhaB gene cluster" | Any source of dhaB — Klebsiella, Clostridium, etc. | Broadly worded |
| "anaerobic or microaerobic" | Standard fermentation modes | Not limiting |
| "recovering 1,3-propanediol" | Any recovery method | Not limiting |

### Step 3: Assess the Narrowest Independent Claim
This is the claim with the broadest scope that's still valid. It defines the practical scope of protection — what you actually need to design around.

### Step 4: Map Dependent Claims
Dependent claims add limitations. They're fallback positions if the independent claim is invalidated:
- "The method of Claim 1 wherein the microorganism is E. coli MG1655"
- "The method of Claim 1 wherein the carbon source comprises glucose and glycerol"

### Step 5: Identify Design-Around Opportunities
For FTO analysis, identify what elements could be changed to avoid infringement:
- Different genus? (e.g., Klebsiella instead of Escherichia)
- Different gene? (e.g., pduCDE instead of dhaB)
- Different product? (e.g., 1,2-propanediol instead of 1,3-propanediol)

---

## Freedom-to-Operate (FTO) Assessment Support

FTO is ultimately a legal determination, but technical input is critical.

### What You Can Provide (Technical)
1. **Relevant patent landscape** — list of patents/applications that might be relevant
2. **Claims mapping** — element-by-element comparison of your process to each patent's claims
3. **Design-around analysis** — technical alternatives that avoid specific claim elements
4. **Prior art identification** — published work that predates the patent and could invalidate claims
5. **Technical opinion on claim validity** — are the claims enabled? Are the examples reproducible?

### What IP Counsel Provides (Legal)
- Legal interpretation of claim scope
- Doctrine of equivalents analysis
- Formal FTO opinion
- Risk assessment and mitigation strategy

### Presenting FTO Analysis

For each relevant patent, create a structured comparison:

```
Patent: US 11,XXX,XXX (Inventor, Year)
Title: [Patent title]
Assignee: [Company/university]
Status: Granted / Pending / Expired

Relevant claims: 1, 3, 7

Element-by-element comparison:
| Claim Element | Our Process | Match? | Notes |
|--------------|-------------|--------|-------|
| [Element 1]  | [What we do] | Yes/No/Partial | [Explanation] |
| [Element 2]  | [What we do] | Yes/No/Partial | [Explanation] |

Risk assessment: High / Medium / Low
Design-around options: [If applicable]
```

---

## Patent Search Strategy

### Where to Search
- **Google Patents** — broadest, easiest to search, full text
- **USPTO PAIR/PatFT** — US patents and applications, prosecution history
- **Espacenet** — European patents, global coverage
- **WIPO PatentScope** — PCT applications
- **Lens.org** — links patents to scholarly citations (powerful for biotech)

### Search Approaches

**Keyword search:** Start broad, then narrow
- "propanediol AND fermentation AND recombinant"
- "succinic acid AND engineered AND microorganism"

**Classification search:** More precise than keywords
- CPC codes for biotech: C12P (fermentation processes), C12N (microorganisms), C07C (organic chemistry)
- For bioplastics: C08G (polyesters), C08L (polymer compositions)

**Citation search:** Find patents that cite or are cited by a known relevant patent

**Inventor/assignee search:** Track specific competitors
- Search by inventor name for academic groups
- Search by assignee for companies

### Patent vs. Patent Application
- Published applications (US 20XX/XXXXXXX) may never grant — claims often change dramatically during prosecution
- Granted patents (US XX,XXX,XXX) have enforceable claims
- Check prosecution history (PAIR) to see what was argued during examination — this limits claim interpretation

---

## Biotech-Specific Patent Considerations

### Genus vs. Species Claims
Biotech patents often claim a genus (e.g., "a microorganism of the family Enterobacteriaceae") but only demonstrate a single species. Broad genus claims may be vulnerable to invalidation if enablement is insufficient.

### Sequence-Based Claims
- Claims to specific DNA/protein sequences are narrow but strong
- Claims to "sequences with ≥80% identity" are broader but may not be enabled
- Check whether the actual sequence listing covers what you'd use

### Process vs. Composition Claims
- Process claims protect the method (how you make something)
- Composition claims protect the thing itself (the engineered organism, the catalyst)
- Composition claims are generally stronger — they cover the product regardless of how it's made

### Provisional Applications
- Establish a priority date but don't grant rights
- The actual claims may change completely in the non-provisional
- Treat as signals of intent, not actual scope of protection
