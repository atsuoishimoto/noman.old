# echo コマンド

標準出力に文字列やテキストを表示します。

## 概要

`echo`コマンドは、指定されたテキストや変数の内容を標準出力（通常は画面）に表示するシンプルなコマンドです。シェルスクリプトでの変数の値の確認や、単純なテキスト出力に広く使用されています。

## オプション

### **-n**

改行を出力しません。通常、`echo`は出力の最後に改行を追加しますが、このオプションを使用すると改行が省略されます。

```console
$ echo -n "Hello"
Hello$
```

出力の後にプロンプトが同じ行に表示されていることに注意してください。

### **-e**

バックスラッシュエスケープシーケンスを解釈します。これにより、特殊文字（\n、\t など）を使用できます。

```console
$ echo -e "Hello\nWorld"
Hello
World
```

### **-E**

バックスラッシュエスケープシーケンスを解釈しません（多くのシステムでのデフォルト動作）。

```console
$ echo -E "Hello\nWorld"
Hello\nWorld
```

## 使用例

### 基本的な使用法

```console
$ echo "Hello, World!"
Hello, World!
```

### 変数の内容を表示

```console
$ name="Taro"
$ echo "My name is $name"
My name is Taro
```

### 複数の引数を渡す

```console
$ echo This is a test
This is a test
```

### エスケープシーケンスを使用する

```console
$ echo -e "Tab:\t|\nNewline"
Tab:	|
Newline
```

## ヒント:

### クォートの違いを理解する

シングルクォート（'）はシェル変数の展開を防ぎ、ダブルクォート（"）は変数展開を許可します。

```console
$ name="Taro"
$ echo "Hello $name"
Hello Taro
$ echo 'Hello $name'
Hello $name
```

### コマンド置換を活用する

バッククォート（`）または$(...)を使用して、コマンドの出力を`echo`に渡すことができます。

```console
$ echo "Today is $(date +%Y-%m-%d)"
Today is 2025-04-30
```

### 複数行のテキストを出力する

ヒアドキュメント構文を使用して、複数行のテキストを出力できます。

```console
$ cat <<EOF
> Line 1
> Line 2
> Line 3
> EOF
Line 1
Line 2
Line 3
```

## よくある質問

#### Q1. `echo`と`printf`の違いは何ですか？
A. `echo`はシンプルなテキスト出力に適していますが、`printf`はより複雑なフォーマット制御が可能です。`printf`はC言語のprintf関数に似た構文を持っています。

#### Q2. `echo`コマンドの出力をファイルに保存するにはどうすればよいですか？
A. リダイレクト演算子（>）を使用します。例：`echo "Hello" > file.txt`

#### Q3. `echo`コマンドでカラーテキストを出力するにはどうすればよいですか？
A. ANSIエスケープシーケンスを使用します。例：`echo -e "\033[31mRed text\033[0m"`

#### Q4. macOSと他のUnixシステムで`echo`の動作に違いはありますか？
A. はい。macOSの`echo`はデフォルトで`-e`オプションが有効になっていないため、エスケープシーケンスを使用するには明示的に`-e`を指定する必要があります。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html

## 改訂履歴

- 2025/04/30 初版作成