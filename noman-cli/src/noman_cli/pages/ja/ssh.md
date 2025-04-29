# SSH コマンド

SSH（Secure Shell）は、ネットワーク上の別のコンピュータに暗号化された安全な接続を確立するためのコマンドです。リモートサーバーへのログイン、コマンド実行、ファイル転送などに使用されます。

## オプション

### **-p（ポート指定）**
標準の22番以外のポートを使用する場合に指定します

```console
$ ssh -p 2222 username@hostname
# ポート2222を使用してリモートサーバーに接続
```

### **-i（秘密鍵ファイル指定）**
特定の秘密鍵ファイルを使用して認証します

```console
$ ssh -i ~/.ssh/my_key username@hostname
# 指定した秘密鍵ファイルを使用して認証
```

### **-X（X11転送）**
X11転送を有効にし、リモートのグラフィカルアプリケーションをローカルで表示できます

```console
$ ssh -X username@hostname
# X11転送を有効にして接続
$ firefox
# リモートサーバー上のFirefoxがローカル画面に表示される
```

### **-L（ローカルポートフォワーディング）**
ローカルポートをリモートサーバー経由で別のサーバーに転送します

```console
$ ssh -L 8080:internal-server:80 username@gateway-host
# ローカルの8080ポートへのアクセスがgateway-host経由でinternal-serverの80ポートに転送される
```

### **-v（詳細表示）**
接続プロセスの詳細情報を表示します（デバッグに役立ちます）

```console
$ ssh -v username@hostname
# 接続の詳細情報が表示される
```

## 使用例

### 基本的な接続

```console
$ ssh user@example.com
# 接続が確立され、リモートサーバーのシェルプロンプトが表示される
```

### リモートコマンド実行

```console
$ ssh user@example.com "ls -la /var/www"
# リモートサーバーの/var/wwwディレクトリの内容が表示される
```

### SSH設定ファイルを使用した接続

```console
$ cat ~/.ssh/config
Host myserver
  HostName example.com
  User username
  Port 2222
  IdentityFile ~/.ssh/custom_key

$ ssh myserver
# 設定ファイルの情報を使用して接続
```

## ヒント:

### SSH鍵認証の設定
パスワード認証よりも安全で便利な鍵認証を設定するには、`ssh-keygen`で鍵ペアを生成し、`ssh-copy-id user@hostname`で公開鍵をリモートサーバーに登録します。

### 接続が頻繁に切れる場合の対策
長時間接続を維持したい場合は、`~/.ssh/config`に以下を追加すると効果的です：
```
Host *
  ServerAliveInterval 60
```

### SCP/SFTPでのファイル転送
SSHプロトコルを使用したファイル転送には`scp`や`sftp`コマンドが利用できます。例：`scp file.txt user@hostname:/path/to/destination/`

## Frequently Asked Questions

#### Q1. SSHとは何ですか？
A. SSHは「Secure Shell」の略で、暗号化された安全な通信チャネルを通じてリモートサーバーに接続するためのプロトコルとコマンドです。

#### Q2. パスワードなしでログインするにはどうすればよいですか？
A. SSH鍵認証を設定します。`ssh-keygen`で鍵ペアを生成し、`ssh-copy-id`で公開鍵をサーバーに登録すると、パスワード入力なしでログインできます。

#### Q3. 「Host key verification failed」エラーが出た場合はどうすればよいですか？
A. サーバーの鍵が変更された可能性があります。安全が確認できれば、`ssh-keygen -R hostname`で古い鍵を削除し、再接続してください。

#### Q4. SSHトンネルとは何ですか？
A. SSHトンネルは暗号化された通信経路を作成し、通常アクセスできないサービスに安全に接続するための機能です。`-L`や`-R`オプションで設定できます。

## macOSでの注意点

macOSでは、SSHクライアントが標準でインストールされていますが、以下の点に注意してください：

- macOS Catalina以降では、秘密鍵のパーミッションが厳格にチェックされます。`chmod 600 ~/.ssh/id_rsa`のように設定してください。
- キーチェーンとの連携により、パスフレーズ付きの鍵でも一度入力すれば記憶されます。
- macOSのSSHは基本的にOpenSSHベースですが、バージョンが古い場合があります。最新機能が必要な場合はHomebrewでOpenSSHをインストールすることを検討してください。

## References

https://www.openssh.com/manual.html

## Revisions

- 2025/04/26 macOSでの注意点を追加。FAQセクションを拡充。