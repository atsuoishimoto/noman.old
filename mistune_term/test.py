import sys
import mistune
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
from pathlib import Path
import ansi_renderer

class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        breakpoint()
        if info:
            if info == "mermaid":
                return "<pre class='mermaid'>\n" + mistune.escape(code) + "\n</pre>"
            else:
                lexer = get_lexer_by_name(info, stripall=True)
                formatter = html.HtmlFormatter(noclasses=True, style="tango")
                return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"


renderer = ansi_renderer.ANSIRenderer()
markdown = mistune.create_markdown(renderer=renderer)

src = """
text1 *test1-1*  
test1-2

text2

text3
"""

s = markdown(src)
print("-------------")
print(s)
