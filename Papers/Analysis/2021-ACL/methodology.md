# Methodology

## Overview

The research creates RTE test sets specifically focused on three types of figurative language: similes, metaphors, and irony. The study involves adapting five existing datasets annotated for figurative language phenomena into over 12,500 RTE examples. The evaluation employs three neural RTE models trained on the MNLI dataset to assess their figurative language comprehension capabilities.

## Data Collection

### Data Sources

The study leverages five existing annotated figurative language datasets:

1. **Simile Dataset** (Chakrabarty et al., 2020)
   - 150 literal sentences from r/WritingPrompts and r/Funny subreddits
   - Each aligned with two human-written simile paraphrases
   - Creates 600 RTE pairs total

2. **Metaphor Dataset** (Chakrabarty et al., 2021)
   - 150 literal sentences curated from different domains and genres
   - Annotated with metaphorical paraphrases by expert annotators
   - Creates 613 RTE pairs total

3. **Irony Verbal Meaning Dataset (SIGN)** (Peled and Reichart, 2017)
   - Parallel dataset of tweets with verbal irony and non-ironic rephrasings
   - 15,000 pairs with option to copy or paraphrase
   - Subset of 2,000 pairs (SIGN2000) annotated for RTE evaluation
   - Creates 2,000 RTE pairs

4. **Irony Speaker-Hearer Dataset (Sim-Hint)** (Ghosh et al., 2020)
   - Parallel dataset of speakers' ironic messages and hearers' interpretations
   - 4,761 ironic-literal pairs
   - Creates 4,762 RTE pairs total

5. **Ironic Intent Dataset** (Van Hee et al., 2018)
   - 4,598 RTE pairs derived from ironic tweets using template-based generation
   - Dataset uses alternating contextual templates

### Data Statistics
- **Total Dataset Size**: 12,437 RTE pairs
- **Simile**: 600 pairs (300 entailed, 300 not-entailed)
- **Metaphor**: 613 pairs (307 entailed, 306 not-entailed)
- **SIGN2000**: 2,000 pairs (133 entailed, 1,867 not-entailed)
- **Sim-Hint**: 4,762 pairs (0 entailed, 4,762 not-entailed)
- **Irony Intent**: 4,601 pairs (2,212 entailed, 2,389 not-entailed)

## System/Model Design

### RTE Framework

The research frames figurative language understanding as an RTE task:
- **Context**: The figurative language expression
- **Hypothesis**: The intended meaning (literal or pragmatic interpretation)
- **Task**: Determine whether the context entails the hypothesis

### Data Transformation

#### Simile RTE Creation
- Treat figurative-literal aligned sentences as entailed context-hypothesis pairs
- Create not-entailed examples by flipping the literal verb/property with antonyms
- Example entailed pair: "They had shut him in a basement that looked like a freight elevator" (figurative) → "They had shut him in a basement that looked dangerously claustrophobic" (literal)
- Example negated pair: "Hitler skittered off like an enthusiastic sloth" (entailed: "slowly") → ("not-entailed: "fast")

#### Metaphor RTE Creation
- Treat metaphorical-literal paraphrases as entailed pairs
- Focus on verb-based metaphors (most frequent type)
- Example: "The tax cut will fertilize the economy" (metaphorical) → "The tax cut will help the economy" (literal)
- Generate not-entailed examples by manually swapping literal verbs with antonyms
- Emphasis on manual replacement to ensure grammatical quality

#### Irony Meaning RTE Creation
- Original ironic messages serve as contexts
- Intended meanings serve as hypotheses
- For SIGN dataset: Subset to 2,000 random pairs (approximately 93% not-entailed)
- For Sim-Hint dataset: All 4,762 pairs used (100% not-entailed)

#### Irony Intent RTE Creation
- Use template-based generation: "Name tweeted that tweet" (context) + "Name was ironic" (hypothesis)
- Names sampled from US Census-based distribution
- Four-way classification: entailed if the model should recognize irony; not-entailed otherwise

## Algorithms and Techniques

### Evaluated Models

#### 1. Bag of Words (NBoW)
- Word embeddings averaged separately for contexts and hypotheses
- Concatenation of averaged representations
- Passed to logistic regression softmax classifier
- Embedding: 300-dimensional GloVe embeddings

#### 2. InferSent
- BiLSTM encoder for context and hypothesis sentences
- Independent encoding of both sentences
- Sentence representations fed to MLP classifier
- Embedding: 300-dimensional GloVe embeddings

#### 3. RoBERTa-large
- Transformer-based pre-trained model
- Fine-tuned on MNLI dataset
- Accessed through Hugging Face Transformers library
- Represents state-of-the-art neural approaches

### Training Setup
- All models trained on MNLI dataset (Multi-Genre Natural Language Inference corpus)
- MNLI contains ~433K sentences from diverse genres and domains
- Multi-class classification task (entailment, neutral, contradiction)

## Evaluation Process

### Evaluation Metrics
- **Primary Metric**: Accuracy (percentage of correctly classified pairs)
- **Error Analysis**: Manual qualitative analysis of model failures

### Analysis Framework

#### Category 1: Linguistic Strategy Analysis
- Examined types of linguistic strategies used in hypotheses
- Categories from Ghosh et al. (2020) typology:
  - Lexical and phrasal antonyms
  - Negation
  - Weakening the intensity of sentiment
  - Interrogative to declarative transformation
  - Counterfactual desiderative constructions
  - Pragmatic inference

#### Category 2: Knowledge-Based Analysis
- **World Knowledge**: Physical and visual world knowledge
- **Conventional vs. Unconventional**: Well-worn versus novel figurative expressions
- **Linguistic Markers**: Detection of irony markers including metaphor, alternate spelling, hashtags

#### Category 3: Error Classification
- Categorized model errors by underlying cause
- Identified systematic failure patterns
- Mapped errors to knowledge type requirements

### Test Set Characteristics
- All datasets framed as binary classification where applicable
- Focus on challenging cases requiring non-literal interpretation
- Mixed class distribution to test real-world inference scenarios
