# git-stash

`git stash`は、作業中の変更を一時的に保存し、ワーキングディレクトリをクリーンな状態に戻すためのGitコマンドです。ブランチの切り替えやプル操作の前に、コミットしたくない変更を一時的に退避させるのに便利です。

## オプション

### **git stash save [メッセージ]**

変更を保存し、オプションでわかりやすいメッセージを付けることができます。

```bash
$ git stash save "ログイン機能の途中作業"
Saved working directory and index state On main: ログイン機能の途中作業
```

### **git stash list**

保存されたスタッシュの一覧を表示します。

```bash
$ git stash list
stash@{0}: On main: ログイン機能の途中作業
stash@{1}: On feature-branch: バグ修正の途中
```

### **git stash apply [stash@{n}]**

保存した変更を現在のブランチに適用します。スタッシュは削除されません。

```bash
$ git stash apply stash@{0}
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   login.js
```

### **git stash pop [stash@{n}]**

保存した変更を適用し、スタッシュリストから削除します。

```bash
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   login.js
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### **git stash drop [stash@{n}]**

特定のスタッシュを削除します。

```bash
$ git stash drop stash@{1}
Dropped stash@{1} (fedcba9876543210abcdef0123456789abcdef01)
```

### **git stash clear**

すべてのスタッシュを削除します。

```bash
$ git stash clear
```

### **git stash show [stash@{n}]**

スタッシュの内容を表示します。`-p`オプションで詳細な差分を確認できます。

```bash
$ git stash show stash@{0}
 login.js | 15 +++++++++++++++
 1 file changed, 15 insertions(+)

$ git stash show -p stash@{0}
diff --git a/login.js b/login.js
index 1234567..abcdefg 100644
--- a/login.js
+++ b/login.js
@@ -10,6 +10,21 @@ function validateForm() {
   // 追加されたコード
+  function checkCredentials() {
+    // ログイン処理
+  }
```

### **git stash branch <ブランチ名> [stash@{n}]**

スタッシュから新しいブランチを作成し、そこに変更を適用します。

```bash
$ git stash branch login-feature stash@{0}
Switched to a new branch 'login-feature'
On branch login-feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   login.js
Dropped stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

## 使用例

### 基本的な使い方

```bash
# 変更を一時保存
$ git stash
Saved working directory and index state WIP on main: abc1234 最後のコミットメッセージ

# 別のブランチで作業
$ git checkout another-branch
Switched to branch 'another-branch'

# 元のブランチに戻る
$ git checkout main
Switched to branch 'main'

# 保存した変更を復元して削除
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   login.js
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### 複数のスタッシュを管理する

```bash
# 変更を説明付きで保存
$ git stash save "ログイン機能の途中作業"
Saved working directory and index state On main: ログイン機能の途中作業

# 別の変更を保存
$ git stash save "ナビゲーションバーの修正"
Saved working directory and index state On main: ナビゲーションバーの修正

# スタッシュ一覧を確認
$ git stash list
stash@{0}: On main: ナビゲーションバーの修正
stash@{1}: On main: ログイン機能の途中作業

# 特定のスタッシュを適用
$ git stash apply stash@{1}
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   login.js
```

## よくある質問

#### Q1. `git stash`と`git stash save`の違いは何ですか？
A. 基本的に同じ機能ですが、`git stash save`ではメッセージを付けることができます。Git 2.16以降では`git stash push`の使用が推奨されています。

#### Q2. スタッシュを適用する際に競合が発生した場合はどうすればよいですか？
A. 通常のマージ競合と同様に解決します。競合ファイルを編集し、`git add`でマークしてから作業を続けます。

#### Q3. 特定のファイルだけをスタッシュに保存できますか？
A. はい、Git 2.13以降では`git stash push -m "メッセージ" [ファイルパス]`を使用できます。

#### Q4. スタッシュした変更を誤って削除してしまった場合、復元できますか？
A. 通常のスタッシュコマンドでは復元できませんが、`git fsck --unreachable`と`git show`を組み合わせて復元できる場合があります。ただし確実ではありません。

## 追加のヒント

- スタッシュはブランチをまたいで適用できますが、競合に注意が必要です。
- 長期間保存する変更はスタッシュではなく、トピックブランチを作成することをお勧めします。
- スタッシュにはインデックスに追加されていない（`git add`していない）ファイルも含まれますが、新規作成した未追跡ファイルは含まれません。未追跡ファイルも含めるには`git stash -u`または`git stash --include-untracked`を使用します。
- スタッシュは内部的にはコミットとして保存されるため、Git履歴を圧迫することはありません。

## 参考資料

https://git-scm.com/docs/git-stash