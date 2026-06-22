# Key Learnings

## Main Contributions

1. **Novel Probing Task**: The paper introduces "Simile Property Probing" — the first systematic task to evaluate PLMs' ability to interpret similes by inferring shared properties from multiple-choice options.
2. **Dataset Construction**: Two multi-choice probing datasets (1,633 examples) constructed from general corpora (BNC, iWeb) and human-designed questions (Quizizz), covering seven property categories with carefully designed hard distractors.
3. **Knowledge-Enhanced Training Objective**: A novel training objective that complements MLM loss with a knowledge embedding loss (TransE-style) modeling the (topic, property, vehicle) triplet relationship, achieving improved performance on both probing and downstream sentiment classification.

## Important Findings

- PLMs already possess simile interpretation ability at the pre-training stage, which can be enhanced through fine-tuning.
- Fine-tuned PLMs still underperform humans by several accuracy points, indicating room for improvement.
- **Vehicle** and **topic** are the most important components for property inference, followed by the **comparator** (simile trigger word). The event component is less critical.
- RoBERTa consistently outperforms BERT, likely due to its larger pre-training corpus containing more similes.
- Models perform better on the Quizzes dataset than the General Corpus dataset, indicating that diverse contexts increase inference difficulty.
- Models perform well on color properties (often inferable without context) but struggle on qualities, temporal properties, and emotions that require deeper contextual understanding.
- The knowledge embedding objective brings representations of topic, property, and vehicle closer together in the embedding space, which correlates with improved performance.

## Lessons Learned

- Structured relational knowledge (topic-property-vehicle triplets) can be effectively incorporated into PLM training via knowledge embedding methods.
- Simple knowledge embedding methods (TransE) are sufficient; more complex variants (TransH, TransD) do not provide significant additional gains for this task.
- Distractor design is critical for probing tasks — distractors must be both true-negative (logically incorrect) and challenging (semantically close to the correct answer).
- Multiple-choice formulation is preferable to cloze tasks for simile property probing because shared properties may not be unique.
- Joint optimization of knowledge embedding and MLM objectives allows PLMs to retain general language understanding while acquiring simile-specific knowledge.

## Practical Takeaways

- When designing probing tasks, careful distractor generation using external knowledge bases (ConceptNet, COMET) and embedding-based similarity selection can significantly improve task difficulty and diagnostic value.
- Component-level analysis (masking/replacement) is an effective method for understanding which parts of the input the model relies on for a given task.
- Knowledge-enhanced objectives are a lightweight and effective way to inject domain-specific relational knowledge into PLMs without requiring architectural changes.
- The simile property probing framework is extensible to other figurative language phenomena and can serve as a benchmark for evaluating PLMs' figurative language understanding.
- The datasets and code are publicly available at https://github.com/Abbey4799/PLMsInterpret-Simile, enabling reproducibility and further research.
