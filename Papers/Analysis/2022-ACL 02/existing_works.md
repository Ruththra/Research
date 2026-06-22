# Existing Works

## Previous Approaches

- **EMB** (Qadir et al., 2016): Obtains a composite simile vector by element-wise sum of word embeddings for vehicle and event, then selects the answer with the shortest cosine distance from the composite vector.
- **Meta4meaning** (Xiao et al., 2016): Ranks properties by statistical association with both topic and vehicle, preferring properties more relevant to the vehicle than the topic.
- **ConScore** (Zheng et al., 2019): Suggests that better properties have a smaller and balanced distance to the topic and vehicle in the word embedding space.
- **MIUWE** (Bar et al., 2020): Assigns scores to properties based on statistical co-occurrences and similarity to collocations of the topic and vehicle.
- Prior work has studied the ability of PLMs to choose or generate plausible continuations in narratives involving figurative language, but does not directly probe simile property inference.

## Related Research

- **Simile Processing**: Prior work focuses on three areas — simile detection and component identification, simile generation, and simile interpretation via property ranking.
- **Probing Tasks for PLMs**: Early work probes linguistic knowledge. Subsequent work evaluates commonsense knowledge including symbolic reasoning, numerical commonsense, and concept properties.
- **Enhancing PLMs via Knowledge Regularization**: Methods include span-boundary objectives, copy-based training, knowledge embedding objectives, and arithmetic relationship modeling.

## Gaps in Existing Solutions

- No prior work systematically evaluates PLMs' ability to interpret similes via a dedicated probing task — this paper claims to be the first.
- Existing simile interpretation methods rely primarily on statistical co-occurrence and embedding similarities, without leveraging the structured relationship between topic, property, and vehicle.
- Previous probing tasks do not address simile interpretation specifically.
- Existing knowledge-enhanced training objectives for PLMs do not incorporate simile-specific relational knowledge (topic-property-vehicle triplets).
- The gap between PLM and human performance in simile interpretation is not well characterized in prior literature.
