# journalctl コマンド

システムログを表示・管理するためのコマンドです。

## 概要

`journalctl` は systemd のジャーナルログを閲覧するためのコマンドです。システムの起動メッセージ、サービスのログ、カーネルメッセージなど、システム全体のログを時系列で表示します。デフォルトでは、すべてのログエントリを表示しますが、様々なオプションを使用して特定のサービス、時間範囲、優先度などでフィルタリングすることができます。

## オプション

### **-f, --follow**

リアルタイムでログを追跡表示します（tail -f のような動作）

```console
$ journalctl -f
4月 30 10:15:23 hostname systemd[1]: Started User Manager for UID 1000.
4月 30 10:15:24 hostname sshd[1234]: Accepted publickey for user from 192.168.1.10 port 54321
4月 30 10:15:25 hostname sudo[1235]: user : TTY=pts/0 ; PWD=/home/user ; USER=root ; COMMAND=/bin/systemctl restart nginx
-- ログが追加されるたびに表示が更新される --
```

### **-u, --unit=**

特定のサービスユニットのログのみを表示します

```console
$ journalctl -u nginx.service
4月 29 08:30:12 hostname systemd[1]: Starting A high performance web server and a reverse proxy server...
4月 29 08:30:12 hostname systemd[1]: Started A high performance web server and a reverse proxy server.
4月 30 10:15:26 hostname systemd[1]: Restarting A high performance web server and a reverse proxy server...
4月 30 10:15:26 hostname systemd[1]: Started A high performance web server and a reverse proxy server.
```

### **-b, --boot**

現在の起動セッションのログのみを表示します

```console
$ journalctl -b
4月 30 08:00:01 hostname kernel: Linux version 5.15.0-25-generic (gcc version 11.2.0)
4月 30 08:00:02 hostname systemd[1]: Detected virtualization kvm.
4月 30 08:00:03 hostname systemd[1]: Detected architecture x86-64.
-- 現在の起動セッションのログが表示される --
```

### **--since=, --until=**

指定した時間範囲のログを表示します

```console
$ journalctl --since="2025-04-30 09:00:00" --until="2025-04-30 10:00:00"
4月 30 09:00:05 hostname systemd[1]: Started Daily apt download activities.
4月 30 09:15:01 hostname CRON[1234]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
4月 30 09:45:23 hostname sshd[1235]: Accepted publickey for user from 192.168.1.10 port 54321
-- 指定した時間範囲のログが表示される --
```

### **-p, --priority=**

指定した優先度以上のログを表示します（0=emerg, 1=alert, 2=crit, 3=err, 4=warning, 5=notice, 6=info, 7=debug）

```console
$ journalctl -p err
4月 29 15:45:12 hostname kernel: CPU: 0 PID: 1234 Comm: process Tainted: G        W  5.15.0-25-generic
4月 30 02:30:45 hostname nginx[5678]: [error] 5678#5678: *1 open() "/var/www/html/favicon.ico" failed (2: No such file or directory)
-- エラー以上の重要度のログのみ表示される --
```

## 使用例

### 特定のプロセスIDのログを表示

```console
$ journalctl _PID=1234
4月 30 10:15:24 hostname sshd[1234]: Accepted publickey for user from 192.168.1.10 port 54321
4月 30 10:20:15 hostname sshd[1234]: Received disconnect from 192.168.1.10 port 54321:11: disconnected by user
4月 30 10:20:15 hostname sshd[1234]: Disconnected from user 192.168.1.10 port 54321
```

### 最新の起動から特定のサービスのログを表示

```console
$ journalctl -b -u ssh.service
4月 30 08:00:45 hostname systemd[1]: Starting OpenBSD Secure Shell server...
4月 30 08:00:46 hostname sshd[1234]: Server listening on 0.0.0.0 port 22.
4月 30 08:00:46 hostname sshd[1234]: Server listening on :: port 22.
4月 30 08:00:46 hostname systemd[1]: Started OpenBSD Secure Shell server.
```

### ログの出力形式を変更（JSON形式）

```console
$ journalctl -b -u ssh.service -o json
{"_HOSTNAME":"hostname","_SYSTEMD_UNIT":"ssh.service","MESSAGE":"Starting OpenBSD Secure Shell server...","__REALTIME_TIMESTAMP":"1714521645000000"}
{"_HOSTNAME":"hostname","_SYSTEMD_UNIT":"ssh.service","MESSAGE":"Server listening on 0.0.0.0 port 22.","__REALTIME_TIMESTAMP":"1714521646000000"}
```

## ヒント:

### ディスク使用量の確認と管理

`journalctl --disk-usage` でジャーナルが使用しているディスク容量を確認できます。容量を節約するには `sudo journalctl --vacuum-size=500M` のようにして古いログを削除できます。

### カーネルメッセージの確認

`journalctl -k` または `journalctl --dmesg` でカーネルメッセージのみを表示できます。これはシステムの問題を診断する際に役立ちます。

### 出力のページャーを無効化

`journalctl --no-pager` を使用すると、lessなどのページャーを使わずに出力を直接表示します。これはログをファイルにリダイレクトする場合に便利です。

### 出力形式のカスタマイズ

`-o` オプションで出力形式を変更できます。例えば `journalctl -o json` でJSON形式、`-o short-precise` で精密なタイムスタンプ付きの短い形式で表示できます。

## よくある質問

#### Q1. journalctlとsyslogの違いは何ですか？
A. journalctlはsystemdのジャーナルシステムを使用し、バイナリ形式で構造化されたログを保存します。従来のsyslogはテキストファイルベースです。journalctlはより多くのメタデータを保持し、検索やフィルタリングが容易です。

#### Q2. ログはどこに保存されていますか？
A. ジャーナルログは通常 `/var/log/journal/` ディレクトリに保存されています。ただし、設定によっては `/run/log/journal/`（揮発性）に保存される場合もあります。

#### Q3. 古いログを削除するにはどうすればよいですか？
A. `sudo journalctl --vacuum-time=1month`（1ヶ月より古いログを削除）や `sudo journalctl --vacuum-size=1G`（ログサイズを1GBに制限）などのコマンドを使用できます。

#### Q4. 特定のユーザーのログだけを見るにはどうすればよいですか？
A. `journalctl _UID=1000` のように、ユーザーIDを指定してフィルタリングできます。

## 参考

https://www.freedesktop.org/software/systemd/man/journalctl.html

## 改訂

- 2025/04/30 初版作成