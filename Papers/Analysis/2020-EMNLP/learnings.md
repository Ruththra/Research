# Key Learnings

## Main Contributions

- The paper introduces simile generation as a new NLG task.
- It proposes a method for automatically constructing a parallel corpus from Reddit similes using commonsense property inference.
- It fine-tunes BART on literal-simile pairs to generate novel similes from literal inputs.

## Important Findings

- SCOPE generates a high proportion of novel similes that do not overlap with training properties.
- Human evaluation shows SCOPE is preferred over retrieval, plain BART, and metaphor masking baselines.
- The model is competitive with human-written similes on several quality dimensions, though humans still remain stronger on average.
- Replacing literal sentences with generated similes in stories improves evocativeness and acceptance.

## Lessons Learned

- Commonsense knowledge is important for mapping a literal property to an appropriate vehicle.
- Relevance matters as much as fluency in creative generation.
- Creative NLG benefits from a combination of weak supervision, pretrained language models, and task-specific evaluation.

## Practical Takeaways

- A weakly supervised corpus can be useful when manual annotation is unavailable.
- Style-transfer framing is effective for generating figurative language.
- Downstream creative tasks, such as storytelling, can benefit from a simile generation module.