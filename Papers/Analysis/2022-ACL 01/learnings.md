# Key Learnings

## Main Contributions

- **Unified framework for SI and SG**: This is the first work to propose a unified framework that solves both simile interpretation and simile generation tasks using pre-trained language models, formalized as simile triple completion (STC).
- **Adjective-Noun Mask Training (ANT)**: A novel secondary pre-training stage that fine-tunes PLMs by masking only nouns and adjectives in amod dependencies, significantly improving prediction diversity for both SI and SG.
- **Pattern Ensemble and Pattern Search**: The combination of averaging predictions over multiple manual patterns (PE) and automatically searching for optimal pattern subsets (PS) improves both the quality and robustness of simile component predictions.
- **No labeled data or knowledge graphs required**: The framework operates without fine-labeled training data or hand-crafted knowledge bases, relying solely on the implicit knowledge encoded in PLMs.

## Important Findings

- **PLMs encode simile knowledge**: Pre-trained language models implicitly learn simile-relevant knowledge (world knowledge, commonsense) from large-scale corpora during pre-training, which can be effectively probed using masked prediction.
- **ANT reduces high-frequency word bias**: Standard MLM predictions heavily favor common words (e.g., "good"), but ANT significantly reduces this bias, confirming that targeted secondary training can redirect model predictions toward more diverse and creative outputs.
- **Pattern combination matters**: The optimal pattern combinations differ by task — for SI, the best subset is {p1, p5} (Class I + Class II), supporting Ortony's (1979) hypothesis that the highlighted attribute is more salient in the vehicle domain. For SG, the best subset is {p3, p4} (Class I + Class II).
- **Automatic vs. human evaluation divergence**: Automatic evaluation scores are higher for SI than SG, while human evaluation scores show the opposite trend. This is attributed to the smaller candidate space for attributes (SI) versus the more varied and unexpected nature of vehicle choices (SG).

## Lessons Learned

- **Diversity-correctness trade-off**: Techniques that improve diversity (like ANT) may temporarily reduce correctness on standard metrics, but this can be compensated for with complementary techniques (PE, PS).
- **Manual patterns have limits**: Hand-designed patterns are heuristic and suboptimal. Automated pattern search can discover non-intuitive but effective pattern combinations that outperform full ensemble approaches.
- **Simile components have asymmetric properties**: Attributes are more constrained (often physical properties of the vehicle), while vehicles are more open-ended and creative. This asymmetry should be accounted for in evaluation and model design.
- **Inter-annotator agreement varies by task**: Human evaluation of simile interpretation achieves substantial agreement, while simile generation shows only moderate agreement, reflecting the inherent subjectivity in evaluating creative language generation.

## Practical Takeaways

- **ANT as a general technique**: The Adjective-Noun Mask Training approach could be applicable to other NLP tasks where prediction diversity is important and standard MLM outputs are overly generic.
- **Pattern ensemble is a simple but effective baseline**: Averaging predictions across multiple pattern variations is a low-cost method to improve robustness, even without pattern search.
- **Vehicle filtering is a practical heuristic**: For simile generation, filtering out vehicles that are too semantically similar to the tenor prevents trivial analogies and improves output quality.
- **Framework simplicity**: The overall framework is straightforward to implement (mask → predict → ensemble → search) and can be reproduced with publicly available code and models, as demonstrated by the authors' released GitHub repository and HuggingFace model.
