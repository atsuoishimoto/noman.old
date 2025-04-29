# basename コマンド概要

`basename`コマンドは、ファイルパスからディレクトリ部分を削除し、ファイル名のみを取得するためのコマンドです。スクリプト内でファイル名だけを抽出したい場合に便利です。

## 主なオプション

- **基本的な使用法**: パスからファイル名部分を抽出する
  - 例: `basename /path/to/file.txt`

- **-s, --suffix=接尾辞**: 指定した接尾辞（拡張子など）を削除する
  - 例: `basename file.txt .txt`

- **-a, --multiple**: 複数のパスを処理する
  - 例: `basename -a /path/to/file1.txt /path/to/file2.txt`

- **-z, --zero**: 出力の区切りとして改行ではなくNULL文字を使用する
  - 例: `basename -z /path/to/file1.txt /path/to/file2.txt`

## 使用例

```bash
# 基本的な使用法
basename /home/user/documents/report.pdf
# 出力
report.pdf

# 拡張子を削除
basename /home/user/documents/report.pdf .pdf
# 出力
report

# 複数のファイルを処理
basename -a /var/log/syslog /etc/hosts /usr/bin/python
# 出力
syslog
hosts
python

# スクリプト内での使用例
FILENAME=$(basename "$FILEPATH")
echo "処理中のファイル: $FILENAME"
```

## 追加情報

- `basename`は主にシェルスクリプト内で使用され、ファイルパスからファイル名部分だけを取り出したい場合に役立ちます。
- `dirname`コマンドと組み合わせると、パスの各部分（ディレクトリとファイル名）を別々に扱うことができます。
- パス操作には、より柔軟な方法として`${変数##*/}`のようなシェルのパラメータ展開を使用することもできます。