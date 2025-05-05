# readlink コマンド

シンボリックリンクの解決先またはファイルの正規名を表示します。

## 概要

`readlink`コマンドは、シンボリックリンクのターゲットやファイルの正規パスを表示します。パス内のシンボリックリンクを解決し、実際の参照先を示します。多くのシンボリックリンクを含むファイルシステムで、ファイルの実際の場所を特定するのに役立ちます。

## オプション

### **-f, --canonicalize**

指定されたパスの各コンポーネントのシンボリックリンクを再帰的にたどり、正規化します

```console
$ ln -s /etc/hosts mylink
$ readlink -f mylink
/etc/hosts
```

### **-e, --canonicalize-existing**

指定されたパスの各コンポーネントのシンボリックリンクを再帰的にたどり正規化しますが、すべてのコンポーネントが存在する必要があります

```console
$ readlink -e mylink
/etc/hosts
$ readlink -e nonexistent
# ファイルが存在しないため出力なし
```

### **-m, --canonicalize-missing**

指定されたパスの各コンポーネントのシンボリックリンクを再帰的にたどり正規化しますが、コンポーネントの存在は必要ありません

```console
$ readlink -m /nonexistent/path/file.txt
/nonexistent/path/file.txt
```

### **-n, --no-newline**

末尾の区切り文字（改行）を出力しません

```console
$ readlink -n mylink && echo " (この文は同じ行に続きます)"
/etc/hosts (この文は同じ行に続きます)
```

### **-z, --zero**

各出力行を改行ではなくNUL文字で終了します

```console
$ readlink -z mylink | hexdump -C
00000000  2f 65 74 63 2f 68 6f 73  74 73 00                 |/etc/hosts.|
0000000b
```

### **-v, --verbose**

エラーを報告します（すべてのシステムで実装されているわけではありません）

```console
$ readlink -v nonexistent
readlink: nonexistent: そのようなファイルやディレクトリはありません
```

## 使用例

### シンボリックリンクの基本的な読み取り

```console
$ ln -s /usr/bin/python3 python
$ readlink python
/usr/bin/python3
```

### 複数のシンボリックリンクを持つファイルの正規パスを見つける

```console
$ ln -s /etc/passwd passwd_link
$ ln -s passwd_link passwd_link2
$ readlink -f passwd_link2
/etc/passwd
```

### 相対パスでの作業

```console
$ mkdir -p dir1/dir2
$ ln -s dir1/dir2 mydir
$ readlink -f mydir
/home/user/dir1/dir2
```

## ヒント:

### 直接解決と完全解決の区別

シンボリックリンクの直接のターゲットだけを見るには通常の`readlink`を使用し、シンボリックリンクのチェーンを最終的な宛先まで追跡するには`readlink -f`を使用します。

### パスがシンボリックリンクかどうかを確認する

`readlink`が何も返さずに非ゼロのステータスで終了する場合、そのパスはシンボリックリンクではありません。これはスクリプトでファイルがシンボリックリンクかどうかをテストするのに使えます。

### 他のコマンドと組み合わせる

シンボリックリンクではなく実際のファイルに対して操作する必要がある場合は、`readlink`の出力を他のコマンドにパイプすると便利です。

## よくある質問

#### Q1. `readlink`と`realpath`の違いは何ですか？
A. どちらもシンボリックリンクを解決しますが、`realpath`は常に絶対パスを提供するのに対し、基本的な`readlink`はシンボリックリンクの直接のターゲットのみを表示します。`readlink -f`は`realpath`に似ています。

#### Q2. オプションなしの`readlink`が何も返さないことがあるのはなぜですか？
A. オプションなしの`readlink`はシンボリックリンクに対してのみ機能します。通常のファイルやディレクトリに使用すると、何も返さずにエラーコードで終了します。

#### Q3. シェルスクリプトで`readlink`を安全に使用するにはどうすればよいですか？
A. `readlink -f "$path"`を使用して正規パスを取得すると、適切に引用符で囲まれていれば、スペースや特殊文字を正しく処理できます。

#### Q4. シンボリックリンクが存在しないファイルを指している場合はどうなりますか？
A. 基本的な`readlink`は、ターゲットが存在しなくてもターゲットパスを表示します。`readlink -e`は失敗しますが、`readlink -f`と`readlink -m`は可能な限り解決します。

## 参照

https://www.gnu.org/software/coreutils/manual/html_node/readlink-invocation.html

## 改訂履歴

- 2025/05/04 初版作成