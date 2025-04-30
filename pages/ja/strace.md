# strace コマンド

プロセスのシステムコールとシグナルをトレースするためのユーティリティ。

## 概要

`strace` はプログラムが実行中に行うシステムコール（OSへの呼び出し）とシグナルを監視・記録するツールです。デバッグやパフォーマンス分析に非常に役立ち、プログラムがどのようにOSと対話しているかを可視化します。システム管理者や開発者がプログラムの動作を理解したり、問題を診断したりする際に頻繁に使用されます。

## オプション

### **-f**

子プロセスも追跡します。プログラムが `fork()` を呼び出した場合に便利です。

```console
$ strace -f ls
execve("/bin/ls", ["ls"], 0x7ffc4d0bb4a0 /* 21 vars */) = 0
brk(NULL)                               = 0x55a932d9c000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
...
```

### **-o ファイル名**

出力を指定したファイルに保存します。

```console
$ strace -o trace.log ls
$ cat trace.log
execve("/bin/ls", ["ls"], 0x7ffd8e5b0810 /* 21 vars */) = 0
brk(NULL)                               = 0x55c3e2a4c000
...
```

### **-p PID**

実行中のプロセスにアタッチします。

```console
$ strace -p 1234
strace: Process 1234 attached
read(3, "some data", 4096)              = 9
write(1, "output", 6)                   = 6
...
```

### **-e expr**

トレースするシステムコールを指定します。

```console
$ strace -e open,read ls
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360q\2\0\0\0\0\0"..., 832) = 832
...
```

### **-c**

各システムコールの統計情報を表示します。

```console
$ strace -c ls
file1.txt  file2.txt  file3.txt
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         9           read
  0.00    0.000000           0         1           write
...
------ ----------- ----------- --------- --------- ----------------
100.00    0.000123                   106        11 total
```

### **-t**

各システムコールの時刻を表示します。

```console
$ strace -t ls
14:23:01 execve("/bin/ls", ["ls"], 0x7ffc4d0bb4a0 /* 21 vars */) = 0
14:23:01 brk(NULL)                     = 0x55a932d9c000
...
```

## 使用例

### 基本的な使い方

```console
$ strace ls
execve("/bin/ls", ["ls"], 0x7ffc4d0bb4a0 /* 21 vars */) = 0
brk(NULL)                               = 0x55a932d9c000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
...
```

### ファイルアクセスのみをトレース

```console
$ strace -e trace=file ls
execve("/bin/ls", ["ls"], 0x7ffd8e5b0810 /* 21 vars */) = 0
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
...
```

### パフォーマンス分析

```console
$ strace -c -p 1234
strace: Process 1234 attached
^C
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 99.82    0.005517          18       302           poll
  0.18    0.000010           0        21           read
...
------ ----------- ----------- --------- --------- ----------------
100.00    0.005527                   323         0 total
```

## ヒント:

### システムコールの絞り込み

`-e trace=network` のように、特定のカテゴリのシステムコールだけをトレースすることで、出力を整理できます。一般的なカテゴリには `file`、`process`、`network`、`signal` などがあります。

### 出力の読みやすさを向上

`-s` オプションを使用して文字列の表示長を増やすことで、より詳細な情報を得られます。例: `strace -s 256 command`

### 時間情報の活用

`-r` オプションを使用すると、各システムコール間の相対時間が表示され、パフォーマンスのボトルネックを特定するのに役立ちます。

## よくある質問

#### Q1. strace を使うとプログラムの実行速度が遅くなりますか？
A. はい、strace はプログラムの実行を大幅に遅くする可能性があります。本番環境での使用は注意が必要です。

#### Q2. root 権限なしで他のユーザーのプロセスをトレースできますか？
A. 通常はできません。他のユーザーのプロセスをトレースするには root 権限が必要です。

#### Q3. strace と ltrace の違いは何ですか？
A. strace はシステムコール（OSへの呼び出し）をトレースするのに対し、ltrace はライブラリ関数の呼び出しをトレースします。

#### Q4. macOS で strace は使えますか？
A. macOS では strace は直接使用できません。代わりに `dtruss` や `dtrace` を使用します。ただし、SIP (System Integrity Protection) が有効な場合は制限があります。

## macOS での注意点

macOS では `strace` コマンドは利用できません。代わりに `dtruss` コマンドを使用できますが、System Integrity Protection (SIP) が有効な場合は制限があります。`dtruss` を使用するには、ターミナルで `sudo dtruss command` のように実行します。また、より高度なトレースには `dtrace` コマンドも利用できます。

## 参考文献

https://man7.org/linux/man-pages/man1/strace.1.html

## 改訂履歴

- 2025/04/30 初版作成