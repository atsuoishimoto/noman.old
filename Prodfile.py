# type: ignore

import datetime
import json
from dotenv import load_dotenv
import yaml

load_dotenv()

import gen_noman
import make_summary
from md2html import md_to_html
from pathlib import Path


TODAY = datetime.datetime.now(tz=datetime.UTC).date().strftime("%Y/%m/%d")
COMMANDDIR = Path("./commands")
COMMANDS = [p for p in COMMANDDIR.glob("*") if p.is_dir()]
PROMPT = Path("./prompts/prompt")
FORMAT = Path("./prompts/format")
MAX_TOKENS = 10000


def lang_prompt(target, stem):
    lang = str(target).split("/")[1]
    dir = Path("./prompts/langs/") / lang
    if dir.is_dir():
        return dir / "*"


def command_prompt(target, stem):
    return (COMMANDDIR / stem).glob("*")


@rule("commands/*/.empty")
def build_command_dir(target):
    p = Path(target)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("")


@rule(
    "pages/*/%.md",
    uses="commands/%/.empty",
    depends=(PROMPT, command_prompt, lang_prompt, FORMAT),
)
def build_noman(target, *deps):
    target = Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    command = target.stem
    lang = target.parts[1]

    prompts = [Path(p).read_text() for p in deps]
    prompts.append(f"""
Command to Explain: {command}
Write in {lang}.
TODAY is {TODAY}.
""")

    if target.is_file():
        current = target.read_text()
        prompts.append(f"<current-documnent>{current}</current-document>")

    text, stop_reason, usage = gen_noman.generate_document(
        *prompts, max_tokens=MAX_TOKENS
    )

    target.write_text(text)

    result = json.dumps(
        {"stop_reason": str(stop_reason), "usage": str(usage)},
        indent=2,
        ensure_ascii=False,
    )
    resultsdir = target.parent / "results"
    resultsdir.mkdir(parents=True, exist_ok=True)
    (resultsdir / f"{target.stem}.json").write_text(result)

def read_commandinfo(command):
    conf = Path("commands") / command / "command.yaml"
    if conf.is_file():
        cmd = yaml.safe_load(conf.read_text())
        return cmd
    return {}

@task
def summary():
    dest = Path("www/ja")
    dest.mkdir(parents=True, exist_ok=True)

    d = make_summary.make_summary(Path("pages/ja"))
    d = {k: {"summary": v} for k, v in sorted(d.items())}
    for k, v in d.items():
        v.update(read_commandinfo(k))

    text = json.dumps(d, ensure_ascii=False, indent=2)
    (dest / "summary.json").write_text(text.strip())
    (dest / "summary.js").write_text(f"pages = {text.strip()};")


    dest = Path("www/en")
    dest.mkdir(parents=True, exist_ok=True)

    d = make_summary.make_summary(Path("pages/en"))
    d = {k: {"summary": v} for k, v in sorted(d.items())}
    for k, v in d.items():
        v.update(read_commandinfo(k))
    text = json.dumps(d, ensure_ascii=False, indent=2)
    (dest / "summary.js").write_text(f"pages = {text.strip()};")

@task
def text():
    for md in Path("pages/ja").glob("*.md"):
        txt = md.with_suffix(".txt")
        run("pandoc", "-f", "markdown", "-t", "plain", "--wrap=none", "-o", txt, md)

    for md in Path("pages/en").glob("*.md"):
        txt = md.with_suffix(".txt")
        run("pandoc", "-f", "markdown", "-t", "plain", "--wrap=none", "-o", txt, md)

@task
def html():
    template = Path("templates/ja.html").read_text()
    dest = Path("www/ja/pages")
    dest.mkdir(parents=True, exist_ok=True)

    for md in Path("pages/ja").glob("*.md"):
        html = template.replace("{{ command }}", md.stem)
        html = html.replace("{{ content }}", md_to_html(md))
        (dest / md.with_suffix(".html").name).write_text(html)

    template = Path("templates/en.html").read_text()
    dest = Path("www/en/pages")
    dest.mkdir(parents=True, exist_ok=True)

    for md in Path("pages/en").glob("*.md"):
        html = template.replace("{{ command }}", md.stem)
        html = html.replace("{{ content }}", md_to_html(md))
        (dest / md.with_suffix(".html").name).write_text(html)


