# sed コマンド

テキストストリームを変換・編集するためのストリームエディタです。

## 概要

`sed`（Stream EDitor）は、テキストファイルやパイプからのテキスト入力を処理するためのコマンドラインユーティリティです。正規表現を使用したパターンマッチングによる置換、削除、挿入などの編集操作を行うことができます。`sed`は非対話的に動作し、スクリプトやコマンドラインから指定された編集コマンドに基づいてテキストを処理します。

## オプション

### **-e スクリプト**

複数の編集コマンドを指定できます。

```console
$ echo "Hello World" | sed -e 's/Hello/Hi/' -e 's/World/Everyone/'
Hi Everyone
```

### **-i[拡張子]**

ファイルを直接編集します。拡張子を指定すると、元のファイルのバックアップが作成されます。

```console
$ sed -i.bak 's/old/new/g' file.txt
# file.txtが直接編集され、file.txt.bakというバックアップファイルが作成される
```

### **-n**

自動出力を抑制し、明示的に出力を指定する場合に使用します。

```console
$ echo -e "line1\nline2\nline3" | sed -n '2p'
line2
```

### **-f スクリプトファイル**

編集コマンドをファイルから読み込みます。

```console
$ echo "commands.sed の内容: s/Hello/Hi/g"
$ echo "Hello World" | sed -f commands.sed
Hi World
```

## 編集コマンド

### **s/パターン/置換/[フラグ]**

パターンに一致するテキストを置換します。

```console
$ echo "Hello World" | sed 's/Hello/Hi/'
Hi World
```

### **g フラグ（全置換）**

行内のすべての一致を置換します。

```console
$ echo "Hello Hello World" | sed 's/Hello/Hi/g'
Hi Hi World
```

### **d（削除）**

パターンに一致する行を削除します。

```console
$ echo -e "line1\nline2\nline3" | sed '2d'
line1
line3
```

### **p（表示）**

パターンに一致する行を表示します（通常は -n と共に使用）。

```console
$ echo -e "line1\nline2\nline3" | sed -n '2p'
line2
```

### **i\（前に挿入）**

指定した行の前に新しいテキストを挿入します。

```console
$ echo -e "line1\nline2" | sed '1i\新しい行'
新しい行
line1
line2
```

### **a\（後に追加）**

指定した行の後に新しいテキストを追加します。

```console
$ echo -e "line1\nline2" | sed '1a\新しい行'
line1
新しい行
line2
```

## 使用例

### 基本的な置換

```console
$ echo "The quick brown fox" | sed 's/brown/red/'
The quick red fox
```

### ファイル内のすべての一致を置換

```console
$ cat sample.txt
Hello World
Hello Everyone
$ sed 's/Hello/Hi/g' sample.txt
Hi World
Hi Everyone
```

### 特定の行を抽出

```console
$ cat numbers.txt
1: First line
2: Second line
3: Third line
$ sed -n '2p' numbers.txt
2: Second line
```

### 複数の編集コマンドを連結

```console
$ echo "Hello World 123" | sed 's/Hello/Hi/g; s/123/456/g'
Hi World 456
```

## ヒント:

### バックアップを作成してから編集

ファイルを直接編集する際は、`-i.bak`オプションを使用してバックアップを作成することをお勧めします。

```console
$ sed -i.bak 's/old/new/g' important_file.txt
# important_file.txtが編集され、important_file.txt.bakというバックアップが作成される
```

### 正規表現の活用

`sed`は強力な正規表現をサポートしています。例えば、`.*`は任意の文字列に一致します。

```console
$ echo "prefix_12345_suffix" | sed 's/prefix_.*_suffix/REPLACED/'
REPLACED
```

### アドレス範囲の指定

特定の行範囲に対して操作を適用できます。

```console
$ cat numbers.txt
1: First line
2: Second line
3: Third line
4: Fourth line
$ sed '2,3d' numbers.txt
1: First line
4: Fourth line
```

## よくある質問

#### Q1. `sed`と`awk`の違いは何ですか？
A. `sed`は主にテキスト置換に特化したストリームエディタであるのに対し、`awk`はより複雑なテキスト処理やデータ抽出のためのプログラミング言語的な機能を持っています。

#### Q2. MacOSの`sed`とGNU `sed`の違いは何ですか？
A. MacOSのデフォルトの`sed`はBSD版で、GNU版とは一部の動作や構文が異なります。特に`-i`オプションでは、MacOSでは必ずバックアップ拡張子を指定する必要があります。

#### Q3. 複数のファイルを一度に編集するにはどうすればよいですか？
A. ワイルドカードを使用するか、ファイル名を複数指定することで可能です：`sed 's/old/new/g' file1.txt file2.txt`

#### Q4. 特定の行だけを編集するにはどうすればよいですか？
A. アドレス指定を使用します：`sed '3s/old/new/' file.txt`は3行目のみを編集します。

## macOSでの注意点

macOSのデフォルトの`sed`はBSD版であり、GNU版とは異なる動作をします。特に以下の点に注意してください：

1. `-i`オプションを使用する場合、必ずバックアップ拡張子を指定する必要があります：
   ```console
   $ sed -i '' 's/old/new/g' file.txt  # バックアップなし
   $ sed -i '.bak' 's/old/new/g' file.txt  # .bakという拡張子でバックアップ
   ```

2. 一部の正規表現構文が異なる場合があります。GNU版の高度な機能を使いたい場合は、Homebrewなどでインストールできます：
   ```console
   $ brew install gnu-sed
   $ gsed -i 's/old/new/g' file.txt  # gsedとして使用
   ```

## 参考資料

https://www.gnu.org/software/sed/manual/sed.html

## 改訂履歴

- 2025/04/30 初版作成