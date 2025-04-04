# sed コマンド概要

`sed`（Stream EDitor）は、テキストファイルやストリームを処理するための強力なテキスト編集ツールです。主にテキストの置換、削除、挿入などの操作を行うために使用されます。

## 主なオプション

- **-e**: 複数の編集コマンドを指定できます
  - 例: `sed -e 's/old/new/' -e 's/foo/bar/' file.txt`

- **-i**: ファイルを直接編集します（インプレース編集）
  - 例: `sed -i 's/old/new/' file.txt`

- **-n**: 自動出力を抑制し、特定のパターンに一致する行のみを表示します
  - 例: `sed -n '/pattern/p' file.txt`

- **-r または -E**: 拡張正規表現を使用します
  - 例: `sed -r 's/(foo|bar)/baz/' file.txt`

## 基本的な使い方

### テキスト置換

```bash
# ファイル内の「apple」を「orange」に置換して表示
sed 's/apple/orange/' fruits.txt
# 出力例:
# I like orange
# orange pie is delicious
# An orange a day keeps the doctor away
```

### 特定の行を削除

```bash
# 「banana」を含む行を削除
sed '/banana/d' fruits.txt
# 出力例:
# I like apple
# apple pie is delicious
# An apple a day keeps the doctor away
```

### 特定の行を表示

```bash
# 「apple」を含む行のみを表示
sed -n '/apple/p' fruits.txt
# 出力例:
# I like apple
# apple pie is delicious
# An apple a day keeps the doctor away
```

### 複数の置換を一度に行う

```bash
# 「apple」を「orange」に、「banana」を「grape」に置換
sed -e 's/apple/orange/g' -e 's/banana/grape/g' fruits.txt
# 出力例:
# I like orange
# orange pie is delicious
# I enjoy eating grape
```

### ファイルを直接編集

```bash
# ファイルを直接編集して「apple」を「orange」に置換
sed -i 's/apple/orange/g' fruits.txt
# コマンド実行後、fruits.txtファイルが直接変更されます
```

## 追加のヒント

- `s/old/new/g` の `g` フラグは、行内のすべての一致を置換します。省略すると最初の一致のみが置換されます。
- バックアップを作成したい場合は `-i.bak` のように拡張子を指定できます（例: `sed -i.bak 's/old/new/' file.txt`）。
- 区切り文字は `/` 以外にも使えます。例えば `s#old#new#` や `s@old@new@` なども有効です。これはパスを扱う際に便利です。
- `sed` は正規表現をサポートしているため、複雑なパターンマッチングが可能です。
- 大文字と小文字を区別せずに置換するには `I` フラグを使用します（例: `s/pattern/replacement/gI`）。