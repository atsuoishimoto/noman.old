import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape
import md2html

env = Environment(
    loader=FileSystemLoader("./templates"),
    autoescape=select_autoescape(
        enabled_extensions=('html', 'xml', 'j2'),
        default_for_string=True,
    )
)


www_ja = Path("www/ja")

index = env.get_template("index.html.j2")
ja = index.render(lang="ja")
(www_ja / "index.html").write_text(ja)


command = env.get_template("command.html.j2")

for md in Path("pages/ja").glob("*.md"):
    html = Markup(md2html.md_to_html(md))
    commandname = md.stem
    page = command.render(lang="ja", content=html, command=commandname)
    (www_ja / "pages" / (commandname+".html")).write_text(page)
    

commandlist = env.get_template("commandlist.html.j2")
summary = json.loads((www_ja/"summary.json").read_text())
summary = sorted(summary.items())
page = commandlist.render(lang="ja", commands=summary)
(www_ja / "commandlist.html").write_text(page)
