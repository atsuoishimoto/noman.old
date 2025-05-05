# realpath コマンド

ファイルの解決された絶対パスを表示します。

## 概要

`realpath`コマンドは、パス名をその絶対パスに解決し、すべてのシンボリックリンクをたどります。特にシンボリックリンクや相対パスを扱う際に、ファイルの実際の場所を特定するのに役立ちます。

## オプション

### **-e, --canonicalize-existing**

パスのすべてのコンポーネントが存在する必要があります

```console
$ realpath -e /etc/hosts
/etc/hosts

$ realpath -e /nonexistent/file
realpath: /nonexistent/file: No such file or directory
```

### **-m, --canonicalize-missing**

パスコンポーネントが存在する必要はなく、ディレクトリである必要もありません

```console
$ realpath -m /nonexistent/file
/nonexistent/file
```

### **-L, --logical**

シンボリックリンクの前に'..'コンポーネントを解決します（デフォルトの動作）

```console
$ ln -s /usr/bin bin_link
$ realpath -L bin_link/../share
/usr/share
```

### **-P, --physical**

シンボリックリンクを遭遇した時点で解決し、その後'..'コンポーネントを解決します

```console
$ ln -s /usr/bin bin_link
$ realpath -P bin_link/../share
/share
```

### **-q, --quiet**

エラーメッセージを抑制します

```console
$ realpath -q /nonexistent/file
$ echo $?
1
```

### **-s, --strip, --no-symlinks**

シンボリックリンクを展開しません

```console
$ ln -s /usr/bin bin_link
$ realpath -s bin_link
/home/user/bin_link
```

### **-z, --zero**

各出力行を改行ではなくNUL文字で終了します

```console
$ realpath -z /etc/hosts | hexdump -C
00000000  2f 65 74 63 2f 68 6f 73  74 73 00                 |/etc/hosts.|
0000000b
```

## 使用例

### 相対パスの解決

```console
$ cd /usr/local
$ realpath bin/../share
/usr/local/share
```

### シンボリックリンクの操作

```console
$ ln -s /var/log logs
$ realpath logs
/var/log
```

### スクリプトで絶対パスを取得する

```console
$ cat myscript.sh
#!/bin/bash
SCRIPT_DIR=$(realpath $(dirname "$0"))
echo "スクリプトの場所: $SCRIPT_DIR"
```

## ヒント:

### シェルスクリプトでの使用

シェルスクリプトを書く際、`SCRIPT_DIR=$(realpath $(dirname "$0"))`を使用してスクリプトディレクトリの絶対パスを取得できます。これにより、スクリプトがどこから呼び出されても正しく動作します。

### 他のコマンドとの組み合わせ

`find`や`xargs`などのコマンドと`realpath`を組み合わせて、ファイルを絶対パスで処理できます：`find . -type f | xargs realpath`

### エラー処理

エラーメッセージを抑制したい場合は`-q`オプションを使用し、代わりに終了ステータスをチェックします。これはエラーを適切に処理したいスクリプトで役立ちます。

## よくある質問

#### Q1. `realpath`と`readlink -f`の違いは何ですか？
A. どちらのコマンドもシンボリックリンクを解決して絶対パスを返しますが、`realpath`はパスの解決方法をより細かく制御するオプションを提供します。`readlink -f`は古いシステムでより一般的に利用可能です。

#### Q2. ファイルが存在するかを確認するために`realpath`をどう使いますか？
A. `realpath -e`を使用すると、ファイルが存在しない場合にエラーを返します。

#### Q3. `realpath`はファイル名の空白を処理できますか？
A. はい、ただしスクリプトで使用する場合は、引数を引用符で囲むようにしてください：`realpath "$filename"`

#### Q4. `-L`と`-P`オプションの違いは何ですか？
A. `-L`（論理的）はシンボリックリンクの前に'..'コンポーネントを解決し、`-P`（物理的）はまずシンボリックリンクを解決してから'..'コンポーネントを解決します。デフォルトは`-L`です。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html

## 改訂履歴

- 2025/05/04 初版作成