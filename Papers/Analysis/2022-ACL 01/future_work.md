# Future Work

## Short-Term Improvements

- **Expand pattern set**: Design and incorporate additional patterns beyond the current 12 to cover a wider range of simile expression forms, including more complex and literary structures.
- **Apply to other PLMs**: Extend the framework to other pre-trained model architectures (e.g., RoBERTa, GPT-2, T5, BART) to verify generalizability and compare performance across model types.
- **Improve ANT training**: Explore alternative secondary pre-training strategies that better balance diversity and correctness, potentially incorporating simile-specific objectives during ANT.
- **Larger-scale evaluation**: Evaluate the framework on larger and more diverse simile datasets, including cross-lingual simile data, to strengthen the validity of findings.

## Long-Term Research Directions

- **Broader figurative language probing**: Extend the approach to probe other types of figurative language from PLMs, such as metaphor, metonymy, and personification, building a comprehensive figurative language understanding framework.
- **Commonsense and world knowledge mining**: Investigate how to mine broader or more complex knowledge from PLMs beyond similes, including commonsense reasoning, causal knowledge, and cultural associations.
- **Continuous pattern optimization**: Replace or complement the discrete pattern search with continuous prompt optimization methods (e.g., prefix-tuning, soft prompts) to automatically discover optimal probing patterns without manual design.
- **Multilingual simile probing**: Adapt and evaluate the framework for multilingual simile interpretation and generation, addressing the scarcity of hand-crafted knowledge bases for non-English languages.

## Potential Extensions

- **Downstream task integration**: Apply the simile knowledge probing framework to downstream NLP tasks such as sentiment analysis, creative writing assistance, question answering, and writing polishing, where figurative language understanding is beneficial.
- **Simile quality scoring**: Develop a scoring mechanism to rank generated similes not just by correctness but by creativity, aptness, and aesthetic quality, potentially using learned metrics.
- **Interactive simile generation**: Build interactive systems where users can provide partial simile components and receive creative, contextually appropriate completions from the model.
- **Cross-modal simile generation**: Explore extending the framework to generate or interpret similes that bridge modalities (e.g., visual similes comparing images to concepts).
