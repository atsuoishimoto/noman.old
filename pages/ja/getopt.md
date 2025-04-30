# getopt コマンド

コマンドラインオプションを解析し、シェルスクリプト内でのオプション処理を簡素化します。

## 概要

`getopt` はシェルスクリプト内でコマンドラインオプションを解析するためのユーティリティです。短いオプション（-a など）と長いオプション（--option など）の両方を処理でき、オプション引数の有無も管理できます。これにより、スクリプト内でのユーザー入力の処理が標準化され、堅牢なスクリプトを作成できます。

## オプション

### **-o, --options**

短いオプション（1文字）を指定します。コロン（:）を付けると、そのオプションは引数を必要とします。

```console
$ getopt -o a:bc -- -a value -b -c
 -a 'value' -b -c --
```

### **-l, --longoptions**

長いオプション名を指定します。コンマで区切り、コロン（:）を付けると引数を必要とします。

```console
$ getopt -o a:bc -l alpha:,beta,gamma -- --alpha=value --beta
 -a 'value' --beta --
```

### **-n, --name**

エラーメッセージに表示するプログラム名を指定します。

```console
$ getopt -n "myscript" -o a:bc -- -a
getopt: option requires an argument -- 'a'
```

### **-q, --quiet**

エラーメッセージを表示しません。

```console
$ getopt -q -o a:bc -- -d
 -- -d
```

## 使用例

### 基本的なシェルスクリプトでの使用

```console
$ cat example.sh
#!/bin/bash
# オプションを解析
OPTS=$(getopt -o a:bc -l alpha:,beta,gamma -n "$(basename $0)" -- "$@")
if [ $? -ne 0 ]; then
    exit 1
fi
eval set -- "$OPTS"

# オプションを処理
while true; do
    case "$1" in
        -a|--alpha) echo "Alpha option with value: $2"; shift 2 ;;
        -b|--beta) echo "Beta option enabled"; shift ;;
        -c|--gamma) echo "Gamma option enabled"; shift ;;
        --) shift; break ;;
        *) echo "Internal error!"; exit 1 ;;
    esac
done

# 残りの引数を処理
echo "Remaining arguments: $@"

$ ./example.sh -a "hello world" -b file1 file2
Alpha option with value: hello world
Beta option enabled
Remaining arguments: file1 file2
```

### 長いオプションの使用

```console
$ ./example.sh --alpha="hello world" --gamma file1 file2
Alpha option with value: hello world
Gamma option enabled
Remaining arguments: file1 file2
```

## ヒント:

### GNU getopt と拡張 getopt の違い

多くのLinuxディストリビューションではGNU getoptが使用されていますが、一部のシステム（特に古いUnix系）では拡張機能（長いオプションなど）をサポートしていない場合があります。スクリプトの互換性を確保するには、最初に `getopt -T` でテストするとよいでしょう。

### エラー処理を忘れずに

getoptの戻り値を確認し、オプション解析に失敗した場合は適切にエラー処理を行いましょう。

### 引数に空白やシェル特殊文字が含まれる場合

引数に空白やシェル特殊文字が含まれる場合は、`eval set -- "$OPTS"` を使用して適切に処理する必要があります。

## よくある質問

#### Q1. getoptとgetopts（シェル組み込みコマンド）の違いは何ですか？
A. `getopt`は外部コマンドで、長いオプション（--option形式）をサポートしています。一方、`getopts`はシェル組み込みコマンドで、短いオプション（-o形式）のみをサポートしますが、より移植性が高いです。

#### Q2. getoptでオプションの順序を強制できますか？
A. いいえ、getoptはオプションの順序を強制しません。ユーザーは任意の順序でオプションを指定できます。

#### Q3. getoptは必須オプションを指定できますか？
A. getopt自体には必須オプションを指定する機能はありません。スクリプト内でオプションが指定されているかどうかを確認する必要があります。

#### Q4. 長いオプションと短いオプションを関連付けるにはどうすればよいですか？
A. スクリプト内の`case`文で、`-a|--alpha)`のように両方のオプションを同じケースで処理します。

## macOSでの注意点

macOSのデフォルトの`getopt`は拡張機能（長いオプションなど）をサポートしていません。GNU getoptを使用するには、Homebrewを使ってインストールする必要があります：

```console
$ brew install gnu-getopt
$ PATH="/usr/local/opt/gnu-getopt/bin:$PATH"
```

または、macOSでは代わりに`getopts`（シェル組み込みコマンド）の使用を検討してください。

## 参考文献

https://man7.org/linux/man-pages/man1/getopt.1.html

## 改訂履歴

- 2025/04/30 初版作成