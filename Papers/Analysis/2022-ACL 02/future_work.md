# Future Work

## Short-Term Improvements

- Experiment with more advanced knowledge embedding methods or hybrid objectives (e.g., combining KE loss with contrastive learning) to further close the gap with human performance.
- Expand the dataset to include more examples, particularly for underrepresented categories (Emotion, Time, Color) and from additional domains (social media, literature).
- Evaluate a broader range of PLM architectures (GPT-style, encoder-decoder, larger models) on the simile property probing task.
- Conduct more systematic hyperparameter studies for the α balancing factor in the joint objective.
- Extend the probing task to open similes where the property is implicit, requiring generative rather than discriminative answers.

## Long-Term Research Directions

- Explore the interpretation of more sophisticated figurative language, such as **metaphor** and **analogy**, building on the simile property probing framework.
- Investigate cross-lingual simile interpretation to determine whether PLMs can transfer simile knowledge across languages.
- Develop methods for **simile generation** that leverage the knowledge-enhanced training objective to produce more human-like similes.
- Integrate multimodal knowledge (e.g., visual properties of entities) to improve property inference for visually-grounded similes.
- Study the developmental trajectory of simile understanding in PLMs across different scales (model size, training data size).

## Potential Extensions

- Apply the knowledge-enhanced objective framework to other relational NLP tasks involving structured knowledge (e.g., analogy resolution, commonsense reasoning).
- Combine the probing task with **chain-of-thought** or **explanation** generation to make the model's reasoning process more transparent.
- Extend the approach to **multi-token properties** without synonym replacement, potentially using span prediction heads.
- Investigate the interaction between simile interpretation and other figurative language phenomena (irony, hyperbole) in a unified framework.
- Deploy the simile property probing dataset as a benchmark for evaluating future PLMs' figurative language understanding capabilities.
