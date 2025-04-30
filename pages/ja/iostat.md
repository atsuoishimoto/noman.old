# iostat コマンド

システムの入出力（I/O）統計情報を表示します。

## 概要

`iostat`コマンドは、CPU使用率やデバイス（ディスク）の入出力統計情報をモニタリングするためのツールです。システム管理者やパフォーマンス分析を行う際に、ディスクのボトルネックを特定したり、システムの全体的なI/Oパフォーマンスを評価したりするのに役立ちます。

## オプション

### **-c**

CPU統計情報のみを表示します。

```console
$ iostat -c
Linux 5.15.0-91-generic (hostname)  2025年04月30日  _x86_64_  (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.75    0.25    0.00   94.75
```

### **-d**

デバイス（ディスク）統計情報のみを表示します。

```console
$ iostat -d
Linux 5.15.0-91-generic (hostname)  2025年04月30日  _x86_64_  (4 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.67       112.50        45.67    1024568     415672
sdb               0.12         1.23         0.00      11200          0
```

### **-x**

拡張統計情報を表示します。より詳細なディスクI/O情報が得られます。

```console
$ iostat -x
Linux 5.15.0-91-generic (hostname)  2025年04月30日  _x86_64_  (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.75    0.25    0.00   94.75

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              4.50    1.17    112.50     45.67     0.00     0.33   0.00  22.22    0.27    2.05   0.01    25.00    39.00   0.25   1.42
sdb              0.12    0.00      1.23      0.00     0.00     0.00   0.00   0.00    0.42    0.00   0.00    10.25     0.00   0.33   0.00
```

### **-p**

特定のデバイスのパーティション統計情報を表示します。

```console
$ iostat -p sda
Linux 5.15.0-91-generic (hostname)  2025年04月30日  _x86_64_  (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.75    0.25    0.00   94.75

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.67       112.50        45.67    1024568     415672
sda1              4.83        98.33        45.67     895432     415672
sda2              0.83        14.17         0.00     129136          0
```

### **-k/-m**

キロバイト（-k）またはメガバイト（-m）単位で統計情報を表示します。

```console
$ iostat -m
Linux 5.15.0-91-generic (hostname)  2025年04月30日  _x86_64_  (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.75    0.25    0.00   94.75

Device             tps    MB_read/s    MB_wrtn/s    MB_read    MB_wrtn
sda               5.67         0.11         0.04      1000        406
sdb               0.12         0.00         0.00        11          0
```

## 使用例

### 継続的なモニタリング（2秒間隔で5回）

```console
$ iostat 2 5
Linux 5.15.0-91-generic (hostname)  2025年04月30日  _x86_64_  (4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.75    0.25    0.00   94.75

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.67       112.50        45.67    1024568     415672
sdb               0.12         1.23         0.00      11200          0

# 2秒後に再度統計情報が表示され、これが合計5回繰り返される
```

### 特定のディスクの詳細情報を表示

```console
$ iostat -xd sda
Linux 5.15.0-91-generic (hostname)  2025年04月30日  _x86_64_  (4 CPU)

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              4.50    1.17    112.50     45.67     0.00     0.33   0.00  22.22    0.27    2.05   0.01    25.00    39.00   0.25   1.42
```

## ヒント:

### 高い%iowait値に注意する

CPU統計で%iowait値が高い場合（10%以上）、ディスクI/Oがシステムのボトルネックになっている可能性があります。

### %util値でディスク使用率を確認

`iostat -x`の%util列は、デバイスの使用率を示します。この値が常に90%以上の場合、そのディスクが飽和状態になっている可能性があります。

### 定期的なモニタリングの設定

`iostat 5`のように間隔を指定すると、5秒ごとに統計情報が更新されます。これにより、時間経過に伴う変化を観察できます。

### NVMe対応

最新のLinuxディストリビューションでは、NVMeデバイスの統計情報も表示できます。デバイス名は通常`nvme0n1`のような形式です。

## よくある質問

#### Q1. iostatとvmstatの違いは何ですか？
A. `iostat`はディスクI/O統計に特化しているのに対し、`vmstat`はメモリ、プロセス、ページング、ブロックI/O、トラップ、CPUアクティビティなど、より広範なシステム統計を提供します。

#### Q2. iostatの出力にある「tps」とは何ですか？
A. tps（Transfers Per Second）は、1秒あたりのI/O要求数を表します。これはディスクへの読み書き操作の頻度を示します。

#### Q3. r_awaitとw_awaitの意味は何ですか？
A. `r_await`は読み取り要求の平均応答時間（ミリ秒）、`w_await`は書き込み要求の平均応答時間を示します。これらの値が高いと、ディスクの応答が遅いことを意味します。

#### Q4. macOSでiostatを使用する際の注意点はありますか？
A. macOSのiostatはLinux版と異なるオプションと出力形式を持っています。例えば、`-x`オプションはなく、代わりに`-d`や`-I`などのオプションがあります。また、出力の列名や意味も異なるため、macOS固有のマニュアルを参照することをお勧めします。

## 参考資料

https://man7.org/linux/man-pages/man1/iostat.1.html

## 改訂履歴

- 2025/04/30 初版作成