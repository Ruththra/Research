# Limitations

## Technical Limitations

- The knowledge-enhanced objective relies on TransE, a relatively simple knowledge embedding method. While the paper notes that more complex methods (TransH, TransD) do not significantly improve results, more advanced knowledge integration approaches (e.g., graph neural networks, neuro-symbolic methods) are unexplored.
- The probing task is limited to closed similes with explicit properties; open similes (where the property is implicit) are not addressed in the evaluation.
- Only BERT and RoBERTa families are evaluated; other PLM architectures (e.g., GPT, T5, DeBERTa) are not tested.
- The component influence analysis uses a simple masking/replacement strategy that may not fully capture the nuanced interactions between components.

## Dataset Limitations

- The dataset size is relatively small (1,633 examples), which may limit generalizability.
- Data is sourced from only two general corpora (BNC, iWeb) and one educational platform (Quizizz), potentially missing simile usage in other domains (e.g., social media, literature, scientific writing).
- All properties are single-token, achieved by replacing multi-token properties with synonyms — this simplifies the task and may not reflect real-world simile complexity.
- The seven property categories are imbalanced, with Qualities (27.78%) heavily represented and Emotion (5.26%) underrepresented.
- Only English similes are studied; cross-lingual generalization is unknown.

## Experimental Limitations

- Human performance baseline is based on only 250 questions with three annotators per question — a larger sample may yield more reliable estimates.
- The downstream task is limited to binary sentiment classification on Amazon reviews; other downstream tasks (e.g., metaphor detection, figurative language understanding) are not evaluated.
- The paper does not explore the effect of different α values in depth beyond testing {3, 5, 10}.
- Fine-tuning for the probing task uses a relatively small training set (4,510 sentences from SPGC).

## Threats to Validity

- **Construct Validity**: The multiple-choice probing format may not fully capture the open-ended nature of human simile interpretation, where multiple valid properties may exist.
- **Internal Validity**: The knowledge-enhanced objective's improvement may be confounded by the additional training signal rather than the specific knowledge embedding formulation.
- **External Validity**: Results may not generalize to other languages, domains, or PLM architectures not tested.
- **Annotation Bias**: Human annotators who confirmed distractors also contributed to human performance measurement, though the paper states they did not participate in data collection.
- **Category Subjectivity**: Property category classification (Table 9) involves some subjectivity, though annotator agreement was required.
