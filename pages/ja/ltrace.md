# ltrace コマンド

実行中のプログラムが行うライブラリコール（関数呼び出し）をトレースします。

## 概要

`ltrace`は、プログラムが実行中に呼び出すライブラリ関数をリアルタイムで監視・表示するデバッグツールです。システム管理者や開発者がプログラムの動作を理解したり、問題を診断したりするのに役立ちます。`strace`がシステムコールを追跡するのに対し、`ltrace`はライブラリ関数の呼び出しを追跡します。

## オプション

### **-c**

関数呼び出しの統計情報を表示します。各関数の呼び出し回数、費やした時間などの概要を示します。

```console
$ ltrace -c ls
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------------------
 28.57    0.000040          40         1 setlocale
 21.43    0.000030          30         1 bindtextdomain
 21.43    0.000030          30         1 textdomain
 14.29    0.000020          20         1 __cxa_atexit
 14.29    0.000020          20         1 isatty
------ ----------- ----------- --------- --------------------
100.00    0.000140                     5 total
```

### **-f**

フォークされた子プロセスも追跡します。プログラムが新しいプロセスを作成する場合に便利です。

```console
$ ltrace -f bash -c "ls"
[pid 12345] __libc_start_main(0x401a90, 2, 0x7ffc123456, 0x4028a0, 0x402880
[pid 12345] setlocale(LC_ALL, "")                                = "en_US.UTF-8"
[pid 12345] bindtextdomain("coreutils", "/usr/share/locale")     = "/usr/share/locale"
[pid 12345] textdomain("coreutils")                              = "coreutils"
...
```

### **-p PID**

既に実行中のプロセスにアタッチします。実行中のプログラムをデバッグする際に便利です。

```console
$ ltrace -p 1234
[pid 1234] read(5, "Hello World", 4096)                         = 11
[pid 1234] printf("Received: %s\n", "Hello World")              = 19
[pid 1234] write(1, "Received: Hello World\n", 23)              = 23
```

### **-S**

ライブラリコールに加えてシステムコールも表示します。プログラムの動作をより包括的に理解するのに役立ちます。

```console
$ ltrace -S ls
SYS_brk(0)                                                       = 0x55a54e2c2000
SYS_access("/etc/ld.so.preload", R_OK)                          = -2
SYS_openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC)    = 3
SYS_fstat(3, 0x7ffd123456)                                      = 0
setlocale(LC_ALL, "")                                           = "en_US.UTF-8"
bindtextdomain("coreutils", "/usr/share/locale")                = "/usr/share/locale"
...
```

## 使用例

### 基本的な使用方法

```console
$ ltrace ls
__libc_start_main(0x401a90, 1, 0x7ffc123456, 0x4028a0, 0x402880) = 0x7f123456
setlocale(LC_ALL, "")                                           = "en_US.UTF-8"
bindtextdomain("coreutils", "/usr/share/locale")                = "/usr/share/locale"
textdomain("coreutils")                                         = "coreutils"
__cxa_atexit(0x402860, 0, 0, 0x736c6974756572)                  = 0
isatty(1)                                                       = 1
...
```

### 特定の関数のみをトレース

```console
$ ltrace -e malloc+free ls
malloc(32)                                                      = 0x55a54e2c3010
malloc(4096)                                                    = 0x55a54e2c4000
malloc(13)                                                      = 0x55a54e2c5000
free(0x55a54e2c5000)                                            = <void>
free(0x55a54e2c4000)                                            = <void>
free(0x55a54e2c3010)                                            = <void>
```

### 出力をファイルに保存

```console
$ ltrace -o trace.log ls
$ cat trace.log
__libc_start_main(0x401a90, 1, 0x7ffc123456, 0x4028a0, 0x402880) = 0x7f123456
setlocale(LC_ALL, "")                                           = "en_US.UTF-8"
...
```

## ヒント:

### デバッグシンボルをインストールする

より詳細な情報を得るには、デバッグシンボルパッケージをインストールしてください。Ubuntuでは`apt install libc6-dbg`のようなコマンドを使用します。

### 出力のフィルタリング

`-e`オプションを使用して特定の関数だけをトレースできます。例えば、`ltrace -e malloc+free+open`とすると、メモリ割り当てとファイル操作のみを追跡できます。

### 再帰的な関数呼び出しの深さ制限

`-L`オプションを使用して、再帰的な関数呼び出しの深さを制限できます。大きなプログラムをトレースする際に出力を管理しやすくします。

## よくある質問

#### Q1. `ltrace`と`strace`の違いは何ですか？
A. `ltrace`はライブラリ関数の呼び出しを追跡するのに対し、`strace`はシステムコール（OSカーネルへの呼び出し）を追跡します。

#### Q2. `ltrace`を使用するために特別な権限が必要ですか？
A. 通常、自分のプロセスをトレースするには特別な権限は必要ありませんが、他のユーザーのプロセスをトレースするには管理者権限（root）が必要です。

#### Q3. `ltrace`の出力が多すぎる場合はどうすればよいですか？
A. `-e`オプションで特定の関数のみをトレースしたり、`-o`オプションで出力をファイルに保存したり、`-c`オプションで統計情報のみを表示したりできます。

#### Q4. macOSで`ltrace`は使用できますか？
A. macOSには標準で`ltrace`は含まれていません。代わりに`dtruss`や`dtrace`などのツールを使用できますが、機能は異なります。Homebrewなどのパッケージマネージャーを通じてインストールすることもできますが、システムの制限により完全な機能を提供できない場合があります。

## 参考文献

https://man7.org/linux/man-pages/man1/ltrace.1.html

## 改訂履歴

- 2025/04/30 初版作成