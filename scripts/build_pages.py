#!/usr/bin/env python3
"""Build the GitHub Pages copy of Dinner Decide.

index.html is written for Claude, which wraps the page in its own <html>/<head>.
This wraps the same file in a normal HTML document and writes docs/index.html.
Outside Claude the app saves to the browser and shares picks between phones as links.

Usage: python3 scripts/build_pages.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
split = src.index("<header")
head_part, body_part = src[:split], src[split:]
# The page already declares a viewport for when it is served as-is; the wrapper below adds its own.
head_part = "\n".join(l for l in head_part.splitlines() if 'name="viewport"' not in l)

icon = ("data:image/svg+xml,"
        "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
        "%3Crect width='64' height='64' rx='14' fill='%232f7a4a'/%3E"
        "%3Ccircle cx='32' cy='34' r='17' fill='none' stroke='white' stroke-width='5'/%3E"
        "%3C/svg%3E")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#2f7a4a">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Dinners">
<meta name="description" content="Decide the week's dinners together, then get the shopping list.">
<link rel="icon" href="{icon}">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head_part.strip()}
</head>
<body>
{body_part.strip()}
</body>
</html>
"""
out = root / "docs" / "index.html"
out.write_text(page, encoding="utf-8")
print(f"Wrote {out.relative_to(root)} ({len(page):,} bytes)")
