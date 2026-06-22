# Future Work

## Short-Term Improvements
- **Faithfulness evaluation**: Evaluate the faithfulness of model-generated NLEs using methods from contemporaneous literature (Sia et al., 2022; Chan et al., 2022), such as logical satisfiability of counterfactuals or the FRAME metric.
- **Bias and credibility studies**: Conduct targeted human studies to assess whether explanations mimic societal biases, are credible, and are free from stereotypes — going beyond the current toxic text verification.
- **Expand model comparisons**: Evaluate additional model architectures (e.g., GPT-3, larger T5 variants, instruction-tuned models) on the FLUTE benchmark to establish more comprehensive baselines.
- **Larger human evaluation**: Scale human evaluation beyond 200 samples to improve statistical reliability and coverage across figurative language types.

## Long-Term Research Directions
- **Broader figurative language coverage**: Extend the dataset to include other forms of figurative language such as hyperbole, irony, personification, litotes, and synecdoche.
- **Multimodal figurative language**: Investigate figurative language understanding in multimodal settings (e.g., memes, comics, videos) where figurative expressions are common.
- **Cross-lingual figurative language**: Develop explanation-based figurative language datasets for non-English languages, as figurative expressions are often language- and culture-specific.
- **Situational and dramatic sarcasm**: Expand the sarcasm portion to capture situational, underplayed, and dramatic forms of sarcasm, which require different types of reasoning and explanations.
- **Positive emotion sarcasm**: The current sarcasm data uses only negative emotions; incorporating positive emotions for sarcasm generation is noted as future work.

## Potential Extensions
- **Explanation quality improvement**: Develop methods to improve the faithfulness and quality of generated explanations, moving beyond plausibility to genuine reasoning transparency.
- **Downstream task transfer**: Investigate whether training on FLUTE improves performance on downstream tasks such as sentiment analysis, dialogue systems, or machine translation where figurative language is prevalent.
- **Adversarial testing**: Use FLUTE as a testbed for adversarial evaluation of figurative language understanding, similar to how e-SNLI has been used to probe NLI model robustness.
- **Neuro-symbolic approaches**: Combine neural models with symbolic reasoning (e.g., Feng et al., 2022) to improve figurative language understanding and explanation generation.
- **Interactive explanation refinement**: Explore human-in-the-loop approaches where models iteratively refine their explanations based on user feedback.
- **Scaling with newer LLMs**: Leverage more recent language models (beyond GPT-3) to generate higher-quality figurative language instances and explanations with reduced expert editing.
