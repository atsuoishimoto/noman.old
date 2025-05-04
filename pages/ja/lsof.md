# lsof コマンド

システム上で開いているファイルとそれを開いているプロセスを一覧表示します。

## 概要

`lsof`（List Open Files）は、システム上で実行中のプロセスによって現在開かれているファイルに関する情報を表示します。特定のファイルを開いているプロセスや、特定のプロセスが開いているファイル、その他のファイル使用状況の詳細を表示できます。このコマンドは、システム管理者や開発者がトラブルシューティングやシステムリソースの監視を行う際に特に役立ちます。

## オプション

### **-p PID**

指定したプロセスIDが開いているファイルを一覧表示します

```console
$ lsof -p 1234
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash     1234   user  cwd    DIR    8,1     4096 131073 /home/user
bash     1234   user  rtd    DIR    8,1     4096      2 /
bash     1234   user  txt    REG    8,1  1113504 917562 /bin/bash
```

### **-i [プロトコル][@ホスト名|ホストアドレス][:サービス|ポート]**

インターネット接続用に開かれたファイルを一覧表示します（プロトコル、ホスト、ポートの指定は任意）

```console
$ lsof -i TCP:22
COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd    1234    root    3u  IPv4  12345      0t0  TCP *:ssh (LISTEN)
sshd    5678    root    4u  IPv6  23456      0t0  TCP *:ssh (LISTEN)
```

### **-u ユーザー名**

特定のユーザーが開いているファイルを一覧表示します

```console
$ lsof -u john
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash     1234   john  cwd    DIR    8,1     4096 131073 /home/john
chrome   2345   john   10u   REG    8,1    12345 262144 /tmp/file.tmp
```

### **-c コマンド**

指定したコマンド名を持つプロセスが開いているファイルを一覧表示します

```console
$ lsof -c nginx
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
nginx   1234 root  cwd    DIR    8,1     4096      2 /
nginx   1234 root  txt    REG    8,1  1234567 917562 /usr/sbin/nginx
nginx   1235 www   cwd    DIR    8,1     4096      2 /
```

### **-t**

プロセスIDのみを表示します（スクリプト作成に便利）

```console
$ lsof -t -i TCP:80
1234
5678
```

## 使用例

### 特定のファイルを開いているプロセスを見つける

```console
$ lsof /var/log/syslog
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
rsyslogd 854 syslog    7w   REG    8,1   256789 131074 /var/log/syslog
```

### ネットワークポートをリッスンしているプロセスを確認する

```console
$ lsof -i -P -n | grep LISTEN
sshd      1234    root    3u  IPv4  12345      0t0  TCP *:22 (LISTEN)
nginx     2345    root    6u  IPv4  23456      0t0  TCP *:80 (LISTEN)
mysqld    3456   mysql   10u  IPv4  34567      0t0  TCP 127.0.0.1:3306 (LISTEN)
```

### 特定のユーザーがディレクトリ内で開いているすべてのファイルを見つける

```console
$ lsof -u john /home/john
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash    1234  john  cwd    DIR    8,1     4096 131073 /home/john
vim     2345  john    4u   REG    8,1    12345 262144 /home/john/document.txt
```

## ヒント:

### 複数のフィルターを組み合わせる

複数のオプションを組み合わせて結果を絞り込むことができます。例えば、`lsof -u ユーザー名 -i TCP`は特定のユーザーのTCP接続を表示します。

### 使用中の削除されたファイルを見つける

`lsof +L1`を使用して、プロセスによってまだ開かれている削除済みファイルを見つけることができます。これはディスク容量の解放を妨げているプロセスを特定するのに役立ちます。

### ネットワーク接続の監視

`lsof -i`を定期的に使用して、ネットワーク接続を監視し、セキュリティ問題を示す可能性がある予期しないネットワークアクティビティを特定します。

### grepと組み合わせて対象を絞った結果を得る

`lsof`の出力を`grep`にパイプして特定の情報をフィルタリングできます。例えば、`lsof | grep "/var/log"`でログファイルにアクセスしているプロセスを見つけることができます。

## よくある質問

#### Q1. 特定のポートを使用しているプロセスを見つけるにはどうすればよいですか？
A. `lsof -i:ポート番号`を使用します（例：HTTPポートの場合は`lsof -i:80`）。

#### Q2. すべてのネットワーク接続を確認するにはどうすればよいですか？
A. `lsof -i`を使用してすべてのネットワーク接続を表示します。`-P`を追加するとサービス名ではなくポート番号が表示されます。

#### Q3. 特定のファイルにアクセスしているプロセスを見つけるにはどうすればよいですか？
A. 単に`lsof /path/to/file`を実行すると、そのファイルを開いているすべてのプロセスが表示されます。

#### Q4. 特定のプロセスが開いているすべてのファイルを見つけるにはどうすればよいですか？
A. `lsof -p PID`を使用します。PIDは対象のプロセスIDです。

## References

https://man7.org/linux/man-pages/man8/lsof.8.html

## Revisions

- 2025/05/04 初回リビジョン