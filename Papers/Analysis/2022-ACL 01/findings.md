# Research Findings

## Research Gaps Identified

- **Reliance on hand-crafted resources for simile tasks**: Existing simile interpretation and generation approaches depend on manually constructed knowledge bases (ConceptNet, FrameNet) or limited training corpora, which are labor-intensive, language-specific, and impose an upper limit on result diversity.
- **Under-exploration of PLM knowledge for similes**: Despite pre-trained language models being shown to encode rich world knowledge (commonsense, syntax, semantics), "few works have explored directly probing the knowledge of simile from the PLMs" prior to this work.
- **No unified framework for SI and SG**: Prior works typically address simile interpretation (SI) and simile generation (SG) as separate tasks with different methods and resources, lacking a unified approach.
- **High-frequency word bias in MLM predictions**: Standard masked language model predictions heavily favor common words, which contradicts the creative and surprising nature of effective similes.
- **Lack of diversity in generated simile components**: Methods relying on small training sets or knowledge graphs inherently cap the variety of generated simile attributes and vehicles, limiting the creative potential of automated approaches.

## Gaps Fulfilled by This Paper

- **First unified framework for SI and SG via PLM probing**: The paper proposes the first unified framework that solves both simile interpretation and simile generation using pre-trained language models, formalized as Simile Triple Completion (STC). The authors state: "To the best of our knowledge, it is the first work to introduce pre-trained language models to unify these tasks."
- **Adjective-Noun Mask Training (ANT) for diversity**: The paper introduces a novel secondary pre-training stage that fine-tunes PLMs by masking only nouns and adjectives in amod dependencies, reducing high-frequency word bias. After ANT, the frequency of common words like "good" drops significantly, and diversity for both SI and SG improves substantially.
- **Pattern Ensemble and Pattern Search for quality improvement**: The paper proposes averaging predictions over multiple manual patterns (PE) and automatically searching for optimal pattern subsets (PS), addressing the pattern dependency issue and improving both quality and robustness of predictions.
- **No labeled data or knowledge graphs required**: The framework operates without fine-labeled training data or hand-crafted knowledge bases, relying solely on implicit knowledge encoded in PLMs, making it more scalable and less labor-intensive than prior approaches.

## Summary

This paper fills the gap of under-exploited PLM knowledge for simile tasks by proposing a unified framework for simile interpretation and generation (STC) that uses masked language model probing with ANT secondary training. It addresses the high-frequency word bias of standard MLMs and eliminates the need for hand-crafted knowledge bases or labeled training data, while achieving improved diversity and correctness over traditional baselines.
