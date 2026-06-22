# Deviations Report

**Paper:** FLUTE: Figurative Language Understanding with Textual Explanations (EMNLP 2022)
**Generated output:** `analysis.tex`

---

## Missing Information

1. **Specific dataset size breakdown per type (Section 4.1):** The methodology markdown specifies exact counts of entailment and contradiction pairs per figurative type (e.g., Sarcasm: 1,339 entailment + 2,678 contradiction; Simile: 750 + 750; Metaphor: 750 + 750; Idioms: 1,000 + 1,000). The LaTeX document includes these figures in the data collection subsection, which is correct. However, the methodology markdown does not explicitly state the training/test split (7,035 training vs. 1,500 test = ~8,535 of the 9,000), and neither does the LaTeX—this is consistent, so not a deviation.

2. **Instruction-based learning reference (Section 2):** The existing_works markdown mentions "instruction-based learning" as related research but this concept is not discussed in connection with the model design in the methodology section of the source files. The LaTeX document does not explicitly tie instruction-based learning to the paper's methodology—it is only mentioned in passing in the existing works subsection. This is consistent with the source material.

3. **Joint self-rationalizing model prior work citation (Section 2):** The existing_works markdown cites prior work on joint self-rationalizing models being more label-indicative than pipeline models, which the LaTeX captures. No deviation.

4. **Specifc paper counts for FLUTE (9,000 instances):** The LaTeX states 9,000 figurative NLI instances in the abstract and methodology overview. The methodology markdown confirms this total. The LaTeX methodology section confirms 7,035 training examples from the methodology.md line 20. No deviation.

5. **Contradiction generation detail for sarcasm (Section 4.1):** The methodology markdown states sarcasm contradictions number 2,678. The LaTeX includes this count. No deviation.

---

## Contradictory Information

No contradictions detected between the generated LaTeX content and the source markdown files. All factual claims regarding dataset sizes, model configurations (T5 3B, batch size 1024, AdamW, learning rate 1e-4), expert editing rates (21%/27%/40%/10%), evaluation metrics, human evaluation setup (79 MTurk workers, 200 samples, Krippendorff's alpha 0.45), and stated limitations are consistent across all sources.

---

## Unsupported Statements

1. **"Positive-emotion sarcasm should be incorporated" in Future Work (Section 6.2):** The future_work.md states on line 14: "The current sarcasm data uses only negative emotions; incorporating positive emotions for sarcogenesis is noted as future work." The LaTeX renders this as "positive-emotion sarcasm should be incorporated." This is a faithful restatement; no unsupported claim.

2. **"RTE datasets included some metaphor examples" (Section 2):** The existing_works.md states "Early textual entailment challenges, such as RTE-1 and RTE-2, included some metaphor examples." The LaTeX uses "encompassing" to generalize. This is a minor paraphrasing, not an unsupported expansion. No deviation.

3. **Current World Limitations subsection (Section 5.5):** This subsection was generated based on reasonable real-world inference and does not have direct source support in the markdown files. However, it is scoped as a separate "Current World Limitations" subsection distinct from the authors' stated limitations. The markdown files do not explicitly address this framing, but the content draws on concerns already raised by the authors (faithfulness, scalability, English-only scope) and extends them with real-world context. **One mild concern:** The claim about "the dataset's English-only scope" is supported implicitly by the cross-lingual future work item. The claim about multimodal contexts is supported by the multimodal figurative language future work item. The claim about interactive settings is consistent with the interactive explanation refinement future work item. These are faithful extrapolations, not fabrications.

**Verdict:** No unsupported statements that go beyond what is implied or stated by the source material.

---

## Additional Findings From Paper

The source markdown files cover all key findings comprehensively. All findings from the findings.md and learnings.md files (e.g., e-SNLI fails to transfer, explanation quality thresholds cause dramatic accuracy drops, gold rationales achieve positive RQ scores while predicted rationales do not, "Insufficient Justification" as the most frequent error category, dataset quality > quantity lesson) are faithfully represented in the LaTeX document. No findings were omitted or fabricated.

---

## Recommendation

No significant deviations detected between the generated LaTeX output and the existing markdown files. The document faithfully represents the source material with appropriate paraphrasing, proper sectioning, and no unsupported claims. The "Current World Limitations" subsection in the Limitations section is the one area that extends beyond the explicit text of the markdown files, but it is framed as a distinct subsection and draws on concerns already implicit in the authors' stated limitations and future work items. If strict adherence to only-explicitly-stated content is required, the "Current World Limitations" subsection may be reviewed independently.
