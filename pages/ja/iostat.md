# iostat コマンド

CPUおよびデバイスとパーティションの入出力統計情報を表示します。

## 概要

`iostat` はCPU統計情報とデバイス、パーティション、ネットワークファイルシステムの入出力統計情報を報告します。システムパフォーマンスの監視、ボトルネックの特定、ディスクI/Oパターンの分析に特に役立ちます。このコマンドはCPUとディスクの使用状況を示し、システム管理者がパフォーマンスの問題を診断するのに役立ちます。

## オプション

### **-c**

CPU統計情報のみを表示します。

```console
$ iostat -c
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98
```

### **-d**

デバイス統計情報のみを表示します。

```console
$ iostat -d
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sdb               0.12         3.45         0.00      30567          0
```

### **-h, --human**

サイズを人間が読みやすい形式で表示します（例：1.0k、234M、2G）。

```console
$ iostat -h
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda              5.73       141.0k       124.5k      1.2G      1.1G
sdb              0.12         3.5k         0.0k     30.6M      0.0k
```

### **-k**

統計情報を1秒あたりのキロバイト単位で表示します。

```console
$ iostat -k
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sdb               0.12         3.45         0.00      30567          0
```

### **-m**

統計情報を1秒あたりのメガバイト単位で表示します。

```console
$ iostat -m
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    MB_read/s    MB_wrtn/s    MB_read    MB_wrtn
sda               5.73         0.14         0.12      1221.1    1078.7
sdb               0.12         0.00         0.00        29.8       0.0
```

### **-x**

拡張統計情報を表示し、デバイス使用状況についてより詳細な情報を提供します。

```console
$ iostat -x
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              3.45    2.28    141.02    124.53     0.12     1.35   3.36  37.25    0.42    2.53   0.01    40.88    54.62   0.25   1.43
sdb              0.12    0.00      3.45      0.00     0.00     0.00   0.00   0.00    0.35    0.00   0.00    28.75     0.00   0.22   0.03
```

### **-p [device]**

システムで使用されているブロックデバイスとそのすべてのパーティションの統計情報を表示します。

```console
$ iostat -p sda
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sda1              0.25         4.32        12.45      38291     110456
sda2              5.48       136.70       112.08    1212141     994111
```

### **interval [count]**

レポート間の間隔（秒単位）と生成するレポートの数を指定します。

```console
$ iostat 2 3
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sdb               0.12         3.45         0.00      30567          0

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.42    0.00    1.56    0.28    0.00   94.74

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               6.50       152.50       138.00         305         276
sdb               0.00         0.00         0.00           0           0

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.36    0.00    1.48    0.32    0.00   94.84

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.50       132.00       118.50         264         237
sdb               0.50         8.00         0.00          16           0
```

## 使用例

### 拡張統計情報によるディスクI/Oの監視

```console
$ iostat -xd 2
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              3.45    2.28    141.02    124.53     0.12     1.35   3.36  37.25    0.42    2.53   0.01    40.88    54.62   0.25   1.43
sdb              0.12    0.00      3.45      0.00     0.00     0.00   0.00   0.00    0.35    0.00   0.00    28.75     0.00   0.22   0.03

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              4.00    3.50    164.00    156.00     0.00     2.00   0.00  36.36    0.38    2.43   0.01    41.00    44.57   0.27   2.01
sdb              0.00    0.00      0.00      0.00     0.00     0.00   0.00   0.00    0.00    0.00   0.00     0.00     0.00   0.00   0.00
```

### 人間が読みやすい形式でのディスク統計情報の表示

```console
$ iostat -dh
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda              5.73       141.0k       124.5k      1.2G      1.1G
sdb              0.12         3.5k         0.0k     30.6M      0.0k
```

### 特定のパーティションの監視

```console
$ iostat -p sda 5
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sda1              0.25         4.32        12.45      38291     110456
sda2              5.48       136.70       112.08    1212141     994111

# 出力は中断されるまで5秒ごとに繰り返されます
```

## ヒント:

### I/Oボトルネックの特定

拡張統計情報（`-x`オプション）の`%util`列を確認して、使用率が100%に近づいているディスクを特定します。これはボトルネックの可能性を示しています。

### I/O待ち時間の監視

`r_await`と`w_await`列の値が高い場合、プロセスがI/O操作の完了を待っていることを示し、システムの速度低下の原因となっている可能性があります。

### 継続的な監視

間隔パラメータを使用してディスクアクティビティを継続的に監視します。例えば、`iostat 5`は5秒ごとに統計情報を更新します。

### 他のツールとの組み合わせ

システムパフォーマンスの包括的な視点を得るために、`iostat`を`top`、`vmstat`、`sar`などの他の監視ツールと組み合わせて使用します。

### アクティブなデバイスに焦点を当てる

パフォーマンスの問題をトラブルシューティングする際は、トランザクション率（tps）が高く、使用率の割合が高いデバイスに焦点を当てます。

## よくある質問

#### Q1. CPU統計情報の%iowaitの値は何を意味しますか？
A. %iowaitは、システムにディスクI/O要求が保留中であった間にCPUがアイドル状態だった時間の割合を表します。iowait値が高いことは、システムがディスク操作によってボトルネックになっていることを示しています。

#### Q2. iostat -xからの拡張統計情報をどのように解釈すればよいですか？
A. 重要な指標には、%util（デバイス使用率）、r_await/w_await（読み取り/書き込み応答時間）、aqu-sz（平均キュー長）があります。高い使用率（>80%）、長い待ち時間、または大きなキューサイズは、潜在的なI/O問題を示しています。

#### Q3. tps、r/s、w/sの違いは何ですか？
A. tps（1秒あたりの転送数）は1秒あたりのI/O要求の総数です。r/sとw/sはこれを読み取り要求と書き込み要求に分解したものです。

#### Q4. iostatでNVMeドライブを監視するにはどうすればよいですか？
A. NVMeドライブはnvme0n1、nvme1n1などとして表示されます。同じiostatコマンドを使用できます。例：`iostat -x nvme0n1`

#### Q5. なぜiostatの値が実行ごとに異なるのですか？
A. iostatの最初のレポートはシステム起動以降の統計情報を示しますが、その後のレポート（間隔を使用する場合）は指定された時間間隔のみの統計情報を示します。

## 参考資料

https://man7.org/linux/man-pages/man1/iostat.1.html

## 改訂履歴

- 2025/05/04 初回改訂