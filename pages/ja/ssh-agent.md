# ssh-agent の概要

ssh-agent は SSH 認証鍵を安全に保存し、管理するためのプログラムです。一度パスフレーズを入力すると、その後の SSH 接続では自動的に認証を行ってくれます。

## 主なオプション

- **-c**: C シェル用のコマンドを出力します
  - 例: `ssh-agent -c`

- **-s**: Bourne シェル用のコマンドを出力します（デフォルト）
  - 例: `ssh-agent -s`

- **-d**: デバッグモードで実行します
  - 例: `ssh-agent -d`

- **-k**: 現在実行中の ssh-agent を終了します
  - 例: `ssh-agent -k`

- **-t** *時間*: 鍵をキャッシュする時間（秒）を指定します
  - 例: `ssh-agent -t 3600`（1時間）

## 使用例

### ssh-agent の起動

```bash
# ssh-agent を起動
eval $(ssh-agent)
# 出力例
Agent pid 12345
```

### 鍵の追加

```bash
# 秘密鍵を ssh-agent に追加
ssh-add ~/.ssh/id_rsa
# 出力例（パスフレーズを求められる場合）
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa
```

### 登録されている鍵の確認

```bash
# 現在 ssh-agent に登録されている鍵を表示
ssh-add -l
# 出力例
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD /home/user/.ssh/id_rsa (RSA)
```

### ssh-agent の終了

```bash
# ssh-agent を終了
eval $(ssh-agent -k)
# 出力例
Agent pid 12345 killed
```

## シェルの起動時に自動的に設定する例

```bash
# .bashrc や .zshrc に以下を追加
if [ -z "$SSH_AUTH_SOCK" ]; then
   eval $(ssh-agent -s)
   ssh-add
fi
```

## 追加情報

- ssh-agent はバックグラウンドで動作し、環境変数 `SSH_AUTH_SOCK` と `SSH_AGENT_PID` を設定します。
- `eval $(ssh-agent)` の形式で実行すると、これらの環境変数が現在のシェルに設定されます。
- 一度 ssh-agent に鍵を追加すると、SSH 接続時に毎回パスフレーズを入力する必要がなくなります。
- セキュリティのため、共有マシンでは使用後に `ssh-agent -k` で終了することをお勧めします。
- macOS では、システムのキーチェーンと統合されているため、別途設定する必要がない場合があります。