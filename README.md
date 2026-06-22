# AI Survivor Guide

This repository builds a small, versioned ebook/manual about understanding the AI era.

Current status: sample/prototype. The first milestone is the publishing pipeline: Markdown in, PDF out, GitHub Release assets attached.

## Audience

The ebook is for ordinary people, beginners, and non-technical professionals trying to understand AI, work, automation, economics, learning, and human relevance.

Core sentence:

> You do not need to become an AI expert. You need enough literacy to make conscious decisions in a world shaped by AI.

This is not a prompt-tricks guide, a product tutorial, or a path to becoming a software engineer.

## Books

- Portuguese (Brazil): `books/pt-br/sobrevivendo-a-era-da-ia.md`
- English (US): `books/en-us/surviving-the-ai-era.md`

Generated PDFs are written to `dist/`:

- `dist/sobrevivendo-a-era-da-ia-pt-br.pdf`
- `dist/surviving-the-ai-era-en-us.pdf`

When built with a version, the version is included in the filename.

## Local Build

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build_pdf.py
```

Optional:

```bash
python scripts/build_pdf.py --version v0.1.0
python scripts/build_pdf.py --book pt-br
python scripts/build_pdf.py --book en-us
```

## Release

Push a version tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

GitHub Actions builds both PDFs and creates a GitHub Release with the generated files attached.

## License

The ebook text is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

Attribution should mention Henrique Riccio. Commercial use requires permission.

See [LICENSE.md](LICENSE.md) for the project-specific license note.
