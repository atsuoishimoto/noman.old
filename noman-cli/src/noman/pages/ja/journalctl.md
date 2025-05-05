# journalctl コマンド

systemdジャーナルからメッセージを検索して表示します。

## 概要

`journalctl`は、systemdジャーナルログを表示・検索するためのコマンドラインユーティリティです。systemdジャーナルは、カーネル、システムサービス、アプリケーションなど様々なソースからログデータを収集・保存する集中型ログシステムです。システムの問題をトラブルシューティングするための強力なフィルタリング機能を提供しています。

## オプション

### **-f, --follow**

リアルタイムでジャーナルを追跡します（`tail -f`と同様）

```console
$ journalctl -f
May 04 14:32:15 hostname systemd[1]: Started Daily apt download activities.
May 04 14:32:16 hostname CRON[12345]: (root) CMD (command being executed)
May 04 14:32:20 hostname sshd[12346]: Accepted publickey for user from 192.168.1.10
```

### **-u, --unit=UNIT**

特定のsystemdユニット（サービス）のログを表示します

```console
$ journalctl -u ssh
May 03 09:15:22 hostname sshd[1234]: Server listening on 0.0.0.0 port 22.
May 03 09:15:22 hostname sshd[1234]: Server listening on :: port 22.
May 04 10:23:45 hostname sshd[5678]: Accepted password for user from 192.168.1.5
```

### **-b, --boot[=ID]**

現在の起動時または特定の起動時のログを表示します

```console
$ journalctl -b
[最新の起動以降のすべてのログを表示]

$ journalctl -b -1
[前回の起動時のログを表示]
```

### **-n, --lines=N**

最新のN行のログを表示します

```console
$ journalctl -n 5
May 04 14:45:10 hostname systemd[1]: Starting Daily apt upgrade and clean activities...
May 04 14:45:11 hostname systemd[1]: Started Daily apt upgrade and clean activities.
May 04 14:45:12 hostname CRON[12347]: (root) CMD (apt-get update)
May 04 14:45:15 hostname kernel: [12345.678901] USB disconnect, device number 5
May 04 14:45:20 hostname NetworkManager[789]: Connectivity established
```

### **--since=DATE, --until=DATE**

指定した日時より新しいまたは古いエントリを表示します

```console
$ journalctl --since="2025-05-03 10:00:00" --until="2025-05-03 11:00:00"
[2025年5月3日の午前10時から11時までのログを表示]
```

### **-p, --priority=PRIORITY**

メッセージの優先度でフィルタリングします（0-7または「err」などの名前）

```console
$ journalctl -p err
May 02 15:30:45 hostname kernel: [12345.678901] CPU: 2 PID: 1234 Comm: process Tainted: G        W  5.15.0-91-generic
May 03 08:12:33 hostname application[5678]: Error: Failed to connect to database
May 04 02:45:12 hostname systemd[1]: Failed to start Apache Web Server.
```

### **-o, --output=FORMAT**

出力形式を制御します（short、verbose、jsonなど）

```console
$ journalctl -o json -n 1
{"_BOOT_ID":"abcdef123456789","_MACHINE_ID":"fedcba987654321","MESSAGE":"System startup complete","PRIORITY":"6","SYSLOG_FACILITY":"3","SYSLOG_IDENTIFIER":"systemd","_UID":"0","_GID":"0","_COMM":"systemd","_PID":"1","_SOURCE_REALTIME_TIMESTAMP":"1714896000000000"}
```

## 使用例

### 特定の期間のログを表示する

```console
$ journalctl --since yesterday --until today
[昨日から今日の現在時刻までのすべてのログを表示]
```

### 実行ファイルでログをフィルタリングする

```console
$ journalctl _COMM=sshd
May 01 08:15:22 hostname sshd[1234]: Server listening on 0.0.0.0 port 22.
May 01 08:15:22 hostname sshd[1234]: Server listening on :: port 22.
May 02 14:23:45 hostname sshd[5678]: Accepted publickey for user from 192.168.1.10
```

### 複数のフィルターを組み合わせる

```console
$ journalctl -u nginx -p err --since today
May 04 03:15:22 hostname nginx[1234]: 2025/05/04 03:15:22 [error] 1234#0: *123 open() "/var/www/html/favicon.ico" failed (2: No such file or directory)
```

### カーネルメッセージを表示する

```console
$ journalctl -k
May 04 00:00:01 hostname kernel: Linux version 5.15.0-91-generic (buildd@ubuntu) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0)
May 04 00:00:01 hostname kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-91-generic root=UUID=abcdef-1234-5678 ro quiet splash
```

## ヒント:

### ページャーコントロールを使用する

大量のログを表示する際、journalctlはページャー（lessのような）を使用します。`/パターン`で検索、`n`で次の一致、`g`で先頭へ移動、`G`で末尾へ移動、`q`で終了できます。

### 永続的なジャーナルストレージ

デフォルトでは、ジャーナルログはメモリにのみ保存される場合があります。再起動後もログを保持するには、`/etc/systemd/journald.conf`に`Storage=persistent`が設定されていることと、`/var/log/journal/`ディレクトリが存在することを確認してください。

### ディスク容量の管理

ジャーナルログは大量のディスク容量を消費する可能性があります。`journalctl --disk-usage`で使用容量を確認し、`journalctl --vacuum-size=1G`でジャーナルサイズを1GBに制限できます。

### 分析用にログをエクスポートする

`journalctl -o export`を使用してログをエクスポートし、別のマシンに転送して`journalctl --file=exported.journal`でインポートすることができます。

## よくある質問

#### Q1. 現在の起動時のログだけを見るにはどうすればよいですか？
A. `journalctl -b`を使用すると、現在の起動時のログのみを表示できます。

#### Q2. 特定のサービスのログを見るにはどうすればよいですか？
A. `journalctl -u サービス名`を使用します。例えば、SSHサービスのログを見るには`journalctl -u ssh`を使用します。

#### Q3. 重要度レベルでログをフィルタリングするにはどうすればよいですか？
A. `journalctl -p 優先度`を使用します。優先度は数字（0-7）または名前（emerg、alert、crit、err、warning、notice、info、debug）で指定できます。

#### Q4. 古いジャーナルログをクリアするにはどうすればよいですか？
A. `journalctl --vacuum-time=2d`で2日より古いエントリを削除するか、`journalctl --vacuum-size=500M`で合計サイズを500MBに制限できます。

#### Q5. リアルタイムでログを追跡するにはどうすればよいですか？
A. `journalctl -f`を使用すると、`tail -f`と同様に、書き込まれるログをリアルタイムで追跡できます。

## 参考資料

https://www.freedesktop.org/software/systemd/man/journalctl.html

## 改訂履歴

- 2025/05/04 初版作成