# pstack コマンド

実行中のプロセスのスタックトレースを表示します。

## 概要

`pstack` は、実行中のプロセスのスタックトレースを表示するコマンドです。プロセスIDを指定することで、そのプロセスの各スレッドの関数呼び出し階層（コールスタック）を確認できます。デバッグやトラブルシューティングの際に、プログラムがどの関数を実行中かを調査するのに役立ちます。

## オプション

`pstack` コマンドには特別なオプションはありません。単にプロセスIDを引数として指定します。

```console
$ pstack PID
```

## 使用例

### 実行中のプロセスのスタックトレースを表示

```console
$ pstack 1234
Thread 1 (process 1234):
#0  0x00007f9a3c8b1aaa in poll () from /lib64/libc.so.6
#1  0x00007f9a3d8dcce5 in ?? () from /lib64/libpthread.so.0
#2  0x000055c7e4a6b2a0 in main () at program.c:42
```

### 複数のスレッドを持つプロセスのスタックトレース

```console
$ pstack 5678
Thread 1 (process 5678):
#0  0x00007f9a3c8b1aaa in poll () from /lib64/libc.so.6
#1  0x00007f9a3d8dcce5 in ?? () from /lib64/libpthread.so.0
#2  0x000055c7e4a6b2a0 in main () at program.c:42

Thread 2 (Thread 0x7f9a3c123456):
#0  0x00007f9a3d8d9aaa in pthread_cond_wait () from /lib64/libpthread.so.0
#1  0x000055c7e4a6c123 in worker_thread () at program.c:78
#2  0x00007f9a3d8d5aa1 in start_thread () from /lib64/libpthread.so.0
```

## ヒント:

### 代替コマンド

多くのLinuxディストリビューションでは、`pstack` は `gdb -p PID -batch -ex "thread apply all bt"` と同等の機能を持ちます。`pstack` がインストールされていない場合は、この代替コマンドを使用できます。

### デバッグシンボルの重要性

詳細なスタックトレースを得るには、デバッグシンボル付きでコンパイルされたプログラムが必要です。シンボルがない場合、関数名や行番号が表示されないことがあります。

### 権限の問題

他のユーザーが所有するプロセスのスタックトレースを取得するには、通常 root 権限が必要です。

## よくある質問

#### Q1. `pstack` コマンドが見つからないというエラーが出ます。どうすればよいですか？
A. 一部のディストリビューションでは `pstack` がデフォルトでインストールされていません。代わりに `gdb -p PID -batch -ex "thread apply all bt"` を使用するか、`gdb-utils` や `elfutils` パッケージをインストールしてください。

#### Q2. スタックトレースに関数名が表示されません。なぜですか？
A. プログラムがデバッグシンボルなしでコンパイルされている可能性があります。デバッグシンボル付きでコンパイルし直すか、デバッグシンボルを含むパッケージをインストールしてください。

#### Q3. `pstack` を使ってハングしているプロセスを診断するにはどうすればよいですか？
A. ハングしているプロセスのPIDを特定し、`pstack PID` を実行します。出力からどの関数でプロセスが停止しているかを確認できます。複数回実行して変化がなければ、その箇所でプロセスがブロックされている可能性が高いです。

## macOSでの注意点

macOSには `pstack` コマンドが標準で含まれていません。代わりに以下の方法を使用できます：

1. `sample` コマンドを使用する：
   ```console
   $ sample PID 1
   ```

2. `lldb` を使用する：
   ```console
   $ lldb -p PID -o "bt all" -o "quit"
   ```

## 参考文献

https://linux.die.net/man/1/pstack

## 改訂履歴

- 2025/04/30 初版作成