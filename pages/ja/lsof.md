# lsof コマンド概要

`lsof`（List Open Files）は、システム上で開いているファイル、ソケット、パイプなどを一覧表示するコマンドです。プロセスが使用しているリソースを特定するのに非常に役立ちます。

## オプション

### **-p [PID]**

特定のプロセスID（PID）が開いているファイルを表示します。

```bash
$ lsof -p 1234
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash    1234 user    cwd    DIR    8,1     4096 131073 /home/user
bash    1234 user    rtd    DIR    8,1     4096      2 /
bash    1234 user    txt    REG    8,1  1113504 917562 /usr/bin/bash
```

### **-i**

ネットワーク接続（TCP/UDP）を表示します。ポート番号やホスト名で絞り込むこともできます。

```bash
$ lsof -i
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
chrome  3456 user    32u  IPv4 789123      0t0  TCP localhost:49152->localhost:http (ESTABLISHED)
sshd    2345 root    3u   IPv4 456789      0t0  TCP *:ssh (LISTEN)
```

### **-u [ユーザー名]**

特定のユーザーが開いているファイルを表示します。

```bash
$ lsof -u user1
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash    1234 user1    cwd    DIR    8,1     4096 131073 /home/user1
chrome  3456 user1    32u  IPv4 789123      0t0  TCP localhost:49152->localhost:http
```

### **-c [コマンド名]**

特定のコマンド/プログラムが開いているファイルを表示します。

```bash
$ lsof -c chrome
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
chrome  3456 user    cwd    DIR    8,1     4096 131073 /home/user
chrome  3456 user    mem    REG    8,1  2345678 917562 /usr/lib/chrome/lib.so
chrome  3456 user    32u  IPv4 789123      0t0  TCP localhost:49152->localhost:http
```

## 使用例

### 特定のポートを使用しているプロセスを見つける

```bash
$ lsof -i :80
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   4567 www-data 6u  IPv4 123456      0t0  TCP *:http (LISTEN)
```
この例では、ポート80（HTTP）を使用しているプロセスがnginxであることがわかる。

### ファイルを開いているプロセスを見つける

```bash
$ lsof /var/log/syslog
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
rsyslogd 789   syslog    7w   REG    8,1   256789 131073 /var/log/syslog
```
この例では、/var/log/syslogファイルを開いているのはrsyslogdプロセスであることがわかる。

### 複数のオプションを組み合わせる

```console
$ lsof -u user1 -i TCP
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
chrome  3456 user1    32u  IPv4 789123      0t0  TCP localhost:49152->localhost:http (ESTABLISHED)
ssh     5678 user1    3r   IPv4 234567      0t0  TCP localhost:22->remote:54321 (ESTABLISHED)
```
この例では、user1ユーザーが使用しているTCP接続のみを表示している。

## よくある質問

### Q1. lsofコマンドは何に使用されますか？
A. システム上で開いているファイル、ソケット、パイプなどを一覧表示し、どのプロセスがどのリソースを使用しているかを確認するために使用されます。

### Q2. 特定のポートを使用しているプロセスを見つけるにはどうすればよいですか？
A. `lsof -i :ポート番号` を使用します。例えば、ポート80を使用しているプロセスを見つけるには `lsof -i :80` を実行します。

### Q3. 特定のファイルを開いているプロセスを見つけるにはどうすればよいですか？
A. `lsof ファイルパス` を使用します。例えば、`lsof /var/log/syslog` はsyslogファイルを開いているプロセスを表示します。

### Q4. lsofの出力が多すぎる場合、どうやって絞り込めますか？
A. grepと組み合わせるか、-p（プロセスID）、-u（ユーザー）、-c（コマンド名）などのオプションを使用して出力を絞り込むことができます。

## 追加のヒント

- `lsof`は管理者権限（root）で実行すると、より多くの情報を表示できます。一般ユーザーでは自分のプロセスに関する情報しか見られない場合があります。
- `lsof +D ディレクトリパス` を使用すると、指定したディレクトリ内のすべてのファイルを開いているプロセスを再帰的に表示できます。
- ネットワークトラブルシューティングでは、`lsof -i` が非常に役立ちます。どのプロセスがどのポートをリッスンしているか、または使用しているかを確認できます。
- `lsof -n -P` オプションを追加すると、ホスト名やポート名の解決を行わず、数値のみで表示するため処理が高速になります。