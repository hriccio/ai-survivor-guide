#!/usr/bin/env python3
"""Build the ebook Markdown sources into PDF files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import markdown
from weasyprint import CSS, HTML


ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = ROOT / "dist"
CSS_PATH = ROOT / "assets" / "css" / "ebook.css"


@dataclass(frozen=True)
class Book:
    key: str
    source: Path
    output_stem: str


BOOKS = {
    "pt-br": Book(
        key="pt-br",
        source=ROOT / "books" / "pt-br" / "sobrevivendo-a-era-da-ia.md",
        output_stem="sobrevivendo-a-era-da-ia-pt-br",
    ),
    "en-us": Book(
        key="en-us",
        source=ROOT / "books" / "en-us" / "surviving-the-ai-era.md",
        output_stem="surviving-the-ai-era-en-us",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build ebook PDFs from Markdown sources.")
    parser.add_argument(
        "--book",
        choices=sorted(BOOKS),
        help="Build only one language version. Defaults to all books.",
    )
    parser.add_argument(
        "--version",
        help="Optional release version to include in generated filenames, for example v0.1.0.",
    )
    return parser.parse_args()


def markdown_to_html(source: Path) -> str:
    if not source.exists():
        raise FileNotFoundError(f"Missing source file: {source}")

    text = source.read_text(encoding="utf-8")
    body = markdown.markdown(
        text,
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.meta",
            "markdown.extensions.toc",
        ],
        output_format="html5",
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{source.stem}</title>
</head>
<body>
{body}
</body>
</html>
"""


def output_path(book: Book, version: str | None) -> Path:
    suffix = f"-{version}" if version else ""
    return DIST_DIR / f"{book.output_stem}{suffix}.pdf"


def build_book(book: Book, version: str | None) -> Path:
    if not CSS_PATH.exists():
        raise FileNotFoundError(f"Missing CSS file: {CSS_PATH}")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    html = markdown_to_html(book.source)
    target = output_path(book, version)
    HTML(string=html, base_url=str(ROOT)).write_pdf(target, stylesheets=[CSS(str(CSS_PATH))])
    return target


def main() -> int:
    args = parse_args()
    selected_books = [BOOKS[args.book]] if args.book else BOOKS.values()

    for book in selected_books:
        target = build_book(book, args.version)
        print(target.relative_to(ROOT))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
