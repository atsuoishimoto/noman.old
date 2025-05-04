# killall コマンド

名前を指定してプロセスを終了させるコマンド。

## 概要

`killall` コマンドは、プロセスID（PID）ではなく、プロセス名に基づいて実行中のプロセスを終了させます。同じプログラムの複数のインスタンスを停止する必要がある場合や、特定のプロセスのPIDがわからない場合に特に便利です。

## オプション

### **-e, --exact**

非常に長い名前に対して完全一致を要求します

```console
$ killall -e firefox
```

### **-I, --ignore-case**

大文字小文字を区別せずにプロセス名を一致させます

```console
$ killall -I firefox
```

### **-i, --interactive**

プロセスを終了する前に確認を求めます

```console
$ killall -i chrome
Kill chrome(1234) ? (y/N) y
Kill chrome(5678) ? (y/N) n
```

### **-l, --list**

既知のすべてのシグナル名を一覧表示します

```console
$ killall -l
HUP INT QUIT ILL TRAP ABRT BUS FPE KILL USR1 SEGV USR2 PIPE ALRM TERM STKFLT CHLD CONT STOP TSTP TTIN TTOU URG XCPU XFSZ VTALRM PROF WINCH POLL PWR SYS
```

### **-q, --quiet**

プロセスが終了しなかった場合にエラーメッセージを表示しません

```console
$ killall -q nonexistentprocess
```

### **-s, --signal SIGNAL, -SIGNAL**

SIGTERMの代わりに特定のシグナルを送信します

```console
$ killall -s SIGKILL firefox
$ killall -KILL firefox  # 同等の指定方法
```

### **-u, --user USER**

指定したユーザーが所有するプロセスのみを終了します

```console
$ killall -u username firefox
```

### **-v, --verbose**

シグナルが正常に送信されたかどうかを報告します

```console
$ killall -v firefox
Killed firefox(1234) with signal 15
```

### **-w, --wait**

終了したすべてのプロセスが完全に終了するまで待機します

```console
$ killall -w firefox
```

## 使用例

### 特定のアプリケーションを終了する

```console
$ killall firefox
```

### 特定のシグナルでプロセスを終了する

```console
$ killall -9 chrome
```

### 特定のユーザーが所有するプロセスを終了する

```console
$ killall -u john java
```

### 確認を求めながらプロセスを終了し、完了を待つ

```console
$ killall -i -w firefox
Kill firefox(1234) ? (y/N) y
```

## ヒント:

### 重要なプロセスには確認オプションを使用する

重要なプロセスを終了する場合は、誤って間違ったプロセスを終了させないように、`-i`（対話式）オプションを常に使用しましょう。

### 事前にプロセス名を確認する

killallを使用する前に`ps aux | grep プロセス名`を実行して、終了させたいプロセスの正確な名前を確認しましょう。

### 完了を待つ

他の操作に進む前にプロセスが完全に終了したことを確認する必要がある場合は、`-w`オプションを使用しましょう。

### 一般的な名前には注意する

ユーザー指定（-u）や対話モード（-i）を使用せずに、「http」や「java」などの非常に一般的なプロセス名でkillallを使用することは避けてください。重要なシステムプロセスが終了する可能性があります。

## よくある質問

#### Q1. `kill`と`killall`の違いは何ですか？
A. `kill`はPID（プロセスID）でプロセスを終了させますが、`killall`はプロセス名でプロセスを終了させます。

#### Q2. 頑固なプロセスを強制終了するにはどうすればよいですか？
A. `killall -9 プロセス名`または`killall -KILL プロセス名`を使用して、プロセスが捕捉または無視できないSIGKILLシグナルを送信します。

#### Q3. 複数の異なるプロセスを一度に終了できますか？
A. はい、すべてのプロセス名をリストするだけです：`killall firefox chrome gedit`

#### Q4. killallが成功したかどうかを確認するにはどうすればよいですか？
A. `-v`（詳細）オプションを使用して、終了した各プロセスの確認メッセージを表示します。

#### Q5. killallはすべてのUnixシステムで利用可能ですか？
A. いいえ、Linuxでは一般的ですが、SolarisなどのUnixバリアントでは異なる`killall`コマンドがあり、すべてのプロセスを終了させるため危険です。不慣れなシステムでは常にmanページを確認してください。

## 参考資料

https://man7.org/linux/man-pages/man1/killall.1.html

## 改訂履歴

- 2025/05/04 初版作成