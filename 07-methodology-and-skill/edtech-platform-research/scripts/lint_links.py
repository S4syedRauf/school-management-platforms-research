#!/usr/bin/env python3
"""Enforce visible full URLs in Markdown reports.

Usage:
  lint_links.py report.md            # report problems, exit 1 if any
  lint_links.py report.md --fix      # rewrite [text](url) as "text (url)" in place

Checks:
  - embedded links [text](https://...) that hide the URL (images are ignored)
  - reference-style definitions [1]: https://... that render invisibly
  - bare domains without scheme (www.example.com) -> suggests https://
  - unencoded parentheses inside URLs
"""
import re
import sys

EMBED = re.compile(r"(?<!!)\[([^\]]+)\]\((https?://[^)\s]+)\)")
REFDEF = re.compile(r"^\s*\[[^\]]+\]:\s*https?://", re.M)
BARE = re.compile(r"(?<![/\w@.])(www\.[a-z0-9-]+\.[a-z.]{2,}[^\s)|]*)", re.I)
URL = re.compile(r"https?://[^\s|<>\"]+")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    fix = "--fix" in sys.argv
    text = open(path, encoding="utf-8").read()
    problems = []

    for m in EMBED.finditer(text):
        if m.group(1).strip() != m.group(2).strip():
            problems.append(f"embedded link: {m.group(0)[:90]}")
    for m in REFDEF.finditer(text):
        problems.append(f"hidden reference definition at offset {m.start()}")
    for m in BARE.finditer(text):
        problems.append(f"bare domain without scheme: {m.group(1)}")
    for m in URL.finditer(text):
        url = m.group(0)
        if "(" in url:
            problems.append(f"unencoded parenthesis in URL: {url}")

    if fix:
        def repl(m):
            label, url = m.group(1), m.group(2)
            return url if label.strip() == url.strip() else f"{label} ({url})"
        text = EMBED.sub(repl, text)
        open(path, "w", encoding="utf-8").write(text)
        print("Rewrote embedded links as visible URLs.")
        return

    if problems:
        print(f"{len(problems)} link problem(s) in {path}:")
        for p in problems[:200]:
            print(" -", p)
        sys.exit(1)
    print(f"OK: all links in {path} are visible full URLs.")


if __name__ == "__main__":
    main()
