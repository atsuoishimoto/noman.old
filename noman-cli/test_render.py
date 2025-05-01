import mistune
import ansi_renderer


def render(s):
    renderer = ansi_renderer.ANSIRenderer()
    markdown = mistune.create_markdown(renderer=renderer)
    dump = mistune.create_markdown(
        renderer=lambda tokens, state: ansi_renderer.dump(tokens)
    )
    return markdown(s)


def test_list():
    s = """
- **11111111111**

  22222222222222222222222
"""
    ret = render(s)
    print(ret)
    print(repr(ret))
    assert repr(ret) == repr(
        "\n-     \x1b[1m11111111111\x1b[0m\n          22222222222222222222222\n"
    )
