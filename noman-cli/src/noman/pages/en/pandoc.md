# pandoc command

Convert documents between various formats.

## Overview

Pandoc is a universal document converter that can transform files between markup formats. It's particularly useful for converting between Markdown, HTML, LaTeX, Word documents, and many other formats. Pandoc preserves document structure and can handle complex elements like tables, footnotes, and bibliographies.

## Options

### **-f, --from=FORMAT**

Specify the input format. If not specified, pandoc will attempt to guess the format.

```console
$ pandoc -f markdown -t html document.md -o document.html
```

### **-t, --to=FORMAT**

Specify the output format.

```console
$ pandoc -t latex document.md -o document.tex
```

### **-o, --output=FILE**

Write output to FILE instead of stdout.

```console
$ pandoc document.md -o document.pdf
```

### **--pdf-engine=PROGRAM**

Use the specified engine when producing PDF output.

```console
$ pandoc document.md --pdf-engine=xelatex -o document.pdf
```

### **--toc, --table-of-contents**

Include an automatically generated table of contents in the output document.

```console
$ pandoc --toc document.md -o document.html
```

### **-s, --standalone**

Produce a standalone document with appropriate headers and footers.

```console
$ pandoc -s document.md -o document.html
```

### **-c, --css=URL**

Link to a CSS style sheet when creating HTML output.

```console
$ pandoc -s -c style.css document.md -o document.html
```

## Usage Examples

### Converting Markdown to HTML

```console
$ pandoc document.md -o document.html
```

### Converting Markdown to PDF

```console
$ pandoc document.md -o document.pdf
```

### Converting HTML to Markdown

```console
$ pandoc -f html -t markdown https://example.com -o example.md
```

### Creating a presentation from Markdown

```console
$ pandoc -t revealjs -s presentation.md -o presentation.html
```

### Converting Word to Markdown

```console
$ pandoc -f docx -t markdown document.docx -o document.md
```

## Tips

### Use Templates for Consistent Output

Pandoc supports custom templates with the `--template` option. Create your own templates for consistent document styling across multiple conversions.

```console
$ pandoc --template=mytemplate.tex document.md -o document.pdf
```

### Handling Citations and Bibliographies

Use `--citeproc` with a bibliography file to automatically format citations:

```console
$ pandoc --citeproc --bibliography=refs.bib paper.md -o paper.pdf
```

### Batch Converting Multiple Files

Use shell loops to convert multiple files at once:

```console
$ for f in *.md; do pandoc "$f" -o "${f%.md}.html"; done
```

## Frequently Asked Questions

#### Q1. What formats does pandoc support?
A. Pandoc supports numerous formats including Markdown, HTML, LaTeX, DOCX, ODT, EPUB, PDF, and many more. Run `pandoc --list-input-formats` or `pandoc --list-output-formats` to see all supported formats.

#### Q2. How do I convert a Markdown file to PDF?
A. Use `pandoc document.md -o document.pdf`. This requires a PDF engine like LaTeX to be installed on your system.

#### Q3. Can pandoc convert a website to Markdown?
A. Yes, you can convert a web page by providing its URL: `pandoc -f html -t markdown https://example.com -o example.md`

#### Q4. How do I include images in my document?
A. In Markdown, use standard image syntax: `![Caption](path/to/image.jpg)`. Pandoc will include these images in the output document.

#### Q5. How can I customize the appearance of my output document?
A. Use CSS for HTML output (`-c style.css`), LaTeX variables for PDF output (`-V variable=value`), or custom templates (`--template=template.tex`).

## macOS Considerations

On macOS, pandoc can be installed via Homebrew with `brew install pandoc`. For PDF output, you'll also need a LaTeX distribution like MacTeX: `brew install --cask mactex`. MacTeX is large (4GB+), so if space is a concern, consider BasicTeX instead: `brew install --cask basictex`.

## References

https://pandoc.org/MANUAL.html

## Revisions

- 2025/05/04 First revision