# pandoc command

Convert documents between various formats.

## Overview

Pandoc is a universal document converter that can transform files from one markup format to another. It supports a wide range of formats including Markdown, HTML, LaTeX, PDF, DOCX, EPUB, and many more. Pandoc is particularly useful for writers, researchers, and content creators who need to repurpose content across different platforms.

## Options

### **-f, --from=FORMAT**

Specify the input format.

```console
$ pandoc -f markdown -t html document.md -o document.html
```

### **-t, --to=FORMAT**

Specify the output format.

```console
$ pandoc -f docx -t markdown document.docx -o document.md
```

### **-o, --output=FILE**

Write output to FILE instead of stdout.

```console
$ pandoc document.md -o document.pdf
```

### **--pdf-engine=PROGRAM**

Specify which program to use for PDF generation.

```console
$ pandoc document.md -o document.pdf --pdf-engine=xelatex
```

### **--toc, --table-of-contents**

Include an automatically generated table of contents.

```console
$ pandoc --toc document.md -o document.html
```

### **-s, --standalone**

Produce a standalone document with appropriate headers and footers.

```console
$ pandoc -s document.md -o document.html
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

### Converting Word to Markdown

```console
$ pandoc report.docx -o report.md
```

### Creating a presentation from Markdown

```console
$ pandoc -t revealjs -s presentation.md -o presentation.html
```

### Converting multiple files to a single output

```console
$ pandoc chapter1.md chapter2.md chapter3.md -o book.pdf
```

## Tips

### Use Templates for Consistent Output

Pandoc supports custom templates with the `--template` option. Create a template once and reuse it for consistent document styling.

```console
$ pandoc --template=mytemplate.tex document.md -o document.pdf
```

### Customize Metadata

Add YAML metadata blocks at the top of your Markdown files to control document properties like title, author, and date.

```markdown
---
title: "My Document"
author: "John Doe"
date: "2025-04-30"
---
```

### Filter Content with Lua Scripts

Use Lua filters to modify the document during conversion, enabling custom processing like syntax highlighting or content transformation.

```console
$ pandoc --lua-filter=myfilter.lua document.md -o document.html
```

### Specify Bibliography for Academic Writing

For academic papers, use the `--bibliography` option to include citations from a BibTeX file.

```console
$ pandoc --bibliography=references.bib paper.md -o paper.pdf
```

## Frequently Asked Questions

#### Q1. What formats does pandoc support?
A. Pandoc supports numerous formats including Markdown, HTML, LaTeX, PDF, DOCX, EPUB, ODT, RST, AsciiDoc, and many more. Use `pandoc --list-input-formats` and `pandoc --list-output-formats` to see all supported formats.

#### Q2. How do I convert a Markdown file to PDF?
A. Use `pandoc document.md -o document.pdf`. Note that PDF conversion requires a LaTeX engine to be installed on your system.

#### Q3. Can pandoc handle images in documents?
A. Yes, pandoc preserves images during conversion. For PDF output, images are included automatically. For HTML, images are referenced or can be embedded with the `--embed-resources` option.

#### Q4. How do I create a table of contents?
A. Use the `--toc` or `--table-of-contents` option to generate an automatic table of contents based on headings in your document.

#### Q5. Does pandoc work on macOS?
A. Yes, pandoc works on macOS, Windows, and Linux. On macOS, it can be installed via Homebrew with `brew install pandoc`.

## References

https://pandoc.org/MANUAL.html

## Revisions

- 2025/04/30 First revision