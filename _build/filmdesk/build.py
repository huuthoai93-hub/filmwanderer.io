#!/usr/bin/env python3
"""Build the FilmDesk landing pages and privacy policy: one static page of each per language.

Run from the repository root:  python3 _build/filmdesk/build.py   (or python3 _build/build_all.py)
Text lives in _build/filmdesk/i18n/<code>.json (landing) and _build/filmdesk/i18n/privacy/<code>.json (policy),
layout in _build/filmdesk/template.html and _build/filmdesk/privacy.html. Pages are written to filmdesk/.
Jekyll (GitHub Pages) skips folders starting with "_", so _build is not published.
"""
import html, json, pathlib, re, urllib.parse

BUILD = pathlib.Path(__file__).resolve().parent
REPO = BUILD.parent.parent
ROOT = REPO / "filmdesk"
BASE = json.loads((REPO / "_build" / "site.json").read_text(encoding="utf-8"))["base"] + "filmdesk/"
# Order matches the app's language picker (AppLanguage).
LANGS = [
    # code, folder, html lang / hreflang, short label, native name
    ("en", "", "en", "EN", "English"),
    ("de", "de/", "de", "DE", "Deutsch"),
    ("fr", "fr/", "fr", "FR", "Français"),
    ("zh-TW", "zh-tw/", "zh-TW", "繁中", "繁體中文"),
    ("ja", "ja/", "ja", "日本語", "日本語"),
    ("ko", "ko/", "ko", "한국어", "한국어"),
    ("vi", "vi/", "vi", "VI", "Tiếng Việt"),
]


def lang_menu(folder, root, sub):
    """Language menu items linking to the same page (sub = "" or "privacy/") in each language."""
    items = []
    for _, f2, t2, _, name in LANGS:
        if f2 == folder:
            items.append(f'        <li><a href="./" aria-current="page" lang="{t2}">{name}</a></li>')
        else:
            items.append(f'        <li><a href="{root}{f2}{sub}" lang="{t2}" hreflang="{t2}">{name}</a></li>')
    return "\n".join(items)


def alternates(sub):
    return "\n".join(
        f'<link rel="alternate" hreflang="{tag}" href="{BASE}{folder}{sub}">' for _, folder, tag, _, _ in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{sub}">'


def mailto(subject, body=None):
    q = {"subject": subject}
    if body is not None:
        q["body"] = body
    return html.escape("mailto:filmwanderer.support@gmail.com?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote), quote=True)


def render(template, values, code, out):
    def fill(m):
        key = m.group(1)
        if key not in values:
            raise SystemExit(f"{code}: missing key {key} for {out.relative_to(ROOT)}")
        return values[key]

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(re.sub(r"\{\{(\w+)\}\}", fill, template), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


# Landing pages: <folder>index.html
template = (BUILD / "template.html").read_text(encoding="utf-8")
for code, folder, tag, short, _ in LANGS:
    text = json.loads((BUILD / "i18n" / f"{code}.json").read_text(encoding="utf-8"))
    root = "../" * folder.count("/")
    values = {k: html.escape(v, quote=True) for k, v in text.items()}
    # Meta line: keep each item whole and end a wrapped line on the separator, never start one with it.
    parts = [html.escape(x) for x in text["hero_meta"].split(" · ")]
    values["hero_meta"] = " ".join(
        f'<span class="nw">{x}{" ·" if i < len(parts) - 1 else ""}</span>' for i, x in enumerate(parts))
    values.update(mail_href=mailto(text["mail_subject"], text["mail_body"]), code=code, html_lang=tag, url=BASE + folder,
                  base=BASE, root=root, hreflangs=alternates(""), langmenu=lang_menu(folder, root, ""), lang_short=short)
    render(template, values, code, ROOT / folder / "index.html")

# Privacy policy: <folder>privacy/index.html. English is the official text; the others are translations of it.
# Values in _build/i18n/privacy/*.json may hold inline HTML (<code>, <strong>, <a>), so only attribute values are escaped.
ATTR_KEYS = {"title", "meta_description", "og_description", "logo_alt", "nav_label", "lang_label"}
template = (BUILD / "privacy.html").read_text(encoding="utf-8")
for code, folder, tag, short, _ in LANGS:
    text = json.loads((BUILD / "i18n" / "privacy" / f"{code}.json").read_text(encoding="utf-8"))
    root = "../" * (folder.count("/") + 1)
    values = {k: html.escape(v, quote=True) if k in ATTR_KEYS else v for k, v in text.items()}
    note = ""
    if code != "en":
        note = (f'      <p class="tr-note"><span>{text["tr_note"]}</span> '
                f'<a href="{root}privacy/" hreflang="en" lang="en">{text["tr_link"]} →</a></p>')
    values.update(translation_note=note, mail_href=mailto(text["mail_subject"]), code=code, html_lang=tag,
                  url=BASE + folder + "privacy/", base=BASE, root=root, hreflangs=alternates("privacy/"),
                  langmenu=lang_menu(folder, root, "privacy/"), lang_short=short)
    render(template, values, code, ROOT / folder / "privacy" / "index.html")
