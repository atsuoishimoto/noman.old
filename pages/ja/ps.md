# ps コマンド

実行中のプロセスに関する情報を表示します。

## 概要

`ps` コマンドはシステム上で現在実行中のプロセスのスナップショットを表示します。プロセスID（PID）、CPU使用率、メモリ消費量、その他のプロセス関連情報の詳細を提供します。このコマンドは多数のオプションで高度にカスタマイズでき、必要に応じて出力をフィルタリングしたりフォーマットしたりすることができます。

## オプション

### **-e, --everyone**

すべてのプロセスに関する情報を表示します（-Aと同等）

```console
$ ps -e
  PID TTY          TIME CMD
    1 ?        00:00:03 systemd
    2 ?        00:00:00 kthreadd
   11 ?        00:00:00 rcu_sched
  950 ?        00:00:00 sshd
 1050 ?        00:00:01 bash
 1234 ?        00:00:00 ps
```

### **-f, --forest**

プロセス階層をツリー状のフォーマットで表示します

```console
$ ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 May01 ?        00:00:03 /sbin/init
root         2     0  0 May01 ?        00:00:00 [kthreadd]
user      1050   950  0 May01 pts/0    00:00:01 bash
user      1234  1050  0 10:15 pts/0    00:00:00 ps -ef
```

### **-u, --user**

特定のユーザーのプロセスを表示します

```console
$ ps -u username
  PID TTY          TIME CMD
 1050 pts/0    00:00:01 bash
 1234 pts/0    00:00:00 ps
 1500 pts/1    00:00:03 vim
```

### **-a, --all**

セッションリーダーと端末に関連付けられていないプロセスを除く、すべてのユーザーのプロセスを表示します

```console
$ ps -a
  PID TTY          TIME CMD
 1234 pts/0    00:00:00 ps
 1500 pts/1    00:00:03 vim
```

### **-x, --all**

制御端末のないプロセスも含めます

```console
$ ps -ax
  PID TTY      STAT   TIME COMMAND
    1 ?        Ss     0:03 /sbin/init
    2 ?        S      0:00 [kthreadd]
 1050 pts/0    Ss     0:01 bash
 1234 pts/0    R+     0:00 ps -ax
```

## 使用例

### 詳細情報付きでプロセスを表示する

```console
$ ps -ef | grep firefox
user      2345  1050  2 10:20 ?        00:00:45 /usr/lib/firefox/firefox
user      2346  2345  0 10:20 ?        00:00:02 /usr/lib/firefox/firefox-bin
```

### メモリ使用量でソートしたプロセスを表示する

```console
$ ps aux --sort=-%mem
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
user      2345  2.0  5.4 1254208 220800 ?      Sl   10:20   0:45 /usr/lib/firefox/firefox
mysql     1234  1.2  3.2  987654 130400 ?      Ssl  May01   2:34 /usr/sbin/mysqld
```

### 特定ユーザーのプロセスツリーを表示する

```console
$ ps -f --forest -u username
UID        PID  PPID  C STIME TTY          TIME CMD
user      1050   950  0 May01 pts/0    00:00:01 bash
user      2345  1050  2 10:20 ?        00:00:45  \_ firefox
user      2346  2345  0 10:20 ?        00:00:02      \_ firefox-bin
user      1500  1050  0 10:15 pts/0    00:00:03  \_ vim document.txt
```

## ヒント:

### 出力フォーマットのカスタマイズ

`-o` オプションを使用して、表示したい列を正確に指定できます：
```console
$ ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem
```

### リソースを大量に消費するプロセスを見つける

`ps` と `sort` を組み合わせて、最もリソースを消費しているプロセスを特定できます：
```console
$ ps aux | sort -nrk 3 | head -5  # CPU使用率の高い上位5つのプロセス
```

### grepでフィルタリングする

`ps` の出力を `grep` にパイプして特定のプロセスを見つけることができます：
```console
$ ps -ef | grep nginx
```
grep プロセス自体を除外するには：`ps -ef | grep [n]ginx` を使用するとよい

## よくある質問

#### Q1. 特定のプロセスのPIDを見つけるにはどうすればよいですか？
A. `ps -C プロセス名` または `ps -ef | grep プロセス名` を使用して特定のプロセスのPIDを見つけることができます。

#### Q2. 端末を持たないプロセスを含むすべてのプロセスを表示するにはどうすればよいですか？
A. `ps aux` または `ps -ef` を使用してシステム上のすべてのプロセスを表示できます。

#### Q3. プロセスをリアルタイムで監視するにはどうすればよいですか？
A. `ps` はスナップショットを提供しますが、プロセスのリアルタイム監視には `top` または `htop` を使用します。

#### Q4. ps aux と ps -ef の違いは何ですか？
A. どちらもすべてのプロセスを表示しますが、`ps aux` はBSD構文を使用し、%CPUと%MEM列を含み、`ps -ef` はUNIX構文を使用し、PPID（親プロセスID）を表示します。

## macOSに関する注意点

macOSでは、`ps` コマンドはLinuxとは若干異なるオプションを持っています。BSD形式のオプション（ダッシュなし）がより一般的に使用されます。例えば、`ps aux` はmacOSで動作しますが、`--forest` のようなGNU固有のオプションは利用できない場合があります。

## 参考資料

https://man7.org/linux/man-pages/man1/ps.1.html

## 改訂履歴

- 2025/05/04 初版作成