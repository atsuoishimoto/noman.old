# git push コマンド

リモートリポジトリに対してローカルの参照と関連オブジェクトを更新します。

## 概要

`git push`はローカルブランチのコミットを対応するリモートリポジトリに送信します。リモート参照（ブランチやタグなど）を更新し、リポジトリを同期させるために必要なオブジェクトを転送します。このコマンドは、あなたの作業を他の人と共有したり、ローカルの変更をリモートリポジトリにバックアップしたりする際に不可欠です。

## オプション

### **-u, --set-upstream**

現在のブランチに対してアップストリームを設定し、今後のプッシュで同じリモートブランチを指定せずに使用できるようにします。

```console
$ git push -u origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### **-f, --force**

非fast-forwardの更新になる場合でも、ローカルブランチでリモートブランチを強制的に更新します。リモート上の変更を上書きする可能性があるため、注意して使用してください。

```console
$ git push -f origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
 + a1b2c3d...e4f5g6h main -> main (forced update)
```

### **--tags**

すべてのローカルタグをリモートリポジトリにプッシュします。

```console
$ git push --tags
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 160 bytes | 160.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:username/repository.git
 * [new tag]         v1.0.0 -> v1.0.0
 * [new tag]         v1.1.0 -> v1.1.0
```

### **--delete**

指定したブランチをリモートリポジトリから削除します。

```console
$ git push origin --delete feature-branch
To github.com:username/repository.git
 - [deleted]         feature-branch
```

### **--dry-run**

実際にプッシュせずに、何が行われるかを表示します。

```console
$ git push --dry-run origin main
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  main -> main
```

## 使用例

### デフォルトのリモートブランチへのプッシュ

```console
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  main -> main
```

### 特定のブランチを特定のリモートにプッシュ

```console
$ git push origin feature-branch
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  feature-branch -> feature-branch
```

### ローカルブランチを異なる名前のリモートブランチにプッシュ

```console
$ git push origin local-branch:remote-branch
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  local-branch -> remote-branch
```

## ヒント:

### トラッキングブランチの設定

新しいブランチを作成する際は、`git push -u origin ブランチ名`を使用してトラッキングを設定しましょう。これにより、毎回リモートとブランチを指定せずに`git pull`や`git push`を使用できるようになります。

### すべてのブランチをプッシュ

`git push --all origin`を使用すると、すべてのローカルブランチをリモートリポジトリにプッシュできます。すべての作業をバックアップしたい場合に便利です。

### プッシュが拒否された場合の対処

リモートにあなたが持っていない作業が含まれているためにプッシュが拒否された場合は、`git pull`を使用してリモートの変更を統合してから再度プッシュしてください。あるいは、あなたの変更が優先されるべきと確信している場合は、`git push --force`を（注意して）使用してください。

### 特定のコミットのみをプッシュ

特定の時点までのコミットのみをプッシュするには、`git push origin <コミットハッシュ>:ブランチ名`を使用します。作業の一部だけを共有したい場合に便利です。

## よくある質問

#### Q1. `git push`と`git push origin main`の違いは何ですか？
A. `git push`は、設定されている場合、現在のブランチをそのアップストリームブランチにプッシュします。`git push origin main`は、現在どのブランチにいるかに関係なく、ローカルのmainブランチをoriginリモートのmainブランチに明示的にプッシュします。

#### Q2. 新しいローカルブランチをリモートリポジトリにプッシュするにはどうすればよいですか？
A. `git push -u origin ブランチ名`を使用して、新しいブランチをプッシュしトラッキングを設定します。

#### Q3. プッシュを取り消すにはどうすればよいですか？
A. プッシュを直接「取り消す」ことはできません。代わりに、ローカルで変更を元に戻し（`git revert`や`git reset`を使用）、その後`git push --force`で新しい状態をプッシュする必要があります。force pushは他の人の作業を上書きする可能性があるため注意してください。

#### Q4. なぜプッシュが拒否されるのですか？
A. プッシュが拒否される一般的な理由は、リモートブランチにあなたのローカルブランチにないコミットがある場合です。これは他の誰かが同じブランチに変更をプッシュした場合に発生します。`git pull`を使用して彼らの変更を統合してからプッシュしてください。

#### Q5. 複数のリモートに一度にプッシュするにはどうすればよいですか？
A. Gitには複数のリモートに同時にプッシュする組み込みの方法はありません。各リモートに個別にプッシュするか、複数のURLを指すリモートを設定する必要があります。

## 参考資料

https://git-scm.com/docs/git-push

## 改訂履歴

2025/05/04 初版作成