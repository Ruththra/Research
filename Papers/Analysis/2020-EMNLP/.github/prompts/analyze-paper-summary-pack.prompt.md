---
description: "Analyze an attached research paper and create six summary markdown files"
name: "Paper Summary Pack"
argument-hint: "Attached paper PDF and output folder"
agent: "agent"
---
Analyze the attached research paper and create the following six Markdown files in the current workspace:

1. `problem.md`
2. `existing_works.md`
3. `methodology.md`
4. `limitations.md`
5. `future_work.md`
6. `learnings.md`

Requirements:
- Read the entire paper before generating any files.
- Use clear Markdown headings and subheadings.
- Extract information only from the paper; do not invent content.
- Keep technical details accurate.
- Include bullet points where appropriate.
- Use concise academic writing.
- If a section is not explicitly stated in the paper, infer it from the content and clearly mention that it is inferred.
- Save each section as a separate Markdown file.
- Return the complete content for all six Markdown files separately.

Use this structure for each file:

`problem.md`
- `# Problem Statement`
- `## Background`
- `## Problem Definition`
- `## Research Objectives`
- `## Key Challenges`

`existing_works.md`
- `# Existing Works`
- `## Previous Approaches`
- `## Related Research`
- `## Gaps in Existing Solutions`

`methodology.md`
- `# Methodology`
- `## Overview`
- `## Data Collection`
- `## System/Model Design`
- `## Algorithms and Techniques`
- `## Evaluation Process`

`limitations.md`
- `# Limitations`
- `## Technical Limitations`
- `## Dataset Limitations`
- `## Experimental Limitations`
- `## Threats to Validity`

`future_work.md`
- `# Future Work`
- `## Short-Term Improvements`
- `## Long-Term Research Directions`
- `## Potential Extensions`

`learnings.md`
- `# Key Learnings`
- `## Main Contributions`
- `## Important Findings`
- `## Lessons Learned`
- `## Practical Takeaways`
