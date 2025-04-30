# git push コマンド

リモートリポジトリに変更を送信するコマンドです。

## 概要

`git push` は、ローカルリポジトリで行った変更（コミット）をリモートリポジトリに送信します。これにより、他の開発者とコードを共有したり、バックアップを作成したりすることができます。デフォルトでは、現在のブランチの変更を、設定されたリモートリポジトリの対応するブランチにプッシュします。

## オプション

### **-u, --set-upstream**

指定したリモートブランチを、現在のブランチの上流（デフォルトの送信先）として設定します。

```console
$ git push -u origin main
Branch 'main' set up to track remote branch 'main' from 'origin'.
Everything up-to-date
```

### **--force, -f**

リモートブランチを強制的に上書きします。通常の `push` が拒否される場合に使用しますが、他の人の変更を上書きする可能性があるため注意が必要です。

```console
$ git push --force origin feature
Counting objects: 5, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 456 bytes | 456.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
 + 7f9d407...2c5e7f0 feature -> feature (forced update)
```

### **--all**

すべてのローカルブランチをリモートにプッシュします。

```console
$ git push --all origin
Counting objects: 10, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 1.22 KiB | 1.22 MiB/s, done.
Total 10 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
 * [new branch]      feature -> feature
 * [new branch]      main -> main
```

### **--tags**

すべてのローカルタグをリモートにプッシュします。

```console
$ git push --tags origin
Counting objects: 1, done.
Writing objects: 100% (1/1), 160 bytes | 160.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To github.com:user/repo.git
 * [new tag]         v1.0 -> v1.0
```

### **--delete**

リモートブランチを削除します。

```console
$ git push origin --delete old-feature
To github.com:user/repo.git
 - [deleted]         old-feature
```

## 使用例

### 基本的な使い方

```console
$ git push
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 267 bytes | 267.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:user/repo.git
   a1b2c3d..e4f5g6h  main -> main
```

### 特定のブランチをプッシュ

```console
$ git push origin feature
Counting objects: 5, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 456 bytes | 456.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:user/repo.git
   7f9d407..2c5e7f0  feature -> feature
```

### 新しいブランチをリモートに作成

```console
$ git push -u origin new-feature
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 267 bytes | 267.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'new-feature' on GitHub by visiting:
remote:      https://github.com/user/repo/pull/new/new-feature
remote: 
To github.com:user/repo.git
 * [new branch]      new-feature -> new-feature
Branch 'new-feature' set up to track remote branch 'new-feature' from 'origin'.
```

## ヒント:

### 初回のプッシュには `-u` オプションを使う

新しいブランチを作成した後の初回プッシュでは、`-u` オプションを使うことで、以降の `git push` や `git pull` で明示的にリモートとブランチを指定する必要がなくなります。

### プッシュする前に最新の変更を取得する

`git pull` を実行してから `git push` することで、競合を避けることができます。

### `--force` は慎重に使う

`--force` オプションは他の開発者の変更を上書きする可能性があるため、共有リポジトリでは特に注意が必要です。代わりに `--force-with-lease` を使うと、他の人の変更がある場合はプッシュが拒否されるため安全です。

```console
$ git push --force-with-lease origin feature
```

### プッシュ拒否時の対処法

リモートに存在する変更と競合する場合、プッシュが拒否されることがあります。その場合は、まず `git pull` で変更を取り込み、必要に応じて競合を解決してから再度プッシュします。

## よくある質問

#### Q1. プッシュが拒否される理由は何ですか？
A. リモートリポジトリに、ローカルにない新しい変更がある場合に拒否されます。まず `git pull` を実行して最新の変更を取得してから再度プッシュしてみてください。

#### Q2. 特定のコミットだけをプッシュするには？
A. Gitでは特定のコミットだけをプッシュすることはできません。ブランチ単位でプッシュします。特定のコミットだけを共有したい場合は、新しいブランチを作成してそこにコミットを含めてプッシュするか、`git cherry-pick` を使用して別のブランチに特定のコミットを適用します。

#### Q3. プッシュした変更を取り消すには？
A. 完全に取り消すことはできませんが、`git revert` で元に戻すコミットを作成し、それをプッシュすることで実質的に変更を取り消すことができます。または、履歴を書き換えて `--force` オプションでプッシュする方法もありますが、共有リポジトリでは避けるべきです。

#### Q4. タグをプッシュするには？
A. `git push origin <タグ名>` で特定のタグを、`git push --tags` ですべてのタグをプッシュできます。

## 参考

https://git-scm.com/docs/git-push

## 改訂

- 2025/04/30 初版作成