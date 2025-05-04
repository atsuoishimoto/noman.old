# rmdir コマンド

ファイルシステムから空のディレクトリを削除します。

## 概要

`rmdir`コマンドはファイルシステムから空のディレクトリを削除します。ファイルやサブディレクトリが含まれていないディレクトリのみを削除できます。内容物があるディレクトリを削除するには、`rm`コマンドと特定のオプションを使用する必要があります。

## オプション

### **-p, --parents**

ディレクトリとその親ディレクトリを削除します。例えば、`rmdir -p a/b/c`は`rmdir a/b/c a/b a`と同様の動作をします。

```console
$ mkdir -p test/nested/dir
$ rmdir -p test/nested/dir
$ ls test
ls: 'test' にアクセスできません: そのようなファイルやディレクトリはありません
```

### **-v, --verbose**

処理されるディレクトリごとに診断メッセージを出力します。

```console
$ mkdir empty1 empty2
$ rmdir -v empty1 empty2
rmdir: ディレクトリ 'empty1' を削除しています
rmdir: ディレクトリ 'empty2' を削除しています
```

### **--ignore-fail-on-non-empty**

ディレクトリが空でないことだけが原因で発生する失敗を無視します。

```console
$ mkdir nonempty
$ touch nonempty/file
$ rmdir --ignore-fail-on-non-empty nonempty
$ ls
nonempty
```

## 使用例

### 単一の空ディレクトリの削除

```console
$ mkdir emptydir
$ rmdir emptydir
$ ls
[emptydir はリストに表示されなくなる]
```

### 複数の空ディレクトリを一度に削除

```console
$ mkdir dir1 dir2 dir3
$ rmdir dir1 dir2 dir3
$ ls
[どのディレクトリもリストに表示されない]
```

### 空でないディレクトリの削除を試みる

```console
$ mkdir nonempty
$ touch nonempty/file
$ rmdir nonempty
rmdir: 'nonempty' を削除できません: ディレクトリが空ではありません
```

## ヒント:

### 先にディレクトリが空かどうかを確認する

`rmdir`を使用する前に、`ls -A ディレクトリ名`でディレクトリが空かどうかを確認できます。何も表示されなければ、そのディレクトリは空です。

### findコマンドと組み合わせて使用する

`find`と組み合わせて複数の空ディレクトリを削除できます: `find /path -type d -empty -exec rmdir {} \;`

### ディレクトリツリーの削除

ディレクトリツリー全体（空でないディレクトリを含む）を削除するには、`rmdir`ではなく`rm -r`を使用します。これはすべての内容を確認なしで削除するため、注意が必要です。

## よくある質問

#### Q1. rmdirが「ディレクトリが空ではありません」というエラーで失敗するのはなぜですか？
A. `rmdir`は空のディレクトリのみを削除します。ディレクトリにファイルやサブディレクトリが含まれている場合は、代わりに`rm -r ディレクトリ名`を使用してください。

#### Q2. rmdirとrm -dはどう違いますか？
A. 空のディレクトリに対しては機能的に同等です。どちらのコマンドも空のディレクトリのみを削除できます。

#### Q3. rmdirで複数のディレクトリを一度に削除できますか？
A. はい、複数のディレクトリを指定できます: `rmdir dir1 dir2 dir3`

#### Q4. 入れ子になった空のディレクトリを削除するにはどうすればよいですか？
A. `-p`オプションを使用します: `rmdir -p 親/子/孫`は、すべてのディレクトリが空であれば3つすべてを削除します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/rmdir-invocation.html

## 改訂履歴

- 2025/05/04 初版作成