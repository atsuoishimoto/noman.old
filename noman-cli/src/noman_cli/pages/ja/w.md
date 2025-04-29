# w コマンド

`w` コマンドは、システムにログインしているユーザーの情報と、各ユーザーが何をしているかを表示します。uptime 情報も同時に表示されます。

## オプション

### **-h**

ヘッダー行を表示しません。

```bash
$ w -h
user     tty      from             login@   idle   JCPU   PCPU  what
tanaka   pts/0    192.168.1.5      10:15    0.00s  0.05s  0.01s  w -h
yamada   pts/1    192.168.1.10     09:30    5:22   0.28s  0.28s  vim document.txt
```

### **-s**

短い形式で表示します。ログイン時間、JCPU、PCPU の列が省略されます。

```bash
$ w -s
 10:30:25 up  3:45,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM              IDLE WHAT
tanaka   pts/0    192.168.1.5       0.00s w -s
yamada   pts/1    192.168.1.10      5:22  vim document.txt
```

### **-f**

FROM フィールド（リモートホスト名）の表示をオン/オフします。

```bash
$ w -f
 10:30:25 up  3:45,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
tanaka   pts/0                      10:15    0.00s  0.05s  0.01s w -f
yamada   pts/1                      09:30    5:22   0.28s  0.28s vim document.txt
```

### **-i**

IP アドレスの代わりにホスト名を表示します。

```bash
$ w -i
 10:30:25 up  3:45,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
tanaka   pts/0    workstation5      10:15    0.00s  0.05s  0.01s w -i
yamada   pts/1    workstation10     09:30    5:22   0.28s  0.28s vim document.txt
```

## 使用例

### 基本的な使用方法

```bash
$ w
 10:30:25 up  3:45,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
tanaka   pts/0    192.168.1.5       10:15    0.00s  0.05s  0.01s w
yamada   pts/1    192.168.1.10      09:30    5:22   0.28s  0.28s vim document.txt
```

### 特定のユーザーの情報を表示

```bash
$ w tanaka
 10:30:25 up  3:45,  2 users,  load average: 0.08, 0.03, 0.01
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
tanaka   pts/0    192.168.1.5       10:15    0.00s  0.05s  0.01s w tanaka
```

## よくある質問

### Q1. `w` コマンドの出力の各列は何を意味していますか？
A. 主な列の意味は以下の通りです：
- USER: ログインしているユーザー名
- TTY: ユーザーが使用している端末
- FROM: ユーザーがログインしている場所（IPアドレスやホスト名）
- LOGIN@: ログインした時刻
- IDLE: アイドル時間（何も操作していない時間）
- JCPU: この端末で実行されたすべてのプロセスの CPU 時間
- PCPU: 現在実行中のプロセスの CPU 時間
- WHAT: ユーザーが実行しているコマンド

### Q2. `w` と `who` コマンドの違いは何ですか？
A. `w` は `who` の拡張版で、ログインユーザーの情報に加えて、システムの負荷情報やユーザーが実行しているコマンドも表示します。`who` はより基本的な情報のみを表示します。

### Q3. システムの負荷平均（load average）の数値は何を意味していますか？
A. 負荷平均は、過去1分、5分、15分間のシステム負荷を示します。値が1.0の場合、CPUが100%使用されていることを意味します。マルチコアシステムでは、コア数に応じて高い値でも正常な場合があります。

## 追加情報

- `w` コマンドは、システム管理者がサーバーの使用状況を監視するのに役立ちます。
- 出力の最初の行は `uptime` コマンドと同じ情報を表示します。
- macOS では Linux 版と比較して表示される情報が若干異なる場合があります。特に FROM フィールドの表示方法が異なることがあります。
- セキュリティ上の理由から、一般ユーザーは他のユーザーが実行しているコマンドの詳細情報を見ることができない場合があります。

## 参考情報

https://man7.org/linux/man-pages/man1/w.1.html