# Methodology

## Overview

The proposed framework unifies simile interpretation (SI) and simile generation (SG) into a Simile Triple Completion (STC) task. Given an incomplete triple (tenor, attribute, vehicle) where one element is missing, the framework constructs masked sentences using manual patterns and employs a pre-trained masked language model (MLM) that has undergone Adjective-Noun Mask Training (ANT) to predict the missing element. Pattern Ensemble (PE) and Pattern Search (PS) are applied to improve prediction quality.

## Data Collection

- **ANT Training Data**: Sentences are extracted from BookCorpus (Zhu et al., 2015) with length less than 64 tokens. Only sentences containing *amod* (adjectival modifier) dependencies are retained, identified using trankit (Nguyen et al., 2021). Nouns or adjectives at the end of amod relations are masked, with each word masked no more than 5 times. The final dataset contains 98K sentences (68K noun-masked, 30K adjective-masked).
- **Evaluation Data**: The dataset from Roncero and de Almeida (2015) is used, containing multiple attributes for each (tenor, vehicle) pair. After filtering by reversing simile triples with attribute frequencies greater than 4, the train set contains 533 samples and the test set contains 145 samples. The train set is used for Pattern Search (D_PS), and the test set is used for final evaluation.

## System/Model Design

- **Base Model**: BERT-Large (340M parameters) serves as the backbone pre-trained MLM.
- **ANT Model (LM_ANT)**: BERT-Large fine-tuned on the constructed ANT dataset using MLM loss with Adam optimizer (learning rate: 5e-5, batch size: 32, max sequence length: 64, 3 epochs).
- **Pattern Design**: 12 manual patterns organized into 4 classes:
  - **Class I**: Models the relationship between all three simile elements (tenor, attribute, vehicle) — patterns p1-p3.
  - **Class II**: Models the relationship between vehicle and attribute — patterns p4-p6.
  - **Class III**: Models the relationship between tenor and attribute — patterns p7-p9.
  - **Class IV**: Models the relationship between tenor and vehicle (attribute omitted) — patterns p10-p12.
- **Vehicle Filtering (for SG)**: Predicted vehicles semantically similar to the tenor are filtered out using GloVe embeddings (threshold: 0.4, the maximum similarity score of tenor-vehicle pairs in the train set).

## Algorithms and Techniques

- **Simile Triple Completion (STC)**: Defines the unified task where a triple (T, A, V) is completed by predicting the missing element. SI: (T, None, V) → predict A. SG: (T, A, None) → predict V.
- **Masked Language Model (MLM) Probing**: Constructs a sentence from the incomplete triple using a pattern, masks the target element, and uses the PLM to predict the masked position over the task-specific vocabulary. The top-K highest probability words are selected as results.
- **Adjective-Noun Mask Training (ANT)**: A secondary pre-training stage where only nouns or adjectives in amod dependencies are masked (not random masking), and masking frequency is capped at 5 per word. This reduces the model's bias toward high-frequency words and increases prediction diversity.
- **Pattern Ensemble (PE)**: Averages the log-probability distributions over all applicable patterns for a given task. For SI: uses patterns from Classes I, II, and III. For SG: uses patterns from Classes I and IV (Class II is excluded as it lacks the vehicle; Class III is excluded for SG as it lacks the vehicle in the target position).
- **Pattern Search (PS)**: Iterates over all subsets of patterns on the training dataset (D_PS) to find the optimal pattern combination that maximizes the pattern ensemble performance, then applies the best subset for inference.

## Evaluation Process

- **Automatic Metrics**:
  - **Diversity (p@K)**: Proportion of unique words in the top-K predicted results across the test set, measuring lexical variety.
  - **Mean Reciprocal Rank (MRR)**: Average of the reciprocal rank of ground-truth label words in the predicted candidate list.
  - **R@K (Recall at K)**: Percentage of label words appearing in the top-K predictions. A predicted word is considered correct if it is a synonym of the label word according to WordNet.
- **Human Evaluation**: Annotators score predicted simile triples on a 3-point scale (0: unacceptable, 1: acceptable, 2: acceptable and creative). Each triple is annotated by 3 independent annotators. Inter-annotator agreement is measured using Fleiss's kappa.
- **Baselines**: Meta4meaning, GEM, ConScore, and vanilla BERT (single pattern MLM prediction without ANT).
