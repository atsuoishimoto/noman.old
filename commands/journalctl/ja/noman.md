# journalctl コマンドの概要

`journalctl` は systemd のジャーナルログを閲覧するためのコマンドです。システムやサービスのログを効率的に検索・フィルタリングできます。

## 主なオプション

- **基本的な使用法**: オプションなしで実行すると、すべてのログエントリを表示します
  - 例: `journalctl`

- **-f, --follow**: リアルタイムでログを追跡表示します（tail -f と同様）
  - 例: `journalctl -f`

- **-u, --unit=名前**: 特定のサービスユニットのログのみを表示します
  - 例: `journalctl -u ssh.service`

- **-b, --boot[=ID]**: 現在または特定の起動時のログを表示します
  - 例: `journalctl -b` (現在の起動)
  - 例: `journalctl -b -1` (前回の起動)

- **--since=日時, --until=日時**: 指定した時間範囲のログを表示します
  - 例: `journalctl --since="2023-04-01" --until="2023-04-02"`
  - 例: `journalctl --since="1 hour ago"`

- **-p, --priority=レベル**: 指定した優先度以上のログを表示します
  - 例: `journalctl -p err` (エラー以上の重要度)

- **-n, --lines=行数**: 表示する行数を制限します
  - 例: `journalctl -n 20`

- **-o, --output=フォーマット**: 出力形式を指定します
  - 例: `journalctl -o json`

## 使用例

```bash
# 基本的な使用法 - すべてのログを表示
journalctl
# 出力例
Apr 01 10:00:00 hostname systemd[1]: Starting System...
Apr 01 10:00:05 hostname sshd[1234]: Server listening on port 22.
...

# SSHサービスのログのみを表示
journalctl -u ssh.service
# 出力例
Apr 01 10:00:05 hostname sshd[1234]: Server listening on port 22.
Apr 01 10:30:15 hostname sshd[1456]: Accepted password for user from 192.168.1.10

# 今日のエラーログのみを表示
journalctl --since=today -p err
# 出力例
Apr 01 11:23:45 hostname app[2345]: Error: Could not connect to database

# リアルタイムでログを監視
journalctl -f
# 出力例（リアルタイムで更新される）
Apr 01 14:30:22 hostname systemd[1]: Started Service.
Apr 01 14:30:25 hostname app[3456]: Processing request...
...
```

## 追加のヒント

- `journalctl` は通常、ページャー（lessなど）を通して表示されるため、スペースキーで次のページ、`q`キーで終了できます。
- `grep` と組み合わせて特定のキーワードを検索することもできます：`journalctl | grep "キーワード"`
- ログが多い場合は `--disk-usage` オプションでジャーナルの使用容量を確認できます。
- `--vacuum-size=サイズ` オプションで古いログを削除し、ディスク容量を解放できます（例：`journalctl --vacuum-size=1G`）。
- `_SYSTEMD_UNIT`, `_HOSTNAME`, `_PID` などのフィールドを使って詳細なフィルタリングも可能です：`journalctl _PID=1234`