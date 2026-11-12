#!/usr/bin/env python3
"""Build the FilmTrail landing page and privacy policy, in seven languages (English at the root).

Run from the repository root:  python3 _build/filmtrail/build.py   (or python3 _build/build_all.py)
Text: _build/filmtrail/i18n/<code>.json and i18n/privacy/<code>.json. Layout: landing.html, privacy.html.
Pages are written to filmtrail/. Jekyll (GitHub Pages) skips folders starting with "_".
"""
import html, json, pathlib, re, urllib.parse

BUILD = pathlib.Path(__file__).resolve().parent
REPO = BUILD.parent.parent
OUT = REPO / "filmtrail"
SITE = json.loads((REPO / "_build" / "site.json").read_text(encoding="utf-8"))
BASE = SITE["base"] + "filmtrail/"
EMAIL = SITE["email"]
SCRIPT = (BUILD / "script.html").read_text(encoding="utf-8")
# Same seven languages as FilmDesk (the app itself is in English and Vietnamese).
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
esc = lambda s: html.escape(s, quote=True)


def lang_menu(folder, root, sub):
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
    return esc(f"mailto:{EMAIL}?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote))


def render(template, values, code, out):
    def fill(m):
        key = m.group(1)
        if key not in values:
            raise SystemExit(f"{code}: missing key {key} for {out.relative_to(REPO)}")
        return values[key]

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(re.sub(r"\{\{(\w+)\}\}", fill, template), encoding="utf-8")
    print("wrote", out.relative_to(REPO))


def frames_html(frames):
    out = []
    for i, f in enumerate(frames, 1):
        items = "\n".join(f"              <li>{esc(x)}</li>" for x in f["l"])
        out.append(f"""        <article class="frame text">
          <span class="edge" aria-hidden="true">FILMTRAIL 400 ▸ {i}</span>
          <span class="big-no" aria-hidden="true">{i:02d}</span>
          <div>
            <span class="no" aria-hidden="true">{i:02d} ▸ {i:02d}A</span>
            <h3>{esc(f["t"])}</h3>
            <p>{esc(f["p"])}</p>
            <ul>
{items}
            </ul>
          </div>
        </article>""")
    return "\n".join(out)


# Landing pages
template = (BUILD / "landing.html").read_text(encoding="utf-8")
for code, folder, tag, short, _ in LANGS:
    text = json.loads((BUILD / "i18n" / f"{code}.json").read_text(encoding="utf-8"))
    root = "../" * folder.count("/")
    values = {k: esc(v) for k, v in text.items() if isinstance(v, str)}
    values.update(
        frames=frames_html(text["frames"]),
        points="\n".join(
            f'          <div class="point"><span class="ic" aria-hidden="true">{i:02d}</span>'
            f"<div><b>{esc(b)}</b><span>{esc(s)}</span></div></div>"
            for i, (b, s) in enumerate(text["points"], 1)),
        faqs="\n".join(f"      <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in text["faqs"]),
        mail_href=mailto(text["mail_subject"], text["mail_body"]), email=EMAIL, email_wbr=EMAIL.replace("@", "@<wbr>"), code=code, html_lang=tag,
        url=BASE + folder, base=BASE, root=root, hreflangs=alternates(""), langmenu=lang_menu(folder, root, ""),
        lang_short=short, script=SCRIPT)
    render(template, values, code, OUT / folder / "index.html")

# Privacy policy. English is the official text. Section HTML is trusted (written here), so it is not escaped.
template = (BUILD / "privacy.html").read_text(encoding="utf-8")
for code, folder, tag, short, _ in LANGS:
    text = json.loads((BUILD / "i18n" / "privacy" / f"{code}.json").read_text(encoding="utf-8"))
    root = "../" * (folder.count("/") + 1)
    secs = text["sections"]
    note = ""
    if code != "en":
        note = (f'      <p class="tr-note"><span>{esc(text["tr_note"])}</span> '
                f'<a href="{root}privacy/" hreflang="en" lang="en">{esc(text["tr_link"])} →</a></p>')
    values = {k: esc(v) for k, v in text.items() if isinstance(v, str)}
    values.update(
        toc="\n".join(f'          <li><a href="#{s["id"]}"><span>{i:02d}</span>{esc(s["h"])}</a></li>'
                      for i, s in enumerate(secs, 1)),
        clauses="\n".join(
            f'        <section class="clause" id="{s["id"]}" aria-labelledby="h{i}">\n'
            f'          <h2 class="head" id="h{i}"><span class="n">{i:02d}</span>{esc(s["h"])}</h2>\n'
            f'          {s["html"].replace(">{{email}}<", ">" + EMAIL.replace("@", "@<wbr>") + "<").replace("{{email}}", EMAIL)}\n'
            f'          <a class="to-toc" href="#toc">↑ {esc(text["toc_h"])}</a>\n        </section>'
            for i, s in enumerate(secs, 1)),
        translation_note=note, email=EMAIL, code=code, html_lang=tag, updated_iso="2026-11-12",
        url=BASE + folder + "privacy/", base=BASE, root=root, hreflangs=alternates("privacy/"),
        langmenu=lang_menu(folder, root, "privacy/"), lang_short=short, script=SCRIPT)
    render(template, values, code, OUT / folder / "privacy" / "index.html")
