# vmstat コマンド
システムの仮想メモリ統計情報を表示します。

## 概要
`vmstat`（Virtual Memory Statistics）は、システムのメモリ、プロセス、CPU、I/O、スワップなどのリソース使用状況に関する統計情報を提供するコマンドです。システム管理者やデバッグ時に、パフォーマンスの問題を特定するのに役立ちます。

## オプション
### **-S**
メモリ表示単位を指定します（k: キロバイト、m: メガバイト、g: ギガバイト）。
```console
$ vmstat -Sm
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0   1892    180   2340    0    0     3     5   36   79  1  1 98  0  0
```

### **-a**
アクティブ/非アクティブメモリの詳細を表示します。
```console
$ vmstat -a
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free  inact active   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1937584 1282144 2397952    0    0     3     5   36   79  1  1 98  0  0
```

### **-d**
ディスク統計情報を表示します。
```console
$ vmstat -d
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12345   3456  123456   12345  56789   7890  567890   56789      0     12
```

### **間隔と回数**
更新間隔（秒）と表示回数を指定できます。
```console
$ vmstat 2 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1937584  184320 2397952    0    0     3     5   36   79  1  1 98  0  0
 0  0      0 1937584  184320 2397952    0    0     0     0  214  412  1  0 99  0  0
 0  0      0 1937584  184320 2397952    0    0     0     0  211  398  0  1 99  0  0
 0  0      0 1937584  184320 2397952    0    0     0     0  209  401  1  0 99  0  0
 0  0      0 1937584  184320 2397952    0    0     0     0  215  405  0  1 99  0  0
```

## 使用例
### 基本的な使用法
```console
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1937584  184320 2397952    0    0     3     5   36   79  1  1 98  0  0
```

### 5秒間隔で継続的に監視
```console
$ vmstat 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1937584  184320 2397952    0    0     3     5   36   79  1  1 98  0  0
 0  0      0 1937584  184320 2397952    0    0     0     0  214  412  1  0 99  0  0
 0  0      0 1937584  184320 2397952    0    0     0     0  211  398  0  1 99  0  0
...
```

### 詳細なメモリ情報の表示
```console
$ vmstat -s
      8169348 K total memory
      2397952 K used memory
      3489712 K active memory
      1282144 K inactive memory
      1937584 K free memory
       184320 K buffer memory
      3649492 K swap cache
      8289276 K total swap
            0 K used swap
      8289276 K free swap
...
```

## ヒント:
### 出力の見方
- **procs**: r（実行待ちプロセス数）、b（割り込み不可能なスリープ状態のプロセス数）
- **memory**: swpd（仮想メモリ使用量）、free（空きメモリ）、buff（バッファ）、cache（キャッシュ）
- **swap**: si（スワップイン）、so（スワップアウト）
- **io**: bi（ブロック入力）、bo（ブロック出力）
- **system**: in（割り込み）、cs（コンテキストスイッチ）
- **cpu**: us（ユーザー時間）、sy（システム時間）、id（アイドル時間）、wa（I/O待ち時間）、st（仮想マシンに奪われた時間）

### 高負荷の兆候
- r値が常に高い場合はCPUバウンドの問題
- si/soの値が継続的に高い場合はメモリ不足の兆候
- wa値が高い場合はI/Oバウンドの問題

### 最初の行は平均値
vmstatを実行すると、最初の行はシステム起動からの平均値であるため、現在の状態を把握するには2行目以降を見るのが良いでしょう。

## よくある質問
#### Q1. vmstatの出力で最も重要な指標は何ですか？
A. 状況によって異なりますが、一般的にはr（実行待ちプロセス数）、free（空きメモリ）、si/so（スワップイン/アウト）、us/sy/wa（CPU使用率）が重要です。

#### Q2. vmstatの更新間隔はどのように設定しますか？
A. `vmstat [間隔(秒)]` のように指定します。例えば `vmstat 5` は5秒ごとに更新します。

#### Q3. 特定のディスクのI/O統計情報だけを見るにはどうすればよいですか？
A. `vmstat -d` でディスク統計を表示し、必要に応じて `grep` と組み合わせて特定のディスクをフィルタリングします。例: `vmstat -d | grep sda`

#### Q4. macOSでvmstatを使用する際の注意点はありますか？
A. macOSでは`vmstat`コマンドの出力形式やオプションがLinuxと異なります。代わりに`vm_stat`コマンドを使用するか、より詳細な情報を得るために`top`や`iostat`などの代替コマンドを検討してください。

## 参考資料
https://man7.org/linux/man-pages/man8/vmstat.8.html

## 改訂履歴
- 2025/04/29 初版作成