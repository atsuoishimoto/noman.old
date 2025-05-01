import mistune
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
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
dump = mistune.create_markdown(
    renderer=lambda tokens, state: ansi_renderer.dump(tokens)
)

src = """
text1 test1-1  
test1-2

*aaa* **bbb** ***bbb*** 

text2

text3
[aaa](http://aaa.com)


abcdefg
> quote?
> quote?
dfasdf

defg

`abcdefgあいうえお`

# heading1 [sadfasd](kasjfnasjkn)
safdasfdas
22222222222222
## heading 2 
### heading 3 
#### heading 4

- a1111
  * b22222  
    d44 `44` 44
  * cccccc
- ddddddddd


2. sadfasdfa
1. asdflkmasdfklm

``` python
def a():
    1+1
```




```
def a():
    1+1
```

- sadfl;kmas asdf asdfasdf asdfadfas fasdf adf asdf  
  ;asl,dfma;sldf,as fasdf asdf asdf aqsd ff aqsdf asd fasdfasdf
  asd;flm,as;dfm,as;dfm

- asdlfkmasldfmkaslfdm asdfas dfas df asdf as
  asdflkmasdlfkma asdf asdf as dfaf 

"""


if 0:
    print(src)
    print("-------------")

    dump(src)

    print("-------------")
    s = markdown(src)
    print("-------------")
    print(s)
    print(repr(s))


if 0:
    s = """
# heading1
22222222222222
"""
    s = markdown(s)
    print(s)
    print(repr(s))


if 0:
    # 表示がおかしい
    s = """
- 11111111111

  22222222222222222222222
"""

    s = markdown(s)
    print(s)
    dump(s)


if 1:
    src = open("../pages/ja/ls.md").read()
    s = markdown(src)
    print(s)
