# Quality Control

QC checklists and acceptance criteria for common biotech lab processes.

## QC Checkpoints

### Post-Cloning QC
| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Insert present | Colony PCR or restriction digest | Correct band size (±5%) |
| Correct sequence | Sanger sequencing (full insert + junctions) | 100% match to design |
| No unintended mutations | Full plasmid sequencing (for critical constructs) | No off-target mutations |
| Plasmid integrity | Miniprep + restriction digest or Nanodrop | A260/280 = 1.8-2.0; expected fragment pattern |
| Copy number / stability | Re-streak from freezer; miniprep after 50 generations | Stable restriction pattern |

### Post-Expression QC
| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Expression confirmed | SDS-PAGE (Coomassie or anti-His Western) | Visible band at expected MW |
| Solubility | Fractionate: pellet vs. supernatant, SDS-PAGE | ≥50% in supernatant (or per project spec) |
| Identity | Western blot or intact mass spec | Correct MW ± post-translational modifications |
| Yield estimate | Bradford/BCA assay + densitometry | Meets project target (e.g., ≥10 mg/L) |

### Post-IMAC (His-tag Purification) QC
| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Purity | SDS-PAGE (Coomassie stain) | ≥90% single band (or per project spec) |
| Identity | Anti-His Western blot or mass spec | Correct target protein |
| Concentration | A280 (using ε from sequence) or Bradford | Within expected range |
| Monodispersity | SEC (analytical) or DLS | Single peak, no aggregates >10% |
| Activity | Functional assay (enzyme activity, binding, etc.) | Meets minimum specific activity |
| Endotoxin (if needed) | LAL assay | <1 EU/mg for in vivo use |
| Purity (for structural) | SEC-MALS, native PAGE | Monodisperse, correct oligomeric state |

### Post-IEX / SEC Polish QC
| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Purity | SDS-PAGE + SEC chromatogram | ≥95% main peak |
| Aggregation | SEC or DLS | Monomer ≥90% |
| Activity retention | Activity assay vs. pre-polish | ≥80% recovery |
| Concentration | A280 or BCA | Sufficient for downstream use |
| Buffer composition | Verify pH, salt, additives | Matches downstream requirements |

### Fermentation QC
| Timepoint | Check | Method |
|-----------|-------|--------|
| Pre-inoculation | Media sterility | Incubate sample 24 h |
| Pre-inoculation | pH, temperature, DO calibration | Probe readings vs. standards |
| Inoculation | Starting OD600, viability | Spectrophotometer, plating |
| Mid-exponential | Growth rate, plasmid retention | OD, selective vs. non-selective plating |
| Post-induction | Expression confirmed | SDS-PAGE of small sample |
| Harvest | Final OD, titer, pH, product concentration | Multiple analytical methods |
| Post-harvest | Sterility | Streak on non-selective plates |

### DNA / RNA QC
| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Concentration | Qubit (DNA/RNA specific) | Meets downstream requirement |
| Purity (protein) | Nanodrop A260/280 | DNA: 1.8-2.0; RNA: 2.0-2.2 |
| Purity (organic) | Nanodrop A260/230 | ≥2.0 |
| Integrity | Agarose gel (DNA) or Bioanalyzer (RNA) | Sharp bands; RNA: RIN ≥ 7 |
| Size | Gel electrophoresis or Bioanalyzer | Expected size ± 5% |

## QC Documentation

For each QC check, record:
1. **Date and operator**
2. **Sample ID** (traceable to source)
3. **Method** (instrument, settings, reference to SOP)
4. **Raw data** (gel image, chromatogram, spectrum)
5. **Result** (quantitative value with units)
6. **Pass/Fail** against acceptance criteria
7. **Action taken** if fail (re-purify, re-express, discard)
8. **Sign-off** (analyst + reviewer for GLP/GMP)
