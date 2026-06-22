# Limitations

## Technical Limitations

- The paper relies on similes that follow the pattern like a, so coverage of other simile forms is limited.
- The approach depends on commonsense property prediction from COMET, which can still produce irrelevant or noisy properties.
- The source reconstruction step can introduce grammatical errors, requiring a separate correction model.
- The paper uses top-k sampling, which may increase diversity but can also produce lower-precision generations.

## Dataset Limitations

- The automatically constructed parallel corpus is weakly supervised and contains noise.
- The paper notes that some collected examples are not true similes, such as expressions like I feel like a fool; this limitation is inferred from the dataset discussion.
- Training data is collected from Reddit, so the style and domain may be biased toward that source.
- The evaluation set is relatively small, with 150 literal sentences annotated by two experts.

## Experimental Limitations

- Automatic metrics such as BLEU are not well suited to creative generation and can understate quality.
- Human evaluation is expensive and uses a limited number of annotators per example.
- The task-based story evaluation is based on a specific GPT-2 storytelling pipeline, so generalization to other generators is inferred rather than directly shown.

## Threats to Validity

- The quality of the parallel corpus depends on several heuristic choices, including property ranking and error correction.
- Because the method is evaluated on a narrow set of literal inputs, performance on broader or more diverse text may differ.
- The paper’s conclusion that SCOPE is better than baselines is supported by the reported evaluations, but the exact margin may depend on the annotation setup and prompts.