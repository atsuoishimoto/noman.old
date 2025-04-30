# ps コマンド

実行中のプロセスに関する情報を表示します。

## 概要

`ps`コマンドは、システム上で現在実行中のプロセスのスナップショットを表示します。引数なしで実行すると、現在のターミナルに関連するプロセスのみを表示しますが、オプションを使用することで、システム全体のプロセスや詳細情報を確認できます。

## オプション

### **-e (すべてのプロセス)**

システム上のすべてのプロセスを表示します。

```console
$ ps -e
  PID TTY          TIME CMD
    1 ?        00:00:03 systemd
    2 ?        00:00:00 kthreadd
  943 ?        00:00:00 sshd
 1028 ?        00:00:02 nginx
```

### **-f (フル形式)**

プロセスの詳細情報（UID、PID、PPID、C、STIME、TTY、TIME、CMD）を表示します。

```console
$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user     12345 12344  0 10:30 pts/0    00:00:00 bash
user     12346 12345  0 10:31 pts/0    00:00:00 ps -f
```

### **-u ユーザー名 (特定ユーザーのプロセス)**

指定したユーザーが所有するプロセスのみを表示します。

```console
$ ps -u user1
  PID TTY          TIME CMD
12345 pts/0    00:00:00 bash
12346 pts/0    00:00:00 vim
12347 pts/0    00:00:00 python3
```

### **aux (BSD形式の詳細表示)**

すべてのプロセスの詳細情報をBSD形式で表示します。最も一般的に使用されるオプションの一つです。

```console
$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 168940  9128 ?        Ss   Apr29   0:03 /sbin/init
user1     1234  0.2  0.5 157812 42312 pts/0    Ss   10:15   0:02 firefox
user1     1235  1.5  0.8 254680 65432 pts/0    R+   10:20   0:05 chrome
```

## 使用例

### プロセスIDで検索

```console
$ ps -p 1234
  PID TTY          TIME CMD
 1234 pts/0    00:00:02 firefox
```

### プロセス名でフィルタリング

```console
$ ps aux | grep nginx
root      1028  0.0  0.1  66104  5256 ?        Ss   Apr29   0:02 nginx: master process
www-data  1029  0.0  0.0  66460  3928 ?        S    Apr29   0:00 nginx: worker process
```

### メモリ使用量でソート

```console
$ ps aux --sort=-%mem | head -5
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
user1     1235  1.5  0.8 254680 65432 pts/0    R+   10:20   0:05 chrome
user1     1236  0.8  0.7 234560 58976 pts/0    S    10:21   0:03 firefox
root      1237  0.5  0.6 198432 49152 ?        Ss   10:22   0:02 dockerd
user1     1238  0.3  0.5 176128 40960 pts/0    S+   10:23   0:01 code
```

## ヒント:

### プロセスツリーの表示

`ps -ef --forest`を使用すると、プロセスの親子関係がツリー形式で表示されます。これにより、どのプロセスがどのプロセスから派生したかが視覚的に理解しやすくなります。

### リアルタイム監視

`ps`はスナップショットを提供するだけなので、リアルタイムでプロセスを監視したい場合は`top`や`htop`コマンドを使用するとよいでしょう。

### CPU/メモリ使用率の高いプロセスを特定

`ps aux --sort=-%cpu`または`ps aux --sort=-%mem`を使用すると、CPU使用率やメモリ使用率の高いプロセスを特定できます。

## よくある質問

#### Q1. `ps`と`top`の違いは何ですか？
A. `ps`はプロセスの静的なスナップショットを提供するのに対し、`top`はリアルタイムで更新される動的な表示を提供します。

#### Q2. 特定のプロセスを名前で検索するにはどうすればよいですか？
A. `ps aux | grep プロセス名`を使用します。ただし、grepプロセス自体も結果に含まれることに注意してください。

#### Q3. プロセスのCPU使用率とメモリ使用率を確認するにはどうすればよいですか？
A. `ps aux`コマンドを使用すると、%CPUと%MEMの列にそれぞれの使用率が表示されます。

#### Q4. macOSでの`ps`コマンドは他のUNIXシステムと違いがありますか？
A. macOSの`ps`コマンドはBSD由来であり、LinuxのようなGNU/Linuxシステムとは若干オプションの動作が異なる場合があります。例えば、`ps aux`は両方で動作しますが、一部の詳細オプションは異なります。

## 参考文献

https://man7.org/linux/man-pages/man1/ps.1.html

## 改訂履歴

- 2025/04/30 初版作成