# Problem Statement

## Background

Similes are figures of speech that compare two fundamentally different entities via shared properties. They are widely used in natural language (e.g., over 30% of comparisons in product reviews are similes) and play a vital role in making utterances more vivid. Simile interpretation is a crucial NLP task that can assist downstream tasks such as understanding figurative language and sentiment analysis. Pre-trained language models (PLMs) have achieved state-of-the-art performance on many NLP tasks and have been shown to encode various kinds of knowledge in their contextual representations. However, whether PLMs can interpret similes by inferring shared properties remains under-explored.

## Problem Definition

The paper investigates the ability of pre-trained language models (PLMs) to interpret similes. Specifically, it asks: **Can PLMs infer the shared properties of similes as well as humans?** The task is formulated as "Simile Property Probing" — given a closed simile with the shared property masked, the model must identify the correct property from four candidate options (one correct, three hard distractors).

## Research Objectives

1. Systematically evaluate the ability of PLMs (BERT and RoBERTa) to interpret similes via a novel simile property probing task.
2. Construct simile property probing datasets from both general textual corpora and human-designed questions, covering 1,633 examples across seven categories.
3. Identify which simile components (topic, vehicle, event, comparator) contribute most to property inference.
4. Propose a knowledge-enhanced training objective to bridge the gap between PLM and human performance.
5. Validate the approach on a downstream sentiment classification task.

## Key Challenges

- Designing distractors that are both **true-negative** (illogical when inserted) and **challenging** (semantically close to the correct answer).
- Avoiding multiple correct answers, which motivates the multiple-choice formulation over a cloze task.
- Bridging the gap between PLM performance and human performance in simile interpretation.
- Incorporating simile-specific knowledge (topic-property-vehicle triplets) into PLM training without disrupting general language understanding.
- Handling diverse context types across different data sources (general corpora vs. educational quizzes).
