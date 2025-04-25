# df コマンド

`df`（disk free）コマンドは、システム上のファイルシステムの空き容量と使用状況を表示するユーティリティです。マウントされているすべてのファイルシステムのディスク使用量を確認できます。

## オプション

### **-h (human-readable)**
サイズを人間が読みやすい形式（KB、MB、GB）で表示します。

```console
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G  7.8G   11G  42% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
/dev/sda3       90G   63G   23G  74% /home
```

### **-T (file-system-type)**
各ファイルシステムのタイプも表示します。

```console
$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4      20971520 8192000 11534336  42% /
tmpfs          tmpfs      4096000       0  4096000   0% /dev/shm
/dev/sda3      ext4      94371840 66060288 24117248  74% /home
```

### **-i (inodes)**
ディスクブロックの代わりにiノード情報を表示します。

```console
$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      1310720 123456 1187264   10% /
tmpfs           999999      1  999998    1% /dev/shm
/dev/sda3      5898240 234567 5663673    4% /home
```

## 使用例

### 特定のファイルシステムの情報表示

```console
$ df -h /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda3        90G   63G   23G  74% /home
```

### 人間が読みやすい形式で全ファイルシステムのタイプも表示

```console
$ df -hT
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sda1      ext4    20G  7.8G   11G  42% /
tmpfs          tmpfs  3.9G     0  3.9G   0% /dev/shm
/dev/sda3      ext4    90G   63G   23G  74% /home
```

## よくある質問

#### Q1. `df`と`du`コマンドの違いは何ですか？
A. `df`はファイルシステム全体のディスク使用量を表示しますが、`du`は特定のディレクトリやファイルのディスク使用量を表示します。

#### Q2. 特定のマウントポイントだけを確認するにはどうすればいいですか？
A. マウントポイントのパスを引数として指定します。例：`df -h /home`

#### Q3. 出力の「Use%」が100%に近い場合はどうすればいいですか？
A. ディスク容量が不足しているため、不要なファイルを削除するか、ディスクの容量を増やすことを検討してください。

## 追加情報

* `-a`オプションを使用すると、通常表示されない0ブロックのファイルシステムも表示されます。
* macOSでは、`-H`オプションを使うと1000単位（KB=1000バイト）で表示され、`-h`は1024単位（KiB=1024バイト）で表示されます。
* ディスク容量が90%以上使用されている場合は、システムのパフォーマンスに影響する可能性があるため注意が必要です。

## macOSでの注意点

macOSでは、デフォルトでHFS+またはAPFSファイルシステムが使用されており、表示される情報がLinuxとは若干異なります。また、`df`コマンドはBSDバージョンが使用されるため、一部のGNU特有のオプションが使えない場合があります。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html