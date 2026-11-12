#!/usr/bin/env python3
"""Build the Film Wanderer home page (index.html, vi/index.html). Run from the repository root."""
import html, json, pathlib, re

BUILD = pathlib.Path(__file__).resolve().parent
REPO = BUILD.parent.parent
SITE = json.loads((REPO / "_build" / "site.json").read_text(encoding="utf-8"))
BASE = SITE["base"]
# code, folder, hreflang, short label, native name, FilmDesk folder, FilmTrail folder
LANGS = [("en", "", "en", "EN", "English", "", ""), ("vi", "vi/", "vi", "VI", "Tiếng Việt", "vi/", "vi/")]
text_all = json.loads((BUILD / "i18n.json").read_text(encoding="utf-8"))
template = (BUILD / "home.html").read_text(encoding="utf-8")
for code, folder, tag, short, _, fd, ft in LANGS:
    root = "../" * folder.count("/")
    values = {k: html.escape(v, quote=True) for k, v in text_all[code].items()}
    menu = "\n".join(
        f'        <li><a href="./" aria-current="page" lang="{t}">{n}</a></li>' if f == folder
        else f'        <li><a href="{root}{f}" lang="{t}" hreflang="{t}">{n}</a></li>'
        for _, f, t, _, n, _, _ in LANGS)
    alts = "\n".join(f'<link rel="alternate" hreflang="{t}" href="{BASE}{f}">' for _, f, t, _, _, _, _ in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}">'
    values.update(html_lang=tag, url=BASE + folder, root=root, hreflangs=alts, langmenu=menu, lang_short=short,
                  folder=fd, ft_folder=ft, email=SITE["email"], play=html.escape(SITE["play_developer"], quote=True))
    out = REPO / folder / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(re.sub(r"\{\{(\w+)\}\}", lambda m: values[m.group(1)], template), encoding="utf-8")
    print("wrote", out.relative_to(REPO))
