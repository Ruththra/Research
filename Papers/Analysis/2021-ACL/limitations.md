# Limitations

## Technical Limitations

### Model Architecture Constraints
- **Transformer Limitations**: RoBERTa-large and other transformer-based models struggle to capture knowledge grounded in visual perception and physical world understanding
- **Contextual Embedding Constraints**: BiLSTM-based approaches (InferSent) show even lower performance on visual and physical reasoning tasks
- **Bag-of-Words Weakness**: Simple aggregation approaches lack sophisticated semantic composition abilities needed for figurative language

### Training Data Limitations
- **Domain Mismatch**: Models trained on MNLI may not transfer well to more specialized or unconventional figurative language
- **Template-Based Generation Issues**: The IIntent dataset, created using templates, exhibits very different distributional properties than MNLI training data, leading to poor model performance (InferSent achieves very low accuracy)

### Model Output Design
- **Binary vs. Multi-class**: While MNLI includes contradiction, neutral, and entailment classes, some test sets are strictly binary, potentially conflating neutral with contradictory examples

## Dataset Limitations

### Simile Dataset Limitations
- **Size Constraints**: Base dataset contains only 150 literal-simile pairs, limiting diversity
- **Source Bias**: Data from specific subreddits (r/WritingPrompts, r/Funny) may not represent full range of simile usage across domains
- **Paraphrase Dependency**: Reliance on human-written paraphrases may introduce systematic biases in figurative expression style

### Metaphor Dataset Limitations
- **Verb-Only Focus**: Analysis acknowledges that while verb-based metaphors are most common, other metaphor types are underrepresented
- **Genre Limitations**: Despite curation from multiple domains, dataset remains relatively small (150 base examples)
- **Annotator Variation**: Expert annotators working independently may introduce inconsistencies in metaphor generation

### Irony Dataset Limitations
- **SIGN2000 Subset**: Restriction to 2,000 random pairs from larger SIGN dataset may not capture full range of irony phenomena
- **Sim-Hint Dominance**: Dataset shows 100% not-entailment class, creating severe class imbalance
- **Social Media Bias**: Heavy reliance on Twitter data may not generalize to other irony usage contexts (spoken language, literature, etc.)
- **Irony Intent Sparsity**: Very low accuracy across models on this task suggests template-based recasting may be problematic

### Shared Dataset Issues
- **Antonym-Based Negation**: Both simile and metaphor use antonym substitution for not-entailed examples, which may introduce systematic patterns that models exploit
- **Limited Rephrasing Strategies**: Hypotheses often rely on lexical antonyms or simple negation rather than complex pragmatic reasoning

## Experimental Limitations

### Model Selection Bias
- **Limited Model Diversity**: Only three model types tested; other architectures or pre-training approaches not evaluated
- **MNLI-Only Training**: All models fine-tuned on MNLI; effects of training on other RTE datasets unknown
- **No Ensemble Methods**: Single-model predictions without ensemble approaches

### Evaluation Constraints
- **No Statistical Significance Testing**: Accuracy scores reported without confidence intervals or significance tests
- **No Cross-Dataset Validation**: Models not tested on figurative language datasets from different domains/sources
- **Limited Error Analysis Scale**: Detailed error analysis appears conducted on sample examples rather than systematic analysis

### Analysis Scope
- **Single Language**: Evaluation limited to English; figurative language challenges may differ across languages
- **Static Evaluation**: No evaluation of model behavior with adversarial or out-of-distribution figurative examples
- **No Comparative Analysis**: Performance not compared against figurative language-specific baselines or specialized models

## Threats to Validity

### Internal Validity Threats

1. **Confounding Variables in Data Creation**
   - Antonym selection methodology may systematically bias not-entailed examples
   - Manual versus automatic annotation processes create different quality profiles
   - Annotator expertise differences between datasets

2. **Model Adaptation Effects**
   - Different fine-tuning procedures or hyperparameters across models
   - Potential optimization toward MNLI characteristics rather than figurative language

3. **Dataset Interaction Effects**
   - Mixing datasets with different collection methodologies and class distributions
   - SIGN2000 subset selection may introduce sampling bias

### External Validity Threats

1. **Generalization Across Figurative Types**
   - Findings on similes, metaphors, and irony may not extend to other figurative language types (personification, metonymy, hyperbole, understatement)
   - Unknown whether limitations transfer to literary or specialized domains

2. **Model Evolution**
   - Models tested represent specific architectural generation (BERT-era transformers)
   - Findings may not apply to newer model architectures or training approaches

3. **Real-World Application Gap**
   - Framing figurative language as binary RTE task may oversimplify real-world inference needs
   - Controlled dataset construction may not reflect authentic figurative language complexity

### Construct Validity Threats

1. **RTE as Proxy for Understanding**
   - RTE performance may not fully capture figurative language comprehension
   - Binary entailment decision oversimplifies understanding requirements

2. **Intended Meaning Ambiguity**
   - Definition of "intended meaning" for figurative language may be context-dependent
   - Multiple valid interpretations possible for same figurative expression

3. **Operational Definitions**
   - Definitions of conventional vs. unconventional metaphors based on frequency, not independent validation
   - Irony markers identified post-hoc rather than theoretically grounded

### Conclusion Validity Threats

1. **Limited Evidence for Causal Claims**
   - Study demonstrates model failures but limited mechanistic explanation
   - Hypotheses about reasons for failure (world knowledge, pragmatic inference) not directly tested

2. **Alternate Explanations**
   - Low IIntent performance attributed to template bias, but other causes not ruled out
   - Model failures might stem from training procedure rather than fundamental understanding limitations
