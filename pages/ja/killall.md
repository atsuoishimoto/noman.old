# killall コマンド

プロセス名を指定して、該当するすべてのプロセスを終了させる。

## 概要

`killall` コマンドは、指定した名前に一致するすべてのプロセスにシグナルを送信します。通常は、特定のプログラムのすべてのインスタンスを一度に終了させるために使用されます。プロセスIDを調べる必要がなく、名前だけで複数のプロセスを終了できるため便利です。

## オプション

### **-i (--interactive)**

各プロセスを終了する前に確認を求めます。

```console
$ killall -i firefox
Kill firefox(1234) ? (y/N) y
Kill firefox(5678) ? (y/N) n
```

### **-I (--ignore-case)**

プロセス名の大文字と小文字を区別せずに一致させます。

```console
$ killall -I firefox
```

### **-e (--exact)**

プロセス名の完全一致を要求します（デフォルトでは部分一致も許容）。

```console
$ killall -e chrome
```

### **-s (--signal)**

送信するシグナルを指定します（デフォルトはTERM）。

```console
$ killall -s KILL firefox
```

### **-u (--user)**

特定のユーザーが所有するプロセスのみを終了します。

```console
$ killall -u username firefox
```

### **-v (--verbose)**

実行内容の詳細を表示します。

```console
$ killall -v firefox
Killed firefox(1234) with signal 15
Killed firefox(5678) with signal 15
```

### **-w (--wait)**

すべてのプロセスが終了するまで待機します。

```console
$ killall -w firefox
```

## 使用例

### 特定のプログラムのすべてのインスタンスを終了

```console
$ killall firefox
```

### 強制的にプロセスを終了（SIGKILL）

```console
$ killall -9 chrome
```

### 特定のユーザーのプロセスのみを終了

```console
$ killall -u username nginx
```

### プロセスが終了するまで待機

```console
$ killall -w -s TERM httpd
```

## ヒント:

### シグナル番号とシグナル名

シグナルは番号（例：9）または名前（例：KILL）で指定できます。一般的なシグナル：
- TERM (15): 通常の終了（デフォルト）
- KILL (9): 強制終了（プロセスが応答しない場合）
- HUP (1): 設定の再読み込み

### 安全な使用法

重要なシステムプロセスを誤って終了させないよう注意してください。特に `-9` オプションは最終手段として使用しましょう。

### プロセス名の確認

`ps aux | grep プロセス名` を使用して、終了させる前に正確なプロセス名を確認することをお勧めします。

## よくある質問

#### Q1. `kill` コマンドと `killall` の違いは何ですか？
A. `kill` はプロセスIDを指定してプロセスを終了させますが、`killall` はプロセス名を指定して、その名前に一致するすべてのプロセスを終了させます。

#### Q2. プロセスが終了しない場合はどうすればよいですか？
A. より強力なシグナルを送信してみてください。例えば `killall -9 プロセス名` を使用すると、SIGKILL シグナルを送信して強制的にプロセスを終了させます。

#### Q3. 特定のユーザーのプロセスだけを終了させるにはどうすればよいですか？
A. `-u` オプションを使用します。例：`killall -u username プロセス名`

#### Q4. `killall` コマンドの実行結果を確認するにはどうすればよいですか？
A. `-v`（verbose）オプションを使用すると、どのプロセスが終了されたかの情報が表示されます。

## macOSでの注意点

macOSの`killall`はLinuxバージョンとは若干動作が異なります。macOSでは完全なプロセス名の一致が必要で、部分一致は機能しません。また、一部のオプション（-I, -e など）がサポートされていない場合があります。

## 参考

https://man7.org/linux/man-pages/man1/killall.1.html

## 改訂履歴

- 2025/04/30 初版作成