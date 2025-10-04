raw = "Summarize AI."

improved = """
You are an expert AI tutor. Summarize the field of Generative AI in **3 bullet points**, each <= 18 words, focusing on core concepts and one real-world use.
"""

few_shot = """
Q: What is a diffusion model?
A: A generative model that iteratively refines noise into an image using learned denoising steps.

Now, apply same clarity to: Summarize Generative AI:
"""

print("RAW PROMPT:\n", raw)
print("\nIMPROVED PROMPT:\n", improved)
print("\nFEW-SHOT PROMPT:\n", few_shot)
