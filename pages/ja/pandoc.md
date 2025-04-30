# pandoc コマンド

ドキュメント形式を変換するための汎用的なコンバーター。

## 概要

pandoc は、あるマークアップ形式から別の形式へドキュメントを変換するためのコマンドラインツールです。Markdown、HTML、LaTeX、Word、PDF など、多数のフォーマット間での変換をサポートしています。学術論文、ブログ記事、技術文書など、さまざまな種類のドキュメントの変換に広く利用されています。

## オプション

### **-f, --from=FORMAT**

入力ファイルのフォーマットを指定します。

```console
$ pandoc -f markdown -t html document.md -o document.html
```

### **-t, --to=FORMAT**

出力ファイルのフォーマットを指定します。

```console
$ pandoc -f docx -t markdown document.docx -o document.md
```

### **-o, --output=FILE**

出力ファイルを指定します。指定しない場合は標準出力に出力されます。

```console
$ pandoc document.md -o document.pdf
```

### **--pdf-engine=PROGRAM**

PDF出力時に使用するエンジンを指定します（pdflatex, xelatex, lualatex など）。

```console
$ pandoc document.md --pdf-engine=xelatex -o document.pdf
```

### **-s, --standalone**

完全なドキュメント（ヘッダーやフッターを含む）を出力します。

```console
$ pandoc -s document.md -o document.html
```

### **--toc, --table-of-contents**

目次を生成します。

```console
$ pandoc --toc document.md -o document.pdf
```

## 主なフォーマットの一覧

- markdown: Markdown（標準）
- gfm: GitHub Flavored Markdown
- html: HTML
- latex: LaTeX
- docx: Microsoft Word
- odt: OpenDocument
- epub: EPUB電子書籍
- pdf: PDF（LaTeXエンジンを使用）
- rst: reStructuredText
- asciidoc: AsciiDoc

## 使用例

### Markdown から HTML への変換

```console
$ pandoc document.md -o document.html
# Markdown ファイルを HTML に変換している
```

### Markdown から PDF への変換

```console
$ pandoc document.md -o document.pdf
# Markdown ファイルを PDF に変換している
```

### Word から Markdown への変換

```console
$ pandoc -f docx -t markdown document.docx -o document.md
# Word ファイルを Markdown に変換している
```

### 目次付きの PDF 生成

```console
$ pandoc --toc --toc-depth=2 document.md -o document.pdf
# 2階層までの目次を含む PDF を生成している
```

### スタイルシートを適用した HTML 生成

```console
$ pandoc document.md -s --css=style.css -o document.html
# カスタム CSS を適用した HTML を生成している
```

## ヒント:

### テンプレートの活用

`--template` オプションを使用して、出力形式に合わせたカスタムテンプレートを適用できます。これにより、一貫したスタイルのドキュメントを生成できます。

### メタデータの追加

YAML形式のメタデータブロックをMarkdownファイルの先頭に追加することで、タイトル、著者、日付などの情報を設定できます。

```markdown
---
title: ドキュメントタイトル
author: 著者名
date: 2025年4月30日
---
```

### フィルターの活用

pandocフィルターを使用すると、変換プロセスをカスタマイズできます。例えば、数式の処理や図表の番号付けなどが可能です。

### PDF生成時の注意点

PDF生成には LaTeX が必要です。macOS では MacTeX、Windows では MiKTeX などをインストールしておく必要があります。

## よくある質問

#### Q1. pandoc で PDF を生成できない場合はどうすればよいですか？
A. LaTeX エンジン（TeX Live や MacTeX など）がインストールされていることを確認してください。また、`--pdf-engine` オプションで別のエンジン（xelatex など）を試してみることも有効です。

#### Q2. 日本語を含むドキュメントを PDF に変換する際の注意点は？
A. `--pdf-engine=xelatex` または `--pdf-engine=lualatex` オプションを使用し、適切なフォントを指定することをお勧めします。また、YAML メタデータで `documentclass: bxjsarticle` などを指定すると良いでしょう。

#### Q3. 複数のファイルを一つのドキュメントに結合するには？
A. 複数のファイルを順番に指定するだけで結合できます：`pandoc file1.md file2.md -o combined.pdf`

#### Q4. スタイルをカスタマイズするには？
A. HTML 出力には `--css` オプション、PDF/LaTeX 出力には `--variable` オプションでスタイル設定が可能です。例：`pandoc --variable=geometry:margin=1in document.md -o document.pdf`

## macOS での注意点

macOS で PDF 出力を行う場合は、MacTeX（https://www.tug.org/mactex/）をインストールしておく必要があります。Homebrew を使用している場合は `brew install --cask mactex` でインストールできます。また、日本語フォントの問題が発生することがあるため、`--pdf-engine=xelatex` オプションの使用をお勧めします。

## 参考資料

https://pandoc.org/MANUAL.html

## 改訂履歴

- 2025/04/30 初版作成