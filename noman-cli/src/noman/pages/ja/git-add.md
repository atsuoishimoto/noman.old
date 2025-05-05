# git add コマンド

ファイルの内容をステージングエリア（インデックス）に追加し、次のコミットの準備をします。

## 概要

`git add` コマンドは、作業ディレクトリ内のファイルの現在の内容で Git インデックスを更新します。これにより、次のコミットに含める変更をマークします。これは Git のワークフローにおける重要なステップであり、コミットする変更を選択的に選ぶことができます。

## オプション

### **-A, --all**

追跡対象および未追跡のすべてのファイルの変更を追加します

```console
$ git add -A
```

### **-u, --update**

追跡対象のファイルのみを更新します（新しいファイルは追加しません）

```console
$ git add -u
```

### **-p, --patch**

インデックスと作業ツリーの間のパッチの一部を対話的に選択します

```console
$ git add -p file.txt
diff --git a/file.txt b/file.txt
index 1234567..abcdefg 100644
--- a/file.txt
+++ b/file.txt
@@ -1,5 +1,6 @@
 This is some text.
-This line will be removed.
+This line was changed.
+This is a new line.
 More text here.
Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? 
```

### **-i, --interactive**

変更された内容を対話的に追加します

```console
$ git add -i
           staged     unstaged path
  1:    unchanged        +2/-1 file.txt
  2:    unchanged        +4/-0 another.txt

*** Commands ***
  1: status       2: update       3: revert       4: add untracked
  5: patch        6: diff         7: quit         8: help
What now> 
```

### **-n, --dry-run**

実際にファイルを追加せず、何が起こるかを表示します

```console
$ git add -n *.txt
add 'file.txt'
add 'notes.txt'
```

## 使用例

### 特定のファイルを追加する

```console
$ git add file1.txt file2.txt
```

### ディレクトリ内のすべてのファイルを追加する

```console
$ git add src/
```

### 特定の拡張子を持つすべてのファイルを追加する

```console
$ git add *.js
```

### リポジトリ内のすべての変更を追加する

```console
$ git add .
```

## ヒント:

### ステージングエリアを戦略的に使用する

ステージングエリアを使うと、焦点を絞ったコミットを作成できます。`git add .` ですべてを一度に追加するのではなく、関連する変更をまとめて追加することで、より意味のあるコミット履歴を作成できます。

### ステージングされた内容を確認する

`git add` を使用した後、`git status` を実行して、次のコミットのためにステージングされた変更を確認しましょう。これにより、意図しない変更を誤ってコミットすることを防げます。

### ステージングを取り消す

誤ってファイルをステージングした場合は、`git restore --staged <file>` （または古い構文 `git reset HEAD <file>`）でステージングを解除できます。

### 複雑な変更には対話モードを使用する

複数の変更があるファイルの場合、`git add -p` を使用してファイルの特定の部分をステージングできます。これは、1つのファイルに関連のない複数の変更を加えた場合に便利です。

## よくある質問

#### Q1. `git add .` と `git add -A` の違いは何ですか？
A. `git add .` は現在のディレクトリとそのサブディレクトリのすべての変更を追加しますが、`git add -A` は現在のディレクトリに関係なく、作業ツリー全体の変更を追加します。

#### Q2. 未追跡のファイルではなく、変更されたファイルと削除されたファイルのみを追加するにはどうすればよいですか？
A. `git add -u` または `git add --update` を使用します。

#### Q3. ファイルの変更の一部だけを追加できますか？
A. はい、`git add -p <file>` または `git add --patch <file>` を使用して、ステージングする変更を対話的に選択できます。

#### Q4. ファイルを追加した後、再び変更した場合はどうなりますか？
A. `git add` を実行した時点で存在していた変更のみがステージングされます。新しい変更は、追加するまでステージングされていない状態のままです。

## 参考文献

https://git-scm.com/docs/git-add

## 改訂履歴

- 2025/05/04 初版作成