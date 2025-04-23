#!/usr/bin/env python3

import sys
from pygments import highlight
from pygments.lexers import MarkdownLexer
from pygments.formatters import Terminal256Formatter, TerminalFormatter

def highlight_markdown_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            code = file.read()
        
        highlighted = highlight(code, MarkdownLexer(), 
            TerminalFormatter(style="staroffice", bg="dark"))
        print(highlighted)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python highlight_markdown.py <markdown_file>")
        sys.exit(1)
    
    highlight_markdown_file(sys.argv[1])
