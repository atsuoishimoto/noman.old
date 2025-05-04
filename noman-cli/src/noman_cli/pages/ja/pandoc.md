# pandoc コマンド

様々な形式の文書を相互に変換します。

## 概要

Pandocは汎用的な文書変換ツールで、マークアップ形式間でファイルを変換できます。特にMarkdown、HTML、LaTeX、Word文書など多くの形式間の変換に役立ちます。Pandocは文書構造を保持し、表、脚注、参考文献などの複雑な要素も処理できます。

## オプション

### **-f, --from=FORMAT**

入力形式を指定します。指定しない場合、pandocは形式を推測しようとします。

```console
$ pandoc -f markdown -t html document.md -o document.html
# MarkdownからHTMLへ変換している
```

### **-t, --to=FORMAT**

出力形式を指定します。

```console
$ pandoc -t latex document.md -o document.tex
# 出力形式をLaTeXに指定している
```

### **-o, --output=FILE**

標準出力ではなく、指定したファイルに出力します。

```console
$ pandoc document.md -o document.pdf
# 出力をdocument.pdfファイルに書き込んでいる
```

### **--pdf-engine=PROGRAM**

PDF出力時に使用するエンジンを指定します。

```console
$ pandoc document.md --pdf-engine=xelatex -o document.pdf
# PDF生成にxelatexエンジンを使用している
```

### **--toc, --table-of-contents**

出力文書に自動生成された目次を含めます。

```console
$ pandoc --toc document.md -o document.html
# 目次を含むHTMLを生成している
```

### **-s, --standalone**

適切なヘッダーとフッターを含む独立した文書を生成します。

```console
$ pandoc -s document.md -o document.html
# 完全なHTMLドキュメントを生成している
```

### **-c, --css=URL**

HTML出力時にCSSスタイルシートをリンクします。

```console
$ pandoc -s -c style.css document.md -o document.html
# style.cssをリンクしたHTML文書を生成している
```

## 使用例

### MarkdownからHTMLへの変換

```console
$ pandoc document.md -o document.html
```

### MarkdownからPDFへの変換

```console
$ pandoc document.md -o document.pdf
```

### HTMLからMarkdownへの変換

```console
$ pandoc -f html -t markdown https://example.com -o example.md
```

### Markdownからプレゼンテーションの作成

```console
$ pandoc -t revealjs -s presentation.md -o presentation.html
```

### WordからMarkdownへの変換

```console
$ pandoc -f docx -t markdown document.docx -o document.md
```

## ヒント:

### テンプレートを使用して一貫した出力を得る

Pandocは`--template`オプションでカスタムテンプレートをサポートしています。複数の変換で一貫した文書スタイルを得るために独自のテンプレートを作成できます。

```console
$ pandoc --template=mytemplate.tex document.md -o document.pdf
```

### 引用と参考文献の処理

`--citeproc`と参考文献ファイルを使用して、引用を自動的に整形できます：

```console
$ pandoc --citeproc --bibliography=refs.bib paper.md -o paper.pdf
```

### 複数ファイルの一括変換

シェルのループを使用して複数のファイルを一度に変換できます：

```console
$ for f in *.md; do pandoc "$f" -o "${f%.md}.html"; done
```

## よくある質問

#### Q1. pandocはどのような形式をサポートしていますか？
A. pandocはMarkdown、HTML、LaTeX、DOCX、ODT、EPUB、PDFなど多数の形式をサポートしています。`pandoc --list-input-formats`または`pandoc --list-output-formats`を実行すると、サポートされているすべての形式を確認できます。

#### Q2. MarkdownファイルをPDFに変換するにはどうすればよいですか？
A. `pandoc document.md -o document.pdf`を使用します。これにはLaTeXなどのPDFエンジンがシステムにインストールされている必要があります。

#### Q3. pandocでウェブサイトをMarkdownに変換できますか？
A. はい、URLを指定することでウェブページを変換できます：`pandoc -f html -t markdown https://example.com -o example.md`

#### Q4. 文書に画像を含めるにはどうすればよいですか？
A. Markdownでは標準的な画像構文を使用します：`![キャプション](path/to/image.jpg)`。pandocは出力文書にこれらの画像を含めます。

#### Q5. 出力文書の外観をカスタマイズするにはどうすればよいですか？
A. HTML出力にはCSS（`-c style.css`）、PDF出力にはLaTeX変数（`-V variable=value`）、またはカスタムテンプレート（`--template=template.tex`）を使用できます。

## macOSに関する注意点

macOSでは、pandocはHomebrewを使って`brew install pandoc`でインストールできます。PDF出力には、LaTeX配布物（MacTeX）も必要です：`brew install --cask mactex`。MacTeXは大きい（4GB以上）ので、容量が気になる場合はBasicTeXを検討してください：`brew install --cask basictex`。

## 参考資料

https://pandoc.org/MANUAL.html

## 改訂履歴

- 2025/05/04 初版作成