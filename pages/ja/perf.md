# perf コマンド

Linuxのパフォーマンス分析ツールで、ハードウェアカウンタ統計やトレース機能を提供します。

## 概要

`perf`は、強力なLinuxプロファイリングおよびパフォーマンス分析ツールです。CPUのパフォーマンスモニタリングハードウェアカウンタにアクセスして、プログラム実行に関する統計情報を収集します。最小限のオーバーヘッドでCPUパフォーマンスイベントのモニタリング、システムコールのトレース、アプリケーションパフォーマンスの分析が可能です。Linuxカーネルツールの一部である`perf`は、開発者がボトルネックを特定し、コードを最適化するのに役立ちます。

## オプション

### **-e, --event**

カウントまたはサンプリングするパフォーマンスイベントを指定します

```console
$ perf stat -e cycles,instructions ./myprogram
 Performance counter stats for './myprogram':

       1,234,567      cycles
       2,345,678      instructions             #    1.90  insn per cycle
       
       0.123456789 seconds time elapsed
```

### **-p, --pid**

プロセスIDによる既存プロセスのプロファイリング

```console
$ perf record -p 1234 -g
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.452 MB perf.data (5093 samples) ]
```

### **-a, --all-cpus**

すべてのCPUのシステム全体のモニタリング

```console
$ perf stat -a sleep 5
 Performance counter stats for 'system wide':

       12,345,678      cpu-cycles           
        5,678,901      instructions              #    0.46  insn per cycle
          123,456      cache-misses

       5.000621884 seconds time elapsed
```

### **-g, --call-graph**

コールグラフ（スタックチェーン/バックトレース）の記録を有効にします

```console
$ perf record -g ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.452 MB perf.data (5093 samples) ]
```

## 使用例

### 基本的なCPU統計情報

```console
$ perf stat ./myprogram
 Performance counter stats for './myprogram':

          0.086283      task-clock (msec)         #    0.733 CPUs utilized
                 2      context-switches          #    0.023 M/sec
                 0      cpu-migrations            #    0.000 K/sec
               108      page-faults               #    0.001 M/sec
           235,538      cycles                    #    2.731 GHz
           580,716      instructions              #    2.47  insn per cycle
           116,931      branches                  #    1.356 M/sec
             3,468      branch-misses             #    2.97% of all branches

       0.117743392 seconds time elapsed
```

### パフォーマンスデータの記録と分析

```console
$ perf record -g ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.452 MB perf.data (5093 samples) ]

$ perf report
# Samples: 5K of event 'cycles'
# Event count (approx.): 2345678901
#
# Overhead  Command      Shared Object        Symbol
# ........  .......  .................  ..............
#
    14.59%  myprogram  myprogram           [.] process_data
    10.21%  myprogram  myprogram           [.] calculate_result
     8.45%  myprogram  libc-2.31.so        [.] malloc
```

### システムコールのトレース

```console
$ perf trace -p 1234
     0.000 ( 0.000 ms): myprogram/1234 write(fd: 1, buf: 0x7f9876543210, count: 16) = 16
     0.223 ( 0.019 ms): myprogram/1234 read(fd: 0, buf: 0x7f9876543210, count: 1024) = 64
     0.415 ( 0.021 ms): myprogram/1234 open(filename: 0x7f9876543210, flags: RDONLY) = 3
```

## ヒント:

### フレームグラフを使用した可視化

FlameGraphのようなツールを使用してperfデータをフレームグラフに変換し、コールスタックを視覚化してコード内のホットスポットを素早く特定できます。

```console
$ perf record -g -F 99 ./myprogram
$ perf script | ./FlameGraph/stackcollapse-perf.pl | ./FlameGraph/flamegraph.pl > profile.svg
```

### 特定のイベントに焦点を当てる

すべてのイベントを収集するのではなく、特定のパフォーマンス問題を診断するためにcache-missesやbranch-missesなどの特定のイベントに焦点を当てます。

```console
$ perf stat -e cache-misses,branch-misses ./myprogram
```

### サンプリングによるオーバーヘッドの削減

本番環境では、頻度を指定してサンプリングを使用することでオーバーヘッドを削減できます：

```console
$ perf record -F 99 -g ./myprogram
```

## よくある質問

#### Q1. `perf stat`と`perf record`の違いは何ですか？
A. `perf stat`はパフォーマンスカウンタの概要を提供し、`perf record`は後で`perf report`で分析するための詳細なサンプルをキャプチャします。

#### Q2. 実行中のアプリケーションをプロファイリングするにはどうすればよいですか？
A. `perf record -p PID`を使用します。PIDは実行中のアプリケーションのプロセスIDです。

#### Q3. 仮想マシンでperfを使用できますか？
A. はい、ただし制限があります。仮想化環境では一部のハードウェアカウンタが利用できなかったり、正確でなかったりする場合があります。

#### Q4. どの関数がCPUを最も使用しているかを確認するにはどうすればよいですか？
A. リアルタイムの関数モニタリングには`perf top`を使用するか、詳細な分析には`perf record`の後に`perf report`を使用します。

#### Q5. perfはすべてのLinuxディストリビューションで動作しますか？
A. ほとんどの最新ディストリビューションはperfをサポートしていますが、機能はカーネルバージョンと構成によって異なる場合があります。

## 参考文献

https://perf.wiki.kernel.org/index.php/Main_Page

## 改訂履歴

- 2025/05/04 初版作成