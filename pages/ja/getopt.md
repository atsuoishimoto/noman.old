# getopt コマンド

コマンドラインオプションを標準化された方法で解析します。

## 概要

`getopt`はコマンドラインユーティリティで、指定された形式に従ってコマンドライン引数を解析し、シェルスクリプトでのオプション処理を容易にします。引数を標準的な形式に並べ替えることで、スクリプトが処理しやすい形に整えます。

## オプション

### **-a, --alternative**

代替解析モードを有効にします（長いオプションが単一のダッシュで始まることを許可）

```console
$ getopt -a -o a:b -l alpha:,beta -- -alpha foo -b
 -a 'foo' -b --
```

### **-l, --longoptions**

認識する長いオプションを定義します

```console
$ getopt -l help,version,output: -- --help --output=file.txt
 --help --output 'file.txt' --
```

### **-n, --name**

エラーメッセージで使用される名前を設定します

```console
$ getopt -n myscript -o a:b -- -x
myscript: invalid option -- 'x'
```

### **-o, --options**

認識する短いオプションを定義します

```console
$ getopt -o a:bc -- -a value -bc
 -a 'value' -b -c --
```

### **-q, --quiet**

エラーメッセージを抑制します

```console
$ getopt -q -o a:b -- -x
 --
```

### **-Q, --quiet-output**

通常の出力を抑制します（有効なオプションの確認時に便利）

```console
$ getopt -Q -o a:b -- -a value
```

### **-s, --shell**

指定されたシェル（bash、sh、csh）に従って引用規則を設定します

```console
$ getopt -s bash -o a: -- -a "file with spaces"
 -a 'file with spaces' --
```

### **-T, --test**

テストモード - 解析されたオプションを出力しますが実行しません

```console
$ getopt -T -o a:b -- -a value -b
 -a 'value' -b --
```

### **-u, --unquoted**

出力を引用符で囲みません

```console
$ getopt -u -o a:b -- -a value
 -a value --
```

## 使用例

### シェルスクリプトでの基本的なオプション解析

```console
$ cat myscript.sh
#!/bin/bash
OPTS=$(getopt -o a:bc -l alpha:,beta,charlie -- "$@")
eval set -- "$OPTS"
while true; do
  case "$1" in
    -a|--alpha) echo "Alpha option with value: $2"; shift 2 ;;
    -b|--beta) echo "Beta option enabled"; shift ;;
    -c|--charlie) echo "Charlie option enabled"; shift ;;
    --) shift; break ;;
    *) echo "Internal error!"; exit 1 ;;
  esac
done
echo "Remaining arguments: $@"

$ ./myscript.sh -a foo --beta arg1 arg2
Alpha option with value: foo
Beta option enabled
Remaining arguments: arg1 arg2
```

### 値に空白を含むオプションの処理

```console
$ getopt -o d: -- -d "my directory"
 -d 'my directory' --
```

### 単一ダッシュの長いオプションに代替モードを使用

```console
$ getopt -a -o "" -l help,version -- -help -version
 --help --version --
```

## ヒント:

### 常にエラーをチェックする

スクリプトを続行する前に、オプションが有効であることを確認するために、常にgetoptのリターンコードをチェックしましょう。

```console
$ if ! OPTS=$(getopt -o a:b -n "$0" -- "$@"); then exit 1; fi
```

### eval set -- を使用して出力を処理する

スクリプトでgetoptを使用する標準的な方法は、その出力をキャプチャし、`eval set --`を使用して処理された引数でスクリプトの引数を置き換えることです。

### 基本的なgetoptよりも拡張getoptを優先する

拡張getopt（util-linuxから）は、一部のシステムで見られる基本バージョンよりも長いオプションとより良いエラー処理をサポートしています。`getopt -V`でどのバージョンを持っているか確認できます。

### 引数の空白の処理

空白を正しく処理するために、getoptに変数を渡す際は常に引用符で囲みましょう：`getopt ... -- "$@"`であり、`getopt ... -- $@`ではありません。

## よくある質問

#### Q1. getoptとgetoptsの違いは何ですか？
A. `getopt`は短いオプションと長いオプションの両方をサポートする外部コマンドであり、`getopts`は短いオプションのみを処理するシェル組み込みコマンドですが、異なるUnixライクシステム間でより移植性があります。

#### Q2. 値を必要とするオプションを指定するにはどうすればよいですか？
A. 短いオプションの場合、オプション文字列でオプション文字の後にコロンを追加します（例：`a:`は`-a value`用）。長いオプションの場合、オプション名の後にコロンを追加します（例：`alpha:`は`--alpha=value`用）。

#### Q3. オプション引数を持つオプションを処理するにはどうすればよいですか？
A. 拡張getoptは、2つのコロンを使用して長いオプションのオプション引数をサポートしています（例：`alpha::`は`--alpha[=value]`用）。

#### Q4. なぜスクリプトが「getopt: unrecognized option」で失敗するのですか？
A. 長いオプションをサポートしない基本バージョンのgetoptを使用している可能性があります。短いオプションのみを使用するか、拡張バージョンにアップグレードしてみてください。

## 参照

https://man7.org/linux/man-pages/man1/getopt.1.html

## 改訂履歴

- 2025/05/04 初版作成