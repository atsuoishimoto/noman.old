# kill コマンド

プロセスにシグナルを送信し、通常はプロセスを終了させます。

## 概要

`kill` コマンドはプロセスにシグナルを送信するもので、主に実行中のプロセスを終了させるために使用されます。名前は「殺す」を意味しますが、実際には様々な種類のシグナルをプロセスに送信でき、単に停止させる以外の制御も可能です。各シグナルには特定の目的があり、デフォルトのシグナルである SIGTERM (15) は、プロセスに対して正常な終了を要求します。

## オプション

### **-s, --signal [シグナル]**

送信するシグナルを指定します（名前または番号で指定可能）

```console
$ kill -s TERM 1234
```

### **-l, --list [シグナル]**

利用可能なシグナル名の一覧を表示、またはシグナル名と番号の相互変換を行います

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

### **-9, -KILL, -SIGKILL**

SIGKILL シグナルを送信します。即時強制終了を行うシグナルで、プロセスが捕捉したり無視したりすることはできません

```console
$ kill -9 1234
```

### **-15, -TERM, -SIGTERM**

SIGTERM シグナル（デフォルト）を送信します。正常な終了を要求するシグナルです

```console
$ kill -15 1234
```

## 使用例

### PID を指定してプロセスを終了する

```console
$ kill 1234
```

### 応答しないプロセスを強制的に終了する

```console
$ kill -9 1234
```

### プロセスにカスタムシグナルを送信する

```console
$ kill -s USR1 1234
```

### 複数のプロセスを一度に終了する

```console
$ kill 1234 5678 9012
```

## ヒント:

### 先にプロセスIDを見つける

`kill` を使用する前に `ps` や `pgrep` を使ってプロセスIDを見つけましょう：

```console
$ ps aux | grep firefox
user     1234  2.0  1.5 3245676 124548 ?      Sl   09:15   0:45 /usr/lib/firefox/firefox
$ kill 1234
```

### 明確さのためにシグナル名を使用する

シグナル名は番号よりも分かりやすいことが多いです：

```console
$ kill -TERM 1234  # kill -15 1234 と同じ
```

### 一般的なシグナルとその用途

- SIGTERM (15): 標準の終了シグナル、クリーンアップを許可
- SIGKILL (9): 強制終了、プロセスが応答しない場合に使用
- SIGHUP (1): 設定ファイルの再読み込みによく使用される
- SIGINT (2): 割り込みシグナル（Ctrl+C を押すのと同じ）

## よくある質問

#### Q1. `kill -9` と通常の `kill` の違いは何ですか？
A. 通常の `kill`（`kill -15` と同等）は SIGTERM を送信し、正常な終了を要求してプロセスにクリーンアップの機会を与えます。`kill -9` は SIGKILL を送信し、クリーンアップなしで即時終了を強制し、プロセスがこのシグナルを捕捉したり無視したりすることはできません。

#### Q2. PID ではなく名前でプロセスを終了するにはどうすればよいですか？
A. `kill` 自体は PID を必要としますが、`pkill` や `killall` を使用して名前でプロセスを終了できます：`pkill firefox` または `killall firefox`。

#### Q3. なぜ一部のプロセスに対して `kill -9` が効かないのですか？
A. 中断不可能なスリープ状態（通常は I/O 待ち）のプロセスやゾンビプロセスは、どのシグナルでも終了できません。また、PID 1（init/systemd）のプロセスはシグナルの扱いが異なります。

#### Q4. 特定のユーザーのすべてのプロセスを終了するにはどうすればよいですか？
A. `pkill -u ユーザー名` を使用して、特定のユーザーが所有するすべてのプロセスを終了できます。

## 参考資料

https://man7.org/linux/man-pages/man1/kill.1.html

## 改訂履歴

- 2025/05/04 初版作成