# w コマンド

現在ログインしているユーザーと彼らの行動を表示します。

## 概要

`w` コマンドは、現在ログインしているユーザーとその活動に関する情報を表示します。ログイン名、端末タイプ、リモートホスト、ログイン時間、アイドル時間、CPU使用率、現在実行中のコマンドを表示します。これはシステム管理者がシステム上のユーザー活動を監視するのに役立ちます。

## オプション

### **-h, --no-header**

ヘッダー情報を表示しません

```console
$ w -h
user     tty      from             login@   idle   JCPU   PCPU  what
john     tty1                      10:15    0.00s  0.05s  0.01s  w -h
alice    pts/0    192.168.1.5      09:30    2:35   0.10s  0.05s  vim report.txt
```

### **-s, --short**

短い形式で表示し、ログイン時間、JCPUとPCPU時間を省略します

```console
$ w -s
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             IDLE   WHAT
john     tty1                       0.00s  w -s
alice    pts/0    192.168.1.5       2:35  vim report.txt
bob      pts/1    10.0.0.2         23.00s  bash
```

### **-f, --from**

`from`（リモートホスト名）フィールドの表示を切り替えます

```console
$ w -f
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY        LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1      10:15     0.00s  0.05s  0.01s  w -f
alice    pts/0     09:30     2:35   0.10s  0.05s  vim report.txt
bob      pts/1     10:05    23.00s  0.07s  0.02s  bash
```

### **-i, --ip-addr**

FROMフィールドにホスト名の代わりにIPアドレスを表示します

```console
$ w -i
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1                      10:15    0.00s  0.05s  0.01s  w -i
alice    pts/0    192.168.1.5      09:30     2:35  0.10s  0.05s  vim report.txt
bob      pts/1    10.0.0.2         10:05    23.00s 0.07s  0.02s  bash
```

## 使用例

### 基本的な使用法

```console
$ w
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1                      10:15    0.00s  0.05s  0.01s  w
alice    pts/0    server2          09:30     2:35  0.10s  0.05s  vim report.txt
bob      pts/1    workstation5     10:05    23.00s 0.07s  0.02s  bash
```

### オプションの組み合わせ

```console
$ w -hi
USER     TTY      FROM             IDLE   JCPU   PCPU  WHAT
john     tty1                      0.00s  0.05s  0.01s  w -hi
alice    pts/0    192.168.1.5      2:35   0.10s  0.05s  vim report.txt
bob      pts/1    10.0.0.2         23.00s 0.07s  0.02s  bash
```

## ヒント:

### 出力列の理解

- **USER**: ログインしているユーザーのユーザー名
- **TTY**: ユーザーがログインしている端末名
- **FROM**: リモートホスト名またはIPアドレス
- **LOGIN@**: ユーザーがログインした時間
- **IDLE**: ユーザーの最後の活動からの経過時間
- **JCPU**: ttyに接続されたすべてのプロセスで使用された時間
- **PCPU**: 現在のプロセスで使用された時間
- **WHAT**: ユーザーが現在実行しているコマンド

### システム負荷の確認

ヘッダーには、システムの稼働時間と過去1分、5分、15分の平均負荷が表示され、システムのパフォーマンスを一目で評価するのに役立ちます。

### 非アクティブなユーザーの特定

IDLE時間が長いユーザーを探すことで、リソースを解放するために終了候補となる可能性のある非アクティブなセッションを特定できます。

## よくある質問

#### Q1. `w`コマンドと`who`コマンドの違いは何ですか？
A. `w`は`who`よりも詳細な情報を提供し、各ユーザーが何をしているか、アイドル時間、CPU使用統計などが含まれます。`who`は単にログインしている人を一覧表示するだけです。

#### Q2. 負荷平均の数値はどのように解釈すればよいですか？
A. 負荷平均は1分、5分、15分間のシステム平均負荷を表します。シングルコアシステムでは、1.0を超える値はシステムが過負荷であることを示します。マルチコアシステムの場合は、コア数で割って負荷を評価します。

#### Q3. IDLEカラムは何を意味しますか？
A. IDLEカラムは、ユーザーが端末で最後に活動してからの経過時間を示します。これは非アクティブなセッションを特定するのに役立ちます。

#### Q4. 特定のユーザーの活動だけを見るにはどうすればよいですか？
A. `w ユーザー名`を使用すると、その特定のユーザーの情報のみが表示されます。

## 参考資料

https://www.man7.org/linux/man-pages/man1/w.1.html

## 改訂履歴

- 2025/05/04 初版作成