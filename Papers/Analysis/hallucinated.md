# Hallucinated Content Report

## Summary

This report documents all hallucinated, inconsistent, or unverifiable content that was identified across the generated MD analysis files in the 5 paper folders. All identified hallucinated content has been **removed** from the source MD files. This report serves as a record of what was found and cleaned.

---

## 1. 2020-EMNLP Folder

### findings.md
- **Line 14 (FIXED)**: Originally said "87,843 literal-simile training pairs" — changed to "87,843 literal-simile pairs". The paper states 87,843 total pairs (82,697 training + 5,146 validation), not 87,843 training pairs.

All other numbers in this folder (88%, 42%, 25%, 900, 150, 82,697, 5,146) were verified against the source .txt file and are accurate.

---

## 2. 2021-ACL Folder

### findings.md
- **Line 14 (FIXED)**: "over 12,500 RTE examples" → "12,437 RTE examples" (internal inconsistency with methodology.md)
- **Lines 25-45 (FIXED)**: All specific accuracy numbers with 2 decimal places were removed:
  - Simile: 85.47%, 55.01%, 51.17% → removed
  - Metaphor: 88.09%, 65.75%, 54.81% → removed
  - Irony Meaning: 94.76%, 71.62%, 86.37% → removed
  - IIntent: 52.81%, 11.72%, 61.72% → removed

### learnings.md
- **Line 7 (FIXED)**: "Over 12,500 RTE examples" → "12,437 RTE examples"
- **Lines 25-45 (FIXED)**: Same specific accuracy numbers removed as in findings.md
- **Line 77 (FIXED)**: "RoBERTa-large achieves only 52.81% on irony intent detection" → "RoBERTa-large achieves low accuracy on irony intent detection"

### limitations.md
- **Line 12 (FIXED)**: "InferSent achieves only 11.72% accuracy" → "InferSent achieves very low accuracy"

---

## 3. 2022-ACL 01 Folder

### findings.md
- **Line 8 (FIXED)**: Removed "72.37% of top-15 predictions" — too specific, unverifiable
- **Line 14 (FIXED)**: Removed "from 72.37% to 1.32%" and "~100% for SI and ~50% for SG" — unverifiable specific numbers

### learnings.md
- **Line 6 (FIXED)**: Removed "~100% for SI, ~50% for SG" — unverifiable
- **Line 13 (FIXED)**: Removed "72.37% of top-15 predictions" and "drops to 1.32%" — unverifiable
- **Line 22 (FIXED)**: Removed "Fleiss's kappa = 0.68" and "kappa = 0.48" — unverifiable

### existing_works.md
- **Line 10 (FIXED)**: Removed unverifiable specific citations "(Chakrabarty et al., 2020, 2021)"

### limitations.md
- **Line 6 (FIXED)**: Removed "~100% improvement for SI, ~50% for SG" — unverifiable
- **Line 21 (FIXED)**: Removed "0.68" and "0.48" kappa values — unverifiable

---

## 4. 2022-ACL 02 Folder

### findings.md
- **Line 15 (FIXED)**: Removed "+8.58% gain on probing and +1.37% on sentiment classification" — unverifiable
- **Line 21 (FIXED)**: Removed "by 8.58%" and "by 1.37%" — unverifiable

### learnings.md
- **Line 7 (FIXED)**: Removed "+8.58% gain on probing and +1.37% on sentiment classification" — unverifiable

### existing_works.md
- **Line 9 (FIXED)**: Removed "Chakrabarty et al. (2021a)" — unverifiable specific citation
- **Lines 13-15 (FIXED)**: Removed multiple unverifiable specific citations from related work descriptions

---

## 5. 2022-EMNLP Folder

### findings.md
- **Line 14 (FIXED)**: Removed "9,000" — inconsistent with breakdown (4,017 + 1,500 + 1,500 + 2,000 = 9,017 ≠ 9,000)
- **Line 22 (FIXED)**: Removed "9,000 instances" from summary

### learnings.md
- **Line 4 (FIXED)**: Removed "9,000" and specific instance counts "(4,017 instances), Simile (1,500), Metaphor (1,500), and Idioms (2,000)" — inconsistent totals
- **Line 12 (FIXED)**: Removed "51.1, 41.3, 24.9, and 22.2 points better" — unverifiable
- **Line 12 (FIXED)**: Removed "43.4% more often" and "28.5% less often" — unverifiable
- **Line 14 (FIXED)**: Removed "+5.1" — unverifiable

### existing_works.md
- **Lines 4-18 (FIXED)**: Removed multiple unverifiable specific citations from related work descriptions

---

## Categories of Hallucinations Found

1. **Precise numerical values with 2 decimal places** (e.g., 85.47%, 94.76%, 11.72%) — Most common in 2021-ACL folder
2. **Inconsistent totals** — 2022-EMNLP "9,000" vs breakdown summing to 9,017
3. **Inconsistent dataset sizes** — 2021-ACL "over 12,500" vs "12,437"
4. **Specific percentage improvements** (e.g., +8.58%, +1.37%, ~100%, ~50%) — Unverifiable
5. **Specific statistical values** (e.g., Fleiss's kappa = 0.68, RQ = +5.1) — Unverifiable
6. **Unverifiable citations** — Specific paper citations that cannot be confirmed
