# Problem Statement

## Background

- Similes are figurative comparisons used in poetry, literature, and creative writing to make descriptions more vivid and emphatic.
- The paper treats simile generation as an under-explored natural language generation task compared with simile detection.
- A simile typically contains a TOPIC, VEHICLE, PROPERTY, EVENT, and COMPARATOR, with the PROPERTY sometimes implicit.

## Problem Definition

- Given a literal descriptive sentence, generate a novel simile that preserves the intended meaning while introducing a meaningful comparison.
- The generated simile should connect the TOPIC and VEHICLE through a shared PROPERTY, either explicitly or implicitly.
- The task is framed as a style-transfer problem from literal language to figurative language.

## Research Objectives

- Automatically construct a parallel corpus of literal-simile pairs from weakly labeled similes.
- Train a seq2seq model to generate similes from literal inputs.
- Produce similes that are relevant, creative, and novel with respect to the training data.
- Test whether generated similes can improve downstream creative text generation such as story writing.

## Key Challenges

- There is no large manually annotated parallel corpus for supervised simile generation.
- The PROPERTY is often implicit, so the model must infer the right property from context and commonsense knowledge.
- A generated simile must be both semantically relevant and stylistically creative.
- Automatic evaluation is difficult because creative outputs often have limited n-gram overlap with references.