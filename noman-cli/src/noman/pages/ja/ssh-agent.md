# ssh-agent コマンド

SSH秘密鍵を管理する認証エージェントで、接続時にパスフレーズの再入力が不要になります。

## 概要

`ssh-agent` はSSH公開鍵認証に使用される秘密鍵を保持するプログラムです。バックグラウンドで動作し、リモートサーバーにSSH接続するたびにパスフレーズを入力する必要がなくなります。エージェントに鍵を追加すると、パスフレーズを一度入力するだけで、エージェントは復号化された鍵をメモリに保持し、以降の接続で使用します。

## オプション

### **-a socket**

エージェントを特定のUnixドメインソケットにバインドします。

```console
$ ssh-agent -a /tmp/ssh-agent.socket
SSH_AUTH_SOCK=/tmp/ssh-agent.socket; export SSH_AUTH_SOCK;
SSH_AGENT_PID=1234; export SSH_AGENT_PID;
echo Agent pid 1234;
```

### **-c**

標準出力にC-shellコマンドを生成します。SHELLがcshスタイルのシェルのように見える場合、これがデフォルトになります。

```console
$ ssh-agent -c
setenv SSH_AUTH_SOCK /tmp/ssh-XXXXXXXXXX/agent.1234;
setenv SSH_AGENT_PID 1234;
echo Agent pid 1234;
```

### **-d**

デバッグモード。エージェントはフォークせず、デバッグ情報を標準エラーに書き込みます。

```console
$ ssh-agent -d
debug: ssh-agent: starting
debug: ssh-agent: listening on socket: /tmp/ssh-XXXXXXXXXX/agent.1234
```

### **-k**

現在のエージェント（SSH_AGENT_PID環境変数で指定）を終了します。

```console
$ ssh-agent -k
Agent pid 1234 killed
```

### **-s**

標準出力にBourne shellコマンドを生成します。SHELLがcshスタイルのシェルのように見えない場合、これがデフォルトになります。

```console
$ ssh-agent -s
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXXXXX/agent.1234; export SSH_AUTH_SOCK;
SSH_AGENT_PID=1234; export SSH_AGENT_PID;
echo Agent pid 1234;
```

### **-t life**

エージェントに追加されるIDのデフォルトの最大有効期間を設定します。有効期間は秒単位または sshd_config(5) で指定された時間形式で指定できます。

```console
$ ssh-agent -t 1h
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXXXXX/agent.1234; export SSH_AUTH_SOCK;
SSH_AGENT_PID=1234; export SSH_AGENT_PID;
echo Agent pid 1234;
```

## 使用例

### ssh-agentを起動して鍵を追加する

```console
$ eval $(ssh-agent)
Agent pid 1234
$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa
```

### 特定の有効期間でssh-agentを起動する

```console
$ eval $(ssh-agent -t 4h)
Agent pid 1235
$ ssh-add
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa
```

### エージェント内の鍵を一覧表示する

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD /home/user/.ssh/id_rsa (RSA)
```

### ssh-agentを終了する

```console
$ eval $(ssh-agent -k)
Agent pid 1234 killed
```

## ヒント:

### ssh-agentを自動的に起動する

シェルの起動ファイル（`.bashrc`や`.zshrc`など）に`eval $(ssh-agent)`を追加すると、ログイン時に自動的にエージェントが起動します。

### ssh-agentとSSH設定ファイルを組み合わせる

ssh-agentとSSH設定ファイル（~/.ssh/config）を組み合わせることで、異なるホストに対して異なる鍵を自動的に管理できます。

### SSHエージェント転送を使用する

他のサーバーにアクセスする必要があるリモートサーバーに接続する場合、`ssh -A user@host`を使用してローカルのエージェントをリモートサーバーに転送できます。信頼できないサーバーではセキュリティリスクがあるため、この機能の使用には注意が必要です。

### 実行中のエージェントを確認する

新しいエージェントを起動する前に、`echo $SSH_AGENT_PID`で既に実行中のエージェントがあるかどうかを確認し、複数のエージェントが実行されるのを避けましょう。

## よくある質問

#### Q1. ssh-agentとssh-addの違いは何ですか？
A. `ssh-agent`は復号化された鍵を保持するバックグラウンドプログラムであり、`ssh-add`は実行中のエージェントに鍵を追加するために使用されます。

#### Q2. 再起動後もssh-agentに鍵を記憶させるにはどうすればよいですか？
A. ssh-agentは再起動後も持続しません。再起動後にエージェントを再起動し、鍵を再度追加する必要があります。keychainなどのツールや起動スクリプトの使用を検討してください。

#### Q3. ssh-agentが実行中かどうかを確認するにはどうすればよいですか？
A. SSH_AGENT_PID環境変数が設定されているかどうかを確認します：`echo $SSH_AGENT_PID`。数値が返される場合、エージェントが実行中です。

#### Q4. ssh-agentから鍵を削除するにはどうすればよいですか？
A. 特定の鍵を削除するには`ssh-add -d ~/.ssh/keyfile`を使用し、すべての鍵を削除するには`ssh-add -D`を使用します。

## macOSに関する考慮事項

macOSでは、システムキーチェーン統合により鍵の自動ロードが可能です。組み込みのssh-agentはlaunchdによって管理され、自動的に起動します。macOSキーチェーンに鍵を追加するには、`ssh-add -K ~/.ssh/id_rsa`（古いバージョン）または`ssh-add --apple-use-keychain ~/.ssh/id_rsa`（新しいバージョン）を使用します。これにより、再起動後も鍵が保持されます。

## 参考資料

https://man.openbsd.org/ssh-agent

## 改訂履歴

- 2025/05/04 初回改訂