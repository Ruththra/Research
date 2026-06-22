# Limitations

## Technical Limitations

- **Pattern design subjectivity**: The 12 manual patterns used in the framework are heuristically designed and may not capture all possible simile expression forms. The pattern search mitigates this but is limited to combinations of the pre-defined set.
- **ANT trades off accuracy for diversity**: While ANT significantly improves prediction diversity for both SI and SG, it slightly decreases the average correctness scores on automatic and human evaluations compared to vanilla BERT, as simile-specific knowledge is not explicitly incorporated during ANT training.
- **Computational cost of Pattern Search**: Pattern search requires iterating over all subsets of patterns on the training dataset, which scales exponentially with the number of patterns (2^12 combinations in this case). This becomes expensive with larger pattern sets.
- **Reliance on BERT-Large**: The framework's performance is tied to a specific pre-trained model architecture and size. The effectiveness with smaller models or other architectures (e.g., GPT, T5) is unexplored.

## Dataset Limitations

- **Small evaluation dataset**: The evaluation is conducted on a relatively small dataset (533 training, 145 test samples) derived from Roncero and de Almeida (2015). This limits the generalizability of the findings.
- **English-only evaluation**: The framework is evaluated only on English simile data. Its effectiveness on other languages is unknown, especially given that hand-crafted knowledge bases are noted to be scarce for non-English languages.
- **Limited simile variety**: The dataset contains annotations for a fixed set of tenor-vehicle pairs with multiple attributes, but does not cover the full diversity of simile usage in natural language (e.g., literary, domain-specific, or culturally specific similes).
- **ANT dataset source**: The ANT training data is derived from BookCorpus, which may not be representative of the simile distribution in other domains or genres.

## Experimental Limitations

- **Narrow baseline comparison**: The baselines compared (Meta4meaning, GEM, ConScore) are primarily traditional methods. Comparison with more recent neural approaches or other PLM probing methods is limited.
- **Single model evaluation**: Only BERT-Large is used as the base model. No experiments with other pre-trained models (e.g., RoBERTa, GPT-2, T5) are conducted to verify the framework's generalizability.
- **Human evaluation subjectivity**: Human evaluation scores (0, 1, 2) rely on subjective judgment. While Fleiss's kappa shows substantial agreement for SI and moderate agreement for SG, the inherent subjectivity remains a concern.
- **No downstream task evaluation**: The framework is evaluated on simile triple completion in isolation. Its utility for downstream NLP tasks (e.g., sentiment analysis, creative writing, question answering) is not assessed.

## Threats to Validity

- **Internal validity**: The filtering of predicted vehicles using GloVe similarity (threshold 0.4) introduces a dependency on the quality of word embeddings. The threshold is derived from the train set and may not generalize to other datasets.
- **External validity**: Results on a single, small, English-only dataset may not generalize to broader simile interpretation/generation scenarios, other languages, or other domains.
- **Construct validity**: The use of WordNet synonyms to determine correctness in R@K may miss semantically valid but non-synonymous predictions, potentially underestimating model performance.
- **Pattern search overfitting**: Pattern search is performed on the same training set used for evaluation selection. While the test set is held out, the pattern selection process may still introduce a form of indirect overfitting to the dataset characteristics.
