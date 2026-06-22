# Problem Statement

## Background
- Figurative language (metaphors, similes, sarcasm, idioms) is central to human communication, enabling expression of complex ideas and emotions implicitly.
- Understanding figurative language remains a bottleneck for NLP systems, as it requires world knowledge, cultural context, and social awareness that current models lack.
- Recent benchmarks frame figurative language understanding as a Recognizing Textual Entailment (RTE) / Natural Language Inference (NLI) task — determining whether a premise entails or contradicts a hypothesis.
- Current NLI benchmarks for figurative language suffer from **spurious correlations** and **annotation artifacts**, allowing large language models (LLMs) to achieve high performance through superficial cues rather than genuine understanding.
- Prior work (e.g., e-SNLI) introduced natural language explanations to NLI to probe whether models are "right for the right reasons," but no such explanation-based dataset exists for figurative language.

## Problem Definition
- There is no dataset that combines figurative language understanding with natural language explanations, making it impossible to assess whether models genuinely comprehend figurative expressions or merely exploit dataset artifacts.
- Existing figurative language NLI datasets lack: (1) free-form textual explanations, (2) diversity in figurative language types, and (3) rigorous quality control to avoid trivial examples.
- Models trained on general NLI explanation datasets (e.g., e-SNLI) perform poorly when applied to figurative language, indicating a gap in transferability.

## Research Objectives
1. Create **FLUTE**, a dataset of 9,000 figurative NLI instances with free-form textual explanations spanning four categories: Sarcasm, Simile, Metaphor, and Idioms.
2. Develop a **scalable model-in-the-loop framework** combining GPT-3, crowd workers, and expert annotators to build the dataset efficiently.
3. Demonstrate that models fine-tuned on FLUTE produce higher quality explanations than models trained on existing NLI explanation datasets (e.g., e-SNLI).
4. Establish baselines and evaluation protocols for figurative language understanding through textual explanations.

## Key Challenges
- **Spurious correlations**: Models can exploit lexical cues (e.g., negation, antonyms) in figurative NLI datasets without truly understanding the figurative meaning.
- **Annotation artifacts**: Minimal-edit approaches to creating non-entailment examples often result in neutral or trivially classifiable instances rather than true contradictions of the figurative expression.
- **Scalability**: Manually creating high-quality explanations for complex linguistic phenomena is expensive and time-consuming.
- **Quality control**: GPT-3 generations can contain social biases, stereotypes, or toxic content, requiring careful expert verification.
- **Diversity**: Figurative language draws on wide cultural knowledge and contexts, making it difficult to capture comprehensively.
- **Faithfulness**: Ensuring that model-generated explanations genuinely reflect the reasoning process rather than post-hoc rationalizations (noted as an open challenge).
