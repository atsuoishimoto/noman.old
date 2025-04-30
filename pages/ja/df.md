# df コマンド

ファイルシステムのディスク容量使用状況を表示します。

## 概要

`df`コマンドは、システム上のファイルシステムの空き容量と使用済み容量を表示します。マウントされているすべてのファイルシステムについて、合計サイズ、使用済み容量、空き容量、使用率などの情報を提供します。ディスク容量の管理や監視に役立ちます。

## オプション

### **-h (human-readable)**

サイズを人間が読みやすい形式（KB、MB、GBなど）で表示します。

```console
$ df -h
Filesystem      Size   Used  Avail Capacity   iused    ifree %iused  Mounted on
/dev/disk1s1s1  466Gi   15Gi  301Gi     5%   488120 4881963880    0%   /
/dev/disk1s2    466Gi  3.0Gi  301Gi     1%        3 4882452000    0%   /System/Volumes/Preboot
/dev/disk1s4    466Gi   20Ki  301Gi     1%       25 4882451978    0%   /System/Volumes/VM
/dev/disk1s5    466Gi  146Gi  301Gi    33%  1835127 4880616873    0%   /System/Volumes/Data
```

### **-T (file-system-type)**

各ファイルシステムのタイプも表示します。

```console
$ df -T
Filesystem     Type     1K-blocks      Used Available Use% Mounted on
/dev/sda1      ext4      41251136  12503812  26530604  33% /
tmpfs          tmpfs      1021880         0   1021880   0% /dev/shm
/dev/sdb1      ext4     103081248  67128932  30520632  69% /home
```

### **-i (inodes)**

ファイルシステムのiノード情報（使用済み、空き、使用率）を表示します。

```console
$ df -i
Filesystem      Inodes  IUsed    IFree IUse% Mounted on
/dev/sda1      2621440 254871  2366569   10% /
tmpfs           255470      1   255469    1% /dev/shm
/dev/sdb1      6553600 421892  6131708    7% /home
```

## 使用例

### 特定のディレクトリのファイルシステム情報を表示

```console
$ df -h /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb1        99G   64G   30G  69% /home
```

### 人間が読みやすい形式でファイルシステムタイプも表示

```console
$ df -hT
Filesystem     Type      Size  Used Avail Use% Mounted on
/dev/sda1      ext4       40G   12G   26G  33% /
tmpfs          tmpfs     999M     0  999M   0% /dev/shm
/dev/sdb1      ext4       99G   64G   30G  69% /home
```

### 特定のファイルシステムタイプのみ表示

```console
$ df -ht ext4
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        40G   12G   26G  33% /
/dev/sdb1        99G   64G   30G  69% /home
```

## ヒント:

### 容量の単位を理解する

`df`コマンドのデフォルト出力は1KBブロック単位です。`-h`オプションを使用すると、KB、MB、GBなどの単位で表示されるため、容量を直感的に把握できます。

### 使用率の監視

ファイルシステムの使用率が90%を超えると、パフォーマンスの低下や問題が発生する可能性があります。定期的に`df -h`を実行して、使用率を監視することをお勧めします。

### ローカルファイルシステムのみ表示

`-l`オプションを使用すると、ローカルファイルシステムのみを表示できます。これは、NFS などのリモートファイルシステムを除外したい場合に便利です。

## よくある質問

#### Q1. `df`と`du`の違いは何ですか？
A. `df`はファイルシステムレベルでディスク使用量を表示しますが、`du`は特定のディレクトリやファイルのディスク使用量を表示します。

#### Q2. なぜ`df`の結果と実際のファイルサイズの合計が一致しないことがありますか？
A. 削除されたがまだプロセスが開いているファイル、ファイルシステムの予約ブロック、ジャーナリングなどが原因で差異が生じることがあります。

#### Q3. macOSで`df`の出力が異なるのはなぜですか？
A. macOSはBSDベースのシステムであり、GNU/Linuxとは若干異なる`df`の実装を使用しています。オプションや出力形式に違いがあります。

## macOSでの注意点

macOSでは、APFS（Apple File System）を使用しており、ボリュームとコンテナの概念があります。`df`の出力には、システムボリュームやデータボリュームなど複数のボリュームが表示されることがあります。また、macOSでは一部のオプション（例：`-T`）が利用できないか、異なる動作をする場合があります。

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html

## 改訂履歴

- 2025/04/30 初版作成