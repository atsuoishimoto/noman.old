# git stash コマンド

作業中の変更を一時的に保存し、クリーンな作業ディレクトリに戻すためのコマンド。

## 概要

`git stash`は、コミットしていない変更（追跡されているファイルの変更とステージングされた変更）を一時的に保存し、作業ディレクトリをクリーンな状態に戻します。これにより、ブランチの切り替えやプル操作などを行う際に、コミットせずに作業を一時退避させることができます。保存した変更は後で元に戻すことができます。

## オプション

### **stash save [メッセージ]**

変更を保存し、オプションでメッセージを付けることができます。

```console
$ git stash save "作業中のログイン機能"
Saved working directory and index state On main: 作業中のログイン機能
```

### **stash list**

保存されたスタッシュの一覧を表示します。

```console
$ git stash list
stash@{0}: On main: 作業中のログイン機能
stash@{1}: On feature-branch: ナビゲーションバーの修正
```

### **stash apply [stash@{n}]**

保存した変更を現在の作業ディレクトリに適用します。スタッシュは削除されません。

```console
$ git stash apply stash@{0}
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   login.js

no changes added to commit (use "git add" and/or "git commit -a")
```

### **stash pop [stash@{n}]**

保存した変更を適用し、スタッシュリストから削除します。

```console
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   login.js

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### **stash drop [stash@{n}]**

特定のスタッシュを削除します。

```console
$ git stash drop stash@{1}
Dropped stash@{1} (f1e2d3c4b5a6)
```

### **stash clear**

すべてのスタッシュを削除します。

```console
$ git stash clear
```

### **stash show [stash@{n}]**

スタッシュの内容を表示します。`-p`オプションで詳細な差分を表示できます。

```console
$ git stash show stash@{0}
 login.js | 15 +++++++++++++++
 1 file changed, 15 insertions(+)

$ git stash show -p stash@{0}
diff --git a/login.js b/login.js
index 1234567..abcdefg 100644
--- a/login.js
+++ b/login.js
@@ -10,6 +10,21 @@ function validateForm() {
   // 入力検証のコード
+  function authenticateUser() {
+    // 認証処理のコード
+  }
```

## 使用例

### 作業中の変更を一時保存してブランチを切り替える

```console
$ git status
On branch feature-login
Changes not staged for commit:
  modified:   login.js

$ git stash
Saved working directory and index state WIP on feature-login: abc1234 最後のコミットメッセージ

$ git checkout main
Switched to branch 'main'

# 作業後、元のブランチに戻って変更を復元
$ git checkout feature-login
Switched to branch 'feature-login'

$ git stash pop
On branch feature-login
Changes not staged for commit:
  modified:   login.js
```

### 未追跡ファイルも含めてスタッシュする

```console
$ git status
On branch feature-login
Changes not staged for commit:
  modified:   login.js
Untracked files:
  auth.js

$ git stash -u
Saved working directory and index state WIP on feature-login: abc1234 最後のコミットメッセージ
```

## ヒント:

### 意味のあるメッセージを付ける

`git stash save "メッセージ"`を使って、スタッシュに説明的なメッセージを付けると、後で内容を思い出しやすくなります。

### 部分的なスタッシュ

`git stash -p`（または `--patch`）を使うと、変更の一部だけをスタッシュできます。各変更ハンクごとに保存するかどうか選択できるため、関連する変更だけをグループ化できます。

### ブランチの作成とスタッシュの適用

```console
$ git stash
$ git stash branch new-branch stash@{0}
```

このコマンドは新しいブランチを作成し、そこにスタッシュを適用して、成功したらスタッシュを削除します。コンフリクトが発生した場合に便利です。

### スタッシュの定期的なクリーンアップ

古いスタッシュは定期的に確認し、不要なものは削除しましょう。長期間放置されたスタッシュは混乱の原因になります。

## よくある質問

#### Q1. スタッシュした変更を間違って削除してしまった場合、復元できますか？
A. 通常のスタッシュ操作では、`git stash drop`や`git stash clear`で削除したスタッシュを復元することはできません。ただし、Gitのreflogを使って最近削除されたスタッシュを見つけられる場合があります。

#### Q2. 複数のブランチで同じスタッシュを適用できますか？
A. はい、`git stash apply`を使えば同じスタッシュを複数のブランチに適用できます。ただし、コンフリクトが発生する可能性があるので注意が必要です。

#### Q3. スタッシュはリモートリポジトリに共有されますか？
A. いいえ、スタッシュはローカルリポジトリにのみ保存され、`git push`でリモートに送信されることはありません。

#### Q4. スタッシュとコミットの違いは何ですか？
A. スタッシュは一時的な保存場所で、履歴に残りません。コミットはリポジトリの履歴に永続的に記録されます。スタッシュは短期的な作業の退避に、コミットは意味のある変更の記録に使用します。

## 参考資料

https://git-scm.com/docs/git-stash

## 改訂履歴

- 2025/04/30 初版作成