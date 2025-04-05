# git-branch コマンド概要

`git-branch`は、Gitリポジトリ内のブランチを作成、一覧表示、削除するためのコマンドです。ブランチは並行して開発を進めるための作業スペースとして機能します。

## オプション

### **-a, --all**:
すべてのブランチ（ローカルとリモート）を表示します。

例:
```bash
git branch -a
```

### **-r, --remotes**:
リモートブランチのみを表示します。

例:
```bash
git branch -r
```

### **-v, --verbose**:
各ブランチの最新のコミットとメッセージを表示します。

例:
```bash
git branch -v
```

### **-d, --delete**:
指定したブランチを削除します。

例:
```bash
git branch -d feature-branch
```

### **-D**:
強制的にブランチを削除します（マージされていなくても）。

例:
```bash
git branch -D feature-branch
```

### **-m, --move**:
ブランチの名前を変更します。

例:
```bash
git branch -m old-name new-name
```

### **--merged**:
現在のブランチにマージ済みのブランチを表示します。

例:
```bash
git branch --merged
```

### **--no-merged**:
現在のブランチにまだマージされていないブランチを表示します。

例:
```bash
git branch --no-merged
```

## 使用例

### 新しいブランチの作成
```bash
# 新しいブランチを作成
git branch feature-login
# 出力なし（成功時）
```

### ブランチの一覧表示
```bash
# 全ブランチを表示
git branch
# 出力例
* main
  feature-login
  bugfix-header
```
（`*`は現在のブランチを示しています）

### ブランチの削除
```bash
# マージ済みブランチの削除
git branch -d feature-login
# 出力例
Deleted branch feature-login (was a1b2c3d).
```

### ブランチ名の変更
```bash
# ブランチ名を変更
git branch -m old-feature new-feature
# 出力なし（成功時）
```

## よくある質問

### Q1. 新しいブランチを作成して、そのブランチに切り替えるには？
A. `git checkout -b ブランチ名`または`git switch -c ブランチ名`を使用します。これは`git branch ブランチ名`と`git checkout ブランチ名`を一度に実行する省略形です。

### Q2. リモートブランチをローカルに取得するには？
A. `git fetch`でリモートの情報を取得した後、`git checkout -b ローカルブランチ名 origin/リモートブランチ名`を実行します。

### Q3. 不要になったリモートブランチを削除するには？
A. `git push origin --delete リモートブランチ名`を使用します。

### Q4. 現在のブランチ名だけを確認するには？
A. `git branch --show-current`を使用します。

### Q5. ブランチの作成元（親ブランチ）を確認するには？
A. `git log --graph --oneline --all`で履歴を視覚的に確認できます。

### Q6. 特定のコミットから新しいブランチを作成するには？
A. `git branch ブランチ名 コミットハッシュ`を使用します。

### Q7. マージ済みのブランチをまとめて削除するには？
A. `git branch --merged | grep -v "\*" | xargs git branch -d`を使用します。

### Q8. ブランチの詳細な情報を確認するには？
A. `git branch -vv`を使用すると、リモートトラッキング情報も含めた詳細が表示されます。

### Q9. 特定のパターンに一致するブランチを検索するには？
A. `git branch --list "pattern*"`を使用します。

### Q10. 最後に作業していたブランチに戻るには？
A. `git checkout -`または`git switch -`を使用します。

## 追加情報

- ブランチ名は、機能や目的を表す分かりやすい名前にすることをお勧めします（例：`feature/login`、`bugfix/header`）。
- 長期間使用しないブランチは定期的に削除して、リポジトリを整理しましょう。
- `git branch`だけでは新しいブランチを作成するだけで、そのブランチに切り替えることはできません。切り替えるには`git checkout`または`git switch`コマンドを使用します。
- リモートブランチの変更を取得するには、まず`git fetch`を実行する必要があります。