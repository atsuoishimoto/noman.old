# killall コマンドの概要

`killall` コマンドは、プロセス名を指定して、そのプロセスを終了させるためのコマンドです。同じ名前のプロセスが複数実行されている場合、すべて終了させることができます。

## 主なオプション

- **-s, --signal [シグナル]**: 送信するシグナルを指定します（デフォルトは SIGTERM）
  - 例: `killall -s KILL firefox`

- **-i, --interactive**: プロセスを終了する前に確認を求めます
  - 例: `killall -i firefox`

- **-u, --user [ユーザー名]**: 指定したユーザーのプロセスのみを終了します
  - 例: `killall -u username firefox`

- **-v, --verbose**: 処理の詳細を表示します
  - 例: `killall -v firefox`

- **-w, --wait**: プロセスが終了するまで待機します
  - 例: `killall -w firefox`

- **-I, --ignore-case**: プロセス名の大文字小文字を区別しません
  - 例: `killall -I firefox`

## 使用例

```bash
# 基本的な使い方（firefoxプロセスをすべて終了）
killall firefox
# 出力はありません（成功した場合）

# 強制終了する（SIGKILL信号を送信）
killall -9 firefox
# または
killall -s KILL firefox

# 対話モードで確認しながら終了
killall -i chrome
# 出力例:
# Kill chrome(1234) ? (y/N) y
# Kill chrome(5678) ? (y/N) n

# 特定ユーザーのプロセスのみを終了
killall -u username nginx
```

## 追加情報

- プロセスが見つからない場合、エラーメッセージが表示されます。
- `-9` オプションは `SIGKILL` シグナルを送信し、プロセスを強制終了します。通常は先に通常の終了（デフォルトの `SIGTERM`）を試すことをお勧めします。
- プロセス名は完全に一致する必要があります。部分一致では機能しません。
- `ps aux` コマンドと組み合わせて使うと、終了したいプロセスを特定するのに役立ちます。
- 管理者権限が必要なプロセスを終了するには `sudo` を使用します（例: `sudo killall apache2`）。