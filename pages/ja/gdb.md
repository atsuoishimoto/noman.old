# gdb コマンド

プログラムのデバッグや実行時の動作を分析するためのコマンドラインデバッガです。

## 概要

GNU Debugger (GDB) は、C、C++、Fortran などのプログラミング言語で書かれたプログラムのデバッグに使用されるツールです。プログラムの実行を制御し、実行中に何が起きているかを確認したり、クラッシュした場合に何が起きたかを調査したりすることができます。ブレークポイントの設定、変数の検査、コードのステップ実行などの機能を提供します。

## オプション

### **-q, --quiet, --silent**

起動時のバナーや著作権情報を表示しません。

```console
$ gdb -q ./myprogram
(gdb) 
```

### **-c FILE**

指定したコアダンプファイルを使用してデバッグを行います。

```console
$ gdb -q ./myprogram -c core
(gdb) bt
#0  0x00005555555551a4 in main () at main.c:15
```

### **-p PID**

実行中のプロセスにアタッチします。

```console
$ gdb -q -p 1234
(gdb) bt
#0  0x00007f8b4c5fe4b0 in poll () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x000055555555a1a4 in main () at main.c:42
```

### **--args**

プログラムに引数を渡します。

```console
$ gdb --args ./myprogram arg1 arg2
(gdb) run
Starting program: /home/user/myprogram arg1 arg2
```

## 使用例

### 基本的なデバッグセッション

```console
$ gdb -q ./myprogram
(gdb) break main
Breakpoint 1 at 0x1149: file main.c, line 5.
(gdb) run
Starting program: /home/user/myprogram

Breakpoint 1, main () at main.c:5
5       int x = 10;
(gdb) next
6       printf("x = %d\n", x);
(gdb) print x
$1 = 10
(gdb) continue
Continuing.
x = 10
[Inferior 1 (process 12345) exited normally]
```

### バックトレースの表示

```console
$ gdb -q ./myprogram
(gdb) run
Starting program: /home/user/myprogram
Program received signal SIGSEGV, Segmentation fault.
0x0000555555555174 in foo () at main.c:12
12      *ptr = 42;  // ここでセグメンテーション違反が発生
(gdb) bt
#0  0x0000555555555174 in foo () at main.c:12
#1  0x00005555555551a4 in main () at main.c:18
```

### 変数の監視

```console
$ gdb -q ./myprogram
(gdb) break 10
Breakpoint 1 at 0x1155: file main.c, line 10.
(gdb) run
Starting program: /home/user/myprogram

Breakpoint 1, main () at main.c:10
10      for (i = 0; i < 5; i++) {
(gdb) watch i
Hardware watchpoint 2: i
(gdb) continue
Continuing.
Hardware watchpoint 2: i

Old value = 0
New value = 1
main () at main.c:10
10      for (i = 0; i < 5; i++) {
```

## ヒント:

### コアダンプファイルの生成を有効にする

プログラムがクラッシュした際にコアダンプファイルを生成するには、以下のコマンドを実行します：
```console
$ ulimit -c unlimited
```

### 便利なGDBコマンド

- `help` - 利用可能なコマンドの一覧を表示
- `info breakpoints` - 設定したブレークポイントの一覧を表示
- `info locals` - 現在のスコープのローカル変数を表示
- `disassemble` - 現在の関数のアセンブリコードを表示

### GDBの設定ファイル

ホームディレクトリに `.gdbinit` ファイルを作成することで、GDB起動時に自動的に実行されるコマンドを設定できます。

## よくある質問

#### Q1. GDBでプログラムを実行するにはどうすればよいですか？
A. まず `gdb ./プログラム名` でGDBを起動し、`run` コマンドを使用してプログラムを実行します。

#### Q2. ブレークポイントを設定するにはどうすればよいですか？
A. `break 関数名` または `break ファイル名:行番号` を使用します。例えば `break main` や `break main.c:15` のように指定します。

#### Q3. プログラムをステップ実行するにはどうすればよいですか？
A. `next` コマンドで次の行に進みます（関数呼び出しの中には入りません）。`step` コマンドを使うと関数呼び出しの中にも入ります。

#### Q4. 変数の値を確認するにはどうすればよいですか？
A. `print 変数名` または短縮形の `p 変数名` を使用します。例えば `print x` や `p array[5]` のように指定します。

#### Q5. macOSでGDBを使用する際の注意点はありますか？
A. macOSではセキュリティ上の理由からGDBの使用に制限があります。GDBを使用するには、コード署名が必要です。また、多くのmacOSユーザーはLLDBを代替として使用しています。

## 参考情報

https://sourceware.org/gdb/current/onlinedocs/gdb/

## 改訂履歴

- 2025/04/30 初版作成