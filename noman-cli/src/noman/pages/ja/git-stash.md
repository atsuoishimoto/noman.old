# git-stash コマンド

作業ディレクトリの変更を一時的に保存して後で使用するためのコマンドです。

## 概要

`git stash`は、作業コピーに加えた変更を一時的に棚上げ（スタッシュ）して、別の作業に取り掛かり、後で再適用できるようにするコマンドです。スタッシュは、現在の作業をコミットする準備ができていないけれども、素早くコンテキストを切り替えて別の作業をする必要がある場合に便利です。

## オプション

### **-u, --include-untracked**

未追跡ファイルもスタッシュに含めます。

```console
$ git stash -u
Saved working directory and index state WIP on main: 2d4e15a Add feature X
```

### **-a, --all**

未追跡ファイルと無視されたファイルの両方をスタッシュに含めます。

```console
$ git stash -a
Saved working directory and index state WIP on main: 2d4e15a Add feature X
```

### **-p, --patch**

HEADと作業ツリーの差分から、スタッシュするハンクを対話的に選択します。

```console
$ git stash -p
diff --git a/file.txt b/file.txt
index 1234567..abcdefg 100644
--- a/file.txt
+++ b/file.txt
@@ -1,4 +1,4 @@
-Old content
+New content
Stash this hunk [y,n,q,a,d,e,?]? y
Saved working directory and index state WIP on main: 2d4e15a Add feature X
```

### **push [<message>]**

ローカルの変更を新しいスタッシュエントリに保存し、HEADに戻します。

```console
$ git stash push -m "WIP: implementing feature Y"
Saved working directory and index state On main: WIP: implementing feature Y
```

### **list**

スタックにあるすべてのスタッシュを一覧表示します。

```console
$ git stash list
stash@{0}: WIP on main: 2d4e15a Add feature X
stash@{1}: On main: WIP: implementing feature Y
```

### **show [<stash>]**

スタッシュに記録された変更を差分として表示します。

```console
$ git stash show stash@{0}
 file.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### **pop [<stash>]**

スタッシュを適用し、スタックから削除します。

```console
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### **apply [<stash>]**

スタッシュをスタックから削除せずに適用します。

```console
$ git stash apply stash@{1}
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
```

### **drop [<stash>]**

スタックからスタッシュを削除します。

```console
$ git stash drop stash@{0}
Dropped stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### **clear**

スタックからすべてのスタッシュを削除します。

```console
$ git stash clear
```

## 使用例

### 基本的なスタッシュのワークフロー

```console
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt

$ git stash
Saved working directory and index state WIP on main: 2d4e15a Add feature X

$ git status
On branch main
nothing to commit, working tree clean

# 他の作業をした後、スタッシュした変更に戻る
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### スタッシュからブランチを作成する

```console
$ git stash branch new-feature stash@{0}
Switched to a new branch 'new-feature'
On branch new-feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

## ヒント:

### スタッシュに名前をつける

後で識別しやすくするために、スタッシュに説明的なメッセージを使用しましょう：

```console
$ git stash push -m "認証機能のリファクタリング途中"
```

### 特定のファイルだけをスタッシュする

コマンドの後にファイルを指定することで、特定のファイルだけをスタッシュできます：

```console
$ git stash push file1.txt file2.txt
```

### スタッシュの内容を詳細に表示する

スタッシュの内容をより詳細に表示するには：

```console
$ git stash show -p stash@{0}
```

### スタッシュからブランチを作成する

スタッシュした変更を独自のブランチにすべきだと気づいた場合：

```console
$ git stash branch new-feature-branch stash@{0}
```

## よくある質問

#### Q1. ブランチを切り替えると、スタッシュした変更はどうなりますか？
A. スタッシュした変更はすべてのブランチで利用可能なままです。あるブランチで変更をスタッシュし、別のブランチで適用することができます。

#### Q2. スタッシュを削除した後に復元することはできますか？
A. はい、スタッシュのコミットハッシュ（削除時に表示される）がわかれば可能です。`git stash apply <commit-hash>`を使用して復元できますが、ガベージコレクタが実行されていない場合に限ります。

#### Q3. スタッシュはどれくらい長く保持されますか？
A. スタッシュは、明示的に`git stash drop`や`git stash clear`で削除するか、ガベージコレクションされるまで（通常は長期間）無期限に保持されます。

#### Q4. `git stash pop`と`git stash apply`の違いは何ですか？
A. `git stash pop`はスタッシュを適用した後、スタッシュリストから削除しますが、`git stash apply`はスタッシュを適用するだけで、将来の使用のためにリストに残します。

#### Q5. 未追跡ファイルをスタッシュできますか？
A. デフォルトでは、`git stash`は変更のある追跡ファイルのみをスタッシュします。未追跡ファイルを含めるには`git stash -u`を、未追跡ファイルと無視されたファイルの両方を含めるには`git stash -a`を使用します。

## 参考

https://git-scm.com/docs/git-stash

## 改訂履歴

- 2025/05/04 初版作成