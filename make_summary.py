from pathlib import Path
import re
import sys
import subprocess

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
        p = subprocess.Popen(["pandoc", "-f", "markdown", "-t", "plain", "--wrap=none"], 
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf8")
        stdout, stderr = p.communicate((m["header"]+"\n"))
        p.stdin.close()
        p.wait()
        d[file.stem] = stdout
    return d



