# git-pull コマンド概要

`git pull`は、リモートリポジトリから最新の変更を取得し、ローカルリポジトリに統合するGitコマンドです。簡単に言えば、`git fetch`と`git merge`を一度に実行する操作です。

## オプション

### **--rebase**:

マージの代わりにリベースを使用して変更を統合します。これにより、コミット履歴がよりクリーンになります。

例: `git pull --rebase origin main`

### **--no-rebase**:

明示的にマージ方式を指定します（デフォルト）。

例: `git pull --no-rebase origin main`

### **--ff-only**:

Fast-forwardが可能な場合のみマージを実行します。コンフリクトを避けたい場合に便利です。

例: `git pull --ff-only origin main`

### **-v, --verbose**:

詳細な情報を表示します。

例: `git pull -v origin main`

### **--no-commit**:

マージ後に自動的にコミットしません。変更を確認してから手動でコミットしたい場合に使用します。

例: `git pull --no-commit origin main`

### **--squash**:

すべての変更を一つのコミットにまとめます。

例: `git pull --squash origin feature-branch`

## 使用例

```bash
# 現在のブランチに対応するリモートブランチから変更を取得
git pull

# 出力例
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/user/repo
   a1b2c3d..e4f5g6h  main     -> origin/main
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

```bash
# 特定のリモートとブランチを指定して変更を取得
git pull origin develop

# リベースを使用して変更を統合
git pull --rebase origin main
```

## よくある質問

### Q1. `git pull`と`git fetch`の違いは何ですか？
A. `git fetch`はリモートの変更を取得するだけですが、`git pull`は取得した変更をローカルブランチに統合（マージまたはリベース）します。

### Q2. `git pull`でコンフリクトが発生した場合はどうすればいいですか？
A. コンフリクトを手動で解決し、変更をステージングして`git commit`を実行します。リベース中のコンフリクトの場合は、解決後に`git rebase --continue`を実行します。

### Q3. 特定のブランチだけを取得するにはどうすればいいですか？
A. `git pull origin <ブランチ名>`のように、リモート名とブランチ名を指定します。

### Q4. `git pull`を安全に実行するには？
A. コミットしていない変更がある場合は先に`git stash`で保存するか、`--ff-only`オプションを使用して競合を避けます。

### Q5. リモートブランチを削除した後、ローカルでも反映させるには？
A. `git pull --prune`を実行すると、リモートで削除されたブランチの参照もローカルから削除されます。

### Q6. `git pull`を実行する前に確認すべきことはありますか？
A. 現在のブランチとコミットしていない変更を確認するために、`git status`を実行するとよいでしょう。

### Q7. `git pull`で特定のコミットだけを取得できますか？
A. いいえ、`git pull`はブランチ全体を取得します。特定のコミットだけ取得したい場合は、`git cherry-pick`を使用します。

### Q8. `git pull`後に元に戻すには？
A. `git reset --hard ORIG_HEAD`を実行すると、`git pull`実行前の状態に戻ります。

### Q9. `git pull`でリモートブランチを追跡するには？
A. `git pull -u origin <ブランチ名>`または`git branch --set-upstream-to=origin/<ブランチ名>`を使用します。

### Q10. `git pull`が「You have divergent branches」エラーを出す場合は？
A. ローカルとリモートの履歴が分岐しています。`git pull --rebase`を使用するか、マージ方法を明示的に選択してください。

## 追加のメモ

- コミットしていない変更がある状態で`git pull`を実行すると、マージコンフリクトが発生する可能性があります。
- チーム作業では、`git pull`を定期的に実行して最新の変更を取り込むことをお勧めします。
- `git pull --rebase`は履歴をクリーンに保ちたい場合に便利ですが、チームでの使用ルールを統一することが重要です。
- 大きな変更を行う前に`git pull`を実行すると、後でのコンフリクト解決が簡単になります。