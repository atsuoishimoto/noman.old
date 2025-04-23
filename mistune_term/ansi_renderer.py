import pprint
from textwrap import indent
from typing import Any, Dict, Iterable, List, cast

from mistune.core import BaseRenderer, BlockState
from mistune.util import strip_end

import theme



def _render_list_item(
    renderer: "BaseRenderer",
    parent: Dict[str, Any],
    item: Dict[str, Any],
    state: "BlockState",
) -> str:
    leading = cast(str, parent["leading"])
    text = ""
    for tok in item["children"]:
        print("2222222222222222222222222", tok)
        if tok["type"] == "list":
            tok["parent"] = parent
        elif tok["type"] == "blank_line":
            continue
        text += renderer.render_token(tok, state)

    lines = text.splitlines()
    text = (lines[0] if lines else "") + "\n"
    prefix = " " * len(leading)
    for line in lines[1:]:
        if line:
            text += prefix + line + "\n"
        else:
            text += "\n"
    return leading + text


def _render_ordered_list(renderer: "BaseRenderer", token: Dict[str, Any], state: "BlockState") -> Iterable[str]:
    attrs = token["attrs"]
    start = attrs.get("start", 1)
    for item in token["children"]:
        leading = str(start) + token["bullet"] + " "
        parent = {
            "leading": leading,
            "tight": token["tight"],
        }
        yield _render_list_item(renderer, parent, item, state)
        start += 1


def _render_unordered_list(renderer: "BaseRenderer", token: Dict[str, Any], state: "BlockState") -> Iterable[str]:
    parent = {
        "leading": token["bullet"] + " ",
        "tight": token["tight"],
    }
    for item in token["children"]:
        yield _render_list_item(renderer, parent, item, state)

def render_list(renderer: "BaseRenderer", token: Dict[str, Any], state: "BlockState") -> str:
    attrs = token["attrs"]
    if attrs["ordered"]:
        children = _render_ordered_list(renderer, token, state)
    else:
        children = _render_unordered_list(renderer, token, state)

    text = "".join(children)
    parent = token.get("parent")
    if parent:
        if parent["tight"]:
            return text
        return text + "\n"
    return strip_end(text) + "\n"



class StyleManager:
    def __init__(self, theme):
        self.theme = theme
        self.fg = theme.fg.default
        self.bg = theme.bg.default
        self.attrs = set()
    
    @contextmanager
    def style(self, name):
        fg = None
        bg = None
        attr = {}

        style = getattr(self.theme, name)
        if style.fg and (style.fg is not self.fg):
            fg = style.fg

        if style.bg and (style.bg is not self.bg):
            bg = style.bg

        attr = style.attr - self.attr

        s = []
        e = []
        if attr:
            s = [attr.reset, *(style.attr | self.attr), fg or self.fg, bg or self.bg)
            e = [attr.reset, *self.attr, self.fg, self.bg)
        else:
            if fg:
                s.append(fg)
                e.append(self.fg)
            if bg:
                s.append(bg)
                e.append(self.bg)
    if fg:
        self.fg = fg

    if bg:
        self.bg = bg

    yield ("".join(s), "".join(e))

    self.fg = save_fg
    self.bg = self.save_bg
    self.attr = self.save_attr

    def __getattr__(self, name):
        return self.style(name)

class ANSIRenderer(BaseRenderer):
    """A renderer for converting Markdown to ANSI colered text."""

    THEME = theme.Dark

    def __init__(self):
        self.theme = StyleManager(self.THEME)

    def __call__(self, tokens: Iterable[Dict[str, Any]], state: BlockState) -> str:

        out = self.render_tokens(tokens, state)
        return strip_end(out)


    def render_token(self, token: Dict[str, Any], state: BlockState) -> str:
        pprint.pprint(token)
        return super().render_token(token, state)

    def render_children(self, token: Dict[str, Any], state: BlockState) -> str:
        children = token["children"]
        return self.render_tokens(children, state)

    def blank_line(self, token, state):
        return ""

    def text(self, token: Dict[str, Any], state: BlockState) -> str:
        return token["raw"].rstrip()

    def emphasis(self, token: Dict[str, Any], state: BlockState) -> str:
        with self.theme.emphasis as s, e:
            return s+self.render_children(token, state)+e

    def strong(self, token: Dict[str, Any], state: BlockState) -> str:
        return "**" + self.render_children(token, state) + "**"

    def link(self, token: Dict[str, Any], state: BlockState) -> str:
        attrs = token["attrs"]
        text = self.render_children(token, state)
        return "`" + text + " <" + cast(str, attrs["url"]) + ">`__"

    def image(self, token: Dict[str, Any], state: BlockState) -> str:
        return "{Images are not supported}"

    def codespan(self, token: Dict[str, Any], state: BlockState) -> str:
        return "``" + cast(str, token["raw"]) + "``"

    def linebreak(self, token: Dict[str, Any], state: BlockState) -> str:
        return "\n"

    def softbreak(self, token: Dict[str, Any], state: BlockState) -> str:
        return " "

    def inline_html(self, token: Dict[str, Any], state: BlockState) -> str:
        return ""

    def paragraph(self, token: Dict[str, Any], state: BlockState) -> str:
        children = token["children"]
        text = self.render_tokens(children, state)
        return text + "\n\n"

    def heading(self, token: Dict[str, Any], state: BlockState) -> str:
        attrs = token["attrs"]
        text = self.render_children(token, state)
        
        return text + "\n" 

    def thematic_break(self, token: Dict[str, Any], state: BlockState) -> str:
        return "--------------\n\n"

    def block_text(self, token: Dict[str, Any], state: BlockState) -> str:
        return self.render_children(token, state) + "\n"

    def block_code(self, token: Dict[str, Any], state: BlockState) -> str:
        attrs = token.get("attrs", {})
        info = cast(str, attrs.get("info"))
        code = indent(cast(str, token["raw"]), "   ")
        if info:
            lang = info.split()[0]
            return ".. code:: " + lang + "\n\n" + code + "\n"
        else:
            return "::\n\n" + code + "\n\n"

    def block_quote(self, token: Dict[str, Any], state: BlockState) -> str:
        text = indent(self.render_children(token, state), "   ")
        prev = token["prev"]
        ignore_blocks = (
            "paragraph",
            "thematic_break",
            "linebreak",
            "heading",
        )
        if prev and prev["type"] not in ignore_blocks:
            text = "..\n\n" + text
        return text

    def block_html(self, token: Dict[str, Any], state: BlockState) -> str:
        raw = token["raw"]
        return ".. raw:: html\n\n" + indent(raw, "   ") + "\n\n"

    def block_error(self, token: Dict[str, Any], state: BlockState) -> str:
        return ""

    def list(self, token: Dict[str, Any], state: BlockState) -> str:
        return render_list(self, token, state)
