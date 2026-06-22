# Existing Works

## Previous Approaches

- **Meta4meaning** (Xiao et al., 2016): Uses trained LSA vector representations based on the degree of abstraction and salience imbalance to select appropriate attributes for simile interpretation.
- **GEM** (Bar et al., 2018): Calculates cosine similarity and normalized PMI between each attribute and tenor/vehicle based on GloVe representations to rank and select the best attribute.
- **ConScore** (Zheng et al., 2020): Proposes a connecting score to select an attribute word for a given tenor-vehicle pair.
- **Knowledge-based approaches** (Gero and Chilton, 2019; Stowe et al., 2021; Veale et al., 2016): Rely on hand-crafted knowledge bases such as ConceptNet and FrameNet to find intermediate attributes for simile interpretation.
- **Sequence-to-sequence models** (Lewis et al., 2020; Zhang et al., 2021): Fine-tune seq2seq models on limited training corpora using pattern-based or knowledge-based approaches for simile generation.
- **Style transfer approaches**: Generate similes using style transfer methods with symbolism and discriminative decoding.

## Related Research

- **Probing knowledge from PLMs**: Petroni et al. (2019), Shin et al. (2020), Haviv et al. (2021), and Jiang et al. (2020) designed discrete patterns to explore commonsense and world knowledge embedded in PLMs.
- **Continuous pattern search**: Zhong et al. (2021) and Li and Liang (2021) probed knowledge by searching for best-performing continuous patterns in embedding space (e.g., prefix-tuning).
- **Simile triple completion**: Song et al. (2021) proposed a knowledge graph embedding approach for metaphor processing and introduced the simile triple formalism.
- **Figurative language and sentiment**: Rentoumi et al. (2012) investigated metaphorical language in sentiment analysis; Zheng et al. (2020) studied simile in question answering.

## Gaps in Existing Solutions

- **Reliance on hand-crafted resources**: Existing SI/SG approaches depend on manually constructed knowledge bases or limited corpora, which are labor-intensive and language-specific (scarce for non-English languages).
- **Limited result diversity**: Methods relying on small training sets or knowledge graphs inherently cap the variety of generated simile components.
- **Under-exploration of PLM knowledge**: Despite PLMs being shown to encode rich world knowledge (commonsense, syntax, semantics), few works have directly probed simile-specific knowledge from these models.
- **No unified framework**: Prior works typically address SI and SG as separate tasks; no prior work unifies both tasks using PLM probing in a single framework.
- **Lack of creativity in predictions**: Standard MLM predictions favor high-frequency, common words, which contradicts the creative and surprising nature of effective similes.
