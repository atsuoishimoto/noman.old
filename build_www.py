from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape

env = Environment(
    loader=FileSystemLoader("./templates"),
    autoescape=select_autoescape(
        enabled_extensions=('html', 'xml', 'j2'),
        default_for_string=True,
    )
)


index = env.get_template("index.html.j2")
ja = index.render(lang="ja")
print(ja)