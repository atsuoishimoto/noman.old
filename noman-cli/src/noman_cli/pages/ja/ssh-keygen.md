# ssh-keygen コマンド

SSH認証に使用する公開鍵と秘密鍵のペアを生成するツール。

## 概要

`ssh-keygen`は、SSHプロトコルで使用する認証鍵を生成、管理、変換するためのコマンドです。パスワードなしでリモートサーバーに安全に接続するための鍵ペア（公開鍵と秘密鍵）を作成できます。デフォルトでは、鍵は`~/.ssh/`ディレクトリに保存されます。

## オプション

### **-t type**

鍵の種類を指定します。一般的な種類は`rsa`、`ed25519`、`dsa`、`ecdsa`です。現在は`ed25519`または`rsa`が推奨されています。

```console
$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_ed25519
Your public key has been saved in /home/user/.ssh/id_ed25519.pub
```

### **-b bits**

鍵のビット数（強度）を指定します。RSA鍵の場合、最低2048ビットが推奨されています。

```console
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
```

### **-f filename**

鍵ファイルの保存先を指定します。

```console
$ ssh-keygen -t ed25519 -f ~/.ssh/github_key
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/github_key
Your public key has been saved in /home/user/.ssh/github_key.pub
```

### **-C comment**

鍵に関連付けるコメントを指定します。通常はメールアドレスや用途を記述します。

```console
$ ssh-keygen -t ed25519 -C "user@example.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_ed25519
Your public key has been saved in /home/user/.ssh/id_ed25519.pub
```

## 使用例

### 基本的な鍵の生成

```console
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCDEFG user@hostname
```

### 公開鍵のフィンガープリントを表示

```console
$ ssh-keygen -lf ~/.ssh/id_ed25519.pub
256 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCDEFG user@example.com (ED25519)
```

### 既存の鍵のパスフレーズを変更

```console
$ ssh-keygen -p -f ~/.ssh/id_ed25519
Enter old passphrase: 
Enter new passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved with the new passphrase.
```

## ヒント:

### パスフレーズの使用

セキュリティを高めるために、鍵にパスフレーズを設定することをお勧めします。これにより、秘密鍵が漏洩した場合でも、パスフレーズなしでは使用できません。

### ssh-agent の活用

パスフレーズを設定した場合、`ssh-agent`を使用すると、一度パスフレーズを入力するだけで、その後はパスフレーズの再入力なしで鍵を使用できます。

```console
$ eval "$(ssh-agent -s)"
Agent pid 12345
$ ssh-add ~/.ssh/id_ed25519
Enter passphrase for /home/user/.ssh/id_ed25519: 
Identity added: /home/user/.ssh/id_ed25519
```

### 公開鍵の配布

生成した公開鍵（`.pub`ファイル）をリモートサーバーの`~/.ssh/authorized_keys`ファイルに追加することで、パスワードなしでログインできるようになります。

```console
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote-server
```

## よくある質問

#### Q1. ssh-keygenで生成された鍵はどこに保存されますか？
A. デフォルトでは、`~/.ssh/`ディレクトリに保存されます。秘密鍵は`id_rsa`や`id_ed25519`などのファイル名で、公開鍵はそれに`.pub`を付けた名前（例：`id_rsa.pub`）で保存されます。

#### Q2. どの鍵の種類を選ぶべきですか？
A. 現在は`ed25519`が推奨されています。これは比較的新しいアルゴリズムで、セキュリティが高く、鍵のサイズも小さいです。互換性が必要な場合は、`rsa`（4096ビット以上）を使用してください。

#### Q3. パスフレーズを忘れた場合はどうすればよいですか？
A. パスフレーズを忘れた場合、その鍵を回復する方法はありません。新しい鍵ペアを生成し、古い公開鍵をサーバーから削除して、新しい公開鍵を追加する必要があります。

#### Q4. 公開鍵をサーバーに追加するにはどうすればよいですか？
A. `ssh-copy-id -i ~/.ssh/keyfile.pub user@server`コマンドを使用するか、公開鍵の内容をサーバーの`~/.ssh/authorized_keys`ファイルに手動で追加します。

## macOSでの注意点

macOSでは、鍵を生成した後、キーチェーンに秘密鍵を追加することができます。これにより、システムが自動的にパスフレーズを管理できるようになります。また、macOS Catalina以降では、デフォルトでOpenSSHが使用されるようになりました。

## 参考資料

https://www.openssh.com/manual.html

## 改訂履歴

- 2025/04/30 初版作成