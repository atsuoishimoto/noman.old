# lsof コマンド

システム上で開いているファイルを一覧表示します。

## 概要

`lsof`（List Open Files）は、プロセスによって開かれているファイル、ソケット、パイプなどのリソースを表示するコマンドです。システム管理やトラブルシューティングに非常に役立ち、どのプロセスがどのファイルやポートを使用しているかを確認できます。

## オプション

### **-p [PID]**

指定したプロセスID（PID）が開いているファイルのみを表示します。

```console
$ lsof -p 1234
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
chrome  1234 user    cwd    DIR    8,1     4096 123456 /home/user
chrome  1234 user    txt    REG    8,1  3284744 789012 /usr/bin/chrome
```

### **-i**

ネットワーク接続（TCP/UDPソケット）を表示します。特定のポートを指定することも可能です。

```console
$ lsof -i :80
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1000   root    6u  IPv4  12345      0t0  TCP *:http (LISTEN)
```

### **-u [ユーザー名]**

特定のユーザーが開いているファイルを表示します。

```console
$ lsof -u username
COMMAND   PID    USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash     2345 username  cwd    DIR    8,1     4096 234567 /home/username
vim      2346 username  cwd    DIR    8,1     4096 234567 /home/username
```

### **-c [コマンド名]**

特定のコマンド/プログラムが開いているファイルを表示します。

```console
$ lsof -c firefox
COMMAND   PID    USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
firefox  3456    user  cwd    DIR    8,1     4096 345678 /home/user
firefox  3456    user  txt    REG    8,1  5678901 456789 /usr/lib/firefox
```

## 使用例

### 特定のファイルを開いているプロセスを見つける

```console
$ lsof /var/log/syslog
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
rsyslogd 854   root    7w   REG    8,1   256789 567890 /var/log/syslog
```

### 特定のポートを使用しているプロセスを見つける

```console
$ lsof -i :3306
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mysqld  1234 mysql   10u  IPv4  12346      0t0  TCP *:mysql (LISTEN)
```

### 削除されたが、まだプロセスが開いているファイルを見つける

```console
$ lsof | grep deleted
chrome    3456 user  123r   REG    8,1    12345 678901 /tmp/file (deleted)
```

## ヒント:

### 複数のオプションを組み合わせる

`lsof -i -u username` のように複数のオプションを組み合わせることで、特定のユーザーのネットワーク接続のみを表示するなど、より絞り込んだ検索が可能です。

### 出力を整理する

`lsof` の出力は非常に多くなることがあります。`grep`、`sort`、`awk` などと組み合わせて必要な情報だけを抽出すると便利です。

### 定期的な監視

`watch lsof -i` のように `watch` コマンドと組み合わせることで、ネットワーク接続の変化をリアルタイムで監視できます。

## よくある質問

#### Q1. `lsof` の出力の各列は何を意味していますか？
A. 主な列は以下の通りです：
- COMMAND: プロセス名
- PID: プロセスID
- USER: ユーザー名
- FD: ファイル記述子（r=読み取り、w=書き込み、u=読み書き両方）
- TYPE: ファイルタイプ（REG=通常ファイル、DIR=ディレクトリ、IPv4/IPv6=ネットワークソケット）
- DEVICE: デバイス番号
- SIZE/OFF: ファイルサイズまたはオフセット
- NODE: iノード番号
- NAME: ファイル名やソケット情報

#### Q2. 特定のポート範囲を監視するにはどうすればよいですか？
A. `lsof -i :1-1024` のように範囲を指定できます。これは1〜1024番のポートを使用しているプロセスを表示します。

#### Q3. macOSで `lsof` を実行すると「permission denied」エラーが出る場合はどうすればよいですか？
A. 多くの場合、`sudo lsof` のように管理者権限で実行する必要があります。特にシステムプロセスが開いているファイルを表示する場合に必要です。

## macOSでの注意点

macOSでは、一部のシステムファイルやプロセスの情報を取得するために管理者権限が必要な場合があります。また、macOSのセキュリティ機能（System Integrity Protection）により、一部のシステムプロセスの情報が制限されることがあります。

また、macOSでは `-X` オプションを使用することで、デバイスファイルの詳細情報を表示できます。これはmacOS固有の機能です。

## 参考資料

https://www.freebsd.org/cgi/man.cgi?query=lsof

## 改訂履歴

- 2025/04/30 初版作成