# kill コマンド

プロセスを終了させるためのシグナルを送信します。

## 概要

`kill` コマンドは、指定したプロセスにシグナルを送信するために使用されます。主にプロセスを終了させる目的で使われますが、実際には様々な種類のシグナルを送信できます。プロセスIDを指定して特定のプロセスを対象にします。

## オプション

### **-l (--list)**

利用可能なシグナルの一覧を表示します。

```console
$ kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

### **-s (--signal)**

送信するシグナルを指定します。シグナル名または番号で指定できます。

```console
$ kill -s TERM 1234
# プロセスID 1234に SIGTERM シグナルを送信する
```

### **-9 (SIGKILL)**

プロセスを強制的に終了させます。これは特殊なシグナルで、プロセスが無視できません。

```console
$ kill -9 1234
# プロセスID 1234を強制終了する
```

## 使用例

### 基本的な使い方

```console
$ kill 1234
# プロセスID 1234に SIGTERM（デフォルトのシグナル）を送信する
```

### 複数のプロセスを終了

```console
$ kill 1234 5678 9012
# 複数のプロセスに同時にシグナルを送信する
```

### プロセスグループを終了

```console
$ kill -TERM -1234
# プロセスグループID 1234のすべてのプロセスに SIGTERM を送信する
```

## ヒント:

### プロセスIDの確認方法

`ps` コマンドを使用して、終了させたいプロセスのIDを確認できます。

```console
$ ps aux | grep firefox
user     1234  2.0  1.5 2345678 123456 ?     Sl   10:00   0:30 /usr/lib/firefox/firefox
```

### シグナルの種類と用途

- **SIGTERM (15)**: デフォルトのシグナルで、プロセスに正常終了を要求します。プロセスは終了前に後片付けができます。
- **SIGKILL (9)**: プロセスを強制終了します。プロセスは後片付けができないため、最終手段として使用します。
- **SIGHUP (1)**: 多くのデーモンプロセスでは設定ファイルの再読み込みを意味します。

### pkill と killall の活用

プロセス名で終了させたい場合は、`pkill` や `killall` コマンドが便利です。

```console
$ pkill firefox
# firefoxという名前のプロセスをすべて終了する
```

## よくある質問

#### Q1. `kill` と `kill -9` の違いは何ですか？
A. 通常の `kill`（SIGTERM）はプロセスに終了を要求しますが、プロセスはこれを無視できます。`kill -9`（SIGKILL）は強制終了であり、プロセスは無視できません。

#### Q2. プロセスが終了しない場合はどうすればいいですか？
A. まず `kill`（SIGTERM）を試し、それでも終了しない場合は `kill -9`（SIGKILL）を使用します。ただし、SIGKILL は最終手段として使用してください。

#### Q3. 特定の名前のプロセスをすべて終了するにはどうすればいいですか？
A. `pkill` または `killall` コマンドを使用します。例: `pkill firefox` または `killall firefox`

#### Q4. シグナルの番号とシグナル名はどちらを使うべきですか？
A. シグナル名（例: SIGTERM）を使用する方が可読性が高く推奨されますが、番号（例: 15）も同様に機能します。

## macOSでの注意点

macOSでは基本的な機能は同じですが、利用可能なシグナルの一覧がLinuxとは若干異なる場合があります。また、macOSの `kill` コマンドはGNU版と比べてオプションが少ない場合があります。

## 参考資料

https://man7.org/linux/man-pages/man1/kill.1.html

## 改訂履歴

- 2025/04/30 初版作成