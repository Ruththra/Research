# Key Learnings

## Main Contributions
- **FLUTE dataset**: A new benchmark of figurative NLI instances with free-form textual explanations spanning Sarcasm, Simile, Metaphor, and Idioms. Both labels and explanations are specifically tied to the figurative expression.
- **Model-in-the-loop framework**: A scalable approach combining GPT-3 generation, crowd worker edits, and expert verification that significantly reduces the human effort needed to create explanation datasets for complex linguistic phenomena.
- **Baseline experiments**: Comprehensive evaluation showing that T5 fine-tuned on FLUTE produces substantially higher quality explanations than T5 fine-tuned on e-SNLI, despite FLUTE being 50X smaller.
- **Evaluation protocol**: Established automatic metrics (Explanation Score, Accuracy@K, Rationale Quality) and human evaluation (Hscore, shortcoming categorization) for assessing figurative language explanation quality.

## Important Findings
- **e-SNLI does not transfer to figurative language**: Models trained on general NLI explanations (e-SNLI) perform poorly on figurative language, with accuracy dropping by nearly half when explanation quality thresholds are applied (Accuracy@50).
- **Explanation quality matters**: When requiring explanations to meet quality thresholds (score > 50 or > 60), T5e-SNLI accuracy drops dramatically, while T5FLUTE maintains significantly higher accuracy across all four figurative language types.
- **Human evaluation confirms automatic metrics**: T5FLUTE Hscore is substantially better than T5e-SNLI across all four figurative language types. Crowd workers answered "Yes" (explanation justifies label) more often and "No" less often for T5FLUTE.
- **Most common explanation shortcoming**: "Insufficient Justification" is the most frequent error category. T5e-SNLI explanations are also frequently "Too Trivial," often following template patterns like "if A then not B."
- **Gold rationales are useful**: Gold (human-verified) rationales achieve positive Rationale Quality scores, confirming that FLUTE explanations genuinely aid prediction, while predicted rationales from both models yield negative RQ scores.
- **GPT-3 + experts is effective**: The model-in-the-loop approach reduced expert editing to 10–40% of generated explanations (depending on figurative type), demonstrating scalability.
- **Contradiction design matters**: FLUTE's contradictions specifically target the figurative expression (e.g., contradicting the metaphor itself), unlike prior datasets that used minimal edits contradicting non-figurative parts.

## Lessons Learned
- **Dataset quality > quantity**: FLUTE (7,035 training examples) outperforms e-SNLI (366,603 examples) for figurative language explanation generation, showing that domain-specific, high-quality data is more valuable than large-scale general data.
- **Expert verification is essential**: GPT-3 alone is insufficient; expert verification and editing (10–40% of instances) are necessary to ensure explanation quality and avoid biases.
- **Joint models outperform pipelines**: Consistent with prior work, joint self-rationalizing models produce more label-indicative explanations than pipeline approaches.
- **Figurative language requires specialized treatment**: General NLI models and datasets do not adequately capture the reasoning needed for figurative language understanding.
- **Emotion-conditioned prompting helps**: For sarcasm, including emotion labels in GPT-3 prompts produces more creative and complex paraphrases that are easier for crowd workers to convert.

## Practical Takeaways
- **For dataset creators**: The model-in-the-loop framework (LLM generation → crowd editing → expert verification) is a viable and scalable approach for building explanation datasets for complex linguistic phenomena.
- **For model developers**: Fine-tuning on domain-specific explanation data (even if small) is more effective than training on large-scale general explanation data for specialized tasks like figurative language understanding.
- **For evaluators**: Standard accuracy is insufficient; explanation quality thresholds (Accuracy@50, Accuracy@60) and human evaluation are necessary to assess genuine model understanding.
- **For researchers**: FLUTE provides a challenging testbed for developing and evaluating models that can genuinely understand and explain figurative language, an important step toward more interpretable NLP systems.
