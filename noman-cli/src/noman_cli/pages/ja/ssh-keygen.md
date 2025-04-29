# ssh-keygen コマンド概要

`ssh-keygen`は、SSHプロトコルで使用する公開鍵と秘密鍵のペアを生成するためのコマンドです。これにより、パスワード入力なしで安全にリモートサーバーに接続できるようになります。

## 主なオプション

- **-t**: 鍵の種類（タイプ）を指定します
  - 例: `ssh-keygen -t rsa`（RSA鍵を生成）
  - 例: `ssh-keygen -t ed25519`（より安全なEd25519鍵を生成）

- **-b**: 鍵のビット長（強度）を指定します
  - 例: `ssh-keygen -t rsa -b 4096`（4096ビットのRSA鍵を生成）

- **-f**: 鍵ファイルの保存先を指定します
  - 例: `ssh-keygen -t rsa -f ~/.ssh/my_key`（指定した場所に鍵を保存）

- **-C**: 鍵にコメントを追加します（通常はメールアドレスなど）
  - 例: `ssh-keygen -t rsa -C "user@example.com"`

- **-p**: 既存の秘密鍵のパスフレーズを変更します
  - 例: `ssh-keygen -p -f ~/.ssh/id_rsa`

## 使用例

### 基本的な鍵の生成
```bash
# デフォルト設定でRSA鍵を生成
ssh-keygen
# 出力例
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
```

### 安全なEd25519鍵の生成（推奨）
```bash
# より安全なEd25519鍵を生成
ssh-keygen -t ed25519 -C "user@example.com"
# 出力例
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_ed25519
Your public key has been saved in /home/user/.ssh/id_ed25519.pub
```

### 公開鍵の表示
```bash
# 生成した公開鍵の内容を表示
cat ~/.ssh/id_ed25519.pub
# 出力例
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJHkl7VrYG4FbLxhVzQm2k7LBQNWBttVS1xfVknvQZHt user@example.com
```

## 追加情報

- パスフレーズは任意ですが、セキュリティ向上のために設定することをお勧めします。
- 生成された公開鍵（`.pub`拡張子のファイル）は、接続先のサーバーの`~/.ssh/authorized_keys`ファイルに追加します。
- 秘密鍵（拡張子なしのファイル）は絶対に他人と共有しないでください。
- 最近のシステムでは、RSAよりもEd25519鍵の使用が推奨されています（より安全で小さいため）。
- 鍵の権限設定は重要です：秘密鍵は`chmod 600 ~/.ssh/id_ed25519`のように設定してください。