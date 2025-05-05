# sed コマンド

テキストのフィルタリングと変換のためのストリームエディタ。

## 概要

`sed`（ストリームエディタ）は、テキストを行ごとに解析して変換する強力なユーティリティです。ファイルや標準入力からテキストを読み取り、指定された編集コマンドを適用し、結果を標準出力に出力します。検索と置換操作、テキスト抽出、その他のテキスト操作をシェルスクリプトやコマンドライン操作で行うために広く使用されています。

## オプション

### **-e スクリプト, --expression=スクリプト**

実行するコマンドセットにスクリプト内のコマンドを追加します。

```console
$ echo "hello world" | sed -e 's/hello/goodbye/' -e 's/world/universe/'
goodbye universe
# 複数の置換コマンドを順番に適用している
```

### **-f スクリプトファイル, --file=スクリプトファイル**

スクリプトファイルからコマンドを読み込み、実行するコマンドセットに追加します。

```console
$ cat script.sed
s/hello/goodbye/
s/world/universe/
$ echo "hello world" | sed -f script.sed
goodbye universe
# ファイルに保存された複数のsedコマンドを実行している
```

### **-i[接尾辞], --in-place[=接尾辞]**

ファイルを直接編集します（接尾辞を指定するとバックアップを作成します）。

```console
$ echo "hello world" > file.txt
$ sed -i 's/hello/goodbye/' file.txt
$ cat file.txt
goodbye world
# ファイルを直接編集して内容を変更している
```

### **-n, --quiet, --silent**

パターンスペースの自動出力を抑制します。

```console
$ echo -e "line 1\nline 2\nline 3" | sed -n '2p'
line 2
# -nオプションと組み合わせて2行目だけを表示している
```

### **-r, --regexp-extended**

スクリプトで拡張正規表現を使用します。

```console
$ echo "hello 123 world" | sed -r 's/[0-9]+/NUMBER/'
hello NUMBER world
# 拡張正規表現を使って数字を置換している
```

## 使用例

### 基本的な置換

```console
$ echo "The quick brown fox" | sed 's/brown/red/'
The quick red fox
# 「brown」を「red」に置換している
```

### グローバル置換

```console
$ echo "one two one three one" | sed 's/one/ONE/g'
ONE two ONE three ONE
# gフラグを使って「one」のすべての出現を「ONE」に置換している
```

### 特定の行を表示

```console
$ cat file.txt
Line 1
Line 2
Line 3
Line 4
$ sed -n '2,3p' file.txt
Line 2
Line 3
# 2行目から3行目までを表示している
```

### 行の削除

```console
$ cat file.txt
Line 1
Line 2
Line 3
Line 4
$ sed '2,3d' file.txt
Line 1
Line 4
# 2行目から3行目までを削除している
```

### 複数の編集コマンド

```console
$ echo "hello world" | sed 's/hello/hi/; s/world/there/'
hi there
# セミコロンで区切って複数のコマンドを実行している
```

## ヒント:

### '/' 以外の区切り文字を使用する

パターンや置換文字列にスラッシュが含まれる場合は、別の区切り文字を使用してエスケープを避けることができます：

```console
$ echo "/usr/local/bin" | sed 's:/usr:~:'
~/local/bin
# パスを扱う際にコロンを区切り文字として使用している
```

### インプレース編集時のバックアップ作成

`-i`オプションを使用してファイルを直接編集する場合は、常にバックアップを作成することをお勧めします：

```console
$ sed -i.bak 's/old/new/g' file.txt
# .bakという拡張子でバックアップファイルが作成される
```

### アドレス範囲

行番号、パターン、または範囲を使用して特定の行をターゲットにできます：
- `1,5` - 1行目から5行目まで
- `/start/,/end/` - パターン「start」からパターン「end」までの行
- `5,+2` - 5行目とその後の2行

### 行の追加、挿入、変更

```console
$ echo -e "line 1\nline 2\nline 3" | sed '2a\new line after 2'
line 1
line 2
new line after 2
line 3
# 2行目の後に新しい行を追加している
```

## よくある質問

#### Q1. ファイル内のテキストを永続的に置換するにはどうすればよいですか？
A. `-i`オプションを使用します：`sed -i 's/old/new/g' filename`。バックアップを作成するには `-i.bak` のように接尾辞を追加します。

#### Q2. パターンに一致する行だけを表示するにはどうすればよいですか？
A. `-n`オプションと`p`コマンドを使用します：`sed -n '/pattern/p' filename`。

#### Q3. 's/pattern/replacement/' と 's/pattern/replacement/g' の違いは何ですか？
A. `g`フラグがない場合、各行の最初の出現のみが置換されます。`g`フラグがあると、すべての出現が置換されます。

#### Q4. パターンに一致する行を削除するにはどうすればよいですか？
A. `d`コマンドを使用します：`sed '/pattern/d' filename`。

#### Q5. sedコマンドで変数を使用するにはどうすればよいですか？
A. 二重引用符を使用し、特殊文字をエスケープします：`sed "s/$var/replacement/g" filename`。

## 参照

https://www.gnu.org/software/sed/manual/sed.html

## 改訂履歴

- 2025/05/04 初版作成