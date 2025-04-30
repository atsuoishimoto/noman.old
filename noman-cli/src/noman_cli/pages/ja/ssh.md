# ssh コマンド

リモートホストに安全に接続し、ログインするためのコマンド。

## 概要

`ssh`（Secure Shell）は、暗号化された安全な通信チャネルを通じてリモートマシンに接続するためのコマンドです。ユーザー認証、データ転送、リモートコマンド実行などを安全に行うことができます。システム管理者やデベロッパーがリモートサーバーを管理する際に広く使用されています。

## オプション

### **-p [ポート番号]**

デフォルト（22）以外のポート番号を指定します。

```console
$ ssh -p 2222 user@example.com
user@example.com's password: 
```

### **-i [秘密鍵ファイル]**

認証に使用する秘密鍵ファイルを指定します。

```console
$ ssh -i ~/.ssh/my_private_key user@example.com
Last login: Wed Apr 30 10:15:23 2025 from 192.168.1.5
```

### **-l [ユーザー名]**

接続先のユーザー名を指定します。

```console
$ ssh -l admin example.com
admin@example.com's password: 
```

### **-v**

詳細な接続情報を表示します（デバッグに役立ちます）。

```console
$ ssh -v user@example.com
OpenSSH_8.6p1, LibreSSL 3.3.5
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to example.com port 22.
...
```

## 使用例

### 基本的な接続

```console
$ ssh user@example.com
user@example.com's password: 
Last login: Wed Apr 30 09:30:45 2025 from 192.168.1.10
[user@example ~]$ 
```

### リモートコマンドの実行

```console
$ ssh user@example.com "ls -la /var/log"
total 156
drwxr-xr-x 10 root  root  4096 Apr 30 10:00 .
drwxr-xr-x 14 root  root  4096 Apr 29 15:30 ..
-rw-r--r--  1 root  root  8192 Apr 30 09:45 auth.log
...
```

### X11転送を有効にした接続

```console
$ ssh -X user@example.com
user@example.com's password: 
Last login: Wed Apr 30 11:20:33 2025 from 192.168.1.10
[user@example ~]$ firefox &
[1] 12345
```

## ヒント:

### SSH鍵の生成

```console
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
```

公開鍵認証を設定すると、パスワード入力なしでログインできるようになります。

### SSH設定ファイルの活用

`~/.ssh/config` ファイルを作成して接続設定を保存できます。

```
Host myserver
    HostName example.com
    User admin
    Port 2222
    IdentityFile ~/.ssh/special_key
```

これにより `ssh myserver` だけで接続できるようになります。

### 接続が切れないようにする

長時間の接続を維持するには、`~/.ssh/config` に以下を追加します：

```
Host *
    ServerAliveInterval 60
```

これにより60秒ごとに信号を送信し、接続が維持されます。

## よくある質問

#### Q1. SSHの接続が拒否される場合はどうすればよいですか？
A. 以下を確認してください：
   - ユーザー名とホスト名が正しいか
   - リモートサーバーでSSHサービスが実行されているか
   - ファイアウォールがSSH接続を許可しているか
   - `-v` オプションを使用してデバッグ情報を確認する

#### Q2. パスワードなしでログインするにはどうすればよいですか？
A. 公開鍵認証を設定します：
   1. `ssh-keygen` で鍵ペアを生成
   2. `ssh-copy-id user@example.com` で公開鍵をサーバーに転送
   3. これにより、パスワード入力なしでログインできるようになります

#### Q3. SSHトンネルとは何ですか？
A. SSHトンネルは、暗号化された接続を通じてポートを転送する機能です。例えば、`ssh -L 8080:localhost:80 user@example.com` は、ローカルの8080ポートへのアクセスをリモートサーバーの80ポートに転送します。

## macOSでの注意点

macOSでは、SSH鍵のパーミッションが重要です。秘密鍵ファイルのパーミッションが適切でないと接続が拒否されることがあります。以下のコマンドで修正できます：

```console
$ chmod 600 ~/.ssh/id_rsa
```

また、macOSのキーチェーンにSSHパスフレーズを保存するには、`~/.ssh/config` に以下を追加します：

```
Host *
    UseKeychain yes
    AddKeysToAgent yes
```

## 参考

https://www.openssh.com/manual.html

## 改訂履歴

- 2025/04/30 初版作成