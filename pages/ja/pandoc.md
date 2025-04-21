# pandoc

Pandocはドキュメント変換ツールで、Markdown、HTML、LaTeX、Word、PDFなど様々なフォーマット間でドキュメントを変換できます。「ユニバーサルドキュメントコンバーター」とも呼ばれています。

## オプション

### **-f, --from=FORMAT**

入力ファイルのフォーマットを指定します。

```bash
$ pandoc -f markdown -t html document.md -o document.html
```

### **-t, --to=FORMAT**

出力ファイルのフォーマットを指定します。

```bash
$ pandoc -f markdown -t latex document.md -o document.tex
```

### **-o, --output=FILE**

出力ファイルを指定します。指定しない場合は標準出力に出力されます。

```bash
$ pandoc document.md -o document.html
```

### **--pdf-engine=PROGRAM**

PDF出力時に使用するエンジンを指定します（pdflatex、xelatex、lualatexなど）。

```bash
$ pandoc document.md --pdf-engine=xelatex -o document.pdf
```

### **-s, --standalone**

完全なドキュメント（ヘッダーやフッターを含む）を出力します。

```bash
$ pandoc -s document.md -o document.html
```

### **--toc**

目次を生成します。

```bash
$ pandoc --toc document.md -o document.html
```

## 使用例

### Markdown から HTML への変換

```bash
$ pandoc document.md -o document.html
```

### Markdown から PDF への変換

```bash
$ pandoc document.md -o document.pdf
```

### Word から Markdown への変換

```bash
$ pandoc document.docx -o document.md
```

### 複数ファイルの結合と変換

```bash
$ pandoc chapter1.md chapter2.md chapter3.md -o book.pdf
```

### スタイルシートの適用

```bash
$ pandoc document.md -c style.css -o document.html
```

## よくある質問

### Q1. Pandocでどのようなフォーマットが扱えますか？
A. Markdown、HTML、LaTeX、Word、PDF、EPUBなど30以上のフォーマットに対応しています。

### Q2. PDFに変換するには何が必要ですか？
A. LaTeXエンジン（TeXLive、MiKTeXなど）がインストールされている必要があります。

### Q3. 目次の深さを調整するにはどうすればよいですか？
A. `--toc-depth=NUMBER` オプションで指定できます。例：`--toc-depth=2`で2階層まで表示。

### Q4. スライドプレゼンテーションは作成できますか？
A. はい、RevealJS、Beamer、PowerPointなどのフォーマットに変換できます。

## 追加情報

- テンプレートを使用すると出力の見た目をカスタマイズできます：`--template=FILE`
- メタデータは `-M KEY=VALUE` または YAML ファイルで指定できます
- macOSでは `brew install pandoc` でインストールできます
- PDF変換にはLaTeXが必要なため、初めて使用する場合はインストールが必要です

## 主なフォーマット一覧

### 入力フォーマット
- markdown (Pandocの拡張Markdown)
- commonmark (CommonMark Markdown)
- gfm (GitHub Flavored Markdown)
- html (HTML)
- latex (LaTeX)
- docx (Microsoft Word)
- odt (OpenDocument)
- epub (EPUB)
- csv (CSV表)
- json (JSONバージョンのnative)

### 出力フォーマット
- html (HTML)
- html5 (HTML5)
- docx (Microsoft Word)
- pdf (PDF)
- latex (LaTeX)
- epub (EPUB電子書籍)
- odt (OpenDocument)
- pptx (PowerPoint)
- revealjs (RevealJSスライド)
- beamer (Beamerスライド)
- rtf (Rich Text Format)
- markdown (Pandoc Markdown)
- plain (プレーンテキスト)

## 参考

https://pandoc.org/MANUAL.html