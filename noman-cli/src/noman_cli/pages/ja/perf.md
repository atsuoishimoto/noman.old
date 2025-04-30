# perf コマンド

システムのパフォーマンスを分析し、プロファイリングするためのツール。

## 概要

`perf`はLinuxカーネルのパフォーマンス分析ツールで、CPUパフォーマンスカウンタ、トレースポイント、ソフトウェアパフォーマンスカウンタなどを使用してシステムやアプリケーションのパフォーマンスを測定します。プロセッサのキャッシュミス、分岐予測ミス、メモリアクセスパターンなどの低レベルの情報から、高レベルのアプリケーションの動作まで幅広く分析できます。

## オプション

### **stat**

プログラムの実行中に基本的なパフォーマンス統計情報を収集します。

```console
$ perf stat ls
README.md  example.c  test.py

 Performance counter stats for 'ls':

              0.57 msec task-clock                #    0.783 CPUs utilized          
                 0      context-switches          #    0.000 K/sec                  
                 0      cpu-migrations            #    0.000 K/sec                  
                53      page-faults               #    0.093 M/sec                  
           1,597,086      cycles                  #    2.802 GHz                    
           1,235,435      instructions            #    0.77  insn per cycle         
             245,128      branches                #  430.048 M/sec                  
               5,843      branch-misses           #    2.38% of all branches        

       0.000728500 seconds time elapsed

       0.000000000 seconds user
       0.000000000 seconds sys
```

### **record**

パフォーマンスデータを記録し、後で分析するために保存します。

```console
$ perf record -g ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.064 MB perf.data (1210 samples) ]
```

### **report**

記録したパフォーマンスデータを分析し、レポートを表示します。

```console
$ perf report
# 対話型のインターフェースが表示される
# サンプルの出力:
# Samples: 1K of event 'cycles', Event count (approx.): 1210
# Overhead  Command      Shared Object        Symbol
# ........  ...........  ...................  .......................
#   33.21%  myprogram    myprogram            [.] process_data
#   21.56%  myprogram    libc-2.31.so         [.] malloc
#   15.87%  myprogram    myprogram            [.] calculate_result
```

### **top**

リアルタイムでシステムのパフォーマンスを監視します。

```console
$ perf top
# リアルタイムのパフォーマンスモニタリング画面が表示される
# CPUサイクルを最も消費している関数が上位に表示される
```

## 使用例

### 特定のプログラムのプロファイリング

```console
$ perf stat -d ./myprogram
# -d オプションで詳細な統計情報が表示される
```

### コールグラフの記録と表示

```console
$ perf record -g ./myprogram
$ perf report --call-graph
# 関数呼び出しのツリーが表示され、どの関数がどれだけの時間を消費しているかが分かる
```

### 特定のイベントの測定

```console
$ perf stat -e cache-misses,cache-references ./myprogram
# キャッシュミスとキャッシュ参照の回数を測定する
```

## ヒント:

### カーネルシンボルの表示

カーネル関数のシンボル情報を表示するには、root権限が必要です。`sudo perf`を使用するか、`/proc/sys/kernel/perf_event_paranoid`の値を調整してください。

### フレームポインタの有効化

より正確なコールグラフを得るには、プログラムをコンパイルする際に`-fno-omit-frame-pointer`オプションを使用してフレームポインタを保持するようにしてください。

### パフォーマンス低下の最小化

`perf`自体がシステムに与える影響を最小限に抑えるために、サンプリング頻度を調整できます。例えば、`-F 99`オプションで99Hzのサンプリングレートを指定できます。

## よくある質問

#### Q1. perfを使うために特別な権限が必要ですか？
A. はい、多くのperfの機能はroot権限または特定のカーネル設定が必要です。一般ユーザーでも使える機能は限られています。

#### Q2. perfはどのようなシステムで使えますか？
A. perfはLinuxカーネル2.6.31以降で利用可能です。ただし、すべての機能を使うには、より新しいカーネルバージョンが必要な場合があります。

#### Q3. perfのデータファイルはどのくらいのサイズになりますか？
A. 記録する時間やイベントの種類によって大きく異なりますが、長時間の記録では数百MBから数GBになることもあります。`--freq`オプションでサンプリング頻度を下げることでサイズを制御できます。

#### Q4. macOSでperfは使えますか？
A. いいえ、perfはLinux固有のツールです。macOSでは代わりに`Instruments`や`DTrace`などのツールが利用可能です。

## 参考文献

https://perf.wiki.kernel.org/index.php/Main_Page

## Revisions

- 2025/04/30 First revision