# Existing Works

## Previous Approaches
- **RTE datasets (RTE-1, RTE-2)**: Early textual entailment challenges included some metaphor examples but were not specifically designed for figurative language.
- Prior work created a diverse RTE dataset including puns as one type of figurative language, but coverage was limited.
- Prior work addressed figurative language in RTE but lacked explanations and had less diversity compared to FLUTE.
- **Big-bench**: Contains metaphor examples but not all have literal paraphrases and contradictions; non-entailment examples often created via minimal edits leading to neutral rather than contradictory instances.
- **IMPLI**: Investigated NLI model performance on figurative language, inspired by prior work on parallel idiomatic expression corpora. However, non-entailment examples were created via minimal edits that often contradicted non-metaphoric parts of sentences rather than the metaphor itself.
- **e-SNLI**: A large-scale NLI dataset with natural language explanations created via crowdsourcing. Used extensively for explanation generation. However, it focuses on general NLI, not figurative language.
- **CoS-E**: Commonsense reasoning with explanations, but not specific to figurative language.
- **Movie Reviews**: Annotator rationale dataset, not focused on figurative language.

## Related Research
- **Sarcasm detection**: Prior work showed crowd workers tend to make minimal edits (negation/antonyms) when creating literal equivalents of sarcastic sentences, leading to trivial examples. Joint modeling of emotion and sarcasm improves detection.
- **Model-in-the-loop for NLI**: Prior work proposed WANLI for worker-AI collaboration in NLI dataset creation. Prior work also explored human-AI collaboration for generating free-text explanations.
- **Explanation quality**: Prior work showed joint self-rationalizing models produce more label-indicative rationales than pipeline models.
- **LLM-based explanation generation**: Prior work used LLMs to explain humor in image captions and sarcasm in dialogues.
- **Instruction-based learning**: Prior work demonstrated the effectiveness of instruction-based fine-tuning for task generalization.

## Gaps in Existing Solutions
- **No explanation-based figurative language dataset**: Prior figurative NLI datasets lack natural language explanations, preventing assessment of whether models understand figurative language for the right reasons.
- **Limited diversity**: Existing datasets cover only one or few types of figurative language; FLUTE spans four (sarcasm, simile, metaphor, idiom).
- **Trivial non-entailment examples**: Minimal-edit approaches in prior work produce neutral examples or contradictions of non-figurative parts, rather than contradictions of the figurative expression itself.
- **Poor transfer from general NLI**: Models trained on e-SNLI (general NLI explanations) perform poorly on figurative language, indicating that general NLI explanations do not transfer to figurative understanding.
- **Scalability challenges**: Purely manual creation of explanation datasets is prohibitively expensive for complex linguistic phenomena.
- **Lack of expert validation**: Many existing datasets rely solely on crowd workers without expert quality checks, risking lower quality.
