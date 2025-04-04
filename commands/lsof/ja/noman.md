# lsof コマンドの概要

`lsof`（List Open Files）は、システム上で開いているファイルとそれを使用しているプロセスを表示するコマンドです。ネットワーク接続、デバイス、ディレクトリなども「ファイル」として扱われます。

## 主なオプション

- **基本使用法**: オプションなしで実行すると、すべての開いているファイルを表示します
  - 例: `lsof`

- **-p [PID]**: 特定のプロセスID（PID）が開いているファイルを表示します
  - 例: `lsof -p 1234`

- **-u [ユーザー名]**: 特定のユーザーが開いているファイルを表示します
  - 例: `lsof -u username`

- **-i**: ネットワーク接続（TCP/UDP）を表示します
  - 例: `lsof -i`
  - 特定のポートを指定: `lsof -i :80`（80番ポートの接続を表示）

- **-c [プログラム名]**: 特定のプログラムが開いているファイルを表示します
  - 例: `lsof -c firefox`

- **+D [ディレクトリ]**: 指定したディレクトリ内のすべての開いているファイルを表示します
  - 例: `lsof +D /var/log`

## 使用例

```bash
# 基本的な使用法（すべての開いているファイルを表示）
lsof | head
# 出力例
COMMAND     PID   USER   FD   TYPE             DEVICE  SIZE/OFF     NODE NAME
systemd       1   root  cwd    DIR                8,1      4096        2 /
systemd       1   root  rtd    DIR                8,1      4096        2 /
systemd       1   root  txt    REG                8,1   1620224   131078 /lib/systemd/systemd
```

```bash
# 特定のポート（例：80番）を使用しているプロセスを表示
lsof -i :80
# 出力例
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1234     root    6u  IPv4  12345      0t0  TCP *:http (LISTEN)
```

```bash
# 特定のファイルを開いているプロセスを確認
lsof /var/log/syslog
# 出力例
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
rsyslogd 854 syslog   7w   REG    8,1    12345 131079 /var/log/syslog
```

## 追加情報

- `lsof` は管理者権限（root）で実行すると、より多くの情報が表示されます。一般ユーザーでは自分のプロセスに関する情報のみ表示されることがあります。
- `-t` オプションを使うと、PIDのみを出力できるため、他のコマンドと組み合わせて使いやすくなります（例：`kill $(lsof -t -i :8080)`）。
- 複数のオプションを組み合わせることで、より絞り込んだ検索が可能です（例：`lsof -u username -i :22`）。
- ファイルシステムのマウントポイントを調べるには `lsof +D /mnt` のように使用できます。