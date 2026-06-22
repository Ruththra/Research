# Methodology

## Overview

The methodology consists of four stages: (1) construction of simile property probing datasets from two sources, (2) empirical evaluation of PLMs in zero-shot and fine-tuned settings, (3) analysis of component contributions to property inference, and (4) design and evaluation of a knowledge-enhanced training objective that combines MLM loss with a knowledge embedding loss.

## Data Collection

- **General Corpus**: British National Corpus (BNC) and iWeb — sentences matching the syntactic pattern "as ADJ as (a, an, the) NOUN" were extracted, yielding 1,917 sentences.
- **Teacher-Designed Quizzes**: Quizizz platform — similes extracted from quiz questions and answers, yielding 875 complete closed similes from 1,235 quizzes.
- **Total**: 1,633 probes covering seven property categories (Qualities, Condition, Sense, Measurement, Color, Time, Emotion).
- **Human Annotation**: Three annotators verified simile identification (Fleiss' Kappa = 0.77) and confirmed distractor quality. Multi-token properties were replaced with single-token synonyms from WordNet and ConceptNet.
- **Training Data (for fine-tuning)**: Standardized Project Gutenberg Corpus (SPGC) — 4,510 simile sentences extracted via pattern matching and dependency parsing.

## System/Model Design

- **Models Evaluated**: BERT-BASE, BERT-LARGE, RoBERTa-BASE, RoBERTa-LARGE.
- **Probing Task Formulation**: Given a simile with the shared property masked, the model selects the correct property from four options (one correct + three hard distractors).
- **Knowledge-Enhanced Objective**: Treats each simile as a triplet (topic, property, vehicle) and applies a knowledge embedding loss based on TransE scoring: L_KE = MSE(E_t + E_p, E_v). The final objective jointly optimizes: L_Ours = α·L_KE + L_MLM, where α is a hyperparameter.
- **Downstream Validation**: Sentiment classification on Amazon reviews (binary, 5,023 reviews, 6:2:2 split) with MLP classifiers on top of frozen PLM representations.

## Algorithms and Techniques

- **Distractor Generation**: Candidates generated from four semantic-related components (topic, vehicle, event, property) using antonyms from WordNet/ConceptNet and HasProperty relations from ConceptNet/COMET. Adjectives/adverbs ranked by frequency in Wikipedia and BookCorpus.
- **Distractor Selection**: Cosine similarity between sentence embeddings (RoBERTa-LARGE [CLS]) with correct property vs. distractor — top 3 most similar (most challenging) distractors selected.
- **Component Influence Analysis**: Each component (topic, vehicle, event, comparator) is masked/replaced to measure its contribution to property inference accuracy.
- **Knowledge Embedding Methods Compared**: TransE (Bordes et al., 2013), TransH (Wang et al., 2014), TransD (Ji et al., 2015) — TransE found to be sufficient.

## Evaluation Process

- **Zero-shot Setting**: Off-the-shelf PLMs with pre-trained masked-word-prediction heads.
- **Fine-tuned Setting**: PLMs fine-tuned with MLM objective on masked property prediction.
- **Knowledge-Enhanced Setting**: PLMs fine-tuned with combined KE + MLM objective.
- **Metrics**: Accuracy on probing task (1,633 examples), accuracy on downstream sentiment classification.
- **Human Performance Baseline**: 250 random questions annotated by three people; majority vote used.
- **Implementation**: HuggingFace Transformers; batch sizes {8, 16}, α in {3, 5, 10}, max sequence length 128, learning rate 1e-5, 10 epochs for probing; 200 epochs for sentiment classification.
