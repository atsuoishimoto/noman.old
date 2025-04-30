# ssh-agent コマンド

SSH認証鍵を安全に管理し、パスフレーズの再入力なしで認証を行うためのエージェントを起動します。

## 概要

ssh-agentは、SSH秘密鍵を安全にメモリ内に保持するプログラムです。一度パスフレーズを入力してキーを登録すると、その後のSSH接続ではパスフレーズの再入力が不要になります。これにより、複数のSSH接続を効率的に行うことができます。通常はシェルの起動時に実行され、環境変数を設定して子プロセスがエージェントと通信できるようにします。

## オプション

### **-c**

C-shellスタイルのコマンドを出力します。

```console
$ ssh-agent -c
setenv SSH_AUTH_SOCK /tmp/ssh-XXXXXXXX/agent.12345;
setenv SSH_AGENT_PID 12345;
echo Agent pid 12345;
```

### **-s**

Bourne shellスタイルのコマンドを出力します（デフォルト）。

```console
$ ssh-agent -s
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXXX/agent.12345; export SSH_AUTH_SOCK;
SSH_AGENT_PID=12345; export SSH_AGENT_PID;
echo Agent pid 12345;
```

### **-d**

デバッグモードで実行します。

```console
$ ssh-agent -d
debug: ssh-agent: starting
debug: ssh-agent: listening on socket: /tmp/ssh-XXXXXXXX/agent.12345
```

### **-k**

実行中のssh-agentを終了します。

```console
$ ssh-agent -k
unset SSH_AUTH_SOCK;
unset SSH_AGENT_PID;
echo Agent pid 12345 killed;
```

## 使用例

### ssh-agentの起動とシェル環境への統合

```console
$ eval $(ssh-agent)
Agent pid 12345
```

### 鍵の追加

```console
$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa
```

### 登録されている鍵の一覧表示

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD /home/user/.ssh/id_rsa (RSA)
```

### 特定の鍵だけを追加

```console
$ ssh-add ~/.ssh/github_rsa
Enter passphrase for /home/user/.ssh/github_rsa: 
Identity added: /home/user/.ssh/github_rsa
```

## ヒント:

### シェルの起動時に自動的に起動する

`.bashrc`や`.zshrc`などのシェル設定ファイルに以下を追加すると、ログイン時に自動的にssh-agentが起動します。

```bash
if [ -z "$SSH_AUTH_SOCK" ]; then
   eval $(ssh-agent -s)
fi
```

### 鍵の有効期限を設定する

`ssh-add -t`オプションを使用して、鍵の有効期限を設定できます。例えば、1時間だけ有効にする場合:

```bash
ssh-add -t 1h ~/.ssh/id_rsa
```

### ssh-agentの共有

tmuxやscreenなどのターミナルマルチプレクサを使用している場合、SSH_AUTH_SOCK環境変数を固定パスにシンボリックリンクすることで、複数のセッション間でssh-agentを共有できます。

## よくある質問

#### Q1. ssh-agentとは何ですか？
A. ssh-agentはSSH認証鍵を安全に保管し、パスフレーズの再入力なしで認証を行うためのプログラムです。

#### Q2. ssh-agentを終了するにはどうすればよいですか？
A. `ssh-agent -k`コマンドを実行するか、プロセスを直接終了（`kill $SSH_AGENT_PID`）することで終了できます。

#### Q3. ssh-agentに登録した鍵を削除するにはどうすればよいですか？
A. `ssh-add -d ~/.ssh/keyfile`で特定の鍵を削除するか、`ssh-add -D`ですべての鍵を削除できます。

#### Q4. ssh-agentが起動しているか確認するにはどうすればよいですか？
A. `echo $SSH_AGENT_PID`を実行して値が表示されるか、`ssh-add -l`を実行して登録されている鍵の一覧が表示されるか確認します。

## macOSでの注意点

macOSではKeychain機能と統合されており、システムのキーチェーンにSSH鍵のパスフレーズを保存することができます。`ssh-add -K`オプションを使用すると、鍵のパスフレーズをキーチェーンに保存できます（macOS 10.12以前）。macOS 10.13以降では、`~/.ssh/config`ファイルに`UseKeychain yes`を追加することで同様の機能を利用できます。

## 参考

https://man.openbsd.org/ssh-agent

## 改訂履歴

- 2025/04/30 初版作成