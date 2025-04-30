# eval コマンド

シェル内で文字列をコマンドとして評価・実行します。

## 概要

`eval` コマンドは、与えられた引数を連結して単一の文字列を形成し、それをシェルコマンドとして実行します。これは変数の間接参照や動的にコマンドを生成する場合に特に役立ちます。シェルスクリプトで変数展開を二重に行いたい場合や、動的に生成されたコマンドを実行したい場合に使用されます。

## オプション

`eval` コマンド自体には特別なオプションはありません。引数として渡された文字列がそのままコマンドとして評価されます。

## 使用例

### 基本的な使用法

```console
$ command="echo Hello, World!"
$ eval $command
Hello, World!
```

### 変数の間接参照

```console
$ name="user"
$ user="John"
$ eval echo \$$name
John
```

### 動的なコマンド生成

```console
$ operation="ls"
$ options="-la"
$ directory="/tmp"
$ eval "$operation $options $directory"
total 8
drwxrwxrwt 5 root  wheel  160 4月 30 10:15 .
drwxr-xr-x 6 root  wheel  192 4月 30 10:15 ..
drwx------ 3 john  staff   96 4月 30 10:15 com.apple.launchd.xxxxx
```

### パイプやリダイレクトを含むコマンド

```console
$ cmd="ls -l | grep .txt > file_list.txt"
$ eval $cmd
# .txtファイルのリストがfile_list.txtに保存される
```

## ヒント:

### 引用符の使用に注意

`eval` に渡す文字列内の引用符は適切にエスケープする必要があります。そうしないと予期しない動作が発生する可能性があります。

```console
$ eval "echo \"This is properly escaped\""
This is properly escaped
```

### セキュリティリスク

ユーザー入力を直接 `eval` に渡すことは避けてください。これはコマンドインジェクション攻撃の原因となる可能性があります。

### 変数展開の順序

`eval` を使用すると、変数は2回展開されます。最初にコマンドラインが解析されるとき、次に `eval` によって解析されるときです。

```console
$ var1="Hello"
$ var2='$var1'
$ echo $var2
$var1
$ eval echo $var2
Hello
```

## よくある質問

#### Q1. `eval` はどのような場合に使うべきですか？
A. 変数の間接参照、動的なコマンド生成、複雑なシェル構文の実行など、通常のシェル展開では不十分な場合に使用します。

#### Q2. `eval` の使用にはどのようなリスクがありますか？
A. ユーザー入力を直接 `eval` に渡すと、コマンドインジェクション攻撃のリスクがあります。信頼できる入力のみを使用し、可能な限り他の方法を検討してください。

#### Q3. `eval` と通常のコマンド実行の違いは何ですか？
A. 通常のコマンド実行では変数は1回だけ展開されますが、`eval` では2回展開されます。これにより、動的に生成されたコマンドや変数の間接参照が可能になります。

## 参照

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/eval.html

## Revisions

- 2025/04/30 初版作成。