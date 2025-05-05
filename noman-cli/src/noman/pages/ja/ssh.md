# ssh コマンド

リモートマシンに暗号化されたネットワーク接続を介して安全に接続します。

## 概要

SSH（Secure Shell）はリモートコンピュータに安全にアクセスするためのプロトコルです。`ssh`コマンドはリモートサーバーへの暗号化された接続を確立し、安全なターミナルアクセス、ファイル転送、ポート転送を可能にします。これはリモートシステムを管理するための標準的な方法であり、telnetのような古い安全でないプロトコルに代わるものです。

## オプション

### **-p, --port ポート番号**

リモートホストに接続するポートを指定します（デフォルトは22）

```console
$ ssh -p 2222 user@example.com
user@example.com's password: 
Last login: Mon May 4 09:15:22 2025 from 192.168.1.5
user@example.com:~$ 
```

### **-i, --identity_file 鍵ファイル**

公開鍵認証に使用するアイデンティティ（秘密鍵）を読み込むファイルを選択します

```console
$ ssh -i ~/.ssh/my_private_key user@example.com
Last login: Mon May 4 10:30:15 2025 from 192.168.1.5
user@example.com:~$ 
```

### **-v, --verbose**

詳細モードを有効にし、接続情報の詳細を表示します（より詳細な情報は-vvや-vvvを使用）

```console
$ ssh -v user@example.com
OpenSSH_8.9p1, LibreSSL 3.3.6
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to example.com port 22.
debug1: Connection established.
...
```

### **-L ローカルポート:ホスト:ホストポート**

ローカルポートフォワーディングを設定し、ローカルポートをリモートホストとポートに接続します

```console
$ ssh -L 8080:localhost:80 user@example.com
user@example.com's password: 
Last login: Mon May 4 11:45:33 2025 from 192.168.1.5
```

### **-X, --enable X11 forwarding**

X11フォワーディングを有効にし、リモートでグラフィカルアプリケーションを実行できるようにします

```console
$ ssh -X user@example.com
user@example.com's password: 
Last login: Mon May 4 12:20:10 2025 from 192.168.1.5
user@example.com:~$ firefox &
[1] 12345
```

## 使用例

### 基本的な接続

```console
$ ssh username@hostname
username@hostname's password: 
Last login: Mon May 4 08:30:45 2025 from 192.168.1.5
username@hostname:~$ 
```

### リモートサーバーでコマンドを実行

```console
$ ssh user@example.com "ls -la /var/log"
total 1024
drwxr-xr-x 10 root root   4096 May  4 08:15 .
drwxr-xr-x 14 root root   4096 Apr 30 09:22 ..
-rw-r-----  1 root adm  125376 May  4 08:10 auth.log
-rw-r-----  1 root adm   15233 May  4 08:12 syslog
```

### SSHを使用した安全なファイルコピー

```console
$ scp -P 2222 localfile.txt user@example.com:/home/user/
user@example.com's password: 
localfile.txt                                 100%  156KB  2.5MB/s  00:00
```

### リモートWebサーバーにアクセスするためのポート転送

```console
$ ssh -L 8080:localhost:80 user@example.com
user@example.com's password: 
Last login: Mon May 4 14:30:22 2025 from 192.168.1.5
```

## ヒント:

### SSH設定ファイルを使用する

`~/.ssh/config`ファイルを作成して、異なるホストの接続設定を保存できます：

```
Host myserver
    HostName example.com
    User username
    Port 2222
    IdentityFile ~/.ssh/id_rsa_example
```

その後、単に`ssh myserver`と入力するだけで接続できます。

### パスワードなしログイン用のSSH鍵を設定する

`ssh-keygen`で鍵を生成し、`ssh-copy-id user@hostname`でリモートサーバーにコピーすることで、パスワード入力を省略できます。

### SSH接続を維持する

タイムアウトを防ぐために、`~/.ssh/config`に以下の行を追加します：

```
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

### マルチホップ接続のためのエージェント転送を使用する

`ssh -A user@server1`を使用して認証エージェントを転送すると、server1から他のサーバーに鍵をコピーせずに接続できます。

## よくある質問

#### Q1. SSH鍵を生成するにはどうすればよいですか？
A. `ssh-keygen -t rsa -b 4096`を使用して強力なRSA鍵ペアを生成します。公開鍵（.pub）はサーバーと共有され、秘密鍵は秘密に保たれます。

#### Q2. SSH接続を高速化するにはどうすればよいですか？
A. `ssh -o ControlMaster=auto -o ControlPath=~/.ssh/control-%h-%p-%r -o ControlPersist=yes user@host`を使用して接続共有を有効にするか、これらの設定をSSH設定ファイルに追加します。

#### Q3. SSH接続の問題をトラブルシューティングするにはどうすればよいですか？
A. `ssh -v user@host`（またはより詳細な情報を得るために`-vv`や`-vvv`）を使用して、問題を特定するのに役立つ詳細な接続情報を確認できます。

#### Q4. サーバー間でファイルを安全にコピーするにはどうすればよいですか？
A. 個々のファイルには`scp`を使用し、ディレクトリや再開機能を持つ効率的な転送には`rsync -e ssh`を使用します。

## macOSでの注意点

macOSでは、SSHエージェントの動作がLinuxとは若干異なります。SSH鍵が適切に読み込まれるようにするには：

1. `ssh-add -K ~/.ssh/your_key`を使用して鍵をmacOSキーチェーンに保存します
2. macOS Monterey（12）以降では、`~/.ssh/config`に以下を追加します：
   ```
   Host *
     UseKeychain yes
     AddKeysToAgent yes
   ```
3. SSH鍵を使用する際、macOSがキーチェーンへのアクセスを求めるプロンプトを表示することがあります

## 参考資料

https://man.openbsd.org/ssh.1

## 改訂履歴

- 2025/05/04 初回改訂