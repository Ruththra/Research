# Research Findings

## Research Gaps Identified

- **No systematic evaluation of PLMs for simile interpretation**: Prior to this paper, "the ability of PLMs to interpret similes remains under-explored." While PLMs had achieved state-of-the-art on many tasks, their capacity to infer shared properties of similes had not been systematically investigated through a dedicated probing task.
- **Existing simile interpretation methods rely on surface statistics**: Prior methods (EMB, Meta4meaning, ConScore, MIUWE) rely primarily on statistical co-occurrence and embedding similarities without leveraging the structured relationship between topic, property, and vehicle.
- **No dedicated probing task for simile property inference**: Previous probing tasks for PLMs do not address simile interpretation specifically, leaving a gap in understanding what PLMs know about figurative comparisons.
- **Gap between PLM and human performance uncharacterized**: The magnitude and nature of the gap between PLM performance and human performance in simile interpretation was not well characterized in prior literature.
- **Lack of structured knowledge integration in PLM training for similes**: Existing knowledge-enhanced training objectives for PLMs do not incorporate simile-specific relational knowledge (topic-property-vehicle triplets).

## Gaps Fulfilled by This Paper

- **First systematic simile property probing task**: The paper introduces "Simile Property Probing" — the first systematic task to evaluate PLMs' ability to interpret similes by inferring shared properties from multiple-choice options. The authors state: "To our best knowledge, we are the first to systematically evaluate the ability of PLMs in interpreting similes."
- **Multi-source probing dataset construction**: The paper constructs two probing datasets (1,633 examples) from general corpora (BNC, iWeb) and human-designed questions (Quizizz), covering seven property categories with carefully designed hard distractors using ConceptNet and COMET.
- **Knowledge-enhanced training objective for simile interpretation**: The paper proposes a novel training objective that complements MLM loss with a knowledge embedding loss (TransE-style) modeling the (topic, property, vehicle) triplet relationship, achieving improved performance on both probing and downstream sentiment classification.
- **Component contribution analysis**: The paper identifies which simile components (topic, vehicle, event, comparator) contribute most to property inference, finding that vehicle and topic are most important, followed by the comparator.
- **Bridging the PLM-human performance gap**: The paper shows that PLMs already possess simile interpretation ability at pre-training and that the knowledge-enhanced objective helps close (though not eliminate) the gap with human performance.

## Summary

This paper fills the gap of unexplored PLM capabilities for simile interpretation by proposing the first systematic simile property probing task and dataset (1,633 examples across 7 categories). It demonstrates that PLMs encode simile-relevant knowledge and proposes a knowledge-enhanced training objective (TransE-style triplet loss) that improves both probing accuracy and downstream sentiment classification.
