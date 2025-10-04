# Prompting & Sampling Cheatsheet

- Role: start with "You are an expert X" to set behavior.
- Context: include required facts, examples, and constraints.
- Format: demand output format (bullets, JSON, table) to simplify parsing.
- Chain-of-thought: only use when you need step-by-step reasoning (and be mindful of safety).
- Sampling: temperature 0.0-1.0 (0.0 deterministic), top-k 0-50, top-p 0.8-0.95.

Top recipes:

- Role + Task + Constraints + Format + Example
- Few-shot: include 1-3 short Q/A examples before the main query.

# Cheatsheet: Prompt recipes & sampling

- Role: "You are an expert X..."
- Context: Provide short context and constraints
- Format: "Respond in 3 bullet points, each <= 18 words"
- Sampling: temperature 0.7 for creativity, 0.0 for deterministic, top_p 0.9, top_k 50
