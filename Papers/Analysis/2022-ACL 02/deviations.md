# Deviations Report

## Analysis: 2022-ACL 02 (Simile Property Probing)

### Missing Information

1. **Problem Section**: The LaTeX document does not explicitly mention the specific statistic "over 30% of comparisons in product reviews are similes" from `problem.md:5`. This contextual detail about simile prevalence was omitted.

2. **Findings Section**: The LaTeX document does not explicitly state that "Fine-tuned PLMs still underperform humans by several accuracy points" which is mentioned in `learnings.md:12`. This quantitative finding about the performance gap is only implicitly covered.

3. **Findings Section**: The specific observation that "Models perform well on color properties (often inferable without context) but struggle on qualities, temporal properties, and emotions" from `learnings.md:16` is not explicitly stated in the LaTeX document.

4. **Learning Section**: The detail about "RoBERTa consistently outperforms BERT, likely due to its larger pre-training corpus containing more similes" from `learnings.md:14` is mentioned but the explicit reasoning about the pre-training corpus size could be more prominent.

5. **Learning Section**: The observation that "Models perform better on the Quizzes dataset than the General Corpus dataset, indicating that diverse contexts increase inference difficulty" from `learnings.md:15` is not explicitly included in the LaTeX document.

### Contradictory Information

No contradictions detected between the generated LaTeX content and the source markdown files.

### Unsupported Statements

No unsupported statements detected. All claims in the LaTeX document are directly supported by content in the source markdown files.

### Additional Findings From Paper

The following details from the source files were not included in the LaTeX document but could enhance completeness:

1. The specific Fleiss' Kappa value (0.77) for annotator agreement is mentioned in the Methodology section but could be highlighted as a finding about data quality.
2. The specific dataset statistics (Qualities 27.78%, Emotion 5.26%) from `limitations.md:15` are mentioned in the Limitations section but the exact percentages could be included for precision.
3. The implementation detail about "200 epochs for sentiment classification" from `methodology.md:36` is included but could be noted as unusually high, potentially indicating training difficulty.

### Recommendation

The LaTeX document is factually consistent with the source markdown files. The omissions are primarily specific quantitative details and observations that were consolidated for narrative flow. For a more comprehensive document, consider:

1. Adding the specific performance gap details (e.g., "several accuracy points") to the Findings section
2. Including the color vs. qualities/emotions performance comparison in the Learning section
3. Explicitly stating the Quizzes vs. General Corpus performance difference
4. Adding the 30% simile prevalence statistic to the Problem section for context

These additions would improve completeness without introducing unsupported claims.
