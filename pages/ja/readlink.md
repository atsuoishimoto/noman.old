# readlink コマンド

シンボリックリンクの参照先（リンク先）を表示します。

## 概要

`readlink`コマンドは、シンボリックリンクが指し示す実際のファイルやディレクトリのパスを表示します。シンボリックリンクの解決や、スクリプト内で実際のファイルパスを取得する際に便利です。

## オプション

### **-f, --canonicalize**

すべてのシンボリックリンクを再帰的に解決し、正規化された絶対パスを表示します。

```console
$ ln -s /etc/hosts mylink
$ readlink -f mylink
/etc/hosts
```

### **-e, --canonicalize-existing**

すべてのコンポーネント（パスの各部分）が存在する場合のみ、正規化された絶対パスを表示します。

```console
$ readlink -e mylink
/etc/hosts

$ readlink -e non_existent_link
# 存在しないリンクの場合は何も出力されない
```

### **-m, --canonicalize-missing**

コンポーネント（パスの各部分）が存在しなくても、正規化された絶対パスを表示します。

```console
$ readlink -m /path/to/non_existent_file
/path/to/non_existent_file
```

### **-n, --no-newline**

出力の最後に改行を付けません。

```console
$ readlink -n mylink && echo " (これはリンク先です)"
/etc/hosts (これはリンク先です)
```

## 使用例

### 基本的な使い方

```console
$ ln -s /var/log/syslog loglink
$ readlink loglink
/var/log/syslog
```

### スクリプト内での使用例

```console
$ cat get_real_path.sh
#!/bin/bash
SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
echo "このスクリプトの実際のパス: $SCRIPT_PATH"
echo "このスクリプトのディレクトリ: $SCRIPT_DIR"

$ ./get_real_path.sh
このスクリプトの実際のパス: /home/user/scripts/get_real_path.sh
このスクリプトのディレクトリ: /home/user/scripts
```

### 複数のシンボリックリンクを解決する

```console
$ mkdir -p test/subdir
$ ln -s test/subdir link1
$ ln -s link1 link2
$ readlink link2
link1
$ readlink -f link2
/home/user/test/subdir
```

## ヒント:

### シンボリックリンクとハードリンクの違い

`readlink`はシンボリックリンク（ソフトリンク）にのみ機能します。ハードリンクは別のファイル名を持つ同じファイルであるため、`readlink`では解決できません。

### スクリプトの実際のパスを取得する

スクリプト内で自身の実際のパスを取得するには、`readlink -f "$0"`を使用します。これはシンボリックリンク経由で実行された場合でも正確なパスを返します。

### 存在しないパスの扱い

`-f`オプションは、リンク先が存在しない場合でもパスを解決しようとしますが、`-e`オプションは全てのコンポーネントが存在する場合のみ結果を返します。

## よくある質問

#### Q1. `readlink`と`realpath`の違いは何ですか？
A. どちらもシンボリックリンクを解決しますが、`realpath`はデフォルトで絶対パスを返し、より多くのオプションを提供します。`readlink`は単純にリンク先を表示することに特化しています。

#### Q2. シンボリックリンクでないファイルに`readlink`を使うとどうなりますか？
A. 通常のファイルに対しては何も出力せず、エラーコードを返します。`-f`オプションを使用した場合は、そのファイルの絶対パスを返します。

#### Q3. 複数のシンボリックリンクが連鎖している場合はどうなりますか？
A. 基本的な`readlink`は最初のリンク先のみを表示しますが、`-f`オプションを使用すると、最終的な実ファイルまですべてのリンクを解決します。

#### Q4. macOSでの`readlink`は GNU版と同じですか？
A. いいえ、macOSのデフォルトの`readlink`は GNU版と比べて機能が制限されています。特に`-f`オプションがありません。代わりに`greadlink`（GNU readlink）をインストールするか、`realpath`コマンドを使用することをお勧めします。

## macOSでの注意点

macOSのデフォルトの`readlink`コマンドは GNU版と互換性がなく、`-f`などの重要なオプションがありません。Homebrewを使って GNU coreutils をインストールすることで、`greadlink`として GNU版を使用できます：

```console
$ brew install coreutils
$ greadlink -f mylink
/etc/hosts
```

または、macOSでは代わりに`realpath`コマンドを使用することもできます：

```console
$ realpath mylink
/etc/hosts
```

## 参照

https://www.gnu.org/software/coreutils/manual/html_node/readlink-invocation.html

## 改訂

- 2025/04/30 初版作成