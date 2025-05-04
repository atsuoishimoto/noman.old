# ssh-keygen コマンド

SSH認証用の鍵ペアを生成、管理、変換します。

## 概要

`ssh-keygen`はSSH認証のための公開鍵/秘密鍵ペアを作成します。これらの鍵を使用すると、リモートシステムへのパスワードなしの安全なログインが可能になります。このコマンドは既存の鍵の管理（パスフレーズの変更や鍵フォーマットの変換など）も行えます。

## オプション

### **-t type**

作成する鍵のタイプを指定します。一般的なタイプには rsa、ed25519、dsa、ecdsaがあります。

```console
$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
# 鍵ペアを保存するファイルを指定するよう求められている
```

### **-f filename**

作成または管理する鍵ファイルの名前を指定します。

```console
$ ssh-keygen -t rsa -f ~/.ssh/my_custom_key
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
# カスタム名の鍵ファイルを作成している
```

### **-b bits**

鍵のビット数を指定します。値が大きいほどセキュリティは強化されますが、処理が遅くなる場合があります。

```console
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
# 4096ビットのRSA鍵を生成している
```

### **-p**

既存の秘密鍵ファイルのパスフレーズを変更します。

```console
$ ssh-keygen -p -f ~/.ssh/id_rsa
Enter old passphrase: 
Enter new passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved with the new passphrase.
# 既存の鍵のパスフレーズを変更している
```

### **-C comment**

鍵にコメントを追加します。通常、鍵の目的や所有者を識別するために使用されます。

```console
$ ssh-keygen -t ed25519 -C "work laptop"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
# 「work laptop」というコメント付きの鍵を生成している
```

## 使用例

### デフォルトのRSA鍵ペアの作成

```console
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
# オプションなしでデフォルトのRSA鍵を生成している
```

### カスタム設定での鍵の生成

```console
$ ssh-keygen -t ed25519 -b 256 -f ~/.ssh/github_key -C "github access"
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/github_key
Your public key has been saved in /home/user/.ssh/github_key.pub
# GitHub用のカスタム設定の鍵を生成している
```

### 公開鍵のフィンガープリントの表示

```console
$ ssh-keygen -lf ~/.ssh/id_rsa.pub
3072 SHA256:abcdef1234567890abcdef1234567890 user@hostname (RSA)
# 公開鍵のフィンガープリントを表示している
```

## ヒント:

### 適切な鍵タイプの選択

Ed25519鍵は、小さな鍵サイズで強力なセキュリティを提供するため、ほとんどの最新システムで推奨されています。RSA鍵（最低2048ビット）は古いシステムとの互換性が高いです。

### 強力なパスフレーズの使用

秘密鍵にパスフレーズを追加すると、セキュリティの追加層が提供されます。誰かが秘密鍵ファイルを入手しても、使用するにはパスフレーズが必要です。

### 鍵のバックアップ

秘密鍵の安全なバックアップを保管してください。鍵を紛失すると、その鍵を認証に使用しているシステムへのアクセスが失われます。

### 鍵のパーミッションは重要

SSHはファイルのパーミッションに敏感です。秘密鍵のパーミッションは600（所有者のみが読み書き可能）に設定する必要があります。

```console
$ chmod 600 ~/.ssh/id_rsa
# 秘密鍵のパーミッションを適切に設定している
```

## よくある質問

#### Q1. 公開鍵をリモートサーバーにコピーするにはどうすればよいですか？
A. `ssh-copy-id username@remote-server`を使用して鍵をコピーしインストールします。または、手動で公開鍵をリモートサーバーの`~/.ssh/authorized_keys`ファイルに追加することもできます。

#### Q2. 鍵タイプの違いは何ですか？
A. RSAは互換性が広いですが、長い鍵が必要です。Ed25519はより新しく、より安全で、短い鍵を使用しますが、古いシステムでは動作しない場合があります。ECDSAとDSAは現在あまり一般的に使用されていません。

#### Q3. 鍵からパスフレーズを削除するにはどうすればよいですか？
A. `ssh-keygen -p -f ~/.ssh/id_rsa`を使用し、新しいパスフレーズを求められたときに空のパスフレーズを入力します。

#### Q4. SSH鍵はどのくらいの頻度で更新すべきですか？
A. ベストプラクティスとしては、年に1回、またはチームメンバーの退職や潜在的な侵害などのセキュリティ上の懸念がある場合に鍵を更新することをお勧めします。

## macOSに関する考慮事項

macOSでは、鍵は同じ場所（`~/.ssh/`）に保存されますが、SSHエージェントに鍵を追加する必要がある場合があります：

```console
$ ssh-add -K ~/.ssh/id_rsa
# macOS Catalina以前で鍵をキーチェーンに追加している
```

macOS Monterey（12）以降では、次のように使用します：

```console
$ ssh-add --apple-use-keychain ~/.ssh/id_rsa
# macOS Monterey以降で鍵をキーチェーンに追加している
```

## 参考資料

https://man.openbsd.org/ssh-keygen.1

## 改訂履歴

- 2025/05/04 初版作成