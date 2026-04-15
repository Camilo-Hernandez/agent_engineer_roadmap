# AGENTS.md

## Project Shape
- Small Python 3.14 project that generates a PDF roadmap with ReportLab.
- Root entrypoint is `main.py`; running it calls `build_pdf()` and writes `hoja_de_ruta_ia_agents_engineer.pdf` at the repo root.
- Content is assembled from modular builders under `src/`:
  - `src/config.py`: document template, output path, color palette, shared paragraph styles.
  - `src/header.py`: title block and Gmail icon path (`assets/gmail_icon.png`).
  - `src/sections.py`: main roadmap sections and resource entries.
  - `src/comparison.py`: comparison table section.
  - `src/footer.py`: closing warning/footer.
  - `src/helpers.py`: shared section divider, URL/link formatting, resource block rendering.

## Verified Commands
- Use `uv` for environment/dependency management; the repo has `pyproject.toml`, `uv.lock`, and `.python-version` set to `3.14`.
- Verified import/run path: `uv run main.py`.
- There is no console script configured in `pyproject.toml`.

## Dependencies
- Runtime dependency declared in `pyproject.toml`: `reportlab>=4.4.10`.
- Locked transitive deps in `uv.lock`: `reportlab 4.4.10`, `pillow 12.1.1`, `charset-normalizer 3.4.6`.

## Automation Reality
- No CI workflows under `.github/workflows/`.
- No test, lint, formatter, typecheck, codegen, pre-commit, `Makefile`, `justfile`, `tox`, or `nox` config is present.
- `README.md` currently exists but is empty; do not rely on it for project behavior.

## Working Notes
- The generated PDF path is hardcoded as `OUTPUT_PATH = "hoja_de_ruta_ia_agents_engineer.pdf"` in `src/config.py`.
- Header rendering depends on `assets/gmail_icon.png`; keep that asset if editing author/contact output.
- Most roadmap copy is Spanish prose embedded directly in Python strings; keep text edits localized to the relevant section builder instead of introducing new data-loading layers unless requested.
- `__pycache__/` and `.venv/` are ignored by `.gitignore`; the output PDF is not ignored.
