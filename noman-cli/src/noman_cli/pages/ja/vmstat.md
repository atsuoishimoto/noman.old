# vmstat コマンド

システムの仮想メモリ統計情報を表示します。

## 概要

`vmstat`はシステムのメモリ、プロセス、ページング、ブロックIO、トラップ、CPUアクティビティに関する情報を提供します。このコマンドはシステムのパフォーマンスをモニタリングし、ボトルネックを特定するのに役立ちます。デフォルトでは、実行時に1回だけ統計情報を表示しますが、定期的な更新も設定できます。

## オプション

### **-S**

メモリ統計の単位を指定します（k: キロバイト、K: キビバイト、m: メガバイト、M: メビバイト）

```console
$ vmstat -S m
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0   3954    227   2456    0    0     3     5   36   79  1  0 99  0  0
```

### **-a**

アクティブおよび非アクティブメモリの詳細を表示します

```console
$ vmstat -a
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free  inact active   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 4050876 1286312 2517092    0    0     3     5   36   79  1  0 99  0  0
```

### **-d**

ディスク統計を表示します

```console
$ vmstat -d
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12345   2345  123456   12345  54321   9876  654321   98765      0     12
```

### **間隔と回数の指定**

指定した秒数ごとに、指定した回数だけ統計情報を表示します

```console
$ vmstat 2 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 4050876   232 2515092    0    0     3     5   36   79  1  0 99  0  0
 0  0      0 4050876   232 2515092    0    0     0     0  214  356  0  0 100  0  0
 0  0      0 4050876   232 2515092    0    0     0     0  212  354  0  0 100  0  0
 0  0      0 4050876   232 2515092    0    0     0     0  215  358  0  0 100  0  0
 0  0      0 4050876   232 2515092    0    0     0     0  213  355  0  0 100  0  0
```

## 使用例

### 基本的な使用法

```console
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 4050876   232 2515092    0    0     3     5   36   79  1  0 99  0  0
```

### 継続的なモニタリング

```console
$ vmstat 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 4050876   232 2515092    0    0     3     5   36   79  1  0 99  0  0
 0  0      0 4050876   232 2515092    0    0     0     0  214  356  0  0 100  0  0
 0  0      0 4050876   232 2515092    0    0     0     0  212  354  0  0 100  0  0
```

### 詳細なメモリ情報の表示

```console
$ vmstat -s
      8167848 K total memory
      1601880 K used memory
      2517092 K active memory
      1286312 K inactive memory
      4050876 K free memory
       232428 K buffer memory
      2282664 K swap cache
      8388604 K total swap
            0 K used swap
      8388604 K free swap
       123456 non-nice user cpu ticks
         1234 nice user cpu ticks
        56789 system cpu ticks
     12345678 idle cpu ticks
         9876 IO-wait cpu ticks
            0 IRQ cpu ticks
         5432 softirq cpu ticks
            0 stolen cpu ticks
       345678 pages paged in
       567890 pages paged out
            0 pages swapped in
            0 pages swapped out
     12345678 interrupts
     23456789 CPU context switches
   1234567890 boot time
        12345 forks
```

## ヒント:

### 出力の読み方

- `r`: 実行待ちのプロセス数（高い値はCPUがボトルネックである可能性を示す）
- `b`: 割り込み不可能なスリープ状態のプロセス数（I/O待ちなど）
- `si/so`: スワップイン/アウト（高い値はメモリ不足を示す）
- `us/sy/id`: ユーザー時間/システム時間/アイドル時間のパーセンテージ

### 効果的なモニタリング

システムの問題を診断する場合は、`vmstat 1`を実行して1秒ごとに更新される統計情報を確認するとよいでしょう。これにより、リアルタイムでの変化を観察できます。

### 他のツールとの組み合わせ

`vmstat`は`top`、`iostat`、`free`などの他のモニタリングツールと組み合わせて使用すると、システムの状態をより包括的に把握できます。

## よくある質問

#### Q1. `vmstat`の出力の各列は何を意味していますか？
A. 主な列の意味は以下の通りです：
- procs: 実行中(r)および待機中(b)のプロセス数
- memory: メモリ使用状況（swpd: 仮想メモリ、free: 空きメモリ、buff: バッファ、cache: キャッシュ）
- swap: スワップイン(si)とスワップアウト(so)の速度
- io: ブロックデバイスの読み込み(bi)と書き込み(bo)の速度
- system: 割り込み(in)とコンテキストスイッチ(cs)の回数
- cpu: CPU使用率（us: ユーザー、sy: システム、id: アイドル、wa: I/O待ち）

#### Q2. `vmstat`で高いCPU使用率を検出した場合、どうすればよいですか？
A. `top`コマンドを使用して、どのプロセスがCPUを多く使用しているかを特定し、必要に応じてそのプロセスの優先度を下げるか終了させることを検討してください。

#### Q3. メモリ不足を示す兆候は何ですか？
A. 高いスワップイン/アウト値（si/so列）、低い空きメモリ（free列）、高いI/O待ち（wa列）などがメモリ不足の兆候です。

## macOSでの注意点

macOSでは`vmstat`コマンドの出力形式やオプションがLinuxとは異なります。macOSでは`vm_stat`コマンドを使用することが推奨されており、ページングの統計情報に焦点を当てています。また、同様の情報を得るために`top`や`iostat`などの代替コマンドも利用できます。

## 参考文献

https://man7.org/linux/man-pages/man8/vmstat.8.html

## 改訂履歴

- 2025/04/30 初版作成