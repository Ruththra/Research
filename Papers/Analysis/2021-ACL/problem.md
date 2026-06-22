# Problem Statement

## Background

Figurative language is ubiquitous in various forms of discourse including novels, poems, films, scientific literature, and social media conversations. It serves important communicative functions:
- Conveying intimacy and interpersonal connection
- Expressing humor and wit
- Communicating intense emotions
- Expressing veiled politeness and politeness markers

Despite its prevalence in human communication, figurative language remains "a bottleneck in automatic text understanding," particularly in Natural Language Processing (NLP) systems.

## Problem Definition

The study investigates how well state-of-the-art Recognizing Textual Entailment (RTE) models capture and understand figurative language. RTE is the task of identifying whether one sentence (context) likely entails another (hypothesis), and serves as a proxy for evaluating NLP systems' natural language understanding capabilities.

The core research question is: **Can neural RTE models trained on popular datasets adequately understand figurative language expressions and their non-literal meanings?**

## Research Objectives

1. Introduce a collection of RTE datasets specifically focused on figurative language phenomena
2. Create over 12,500 RTE examples by leveraging five existing datasets annotated for figurative language types (similes, metaphors, and irony)
3. Evaluate state-of-the-art RTE models' performance on understanding different aspects of figurative language
4. Provide a challenging testbed for evaluating RTE models' capabilities in handling non-literal language comprehension

## Key Challenges

- **Non-Literal Meaning Interpretation**: Figurative language requires understanding beyond literal word meanings
- **Pragmatic Inference**: Models must understand speaker intent and contextual implications
- **World Knowledge**: Effective figurative language understanding requires grounding in real-world knowledge
- **Linguistic Diversity**: Different figurative language types (similes, metaphors, irony) employ distinct mechanisms for conveying non-literal meaning
- **Semantic Complexity**: Figurative expressions often involve abstract concepts and connections between seemingly unrelated ideas
- **Unconventional Expressions**: Well-worn (conventional) versus novel (unconventional) figurative expressions pose different challenges
- **Absence in Training Data**: Current RTE datasets (like MNLI) contain figurative language but lack explicit focus on these phenomena
