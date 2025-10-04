# Generative AI Workshop — [Your Workshop Name]

Welcome — this repo contains slides, runnable demos (Colab + Python), prompt examples, and notes for the workshop.

## Structure

- `slides/` — presentation slides per session section
- `notebooks/` — Colab-ready notebooks for live demos
- `code/` — simple scripts (Python) for local/Colab runs
- `examples/` — saved outputs and prompt examples
- `docs/quick_start.md` — how to run demos quickly

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
