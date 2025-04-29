# ssh-copy-id コマンド概要

`ssh-copy-id`は、リモートサーバーに自分の公開SSHキーをコピーするためのコマンドです。これにより、パスワード入力なしでSSH接続ができるようになります。

## 主なオプション

- **-i [identity_file]**: 使用する公開鍵ファイルを指定します
  - 例: `ssh-copy-id -i ~/.ssh/id_rsa.pub user@server`

- **-p [port]**: 標準の22番以外のSSHポートを使用する場合に指定します
  - 例: `ssh-copy-id -p 2222 user@server`

- **-f**: 既存の公開鍵が存在する場合でも強制的に追加します
  - 例: `ssh-copy-id -f user@server`

- **-n**: 実際にコピーせず、何が行われるかをシミュレーションします（ドライラン）
  - 例: `ssh-copy-id -n user@server`

## 使用例

### 基本的な使用方法

```bash
# デフォルトの公開鍵をリモートサーバーにコピーする
ssh-copy-id username@remote-server

# 出力例
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
username@remote-server's password: 

# 成功した場合の出力
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'username@remote-server'"
and check to make sure that only the key(s) you wanted were added.
```

### 特定の公開鍵ファイルを指定する場合

```bash
# 特定の公開鍵ファイルを使用する
ssh-copy-id -i ~/.ssh/custom_key.pub username@remote-server

# 出力例は基本的な使用方法と同様
```

### 異なるポートを使用する場合

```bash
# ポート2222を使用する
ssh-copy-id -p 2222 username@remote-server

# 出力例は基本的な使用方法と同様
```

## 追加情報

- 初めて接続するサーバーの場合、ホストキーの確認メッセージが表示されます。「yes」と入力して続行してください。
- リモートサーバーでは、コピーされた公開鍵は `~/.ssh/authorized_keys` ファイルに追加されます。
- このコマンドを実行するには、最初の接続時にはリモートサーバーのパスワードが必要です。
- 公開鍵がコピーされた後は、`ssh username@remote-server` でパスワードなしでログインできるようになります。
- 公開鍵がない場合は、先に `ssh-keygen` コマンドを実行して鍵ペアを生成する必要があります。