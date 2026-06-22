# Problem Statement

## Background

Simile is a figurative language device in which two fundamentally different things are explicitly compared using "like" or "as." Simile interpretation (SI) and simile generation (SG) are two core tasks in simile research. SI aims to find a suitable attribute given a tenor and vehicle, while SG aims to select a proper vehicle given a tenor and attribute. These two tasks can be unified into the form of Simile Triple Completion (STC), where a simile sentence is represented as a triple (tenor, attribute, vehicle).

Previous works on SI and SG have relied on limited training corpora or hand-crafted knowledge bases (e.g., ConceptNet, FrameNet), which are labor-intensive, time-consuming, and impose an upper limit on the diversity of generated results.

## Problem Definition

How can simile knowledge be effectively probed from pre-trained language models (PLMs) to solve both simile interpretation and simile generation tasks in a unified framework, without requiring fine-labeled training data or manually constructed knowledge graphs?

## Research Objectives

- To propose a unified framework that solves both SI and SG tasks by probing simile knowledge from pre-trained masked language models.
- To improve the diversity and creativity of predicted simile components (attributes and vehicles) beyond what standard MLM predictions offer.
- To leverage pattern ensemble and pattern search techniques to enhance the quality of predictions.
- To demonstrate that PLMs implicitly encode simile knowledge learned from large-scale corpora during pre-training.

## Key Challenges

- **High-frequency word bias**: PLMs trained with MLM loss tend to predict common words (e.g., good, bad, big), which conflicts with the creative and unexpected nature of simile sentences.
- **Pattern dependency**: Different patterns yield different prediction preferences, and relying on a single pattern is insufficient for robust results.
- **Knowledge extraction without labeled data**: Probing implicit simile knowledge from PLMs without task-specific labeled training data or explicit knowledge bases.
- **Limited prior work**: Few studies have explored directly probing simile knowledge from PLMs, making this a novel research direction with limited established baselines.
