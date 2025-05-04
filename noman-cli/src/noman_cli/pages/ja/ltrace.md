# ltrace コマンド

プログラムのライブラリ呼び出しをトレースします。

## 概要

`ltrace`はプログラムが行う動的ライブラリ呼び出しを表示するデバッグユーティリティです。システムコールやプロセスが受信したシグナルも表示できます。このツールは、ソースコードが利用できない場合のプログラムのデバッグや、プログラムがライブラリとどのように相互作用するかを理解するのに特に役立ちます。

## オプション

### **-c, --count**

各ライブラリ呼び出しの時間と回数をカウントし、最後に要約を報告します。

```console
$ ltrace -c ls
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------------------
 21.05    0.000080          2        40 strlen
 15.79    0.000060          2        30 __ctype_b_loc
 10.53    0.000040          2        20 readdir64
  7.89    0.000030          2        15 fwrite
  5.26    0.000020          2        10 malloc
  5.26    0.000020          2        10 free
  5.26    0.000020          2        10 __errno_location
  5.26    0.000020          2        10 __cxa_atexit
  5.26    0.000020         20         1 opendir
  5.26    0.000020         20         1 closedir
  5.26    0.000020         20         1 setlocale
  5.26    0.000020         20         1 isatty
  2.63    0.000010         10         1 bindtextdomain
------ ----------- ----------- --------- --------------------
100.00    0.000380                   150 total
```

### **-f, --follow**

現在トレースされているプロセスによって作成される子プロセスをトレースします。

```console
$ ltrace -f ./program
[pid 12345] malloc(32)                                  = 0x55d7e9fa7260
[pid 12345] fork()                                      = 12346
[pid 12346] malloc(64)                                  = 0x55d7e9fa7290
```

### **-e, --expr=EXPR**

トレースまたはフィルタリングするライブラリ呼び出しを指定します。形式は[!][?][=][%][/@][+|-]pattern[@arch][:function]です。

```console
$ ltrace -e malloc+free ls
ls->malloc(32)                                          = 0x55d7e9fa7260
ls->malloc(64)                                          = 0x55d7e9fa7290
ls->free(0x55d7e9fa7260)                                = <void>
ls->free(0x55d7e9fa7290)                                = <void>
```

### **-p, --pid=PID**

指定されたPIDのプロセスにアタッチしてトレースを開始します。

```console
$ ltrace -p 1234
[pid 1234] read(5, "data", 1024)                        = 4
[pid 1234] write(1, "output", 6)                        = 6
```

### **-S, --summary**

トレースの最後にライブラリ呼び出しの使用状況の要約を表示します。

```console
$ ltrace -S ls
ls->__libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
...
+++ exited (status 0) +++
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------------------
 21.05    0.000080          2        40 strlen
 15.79    0.000060          2        30 __ctype_b_loc
 10.53    0.000040          2        20 readdir64
```

### **-o, --output=FILE**

トレース出力を標準エラー出力ではなくFILEに書き込みます。

```console
$ ltrace -o trace.log ls
$ cat trace.log
ls->__libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
ls->setlocale(6, "")                                    = "en_US.UTF-8"
ls->bindtextdomain("coreutils", "/usr/share/locale")    = "/usr/share/locale"
```

## 使用例

### 基本的な使用法

```console
$ ltrace ls
ls->__libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
ls->setlocale(6, "")                                    = "en_US.UTF-8"
ls->bindtextdomain("coreutils", "/usr/share/locale")    = "/usr/share/locale"
ls->textdomain("coreutils")                             = "coreutils"
ls->__cxa_atexit(0x4014a0, 0, 0, 0x736c6974)            = 0
ls->getenv("QUOTING_STYLE")                             = nil
...
+++ exited (status 0) +++
```

### 特定のライブラリ呼び出しのトレース

```console
$ ltrace -e malloc+free+open ./program
./program->malloc(1024)                                 = 0x55d7e9fa7260
./program->open("/etc/passwd", 0, 0)                    = 3
./program->malloc(2048)                                 = 0x55d7e9fa7660
./program->free(0x55d7e9fa7260)                         = <void>
./program->free(0x55d7e9fa7660)                         = <void>
```

### 時間情報付きのトレース

```console
$ ltrace -tt ./program
15:30:45.123456 __libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
15:30:45.123789 setlocale(6, "")                        = "en_US.UTF-8"
15:30:45.124012 malloc(1024)                            = 0x55d7e9fa7260
15:30:45.124234 free(0x55d7e9fa7260)                    = <void>
```

## ヒント:

### ノイズをフィルタリングする

`-e`オプションを使用して、関心のある特定の関数呼び出しに焦点を当てましょう。これにより出力量が減少し、分析が容易になります。

### straceと組み合わせる

包括的なデバッグのために、ライブラリ呼び出し用の`ltrace`とシステムコール用の`strace`の両方を使用しましょう。これによりプログラムの動作の完全な全体像が得られます。

### 分析のための出力リダイレクト

複雑なプログラムの場合、`-o`で出力をファイルにリダイレクトし、`grep`や`awk`などのツールを使用してトレースデータを分析しましょう。

### コアダンプとの併用

クラッシュのデバッグ時には、`ltrace`でプログラムを実行して、クラッシュ前に行われたライブラリ呼び出しを確認しましょう。

## よくある質問

#### Q1. ltraceとstraceの違いは何ですか？
A. `ltrace`はライブラリ呼び出し（libcなどの共有ライブラリ内の関数）をトレースするのに対し、`strace`はシステムコール（カーネルとの直接的な相互作用）をトレースします。`ltrace`は`printf()`のようなより高レベルの操作を表示し、`strace`は`write()`のようなより低レベルの操作を表示します。

#### Q2. ltraceはトレース対象のプログラムを遅くしますか？
A. はい、トレースには大きなオーバーヘッドが加わります。傍受される各呼び出しはコンテキストスイッチを必要とし、特に多くのライブラリ呼び出しを行うプログラムでは、かなり遅くなる可能性があります。

#### Q3. 特定のライブラリ関数だけをトレースするにはどうすればよいですか？
A. `-e`オプションをパターンと共に使用します。例えば：`ltrace -e malloc+free+fopen ./program`とすると、メモリ割り当てとファイル操作のみをトレースします。

#### Q4. ltraceは静的にリンクされたプログラムをトレースできますか？
A. いいえ、`ltrace`は主に動的にリンクされたプログラムで動作します。静的にリンクされたプログラムでは、ライブラリ呼び出しは実行可能ファイルにコンパイルされ、動的リンカーを通じて行われません。

## 参考資料

https://man7.org/linux/man-pages/man1/ltrace.1.html

## 改訂履歴

- 2025/05/04 初版作成