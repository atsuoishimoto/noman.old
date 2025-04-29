# sed コマンド

テキストストリームに対して変換や置換などの編集操作を行います。

## 概要
`sed`（Stream EDitor）は、テキストファイルやストリームを処理するためのテキスト変換ツールです。パターンマッチングを使用してテキストを検索・置換したり、特定の行を削除・追加したりすることができます。コマンドラインから直接実行でき、シェルスクリプト内でも頻繁に使用されます。

## オプション
### **-e**：複数の編集コマンドを指定
複数の編集操作を一度に実行できます。

```console
$ echo "Hello World" | sed -e 's/Hello/Hi/' -e 's/World/Everyone/'
Hi Everyone
```

### **-i**：ファイルを直接編集
ファイルを直接変更します（元のファイルを上書き）。

```console
$ sed -i 's/old/new/g' file.txt
# file.txtの「old」を「new」に置き換えて保存する
```

### **-n**：自動出力を抑制
マッチした行のみを出力します（デフォルトではすべての行が出力されます）。

```console
$ sed -n '/pattern/p' file.txt
# 「pattern」を含む行のみを表示する
```

### **-r/-E**：拡張正規表現を使用
拡張正規表現を使用できるようにします。

```console
$ echo "123 456" | sed -E 's/[0-9]+/NUM/g'
NUM NUM
# すべての数字の並びを「NUM」に置換する
```

## 編集コマンド
### **s**：置換（substitute）
テキストパターンを検索して置換します。

```console
$ echo "Hello World" | sed 's/Hello/Hi/'
Hi World
# 「Hello」を「Hi」に置換する
```

### **d**：削除（delete）
指定したパターンや行を削除します。

```console
$ echo -e "Line 1\nLine 2\nLine 3" | sed '2d'
Line 1
Line 3
# 2行目を削除する
```

### **p**：表示（print）
通常は `-n` オプションと組み合わせて使用し、特定のパターンに一致する行のみを表示します。

```console
$ echo -e "apple\nbanana\napricot" | sed -n '/^a/p'
apple
apricot
# 「a」で始まる行のみを表示する
```

### **i**：挿入（insert）
指定した行の前に新しいテキストを挿入します。

```console
$ echo -e "Line 1\nLine 2" | sed '1i\New Line'
New Line
Line 1
Line 2
# 1行目の前に「New Line」を挿入する
```

### **a**：追加（append）
指定した行の後に新しいテキストを追加します。

```console
$ echo -e "Line 1\nLine 2" | sed '1a\New Line'
Line 1
New Line
Line 2
# 1行目の後に「New Line」を追加する
```

## 使用例
### 基本的な置換
```console
$ echo "The quick brown fox" | sed 's/brown/red/'
The quick red fox
# 最初に出現する「brown」を「red」に置換する
```

### グローバル置換（g フラグ）
```console
$ echo "brown paper brown bag" | sed 's/brown/white/g'
white paper white bag
# すべての「brown」を「white」に置換する
```

### 特定の行を削除
```console
$ cat file.txt
Line 1
Line 2
Line 3
Line 4

$ sed '2d' file.txt
Line 1
Line 3
Line 4
# 2行目を削除する
```

### 特定のパターンを含む行を削除
```console
$ sed '/pattern/d' file.txt
# 「pattern」を含む行を削除する
```

### 範囲指定での編集
```console
$ sed '2,4s/old/new/g' file.txt
# 2行目から4行目までの「old」を「new」に置換する
```

## ヒント:
### バックアップを作成しながら編集
ファイルを直接編集する際は、バックアップを作成することをお勧めします。
```console
$ sed -i.bak 's/old/new/g' file.txt
# file.txt.bakというバックアップファイルが作成される
```

### 置換時に一致したパターンを参照
`&`記号を使うと、一致したパターン全体を参照できます。
```console
$ echo "Hello" | sed 's/Hello/& World/'
Hello World
# 「Hello」を「Hello World」に置換する
```

### 複数行の処理
`N`コマンドを使うと、複数行にまたがるパターンを処理できます。
```console
$ sed 'N; s/\n/ /' file.txt
# 改行を空白に置換して2行を1行にする
```

## よくある質問
#### Q1. sedの基本的な構文は？
A. 基本構文は `sed 'コマンド' ファイル` です。コマンドには `s/検索パターン/置換テキスト/フラグ` などがあります。

#### Q2. 元のファイルを変更せずに結果を確認するには？
A. デフォルトでは、`sed`は標準出力に結果を表示し、元のファイルは変更しません。変更を適用するには `-i` オプションを使用します。

#### Q3. 特定の行だけを編集するには？
A. `sed '行番号s/old/new/'` のように行番号を指定できます。例：`sed '3s/old/new/' file.txt`

#### Q4. 正規表現を使用できますか？
A. はい、`sed`は基本的な正規表現をサポートしています。拡張正規表現を使用するには `-E`（または `-r`）オプションを使用します。

#### Q5. 複数のファイルを一度に編集できますか？
A. はい、複数のファイルを指定できます。例：`sed 's/old/new/g' file1.txt file2.txt`

## macOSでの注意点
- macOSの`sed`はBSD版で、GNU版と若干動作が異なります。
- 特に `-i` オプションでは、macOSでは `-i ''` のように空の拡張子を指定する必要があります：
  ```console
  $ sed -i '' 's/old/new/g' file.txt
  ```
- GNU版の高度な機能の一部がサポートされていない場合があります。
- macOSでGNU版のsedを使用したい場合は、Homebrewで `gsed` をインストールできます：
  ```console
  $ brew install gnu-sed
  $ gsed -i 's/old/new/g' file.txt
  ```

## 参照
https://www.gnu.org/software/sed/manual/sed.html

## 改訂履歴
- 2025/04/27 編集コマンドセクションを追加し、macOSでの注意点を拡充。拡張正規表現のオプションを追加。
- 2025/04/27 初回作成