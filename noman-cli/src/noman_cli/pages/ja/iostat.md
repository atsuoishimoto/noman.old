# iostat コマンド
システムの入出力統計情報を表示します。

## 概要
iostat コマンドは、CPU 使用率、デバイスの入出力統計、およびパーティションの使用状況を監視するためのツールです。システム管理者やパフォーマンス分析者がディスクの I/O パフォーマンスを評価するのに役立ちます。

## オプション
### **-c**
CPU 統計情報のみを表示します。
```console
$ iostat -c
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.33    0.00   95.00
```

### **-d**
デバイスの統計情報のみを表示します。
```console
$ iostat -d
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.67       112.73        45.12    9876543    3456789
sdb               0.23         5.67         0.00     123456          0
```

### **-x**
拡張統計情報を表示します。より詳細なディスク使用状況が確認できます。
```console
$ iostat -x
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.33    0.00   95.00

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              3.45    2.22    112.73     45.12     0.00     1.12   0.00  33.53    0.28    2.30   0.01    32.68    20.32   0.20   0.11
sdb              0.23    0.00      5.67      0.00     0.00     0.00   0.00   0.00    0.35    0.00   0.00    24.65     0.00   0.22   0.01
```

### **-k**
キロバイト単位で統計を表示します。
```console
$ iostat -k
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.33    0.00   95.00

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.67       112.73        45.12    9876543    3456789
sdb               0.23         5.67         0.00     123456          0
```

### **-m**
メガバイト単位で統計を表示します。
```console
$ iostat -m
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.33    0.00   95.00

Device             tps    MB_read/s    MB_wrtn/s    MB_read    MB_wrtn
sda               5.67         0.11         0.04       9643       3375
sdb               0.23         0.01         0.00        120          0
```

### **-p**
パーティション単位の統計情報を表示します。
```console
$ iostat -p ALL
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.33    0.00   95.00

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.67       112.73        45.12    9876543    3456789
sda1              4.32        98.45        45.12    8654321    3456789
sda2              1.35        14.28         0.00    1222222          0
sdb               0.23         5.67         0.00     123456          0
```

## 使用例
### 定期的な統計情報の更新
```console
$ iostat 2 5
# 2秒間隔で5回統計情報を表示する
```

### CPU とディスク情報を同時に表示
```console
$ iostat -cd
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.33    0.00   95.00

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.67       112.73        45.12    9876543    3456789
sdb               0.23         5.67         0.00     123456          0
```

### 特定のデバイスの詳細情報を表示
```console
$ iostat -xd /dev/sda
Linux 5.15.0-91-generic (hostname)  2025年04月29日  _x86_64_  (8 CPU)

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              3.45    2.22    112.73     45.12     0.00     1.12   0.00  33.53    0.28    2.30   0.01    32.68    20.32   0.20   0.11
```

## ヒント:
### I/O 問題の診断
%iowait の値が高い場合（10%以上）、ディスク I/O がボトルネックになっている可能性があります。iostat -x を使用して詳細な分析を行いましょう。

### 定期的なモニタリング
`iostat 5` のように間隔を指定すると、5秒ごとに統計情報が更新されます。これにより、時間経過に伴う変化を観察できます。

### 人間が読みやすい形式での表示
`iostat -h` または `iostat -m` を使用すると、サイズがキロバイトやメガバイト単位で表示され、大きな数値を理解しやすくなります。

## よくある質問
#### Q1. iostat と vmstat の違いは何ですか？
A. iostat はディスク I/O に特化しており、より詳細なディスク統計を提供します。vmstat はメモリ、プロセス、ページング、ブロック I/O、CPU 活動など、より広範なシステム情報を表示します。

#### Q2. iostat の出力で最も重要な指標は何ですか？
A. %util（デバイス使用率）、r_await/w_await（読み書き待ち時間）、tps（1秒あたりの転送数）が重要です。%util が高い場合はディスクがボトルネックになっている可能性があります。

#### Q3. iostat の最初の出力と後続の出力の違いは何ですか？
A. 最初の出力はシステム起動時からの累積統計を示し、後続の出力は指定した間隔での統計を示します。そのため、パフォーマンス分析には通常、2回目以降の出力を参照します。

## macOS での注意点
macOS では iostat コマンドの出力形式と利用可能なオプションが Linux と異なります。macOS では主に `-w`（待機時間を指定）と `-c`（CPU 情報を含める）オプションが使用されます。また、拡張統計（-x）は利用できません。

## 参考資料
https://man7.org/linux/man-pages/man1/iostat.1.html

## 改訂履歴
- 2025/04/29 初版作成