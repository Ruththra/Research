# Research Findings

## Research Gaps Identified

- **No prior work on simile generation as a task**: The paper states that while simile detection has been studied extensively, "research on simile generation is under-explored." Prior computational work focused on simile detection and analysis, not generation.
- **Lack of parallel training data for simile generation**: There was no large-scale parallel corpus of [literal sentence, simile] pairs available before this work. Existing simile datasets were small (a few hundred examples) or from restricted domains like Amazon product reviews.
- **No commonsense property inference mechanism for figurative language generation**: Earlier metaphor generation methods relied on templates, heuristics, or lexical databases. The paper notes that existing approaches do not preserve contextual relevance between literal input and generated figure of speech, and lack explicit handling of commonsense property mappings.
- **Difficulty of implicit property inference**: The PROPERTY in similes is often implicit (e.g., "The boy was like an ox" implies "strong"), and the paper identifies that generating open similes is more challenging than closed similes because the property must be inferred from context and commonsense knowledge.
- **Absence of creative NLG evaluation frameworks**: Standard automatic metrics like BLEU are not well-suited for creative text generation because creative outputs have limited n-gram overlap with references, making evaluation of novelty and relevance difficult.

## Gaps Fulfilled by This Paper

- **First systematic approach to simile generation**: The paper introduces simile generation as a new NLG task and proposes SCOPE (Style transfer through COmmonsense PropErty), the first framework to tackle it. The authors state: "To the best of our knowledge, this is the first work in attempting to generate similes."
- **Automatic construction of a large parallel corpus**: The paper proposes a method to automatically construct 87,843 literal-simile pairs from Reddit similes by using COMET (commonsense knowledge) to infer properties and transform similes into literal sentences. This solves the lack of training data.
- **Commonsense property inference via COMET**: The paper leverages structured commonsense knowledge (COMET's HasProperty relation) to infer candidate properties for vehicles, enabling the model to learn meaningful property mappings between topics and vehicles without manual annotation.
- **Style-transfer framing for figurative language**: By framing simile generation as a style-transfer problem from literal to figurative language, the paper enables the use of pretrained seq2seq models (BART) to generate creative similes. The model generates 88% novel similes that do not share properties with training data.
- **Task-based evaluation for creative NLG**: The paper introduces a downstream task-based evaluation showing that replacing literal sentences with SCOPE-generated similes in GPT-2-generated stories improves evocativeness (preferred 42% of the time vs. 25% for stories without similes).

## Summary

This paper fills the gap of simile generation as an under-explored NLG task by proposing a style-transfer framework that uses commonsense property inference (COMET) to automatically construct training data and fine-tune BART for creative simile generation. It contributes the first large-scale parallel corpus for simile generation and demonstrates that generated similes can improve downstream creative writing tasks.
