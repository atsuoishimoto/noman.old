# git-merge コマンド概要

`git-merge`は、異なるブランチの変更を現在のブランチに統合するGitコマンドです。複数の開発ラインを一つにまとめる際に使用されます。

## オプション

### **--no-ff**:

Fast-forwardマージを行わず、常にマージコミットを作成します。

例: `git merge --no-ff feature-branch`

### **--ff-only**:

Fast-forwardマージのみを許可し、マージコミットが必要な場合は失敗します。

例: `git merge --ff-only release-branch`

### **--squash**:

ブランチの全変更を一つのコミットにまとめてマージします。

例: `git merge --squash bugfix-branch`

### **-m, --message**:

マージコミットのメッセージを指定します。

例: `git merge -m "Merge feature X into main" feature-branch`

### **--abort**:

コンフリクト発生時にマージを中止し、マージ前の状態に戻します。

例: `git merge --abort`

### **--continue**:

コンフリクト解決後にマージを続行します。

例: `git merge --continue`

### **-s, --strategy**:

マージ戦略を指定します（recursive, resolve, octopus, ours, subtree）。

例: `git merge -s recursive feature-branch`

## 使用例

```bash
# 基本的なマージ（feature-branchをマージ）
git merge feature-branch
# 出力例
Updating a1b2c3d..e4f5g6h
Fast-forward
 file.txt | 10 ++++++++--
 1 file changed, 8 insertions(+), 2 deletions(-)

# マージコミットを強制的に作成
git merge --no-ff feature-branch
# 出力例
Merge made by the 'recursive' strategy.
 file.txt | 10 ++++++++--
 1 file changed, 8 insertions(+), 2 deletions(-)

# コンフリクトが発生した場合
git merge conflicting-branch
# 出力例
Auto-merging file.txt
CONFLICT (content): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.

# コンフリクト解決後
git add file.txt
git merge --continue
```

## よくある質問

### Q1. Fast-forwardマージとは何ですか？
A. 現在のブランチの先端がマージするブランチの直接の親である場合、ブランチポインタを前に進めるだけの単純なマージです。新しいコミットは作成されません。

### Q2. マージコンフリクトが発生したらどうすればいいですか？
A. コンフリクトが発生したファイルを編集してコンフリクトを解決し、`git add`でマークしてから`git merge --continue`または`git commit`を実行します。

### Q3. マージを取り消すにはどうすればいいですか？
A. マージ完了前なら`git merge --abort`、完了後なら`git reset --hard ORIG_HEAD`を使用します。

### Q4. squashマージとは何ですか？
A. ブランチの全変更を一つのコミットにまとめてマージする方法です。ブランチの履歴は保持されません。

### Q5. マージ後に不要になったブランチを削除するにはどうすればいいですか？
A. `git branch -d branch-name`コマンドでブランチを削除できます。

### Q6. 特定のファイルだけをマージすることはできますか？
A. Gitは部分的なマージを直接サポートしていませんが、`git checkout`を使って特定のファイルを取得することができます。

### Q7. マージ戦略の違いは何ですか？
A. 主に使われる`recursive`は複数の共通祖先を処理できますが、`ours`は相手の変更を無視し、`theirs`は自分の変更を無視します。

### Q8. マージ前に変更内容を確認するには？
A. `git diff branch-name`で現在のブランチとマージ予定のブランチの差分を確認できます。

### Q9. リモートブランチをマージするには？
A. まず`git fetch`でリモートブランチを取得し、その後`git merge origin/branch-name`を実行します。

### Q10. マージコミットのメッセージを後から変更できますか？
A. `git commit --amend`を使用してマージコミットのメッセージを変更できます。

## 追加メモ

- マージ前に`git fetch`と`git pull`を実行して最新の変更を取得することをお勧めします。
- 重要な変更をマージする前には、別のブランチで試すか、`git stash`を使って作業中の変更を保存しておくと安全です。
- 複雑なマージの場合は、視覚的なツール（GitKraken、SourceTree等）を使用すると理解しやすくなります。
- `git log --graph --oneline`を使うと、ブランチとマージの履歴を視覚的に確認できます。