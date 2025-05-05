# vmstat コマンド

仮想メモリの統計情報を表示し、システムのプロセス、メモリ、ページング、ブロックI/O、トラップ、およびCPUアクティビティに関する情報を提供します。

## 概要

`vmstat`（仮想メモリ統計）は、システムメモリ、プロセス、割り込み、ページング、ブロックI/O、およびCPU使用率に関する情報を表示します。システムパフォーマンスの監視やボトルネックの特定に特に役立ちます。このコマンドは、現在のシステム状態のスナップショットを提供したり、指定した間隔で継続的な監視を行ったりすることができます。

## オプション

### **-a, --active**

アクティブおよび非アクティブメモリを表示します

```console
$ vmstat -a
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free  inact active   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 6291456 1048576 2097152    0    0     0     2    9   10  1  1 98  0  0
```

### **-d, --disk**

ディスク統計情報を報告します

```console
$ vmstat -d
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15748  23182  313544   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0
```

### **-s, --stats**

様々なイベントカウンターとメモリ統計の表を表示します

```console
$ vmstat -s
      8167848 K total memory
      1872016 K used memory
      1224268 K active memory
       525148 K inactive memory
      6295832 K free memory
       226748 K buffer memory
      1654304 K swap cache
      8388604 K total swap
            0 K used swap
      8388604 K free swap
        24818 non-nice user cpu ticks
          226 nice user cpu ticks
        18911 system cpu ticks
      2137707 idle cpu ticks
         2660 IO-wait cpu ticks
            0 IRQ cpu ticks
         1367 softirq cpu ticks
            0 stolen cpu ticks
       772844 pages paged in
      1492454 pages paged out
            0 pages swapped in
            0 pages swapped out
      2838484 interrupts
      6547301 CPU context switches
   1588876743 boot time
        16793 forks
```

### **-t, --timestamp**

各行にタイムスタンプを追加します

```console
$ vmstat -t 1 3
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu----- -----timestamp-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st                 EDT
 0  0      0 6295832 226748 1654304    0    0     0     2    9   10  1  1 98  0  0 2025-05-04 10:15:01
 0  0      0 6295832 226748 1654304    0    0     0     0  104  168  0  0 100  0  0 2025-05-04 10:15:02
 0  0      0 6295832 226748 1654304    0    0     0     0  104  167  0  0 100  0  0 2025-05-04 10:15:03
```

### **-S, --unit [k|K|m|M]**

出力を1000（k）、1024（K）、1000000（m）、または1048576（M）バイト間で切り替えます

```console
$ vmstat -S M
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0   6002    216   1578    0    0     0     2    9   10  1  1 98  0  0
```

## 使用例

### 間隔とカウントを指定した基本的な使用法

```console
$ vmstat 2 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 6295832 226748 1654304    0    0     0     2    9   10  1  1 98  0  0
 0  0      0 6295832 226748 1654304    0    0     0     0  104  168  0  0 100  0  0
 0  0      0 6295832 226748 1654304    0    0     0     0  103  166  0  0 100  0  0
 0  0      0 6295832 226748 1654304    0    0     0     0  105  169  0  0 100  0  0
 0  0      0 6295832 226748 1654304    0    0     0    12  106  171  0  0 100  0  0
```

### ディスクアクティビティの監視

```console
$ vmstat -d 1 3
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15748  23182  313544   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0

disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15748  23182  313544   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0

disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15749  23182  313552   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0
```

### メモリ統計の表示

```console
$ vmstat -s | grep memory
      8167848 K total memory
      1872016 K used memory
      1224268 K active memory
       525148 K inactive memory
      6295832 K free memory
       226748 K buffer memory
```

## ヒント:

### 出力フィールドの理解

- **procs**: 'r'は実行可能なプロセス（実行中または実行時間待ち）、'b'は割り込み不可能なスリープ状態のプロセスを示します
- **memory**: 'swpd'は使用中の仮想メモリ、'free'はアイドル状態のメモリ、'buff'はバッファとして使用されるメモリ、'cache'はキャッシュとして使用されるメモリです
- **swap**: 'si'はディスクからスワップインされたメモリ、'so'はディスクにスワップアウトされたメモリです
- **io**: 'bi'はブロックデバイスから受信したブロック、'bo'はブロックデバイスに送信したブロックです
- **system**: 'in'は1秒あたりの割り込み数、'cs'は1秒あたりのコンテキストスイッチ数です
- **cpu**: ユーザーモード('us')、システムモード('sy')、アイドル('id')、I/O待ち('wa')、仮想マシンから盗まれた('st')の合計CPU時間の割合です

### 最初の行と後続の行の違い

出力の最初の行は前回の再起動以降の平均値を示し、後続の行はサンプリング期間の情報を示します。現在の統計情報については、常に2行目以降を見るようにしましょう。

### メモリのボトルネックの特定

'si'と'so'の値が高い場合は、過剰なスワッピングを示しており、システムにより多くのRAMが必要か、メモリ使用量の最適化が必要であることを示唆しています。

### I/O問題の検出

CPU部分の'wa'（I/O待ち）の割合が高い場合は、システムがディスク操作の完了を待つのに多くの時間を費やしていることを示しています。

## よくある質問

#### Q1. vmstat出力の'r'列は何を意味していますか？
A. 'r'列は実行時間を待っているプロセスの数を示します。高い数値（CPUコア数より大きい）はCPUの競合を示しています。

#### Q2. vmstatでメモリ使用量を監視するにはどうすればよいですか？
A. 詳細なメモリ統計を見るには`vmstat -s`を使用するか、アクティブ/非アクティブメモリを見るには`vmstat -a`を使用します。継続的な監視には、間隔を追加します：`vmstat 5`。

#### Q3. バッファメモリとキャッシュメモリの違いは何ですか？
A. バッファメモリ（'buff'）はディスクブロック操作に使用され、キャッシュメモリ（'cache'）はファイルシステムデータに使用されます。どちらもアプリケーションがメモリを必要とするときに再利用できます。

#### Q4. 高い'wa'（I/O待ち）値をどう解釈すればよいですか？
A. I/O待ち時間の割合が高い（10％以上）場合、CPUがディスク操作の完了を待っていることを示します。これは、より高速なストレージやI/Oの最適化で解決できるディスクI/Oのボトルネックを示唆しています。

## 参考文献

https://man7.org/linux/man-pages/man8/vmstat.8.html

## 改訂履歴

- 2025/05/04 初回改訂