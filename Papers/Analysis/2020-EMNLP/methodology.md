# Methodology

## Overview

- The paper proposes SCOPE, a style-transfer framework for simile generation through commonsense property inference.
- The method has two stages: create literal-simile training pairs automatically, then fine-tune BART on those pairs.

## Data Collection

- Similes are collected from Reddit using distant supervision with the pattern like a.
- The target side of the parallel corpus is the collected simile.
- The source side is a literal sentence produced by removing the comparator and replacing the vehicle with a property inferred from commonsense knowledge.
- COMET is used with the HasProperty relation to infer candidate properties for the vehicle.
- The top five candidate properties are generated, then ranked using GPT perplexity; a grammatical error correction model is used to clean the resulting literal sentence.
- The paper reports 87,843 literal-simile pairs, with 82,697 for training and 5,146 for validation.
- For testing, 150 literal sentences are sampled from WritingPrompts and corresponding similes are written by two literary experts.

## System/Model Design

- BART is used as the base sequence-to-sequence model.
- The encoder input is the literal sentence and the decoder target is the simile.
- At inference time, the model generates similes with top-k sampling.

## Algorithms and Techniques

- Commonsense inference: COMET provides candidate properties associated with the vehicle.
- Property selection: GPT perplexity is used to choose the best literal reconstruction.
- Error correction: a grammatical error correction model removes malformed outputs from the transformation step.
- Decoding: top-k sampling is used for creative generation.

## Evaluation Process

- Automatic metrics: BLEU-1, BLEU-2, BERTScore, and novelty.
- Human evaluation: 900 utterances are rated on Creativity, Overall Quality, Relevance to Property, and Relevance to Topic.
- Pairwise comparison is performed against two human authors, retrieval-based generation, BART, and metaphor masking.
- A downstream task-based evaluation tests whether replacing literal sentences in GPT-2 generated stories with SCOPE similes improves story quality.