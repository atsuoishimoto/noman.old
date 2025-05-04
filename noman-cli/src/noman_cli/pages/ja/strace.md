# strace コマンド

プロセスが行うシステムコールとシグナルをトレースします。

## 概要

`strace`はLinux向けの診断・デバッグツールで、指定したプログラムのシステムコールとシグナルを監視します。プロセスが行うシステムコールとプロセスが受け取るシグナルを傍受して記録します。このツールは問題のトラブルシューティング、プログラムがオペレーティングシステムとどのように相互作用するかの理解、パフォーマンス問題の分析に非常に役立ちます。

## オプション

### **-f, --follow-forks**

現在トレースされているプロセスによって作成される子プロセスもトレースします。

```console
$ strace -f ./my_program
[pid 12345] execve("./my_program", ["./my_program"], 0x7ffc123456) = 0
[pid 12345] brk(NULL)                  = 0x55555555
[pid 12345] clone(...)                 = 12346
[pid 12346] open("file.txt", O_RDONLY) = 3
```

### **-o, --output=FILE**

トレース出力を標準エラー出力ではなく指定したファイルに書き込みます。

```console
$ strace -o trace.log ls
$ cat trace.log
execve("/bin/ls", ["ls"], 0x7ffc123456) = 0
brk(NULL)                               = 0x55555555
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
```

### **-p, --attach=PID**

指定したPIDのプロセスにアタッチしてトレースを開始します。

```console
$ strace -p 1234
Process 1234 attached
read(3, "Hello World", 1024)            = 11
write(1, "Hello World", 11)             = 11
```

### **-e, --expr=EXPR**

トレースするイベントやトレース方法を指定する修飾子です。

```console
$ strace -e open,close ls
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
close(3)                                = 0
open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
close(3)                                = 0
```

### **-c, --summary-only**

各システムコールの時間、呼び出し回数、エラー数をカウントして要約を報告します。

```console
$ strace -c ls
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 25.91    0.000091          5        18           mmap
 17.66    0.000062          6        10           openat
 11.08    0.000039          3        12           close
  9.12    0.000032          5         6           read
  8.83    0.000031          5         6           fstat
  ...
------ ----------- ----------- --------- --------- ----------------
100.00    0.000351                   98         5 total
```

### **-t, --relative-timestamps**

各出力行の先頭に時刻を付加します。

```console
$ strace -t ls
14:15:32 execve("/bin/ls", ["ls"], 0x7ffc123456) = 0
14:15:32 brk(NULL)                      = 0x55555555
14:15:32 access("/etc/ld.so.preload", R_OK) = -1 ENOENT
```

## 使用例

### プログラムの最初から最後までトレース

```console
$ strace ls -l
execve("/bin/ls", ["ls", "-l"], 0x7ffc123456) = 0
brk(NULL)                               = 0x55555555
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
...
write(1, "total 20\n-rw-r--r-- 1 user user...", 612) = 612
exit_group(0)                           = ?
+++ exited with 0 +++
```

### 特定のシステムコールのトレース

```console
$ strace -e trace=open,read,write echo "Hello World"
execve("/bin/echo", ["echo", "Hello World"], 0x7ffc123456) = 0
write(1, "Hello World\n", 12)           = 12
+++ exited with 0 +++
```

### ファイルアクセスパターンの分析

```console
$ strace -e trace=file ls
execve("/bin/ls", ["ls"], 0x7ffc123456) = 0
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
stat(".", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
+++ exited with 0 +++
```

## ヒント:

### 特定のシステムコールでノイズをフィルタリング

デバッグ時には、`-e trace=`の後にシステムコール名を指定して関連するシステムコールに焦点を当てましょう。例えば、`strace -e trace=open,read,write`を使用すると、ファイル操作のみを表示できます。

### 出力をファイルにリダイレクト

長時間実行されるプロセスの場合、`-o filename.log`で出力をファイルにリダイレクトすると、端末が煩雑になるのを避け、後で分析することができます。

### 実行中のプロセスをトレース

`-p PID`を使用して、すでに実行中のプロセスにアタッチできます。これは、プログラムがすでに問題を抱えていて、再起動したくない場合に便利です。

### システムコールの時間を測定

各システムコールにかかる時間を表示するには`-T`を使用します。これはパフォーマンスのボトルネックを特定するのに役立ちます。

### ネットワークアクティビティのトレース

ネットワーク関連のシステムコールに焦点を当てるには`-e trace=network`を使用します。これは接続問題のデバッグに役立ちます。

## よくある質問

#### Q1. straceとltraceの違いは何ですか？
A. `strace`はシステムコール（プログラムとカーネルの間の相互作用）をトレースするのに対し、`ltrace`はライブラリコール（プログラムとライブラリの間の相互作用）をトレースします。

#### Q2. straceの出力の冗長性を減らすにはどうすればよいですか？
A. `-e trace=`を使用して関心のあるシステムコールのみを指定するか、`-c`を使用して詳細な出力ではなく要約カウントを取得します。

#### Q3. straceはトレース対象のプログラムを遅くすることがありますか？
A. はい、`strace`はすべてのシステムコールを傍受するため、かなりのオーバーヘッドが発生します。パフォーマンスに敏感なアプリケーションでは、使用を控えるか、特定のフィルターを使用してください。

#### Q4. 子プロセスを作成するプログラムをトレースするにはどうすればよいですか？
A. `-f`オプションを使用してフォークをフォローし、子プロセスもトレースします。

#### Q5. macOSでstraceを使用できますか？
A. いいえ、`strace`はLinux固有のツールです。macOSでは、同様の機能のために`dtruss`や`dtrace`を使用できますが、これらは管理者権限が必要です。

## 参考文献

https://man7.org/linux/man-pages/man1/strace.1.html

## 改訂履歴

2025/05/04 初版作成