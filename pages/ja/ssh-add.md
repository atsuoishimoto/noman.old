# ssh-add コマンド概要

`ssh-add` は SSH 認証エージェント（ssh-agent）に秘密鍵を追加するコマンドです。これにより、パスフレーズを毎回入力することなく、SSH 接続を行うことができます。

## 主なオプション

- **引数なし**: デフォルトの SSH 秘密鍵（`~/.ssh/id_rsa`、`~/.ssh/id_dsa`、`~/.ssh/id_ecdsa`、`~/.ssh/id_ed25519` など）をエージェントに追加します。
  - 例: `ssh-add`

- **-l**: 現在エージェントに登録されている鍵の一覧を表示します。
  - 例: `ssh-add -l`

- **-d [鍵ファイル]**: 指定した鍵をエージェントから削除します。
  - 例: `ssh-add -d ~/.ssh/id_rsa`

- **-D**: エージェントに登録されているすべての鍵を削除します。
  - 例: `ssh-add -D`

- **-t [秒数]**: 指定した時間（秒）だけ鍵をエージェントに追加します。時間が経過すると自動的に削除されます。
  - 例: `ssh-add -t 3600` （1時間後に削除）

## 使用例

```bash
# デフォルトの SSH 鍵をエージェントに追加
ssh-add
# 出力例
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa (/home/user/.ssh/id_rsa)

# 特定の鍵ファイルを追加
ssh-add ~/.ssh/my_custom_key
# 出力例
Enter passphrase for /home/user/.ssh/my_custom_key: 
Identity added: /home/user/.ssh/my_custom_key (/home/user/.ssh/my_custom_key)

# 登録されている鍵の一覧を表示
ssh-add -l
# 出力例
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD /home/user/.ssh/id_rsa (RSA)
4096 SHA256:1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcd /home/user/.ssh/my_custom_key (RSA)

# すべての鍵を削除
ssh-add -D
# 出力例
All identities removed.
```

## 追加情報

- `ssh-add` を使用する前に、`ssh-agent` が実行されている必要があります。通常は、ログイン時に自動的に起動されますが、起動していない場合は `eval $(ssh-agent)` で起動できます。

- 一時的な SSH 接続のために鍵を追加する場合は、`-t` オプションを使用して有効期限を設定することでセキュリティを向上させることができます。

- macOS では、`-K` オプションを使用して、鍵をキーチェーンに保存することができます（macOS 特有の機能）。

- 秘密鍵にパスフレーズが設定されていない場合は、パスフレーズの入力を求められません。ただし、セキュリティ上の理由から、重要な鍵にはパスフレーズを設定することをお勧めします。