# ssh-add コマンド

SSH認証エージェントに秘密鍵を追加し、接続認証に使用します。

## 概要

`ssh-add`はSSH認証に使用される秘密鍵を管理します。SSHエージェント（ssh-agent）に鍵を追加することで、復号化された秘密鍵をメモリに安全に保存し、リモートサーバーに接続するたびにパスフレーズを再入力する必要がなくなります。

## オプション

### **-l** / **--list**

エージェントに現在登録されているすべての鍵の指紋を一覧表示します。

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD user@hostname (RSA)
```

### **-D** / **--delete-all**

エージェントからすべての鍵を削除します。

```console
$ ssh-add -D
All identities removed.
```

### **-d** / **--delete**

指定した鍵をエージェントから削除します。

```console
$ ssh-add -d ~/.ssh/id_rsa
Identity removed: /home/user/.ssh/id_rsa (user@hostname)
```

### **-t** / **--lifetime seconds**

エージェントに鍵を追加する際に最大有効期間を設定します。この時間が経過すると、鍵は自動的に削除されます。

```console
$ ssh-add -t 3600 ~/.ssh/id_rsa
Identity added: /home/user/.ssh/id_rsa (user@hostname)
Lifetime set to 3600 seconds
```

### **-k** / **--lock-agent**

パスワードでエージェントをロックします。

```console
$ ssh-add -k
Enter lock password: 
Again: 
Agent locked.
```

### **-x** / **--lock**

パスワードでエージェントをロックします（-kの代替）。

```console
$ ssh-add -x
Enter lock password: 
Again: 
Agent locked.
```

### **-X** / **--unlock**

エージェントのロックを解除します。

```console
$ ssh-add -X
Enter unlock password: 
Agent unlocked.
```

## 使用例

### ファイルを指定せずに鍵を追加する

```console
$ ssh-add
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa (user@hostname)
```

### 特定の鍵ファイルを追加する

```console
$ ssh-add ~/.ssh/github_key
Enter passphrase for /home/user/.ssh/github_key: 
Identity added: /home/user/.ssh/github_key (user@github)
```

### エージェントに鍵が登録されているか確認する

```console
$ ssh-add -l
The agent has no identities.
```

## ヒント:

### ssh-addを使用する前にssh-agentを起動する

SSH鍵を追加する前にSSHエージェントが実行されている必要があります。ほとんどのシステムでは、次のコマンドで起動できます：

```console
$ eval $(ssh-agent)
Agent pid 12345
```

### ログイン時に自動的に鍵を追加する

シェルの起動ファイル（`.bashrc`や`.zshrc`など）に以下を追加すると、ログイン時に自動的に鍵が追加されます：

```bash
if [ -z "$SSH_AUTH_SOCK" ]; then
   eval $(ssh-agent -s)
   ssh-add
fi
```

### SSH設定ファイルで鍵管理を行う

手動で鍵を追加する代わりに、`~/.ssh/config`で特定のホストに使用する鍵を指定できます：

```
Host github.com
  IdentityFile ~/.ssh/github_key
```

## よくある質問

#### Q1. なぜssh-addを使用する必要があるのですか？
A. `ssh-add`を使うと、秘密鍵を一度復号化してメモリに保存できるため、サーバーに接続するたびにパスフレーズを入力する必要がなくなります。

#### Q2. 鍵がすでに追加されているかどうかを確認するにはどうすればよいですか？
A. `ssh-add -l`を実行すると、現在エージェントに読み込まれているすべての鍵が表示されます。

#### Q3. ssh-addコマンドで「Could not open a connection to your authentication agent」というエラーが表示されます
A. これはSSHエージェントが実行されていないことを意味します。まず`eval $(ssh-agent)`でエージェントを起動してください。

#### Q4. 再起動後もssh-addで鍵を記憶させるにはどうすればよいですか？
A. SSHエージェントは再起動後も維持されません。`keychain`などのツールを使用するか、ログインスクリプトに鍵追加コマンドを追加してください。

## macOSに関する注意点

macOSでは、SSHエージェントがKeychainと統合されているため、`ssh-add -K`（大文字のK）で追加された鍵はKeychainに保存され、ログイン時に自動的に読み込まれます。新しいmacOSバージョン（Monterey以降）では、`-K`の代わりに`--apple-use-keychain`を使用してください。

## 参考資料

https://man.openbsd.org/ssh-add.1

## 改訂履歴

- 2025/05/04 初版作成