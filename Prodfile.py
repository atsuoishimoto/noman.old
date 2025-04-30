# type: ignore
import os
import datetime
import json
from dotenv import load_dotenv
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup
import re
import sys
import subprocess
import mistune
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name

load_dotenv()

from anthropic import Anthropic

api_key = os.environ["NOMAN_ANTHROPIC_API_KEY"]
client = Anthropic(api_key=api_key)

import make_summary


TODAY = datetime.datetime.now(tz=datetime.UTC).date().strftime("%Y/%m/%d")
COMMANDDIR = Path("./commands")
COMMANDS = [p for p in COMMANDDIR.glob("*") if p.is_dir()]
PROMPT = Path("./prompts/prompt")
FORMAT = Path("./prompts/format")
MAX_TOKENS = 10000
WWW = Path("./www")

JINJA = Environment(
    loader=FileSystemLoader("./templates"),
    autoescape=select_autoescape(
        enabled_extensions=("html", "xml", "j2"),
        default_for_string=True,
    ),
)


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


def generate_document(*prompts, max_tokens):
    contents = []
    for prompt in prompts:
        if not prompt.strip():
            continue
        message = {
            "type": "text",
            "text": prompt,
        }
        contents.append(message)

    messages = [{"role": "user", "content": contents}]

    import pprint

    pprint.pprint(messages)

    # check OverloadedError?
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=max_tokens,
        temperature=0.2,
        messages=messages,
    )
    if str(response.stop_reason) != "end_turn":
        raise ValueError(
            f"generate_document failed: "
            f"stop_reason: {response.stop_reason!s} "
            f"usage: {response.usage}\n"
            f"{response.content[0].text}"
        )

    return response.content[0].text, response.stop_reason, response.usage


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

    text, stop_reason, usage = generate_document(*prompts, max_tokens=MAX_TOKENS)

    target.write_text(text)

    result = json.dumps(
        {"stop_reason": str(stop_reason), "usage": str(usage)},
        indent=2,
        ensure_ascii=False,
    )
    resultsdir = target.parent / "results"
    resultsdir.mkdir(parents=True, exist_ok=True)
    (resultsdir / f"{target.stem}.json").write_text(result)


@task
def summary():
    for lang in ["ja", "en"]:
        dest = WWW / lang
        dest.mkdir(parents=True, exist_ok=True)

        d = make_summary.make_summary(Path(f"pages/{lang}"))
        d = {k: {"summary": v} for k, v in sorted(d.items())}
        for k, v in d.items():
            v.update(read_commandinfo(k))

        text = json.dumps(d, ensure_ascii=False, indent=2)
        (dest / "summary.json").write_text(text.strip())
        (dest / "summary.js").write_text(f"pages = {text.strip()};")


def read_commandinfo(command):
    conf = Path("commands") / command / "command.yaml"
    if conf.is_file():
        cmd = yaml.safe_load(conf.read_text())
        return cmd
    return {}


def make_summary(dir):
    d = {}
    files = dir.glob("*.md")
    for file in files:
        print(file)
        src = file.read_text()
        m = re.search(r"#.*\n(?P<header>([^#].*\n+))", src)
        if not m:
            print("invalid md", file)
            sys.exit(1)
        p = subprocess.Popen(
            ["pandoc", "-f", "markdown", "-t", "plain", "--wrap=none"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            encoding="utf8",
        )
        stdout, stderr = p.communicate((m["header"] + "\n"))
        p.stdin.close()
        p.wait()
        stdout = "".join(stdout.split("\n")).strip()
        d[file.stem] = {"summary": stdout, **read_commandinfo(file.stem)}

    return sorted(d.items())


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            if info == "mermaid":
                return "<pre class='mermaid'>\n" + mistune.escape(code) + "\n</pre>"
            else:
                lexer = get_lexer_by_name(info, stripall=True)
                formatter = html.HtmlFormatter(noclasses=True, style="tango")
                return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"


renderer = HighlightRenderer()
markdown = mistune.create_markdown(renderer=renderer)


@task
def build_www():
    command = JINJA.get_template("command.html.j2")
    commandlist = JINJA.get_template("commandlist.html.j2")

    for lang in ["ja", "en"]:
        dest = WWW / lang
        pagedir = Path(f"pages/{lang}")
        for md in pagedir.glob("*.md"):
            html = Markup(markdown(md.read_text()))
            commandname = md.stem
            page = command.render(lang="ja", content=html, command=commandname)
            (dest / "pages" / (commandname + ".html")).write_text(page)

            src = md.read_text()
            m = re.search(r"#.*\n(?P<header>([^#].*\n+))", src)
            if not m:
                print("invalid md", file)
                sys.exit(1)

        summary = make_summary(pagedir)
        page = commandlist.render(lang="ja", commands=summary)
        (dest / "commandlist.html").write_text(page)
        j = json.dumps(dict(summary), ensure_ascii=False, indent=2)
        (dest / "summary.js").write_text(f"pages = {j.strip()};")


@task
def build_cli():
    for lang in ["ja", "en"]:
        run("cp", f"pages/{lang}/*.md", f"noman-cli/src/noman_cli/pages/{lang}")
        run("cp", f"pages/{lang}/*.md", f"noman-cli/src/noman_cli/pages/{lang}")
    run("uv build", cwd="noman-cli")
