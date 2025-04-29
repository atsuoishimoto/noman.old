# pstack コマンド
実行中のプロセスのスタックトレースを表示します。

## 概要
`pstack`は、実行中のプロセスのスタックトレース（関数呼び出し階層）を表示するコマンドです。デバッグやトラブルシューティングの際に、プロセスが現在どの関数を実行しているか、どのような呼び出し経路をたどってきたかを確認するのに役立ちます。内部的には`gdb`を使用してスタック情報を取得しています。

## オプション
`pstack`コマンドには特別なオプションはなく、引数としてプロセスIDを指定するだけです。

```console
$ pstack PID
```

## 使用例

### 特定のプロセスのスタックトレースを表示
```console
$ pstack 1234
#0  0x00007f9a0c3e83e3 in __read_nocancel () from /lib64/libc.so.6
#1  0x00007f9a0c0cf6a0 in ?? () from /lib64/libpthread.so.0
#2  0x00000000004006e5 in main () at example.c:15
```
この例では、PID 1234のプロセスが現在`__read_nocancel`関数内にあり、`main`関数から呼び出されていることがわかります。

### 複数のスレッドを持つプロセスのスタックトレース
```console
$ pstack 5678
Thread 1 (process 5678):
#0  0x00007f9a0c3e83e3 in poll () from /lib64/libc.so.6
#1  0x00000000004007c2 in worker_thread () at multi_thread.c:42
#2  0x00007f9a0c0ce5a0 in start_thread () from /lib64/libpthread.so.0

Thread 2 (process 5682):
#0  0x00007f9a0c3e83e3 in nanosleep () from /lib64/libc.so.6
#1  0x0000000000400705 in worker_thread () at multi_thread.c:30
#2  0x00007f9a0c0ce5a0 in start_thread () from /lib64/libpthread.so.0
```
マルチスレッドプロセスの場合、各スレッドのスタックトレースが表示されます。

## ヒント:
### プロセスIDの特定
`ps`コマンドを使用して、調査したいプロセスのPIDを特定できます。
```console
$ ps aux | grep プログラム名
```

### 定期的なスタックトレースの取得
問題の原因を特定するために、一定間隔でスタックトレースを取得することが有効です。
```console
$ while true; do pstack PID >> stack_trace.log; sleep 5; done
```
これにより5秒ごとにスタックトレースを記録できます。

### 権限の問題
他のユーザーが所有するプロセスのスタックトレースを取得するには、通常root権限が必要です。

## よくある質問
#### Q1. `pstack`と`gdb`の違いは何ですか？
A. `pstack`は`gdb`のラッパーで、スタックトレースのみを簡単に取得するために最適化されています。`gdb`はより多機能なデバッガで、ブレークポイントの設定や変数の検査など、より詳細なデバッグ機能を提供します。

#### Q2. `pstack`がインストールされていない場合はどうすればよいですか？
A. 多くのLinuxディストリビューションでは、`gdb`を使って同様の情報を取得できます：`gdb -p PID -batch -ex "thread apply all bt" -ex "quit"`

#### Q3. `pstack`を使用するとプロセスは一時停止しますか？
A. はい、`pstack`はプロセスに一時的にアタッチして情報を取得するため、その間プロセスは一時停止します。ただし、情報取得後すぐに実行が再開されます。

#### Q4. macOSで`pstack`を使用できますか？
A. macOSには`pstack`コマンドが標準で含まれていません。代わりに`lldb`を使用して同様の情報を取得できます：`lldb -p PID -o "bt all" -o "quit"`

## 参考資料
https://linux.die.net/man/1/pstack

## 改訂
- 2025/04/29 初版作成