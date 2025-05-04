# git reset コマンド

指定した状態に現在のHEADをリセットします。

## 概要

`git reset`は、現在のブランチポインタを別のコミットに移動させることで変更を元に戻すコマンドです。使用するモードによって、ステージングエリア（インデックス）や作業ディレクトリも変更できます。このコマンドは、ファイルのステージング解除、コミットの取り消し、またはGit履歴内の以前の状態に完全に戻すために一般的に使用されます。

## オプション

### **--soft**

HEADを指定したコミットに移動しますが、インデックスと作業ディレクトリは変更しません。これにより、すべての変更をステージングしたまま、コミットを取り消すことができます。

```console
$ git reset --soft HEAD~1
```

### **--mixed（デフォルト）**

HEADを指定したコミットに移動し、インデックスを一致するように更新しますが、作業ディレクトリは変更しません。これにより、変更を作業ディレクトリに保持したまま、ステージングを解除します。

```console
$ git reset HEAD file.txt
```

### **--hard**

HEADを指定したコミットに移動し、インデックスと作業ディレクトリの両方を一致するように更新します。これにより、ステージングエリアと作業ディレクトリのすべての変更が破棄されます。

```console
$ git reset --hard HEAD~2
```

### **--patch (-p)**

リセットする変更の塊（ハンク）を対話的に選択します。

```console
$ git reset -p
```

### **--keep**

インデックスエントリをリセットしますが、インデックスと作業ツリーの間で異なるファイルは保持します。

```console
$ git reset --keep HEAD~1
```

## 使用例

### ファイルのステージング解除

```console
$ git add file.txt
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   file.txt

$ git reset file.txt
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
```

### 最後のコミットを取り消すが変更は保持する

```console
$ git reset --soft HEAD~1
```

### 最近のコミットと変更を完全に破棄する

```console
$ git reset --hard HEAD~3
HEAD is now at a1b2c3d 3コミット前のメッセージ
```

### 特定のコミットにリセットする

```console
$ git reset --mixed 5a78ef2
```

## ヒント:

### リセットを安全に試す

`git reset --hard`を使用する前に、`git branch backup-branch`でバックアップブランチを作成しておくと、必要に応じて復元できます。

### ハードリセットから復元する

誤って`--hard`で遠くまでリセットしてしまった場合は、`git reflog`を使用して戻りたいコミットを見つけ、`git reset --hard COMMIT_HASH`で戻ることができます。

### すべてのファイルのステージング解除

引数なしで`git reset`を使用すると、作業ディレクトリの変更を保持したまま、すべてのファイルのステージングを解除できます。

### 選択的なステージング解除

`git reset -p`を使用すると、ステージング解除するファイルの特定の部分を選択できる対話的なステージング解除が可能です。

## よくある質問

#### Q1. `git reset`と`git revert`の違いは何ですか？
A. `git reset`はブランチポインタを移動させて履歴を変更しますが、`git revert`は以前の変更を元に戻す新しいコミットを作成し、履歴を保持します。

#### Q2. `git reset --hard`を元に戻すにはどうすればよいですか？
A. `git reflog`を使用してリセット前のコミットハッシュを見つけ、`git reset --hard COMMIT_HASH`でその時点に復元します。

#### Q3. 公開ブランチで`git reset`を使用できますか？
A. 共有リポジトリにすでにプッシュしたブランチでは、履歴を書き換えるため`git reset`の使用は推奨されません。代わりに`git revert`を使用してください。

#### Q4. すべてのファイルのステージングを解除するにはどうすればよいですか？
A. 引数なしで`git reset`を実行すると、すべてのファイルのステージングが解除されます。

#### Q5. `git reset HEAD~1`の`HEAD~1`とは何を意味しますか？
A. `HEAD~1`は現在のHEADの前のコミット（履歴の1コミット前）を指します。

## 参考資料

https://git-scm.com/docs/git-reset

## 改訂履歴

- 2025/05/04 初版作成