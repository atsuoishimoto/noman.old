# perf コマンド
システムのパフォーマンスを分析し、プロファイリングするためのツール。

## 概要
`perf`はLinuxカーネルのパフォーマンス分析ツールで、CPUパフォーマンスカウンタ、トレースポイント、ソフトウェアパフォーマンスカウンタなどを使用してシステムやアプリケーションのパフォーマンスを測定します。プログラムの実行時間、キャッシュミス、ブランチ予測ミスなどの低レベルのシステム情報を収集できます。

## オプション
### **stat**
プログラムの実行中に基本的なパフォーマンス統計情報を収集します。

```console
$ perf stat ls
README.md  main.c  Makefile

 Performance counter stats for 'ls':

              2.30 msec task-clock                #    0.778 CPUs utilized          
                 0      context-switches          #    0.000 K/sec                  
                 0      cpu-migrations            #    0.000 K/sec                  
               107      page-faults               #    0.047 M/sec                  
         1,597,086      cycles                    #    0.694 GHz                    
         1,271,209      instructions              #    0.80  insn per cycle         
           262,930      branches                  #  114.230 M/sec                  
            10,493      branch-misses             #    3.99% of all branches        

       0.002956893 seconds time elapsed

       0.001953000 seconds user
       0.000000000 seconds sys
```

### **record**
パフォーマンスデータを記録し、後で分析するために保存します。

```console
$ perf record -g ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.452 MB perf.data (5621 samples) ]
```

### **report**
記録したパフォーマンスデータを分析し、結果を表示します。

```console
$ perf report
# 対話型のインターフェースが表示される
# サンプルの出力:
# Samples: 5K of event 'cycles', Event count (approx.): 2513942899
# Overhead  Command      Shared Object        Symbol
# ........  .......  .................  ..............
#   33.57%  myprogram  myprogram           [.] process_data
#   21.43%  myprogram  libc-2.31.so        [.] malloc
#   15.28%  myprogram  myprogram           [.] calculate_result
```

### **top**
リアルタイムでシステムのパフォーマンスを監視します。

```console
$ perf top
# リアルタイムで更新される対話型の画面が表示される
# サンプルの出力:
# Samples: 42K of event 'cycles', 4000 Hz, Event count (approx.): 21169767618
# Overhead  Shared Object        Symbol
# ........  .................  ..............
#   12.50%  [kernel]            [k] _raw_spin_unlock_irqrestore
#    8.32%  [kernel]            [k] finish_task_switch
#    6.43%  [kernel]            [k] native_queued_spin_lock_slowpath
```

## 使用例
### システム全体のプロファイリング
```console
$ perf record -a -g sleep 10
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 3.522 MB perf.data (16721 samples) ]
$ perf report
# 対話型のレポートが表示される
```
システム全体のアクティビティを10秒間記録し、その後分析するためのコマンドである

### 特定のプロセスのプロファイリング
```console
$ perf record -p 1234 -g -- sleep 30
[ perf record: Woken up 3 times to write data ]
[ perf record: Captured and wrote 8.124 MB perf.data (38721 samples) ]
```
PID 1234のプロセスを30秒間プロファイリングする

### メモリアクセスのプロファイリング
```console
$ perf mem record ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 2.452 MB perf.data (12621 samples) ]
$ perf mem report
# メモリアクセスに関する詳細なレポートが表示される
```

## ヒント:
### カーネルシンボルの表示
カーネルシンボルを表示するには、`linux-tools`パッケージと`linux-headers`パッケージをインストールしてください。これにより、カーネル関数の名前が表示されるようになります。

### フレームポインタの有効化
より正確なコールグラフを得るには、プログラムをコンパイルする際に`-fno-omit-frame-pointer`オプションを使用してください。これにより、`perf`がスタックトレースを正確に再構築できるようになります。

### 特権レベル
多くの`perf`コマンドは特権が必要です。一般ユーザーとして実行する場合は、`/proc/sys/kernel/perf_event_paranoid`の値を調整するか、`sudo`を使用してください。

## Frequently Asked Questions
#### Q1. `perf`はどのようなシステムで使用できますか？
A. `perf`はLinuxカーネルの一部であり、主にLinuxシステムで使用できます。他のOSでは使用できません。

#### Q2. `perf`を使用するために必要なパッケージは何ですか？
A. 多くのLinuxディストリビューションでは、`linux-tools-common`や`linux-tools-$(uname -r)`などのパッケージをインストールする必要があります。

#### Q3. `perf`で収集したデータはどのように視覚化できますか？
A. `perf report`コマンドは基本的な視覚化を提供します。より高度な視覚化には、FlameGraph、perf-toolsなどのツールを使用できます。

#### Q4. `perf`はどのくらいのオーバーヘッドがありますか？
A. `perf`のオーバーヘッドは比較的低いですが、サンプリング頻度やイベントの種類によって異なります。通常、数パーセント程度です。

## References
https://perf.wiki.kernel.org/index.php/Main_Page

## Revisions
- 2025/04/29 初版作成。