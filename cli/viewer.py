import sys
import subprocess
import mistune
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
from pathlib import Path
import ansi_renderer


renderer = ansi_renderer.ANSIRenderer()
markdown = mistune.create_markdown(renderer=renderer)
dump = mistune.create_markdown(renderer=lambda tokens, state: ansi_renderer.dump(tokens))


src = open(sys.argv[1]).read()

if len(sys.argv) == 3 and sys.argv[2] == '1':
    print(dump(src))
else:
    s = markdown(src)

    p = subprocess.Popen(["less", "-R"], stdin=subprocess.PIPE)
    p.stdin.write(s.encode())
    p.stdin.close()
    sys.exit(p.wait())
