# ssh-copy-id コマンド

リモートホストに SSH 公開鍵を安全にコピーするためのユーティリティです。

## 概要

`ssh-copy-id` は、ローカルマシンの SSH 公開鍵をリモートホストの認証済み鍵ファイル（通常は `~/.ssh/authorized_keys`）に追加するコマンドです。これにより、パスワード入力なしでリモートホストに SSH 接続できるようになります。公開鍵認証の設定を簡単に行うことができます。

## オプション

### **-i [identity_file]**

使用する公開鍵ファイルを指定します。指定しない場合は、デフォルトの鍵（通常は `~/.ssh/id_rsa.pub`）が使用されます。

```console
$ ssh-copy-id -i ~/.ssh/custom_key.pub user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### **-f**

鍵がすでに存在する場合でも強制的に追加します。

```console
$ ssh-copy-id -f user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### **-p [port]**

リモートホストの SSH ポートを指定します（デフォルトは 22）。

```console
$ ssh-copy-id -p 2222 user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p 2222 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

## 使用例

### 基本的な使用方法

```console
$ ssh-copy-id user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### 特定の鍵を使用する場合

```console
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### 非標準ポートを使用する場合

```console
$ ssh-copy-id -p 2222 user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p 2222 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

## ヒント:

### 事前に SSH 鍵を生成する

`ssh-copy-id` を使用する前に、SSH 鍵ペアが必要です。鍵がない場合は、`ssh-keygen` コマンドで生成できます。

```console
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
```

### 複数のサーバーに鍵をコピーする

複数のサーバーに同じ鍵をコピーする場合は、コマンドを繰り返し実行するだけです。スクリプトを使用して自動化することも可能です。

### リモートホストのディレクトリ権限を確認する

接続に問題がある場合は、リモートホストの `~/.ssh` ディレクトリの権限が適切か確認してください。通常、`~/.ssh` は `700`、`~/.ssh/authorized_keys` は `600` の権限が必要です。

## よくある質問

#### Q1. `ssh-copy-id` とは何ですか？
A. SSH 公開鍵をリモートホストの認証済み鍵ファイルに追加するためのユーティリティです。これにより、パスワードなしでリモートホストに SSH 接続できるようになります。

#### Q2. 公開鍵がすでにリモートホストに存在する場合はどうなりますか？
A. `ssh-copy-id` は既存の鍵をスキップし、新しい鍵のみを追加します。強制的に追加するには `-f` オプションを使用します。

#### Q3. リモートホストに `.ssh` ディレクトリが存在しない場合はどうなりますか？
A. `ssh-copy-id` は必要なディレクトリと `authorized_keys` ファイルを自動的に作成し、適切な権限を設定します。

#### Q4. Windows で `ssh-copy-id` を使用できますか？
A. Windows 10 以降の OpenSSH クライアントには `ssh-copy-id` が含まれていない場合があります。代わりに、PowerShell スクリプトや Git Bash などの代替手段を使用できます。

## macOS での注意点

macOSでは、`ssh-copy-id` コマンドはデフォルトでインストールされていますが、古いバージョンの場合は Homebrew を使用してインストールできます：

```console
$ brew install ssh-copy-id
```

macOS の場合、SSH 鍵は通常 `/Users/ユーザー名/.ssh/` ディレクトリに保存されます。

## 参考資料

https://www.ssh.com/ssh/copy-id

## 改訂履歴

- 2025/04/30 初版作成