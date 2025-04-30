# file コマンド

ファイルの種類を判別します。

## 概要

`file` コマンドはファイルの内容を検査し、そのファイルの種類（テキスト、実行可能ファイル、画像など）を判定します。このコマンドは、拡張子がないファイルや、拡張子が実際の内容と一致しないファイルの種類を特定するのに役立ちます。

## オプション

### **-b (--brief)**

ファイル名を表示せず、ファイルタイプのみを出力します。

```console
$ file -b sample.txt
ASCII text
```

### **-i (--mime)**

MIMEタイプ形式でファイルの種類を表示します。

```console
$ file -i sample.txt
sample.txt: text/plain; charset=us-ascii
```

### **-z (--uncompress)**

圧縮ファイルの内容を検査します。

```console
$ file -z archive.gz
archive.gz: ASCII text (gzip compressed data, was "sample.txt")
```

### **-L (--dereference)**

シンボリックリンクをたどり、リンク先のファイルの種類を表示します。

```console
$ file -L symlink.txt
symlink.txt: ASCII text
```

## 使用例

### 基本的な使用法

```console
$ file sample.txt
sample.txt: ASCII text

$ file /bin/bash
/bin/bash: Mach-O 64-bit executable x86_64
```

### 複数ファイルの種類を確認

```console
$ file *
document.txt:  ASCII text
image.jpg:     JPEG image data, JFIF standard 1.01
program:       Mach-O 64-bit executable x86_64
archive.zip:   Zip archive data, at least v2.0 to extract
```

### ディレクトリの確認

```console
$ file /etc
/etc: directory
```

## ヒント:

### マジックナンバーによる判定

`file` コマンドは「マジックナンバー」と呼ばれるファイル先頭のバイトパターンを検査して種類を判定しています。そのため、拡張子に関係なく実際の内容に基づいて判定できます。

### スクリプトでの活用

シェルスクリプト内で `file` コマンドを使用して、処理前にファイルの種類を確認することで、不適切なファイルタイプによるエラーを防ぐことができます。

### バイナリファイルの識別

テキストエディタで開く前にファイルがバイナリかテキストかを確認するのに役立ちます。バイナリファイルをテキストエディタで開くと文字化けの原因になります。

## よくある質問

#### Q1. `file` コマンドはどのようにファイルの種類を判定しますか？
A. ファイルの先頭部分のバイトパターン（マジックナンバー）、テキスト分析、その他の特徴を調べて判定します。

#### Q2. ファイルの拡張子と `file` コマンドの結果が異なる場合はどうすればよいですか？
A. 通常は `file` コマンドの結果が実際のファイル内容を反映しています。必要に応じて拡張子を変更するか、適切なアプリケーションで開くことを検討してください。

#### Q3. `file` コマンドが「data」や「ASCII text」としか表示しない場合はどうすればよいですか？
A. これはファイルの内容が特定のパターンに一致しないか、一般的なテキストデータであることを示しています。より詳細な情報を得るには、ファイルの内容を直接確認する必要があるかもしれません。

## macOSでの注意点

macOSの `file` コマンドはBSD由来であり、Linux版と若干の違いがあります。特に `-z` オプションの動作が異なる場合があります。また、macOSでは実行可能ファイルの判定結果が「Mach-O」形式で表示されます。

## 参考資料

https://man7.org/linux/man-pages/man1/file.1.html

## 改訂履歴

- 2025/04/30 初版作成