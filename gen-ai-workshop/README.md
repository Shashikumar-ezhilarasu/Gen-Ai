# Generative AI Workshop

Welcome — this repo contains slides, runnable demos (Colab + Python), prompt examples, and notes for the workshop.

## Structure

- `slides/` — presentation slides per session section
- `notebooks/` — Colab-ready notebooks for live demos
- `code/` — simple scripts (Python) for local/Colab runs
- `examples/` — saved outputs and prompt examples
- `docs/quick_start.md` — how to run demos quickly

Direct useful files and paths (relative to repo root `gen-ai-workshop/`):

- Slides:

  - `gen-ai-workshop/slides/01-intro.pptx` (outline in `gen-ai-workshop/slides/01-intro.md`)
  - `gen-ai-workshop/slides/02-how-it-works.pptx` (outline in `gen-ai-workshop/slides/02-how-it-works.md`)
  - `gen-ai-workshop/slides/03-prompt-engineering.pptx` (outline in `gen-ai-workshop/slides/03-prompt-engineering.md`)
  - `gen-ai-workshop/slides/04-live-demos.pptx` (outline in `gen-ai-workshop/slides/04-live-demos.md`)
  - `gen-ai-workshop/slides/05-ethics-qna.pptx` (outline in `gen-ai-workshop/slides/05-ethics-qna.md`)

- Notebooks (Open in Colab links are included in the notebooks):

  - `gen-ai-workshop/notebooks/demo_text_generation.ipynb`
  - `gen-ai-workshop/notebooks/demo_image_generation.ipynb`

- Code demos:

  - `gen-ai-workshop/code/text_generation.py` (run `python code/text_generation.py --example`)
  - `gen-ai-workshop/code/image_generation.py` (GPU/Colab recommended)
  - `gen-ai-workshop/code/prompt_examples.py` (prompt engineering examples)

- Examples and fallbacks:

  - `gen-ai-workshop/examples/outputs/demo_text_example.txt`
  - `gen-ai-workshop/examples/outputs/demo_image_example.svg`
  - `gen-ai-workshop/examples/sample_prompts.md`
  - `gen-ai-workshop/examples/exercises.md`

- Docs and learning resources:

  - `gen-ai-workshop/docs/quick_start.md`
  - `gen-ai-workshop/docs/resources.md`
  - `gen-ai-workshop/docs/beginner_projects.md` (LLM/RAG + Google AI / NotebookLM project links)

- Cheatsheet and legal:
  - `gen-ai-workshop/CHEATSHEET.md`
  - `gen-ai-workshop/DISCLAIMER.md`
  - `gen-ai-workshop/LICENSE` (code: MIT)
  - `gen-ai-workshop/SLIDES_LICENSE` (slides: CC-BY)

## Quick start (local)

1. Clone repo `git clone <repo-url>`
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Run `python code/text_generation.py --example`

Prefer using the notebooks in `notebooks/` for participants (Open in Colab badge included).

## License

Slides: CC-BY; Code: MIT.

Questions / issues: Use GitHub Issues or Discussions.

Cheatsheet: see `CHEATSHEET.md` for quick prompting recipes and sampling settings.

Notebooks include an "Open in Colab" link at the top of each demo. If you plan to use Colab during the workshop, enable GPU for the image demo notebook.
