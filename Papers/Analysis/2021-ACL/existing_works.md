# Existing Works

## Previous Approaches

### RTE Evaluation for Specific Phenomena
Recent work has tested RTE systems for an expanded range of inference patterns and linguistic phenomena:
- **Pragmatic inferences** (Jeretic et al., 2020)
- **Veridicality** and related semantic properties (Ross and Pavlick, 2019)
- **Function word comprehension** (Kim et al., 2019)
- **Compositionality in sentence embeddings** (Dasgupta et al., 2018)
- **Temporal and aspectual entailment** (Kober et al., 2019)
- **Simple lexical inferences** (Glockner et al., 2018)

### Figurative Language in NLP
The exploration of figurative language within RTE frameworks is not entirely novel:
- **Agerri (2008)**: Analyzed examples in Pascal RTE-1 and RTE-2 datasets requiring understanding of metaphors
- **Agerri et al. (2008)**: Presented an approach for RTE systems to process metaphors
- **Poliak et al. (2018)**: Created a diverse collection of RTE datasets including figurative language examples, specifically focusing on pun identification

### Figurative Language Research
Broader research on figurative language generation and understanding:
- **Simile Studies**: Chakrabarty et al. (2020) released test sets of literal sentences paired with human-written simile paraphrases
- **Metaphor Generation**: Chakrabarty et al. (2021) created diverse metaphor test sets from multiple domains
- **Irony Analysis**: Peled and Reichart (2017) created parallel datasets of ironic tweets and non-ironic rephrasings; Ghosh et al. (2020) developed speaker-hearer interpretation datasets

## Related Research

### Visual and Perceptual Knowledge
- Transformers-based contextual language models poorly capture knowledge grounded in visual perception (Weir et al., 2020)
- This limitation extends to understanding comparisons requiring visual and physical world knowledge

### Metaphor Comprehension
- Understanding metaphors requires comprehending abstract concepts and making connections between seemingly unrelated ideas (Gutierrez et al., 2016; Mohammad et al., 2016)
- Metaphors express deep feelings and complex attitudes (Veale et al., 2016)
- Cognitive factors affect metaphor interpretation difficulty (Kintsch and Bowles, 2002; Glucksberg, 1998)

### Irony Understanding
- Speakers using irony typically mean the opposite of what they say (Sperber and Wilson, 1981; Dews et al., 2007)
- Irony serves social and communicative functions (Jorgensen, 1996)
- Figurative language is essential for emotional communication (Fussell and Moss, 1998)

## Gaps in Existing Solutions

1. **Limited Focus on Figurative Language in RTE**: While figurative language appears in existing RTE datasets like MNLI, these datasets lack explicit focus on figurative phenomena

2. **Lack of Comprehensive Datasets**: No systematic collection of RTE examples specifically designed to test figurative language understanding across multiple types

3. **Insufficient Analysis of Model Failures**: Limited detailed analysis of how and why neural RTE models fail on figurative language tasks

4. **Pragmatic Inference Gap**: Existing models struggle with pragmatic inferences required by figurative language, particularly for irony and non-literal meaning comprehension

5. **World Knowledge Integration**: Models lack sufficient grounding in world knowledge needed for interpreting comparative figurative expressions

6. **Unconventional vs. Conventional Distinction**: Limited investigation of how model performance differs across well-worn versus novel figurative expressions

7. **Irony Marker Recognition**: Insufficient handling of linguistic irony markers (metaphors within irony, alternate spelling, hashtags) that signal ironic intent
