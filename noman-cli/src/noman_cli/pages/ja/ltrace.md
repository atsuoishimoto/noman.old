# ltrace コマンド
実行中のプログラムが行うライブラリコールをトレースします。

## 概要
`ltrace`は、プログラムが実行中に呼び出すライブラリ関数（C標準ライブラリなど）を追跡し表示するデバッグツールです。プログラムの動作を理解したり、バグを特定したりする際に役立ちます。`strace`がシステムコールを追跡するのに対し、`ltrace`はライブラリコールに焦点を当てています。

## オプション
### **-c**
統計情報をまとめて表示します。各ライブラリ関数の呼び出し回数、費やした時間などを集計します。

```console
$ ltrace -c ls
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------------------
 24.39    0.000100          33         3 __errno_location
 21.95    0.000090          30         3 sigaction
 14.63    0.000060          20         3 readdir
  9.76    0.000040          20         2 closedir
  7.32    0.000030          15         2 opendir
  7.32    0.000030          15         2 strlen
  7.32    0.000030          15         2 malloc
  4.88    0.000020          10         2 free
  2.44    0.000010          10         1 fclose
------ ----------- ----------- --------- --------------------
100.00    0.000410                    20 total
```

### **-f**
子プロセスも追跡します。プログラムがforkやexecを使用して他のプロセスを起動する場合に便利です。

```console
$ ltrace -f make
[pid 12345] __libc_start_main(0x401500, 2, 0x7ffc123456, 0x4016a0 <unfinished ...>
[pid 12345] getopt_long(2, 0x7ffc123456, "df:j:kmNnprRsS:t", 0x7f123456, 0) = -1
[pid 12345] fork() = 12346
[pid 12346] execve("/bin/sh", ["sh", "-c", "gcc -o hello hello.c"], 0x7ffc123456 <unfinished ...>
...
```

### **-p PID**
実行中のプロセスにアタッチします。すでに動作しているプログラムを途中から追跡したい場合に使用します。

```console
$ ltrace -p 1234
[pid 1234] read(5, "Hello World", 1024)                = 11
[pid 1234] printf("Received: %s\n", "Hello World")     = 19
[pid 1234] write(1, "Received: Hello World\n", 19)     = 19
```

### **-e PATTERN**
特定のライブラリ関数だけを追跡します。大量の出力から必要な情報だけを絞り込みたい場合に便利です。

```console
$ ltrace -e malloc+free ls
ls->malloc(32)                                       = 0x55d5e9fa72a0
ls->malloc(13)                                       = 0x55d5e9fa72d0
ls->free(0x55d5e9fa72d0)                             = <void>
ls->free(0x55d5e9fa72a0)                             = <void>
+++ exited (status 0) +++
```

## 使用例
### 基本的な使い方
```console
$ ltrace ls
__libc_start_main(0x401670, 1, 0x7ffc123456, 0x4017a0 <unfinished ...>
strrchr("ls", '/')                                   = NULL
setlocale(LC_ALL, "")                                = "ja_JP.UTF-8"
bindtextdomain("coreutils", "/usr/share/locale")     = "/usr/share/locale"
textdomain("coreutils")                              = "coreutils"
__cxa_atexit(0x401930, 0, 0, 0x736c)                 = 0
getenv("POSIXLY_CORRECT")                            = NULL
...
+++ exited (status 0) +++
```

### 特定の関数を追跡する
```console
$ ltrace -e malloc+free+open firefox
firefox->malloc(832)                                 = 0x55d5e9fa72a0
firefox->open("/etc/passwd", 0, 0)                   = 3
firefox->malloc(1024)                                = 0x55d5e9fa7500
firefox->free(0x55d5e9fa72a0)                        = <void>
...
```

### 出力をファイルに保存する
```console
$ ltrace -o trace.log ./myprogram
$ cat trace.log
__libc_start_main(0x400526, 1, 0x7ffc123456, 0x400580 <unfinished ...>
printf("Hello, World!\n")                            = 14
puts("Program finished")                             = 17
+++ exited (status 0) +++
```

## ヒント:
### 出力の読み方
関数名の後の括弧内は引数、等号の後は戻り値を示しています。`<unfinished ...>`は関数がまだ終了していないことを、`<... function resumed>`は中断された関数の処理が再開されたことを示します。

### システムコールとの違い
`ltrace`はライブラリコールを追跡し、`strace`はシステムコールを追跡します。両方を使うことで、プログラムの動作をより深く理解できます。

### デバッグシンボルの重要性
デバッグシンボルがあるプログラムでは、より詳細な情報が得られます。`-debug`パッケージをインストールするか、コンパイル時に`-g`オプションを使用すると良いでしょう。

### 大きなプログラムでの使用
大規模なプログラムでは出力が膨大になるため、`-e`オプションで特定の関数に絞るか、`-o`で出力をファイルに保存して後で分析することをお勧めします。

## よくある質問
#### Q1. ltraceとstraceの違いは何ですか？
A. `ltrace`はライブラリ関数呼び出し（printf、mallocなど）を追跡し、`strace`はシステムコール（read、writeなど）を追跡します。

#### Q2. ltraceを使うにはroot権限が必要ですか？
A. 自分のプロセスを追跡する場合は不要ですが、他のユーザーのプロセスを追跡する場合はroot権限が必要です。

#### Q3. 出力が多すぎる場合はどうすればよいですか？
A. `-e`オプションで特定の関数だけを追跡するか、`-o`オプションで出力をファイルに保存して後で検索・フィルタリングすることができます。

#### Q4. 静的にリンクされたプログラムでltraceは使えますか？
A. 静的にリンクされたプログラムでは、ライブラリ関数が実行ファイルに組み込まれているため、`ltrace`の効果は限定的です。

## macOSでの注意点
macOSでは`ltrace`は標準でインストールされておらず、代わりに`dtruss`や`dtrace`などのツールが使用されます。Homebrewなどのパッケージマネージャーを使ってインストールすることもできますが、システム保護機能（SIP）により機能が制限される場合があります。

## 参考資料
https://man7.org/linux/man-pages/man1/ltrace.1.html

## 改訂履歴
- 2025/04/29 初版作成