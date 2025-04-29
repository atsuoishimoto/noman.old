# `file` コマンド概要

`file` コマンドはファイルの種類（タイプ）を判別するためのコマンドです。ファイルの内容を解析し、テキストファイル、実行ファイル、画像ファイルなどの種類を表示します。

## 主なオプション

- **-b, --brief**: ファイル名を表示せず、ファイルタイプのみを表示します
  - 例: `file -b document.txt`

- **-i, --mime**: MIMEタイプ形式でファイルタイプを表示します
  - 例: `file -i image.jpg`

- **-z, --uncompress**: 圧縮ファイルの内容を解析します
  - 例: `file -z archive.gz`

- **-L, --dereference**: シンボリックリンクをたどってリンク先のファイルタイプを表示します
  - 例: `file -L symlink`

## 使用例

```bash
# 基本的な使い方
$ file document.txt
# 出力例
document.txt: ASCII text

# 複数のファイルを一度に調べる
$ file document.txt image.jpg script.sh
# 出力例
document.txt: ASCII text
image.jpg: JPEG image data, JFIF standard 1.01
script.sh: Bourne-Again shell script, ASCII text executable

# -b オプションでファイル名を省略
$ file -b document.txt
# 出力例
ASCII text

# -i オプションでMIMEタイプを表示
$ file -i document.txt
# 出力例
document.txt: text/plain; charset=us-ascii

# バイナリファイルの確認
$ file /bin/ls
# 出力例
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32
```

## 追加メモ

- ファイルに拡張子がない場合や、拡張子が実際の内容と一致しない場合に特に役立ちます。
- `file` コマンドは「マジックナンバー」と呼ばれるファイル先頭のバイトパターンを解析して判定を行います。
- スクリプトファイルの場合は、シバン（`#!`）行を検出して言語を判別します。
- 大量のファイルを処理する場合は、`find` コマンドと組み合わせて使うと便利です。例：`find . -type f -exec file {} \;`