# Deviations Report

## Missing Information

- The LaTeX document does not include the exact inter-annotator agreement values (Krippendorff's alpha) reported in Table 8 of the paper. These are mentioned in the methodology markdown but omitted from the LaTeX evaluation section.
- The LaTeX does not reproduce the specific Pearson correlation values (0.54, 0.52, 0.31) between OQ and other metrics mentioned in the paper's Section 4.2.
- The paper's finding that BLEU-1 and BLEU-2 between the two literary experts are 4.12 and 0.52 respectively is not included in the LaTeX document.
- The exact number of Turkers per evaluation task (86, 48, 42, 46) from Table 8 is not mentioned in the LaTeX document.

## Contradictory Information

- No contradictions detected between the LaTeX document and the markdown source files.

## Unsupported Statements

- The LaTeX document states "41% of test properties are unseen during training." This is supported by the paper's Section 4.1 and is factually consistent.
- The LaTeX document states the model "wins against two literary experts on Overall Quality 32.6% and 41.3% of the time." These figures are correctly attributed from Table 4 of the paper.
- All quantitative claims in the LaTeX are directly traceable to the paper or the markdown analysis files.

## Additional Findings From Paper

- The paper's Appendix A.2 discusses that 1.1% of the weakly supervised data contains non-simile instances (e.g., "I feel like a fool") and notes that the transformation method still works on these cases. The LaTeX mentions the 1.1% noise rate but does not include the additional observation from the appendix that the transformation remains beneficial even on noisy examples.
- The paper's Appendix A.1 specifies that MAX-TOKENS is set to 1024 and that the same hyperparameters as the CNN-DM summarization fine-tuning are used except for this value. The LaTeX does not include these implementation details.
- The paper notes that the BART-large checkpoint has 400 million parameters and was trained on 4 RTX 2080 GPUs for 52 minutes. These are included in the LaTeX.

## Recommendation

The LaTeX document is factually consistent with the paper and the markdown analysis files. The missing information consists primarily of secondary numerical details (correlation coefficients, inter-annotator agreement, per-task worker counts) that do not affect the main narrative. If completeness is desired, these values can be added to the Evaluation section. No corrections are needed.
