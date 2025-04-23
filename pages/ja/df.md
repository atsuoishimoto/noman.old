# df

`df`コマンドは、ファイルシステムのディスク容量使用状況を表示するためのコマンドです。マウントされているファイルシステムの合計サイズ、使用量、空き容量などを確認できます。

## オプション

### **-h (human-readable)**

サイズを人間が読みやすい形式（KB、MB、GBなど）で表示します。

```bash
$ df -h
Filesystem      Size   Used  Avail Capacity  iused    ifree %iused  Mounted on
/dev/disk1s1s1  234Gi   14Gi  216Gi     7%   488125 2147996154    0%   /
/dev/disk1s2    234Gi  1.0Gi  216Gi     1%        3 2148484276    0%   /System/Volumes/Preboot
/dev/disk1s4    234Gi  5.4Mi  216Gi     1%       25 2148484254    0%   /System/Volumes/VM
/dev/disk1s5    234Gi  1.5Gi  216Gi     1%     1412 2148482867    0%   /System/Volumes/Update
/dev/disk1s3    234Gi  1.1Gi  216Gi     1%     1194 2148483085    0%   /System/Volumes/Data
```

### **-T (type)**

各ファイルシステムのタイプも表示します。

```bash
$ df -T
Filesystem     Type         1K-blocks      Used Available Use% Mounted on
/dev/sda1      ext4          41251136  12503812  26651320  32% /
tmpfs          tmpfs          1022784         0   1022784   0% /dev/shm
/dev/sdb1      ext4         961432072 923042160  38389912  96% /home
```

### **-i (inodes)**

ディスクブロックの代わりにiノード情報を表示します。

```bash
$ df -i
Filesystem      Inodes  IUsed    IFree IUse% Mounted on
/dev/disk1s1s1 2148484279 488125 2147996154    0% /
/dev/disk1s2   2148484279      3 2148484276    0% /System/Volumes/Preboot
/dev/disk1s4   2148484279     25 2148484254    0% /System/Volumes/VM
/dev/disk1s5   2148484279   1412 2148482867    0% /System/Volumes/Update
/dev/disk1s3   2148484279   1194 2148483085    0% /System/Volumes/Data
```

### **-a (all)**

通常表示されない特殊なファイルシステム（/procや/sysなど）も含めて全てのファイルシステムを表示します。

```bash
$ df -a
Filesystem     1K-blocks      Used Available Use% Mounted on
/dev/disk1s1s1  244277768  14680928 226548840   7% /
devfs                 191       191         0 100% /dev
/dev/disk1s5   244277768   1572864 226548840   1% /System/Volumes/Data
/dev/disk1s4   244277768      5536 226548840   1% /System/Volumes/VM
/dev/disk1s2   244277768   1048576 226548840   1% /System/Volumes/Preboot
/dev/disk1s6   244277768   1572864 226548840   1% /System/Volumes/Update
map auto_home           0         0         0   0% /System/Volumes/Data/home
```

## 使用例

### 特定のディレクトリやファイルのファイルシステム情報を表示

```bash
$ df -h /home
Filesystem      Size   Used  Avail Capacity  iused    ifree %iused  Mounted on
/dev/disk1s5    234Gi  1.5Gi  216Gi     1%     1412 2148482867    0%   /System/Volumes/Data
```

### 人間が読みやすい形式で全ファイルシステムのタイプも表示

```bash
$ df -hT
Filesystem     Type         Size   Used  Avail Capacity  Mounted on
/dev/disk1s1s1 apfs         234Gi   14Gi  216Gi     7%   /
devfs          devfs        191Ki  191Ki     0B   100%   /dev
/dev/disk1s5   apfs         234Gi  1.5Gi  216Gi     1%   /System/Volumes/Data
/dev/disk1s4   apfs         234Gi  5.4Mi  216Gi     1%   /System/Volumes/VM
/dev/disk1s2   apfs         234Gi  1.0Gi  216Gi     1%   /System/Volumes/Preboot
/dev/disk1s6   apfs         234Gi  1.5Gi  216Gi     1%   /System/Volumes/Update
```

## よくある質問

### Q1. `df`と`du`の違いは何ですか？
A. `df`はファイルシステム全体のディスク使用状況を表示しますが、`du`は特定のディレクトリやファイルのディスク使用量を表示します。`df`はファイルシステムレベル、`du`はファイルやディレクトリレベルの情報を提供します。

### Q2. ディスク容量が足りなくなった時、どのパーティションが問題なのかを確認するには？
A. `df -h`を実行して、「Use%」や「Capacity」列が高い値（90%以上）のファイルシステムを確認します。それが容量不足のパーティションです。

### Q3. iノード情報を確認する必要があるのはどんな時ですか？
A. ディスク容量に余裕があるのにファイルが作成できない場合は、iノードが不足している可能性があります。`df -i`でiノードの使用状況を確認できます。多数の小さなファイルがある環境ではiノード不足が起きることがあります。

## 追加情報

- macOSでは、`df`コマンドの出力形式がLinuxと若干異なります。特に、macOSではデフォルトで512バイトブロックを使用しますが、多くのLinuxディストリビューションでは1KBブロックを使用します。
- ディスク容量が90%以上使用されている場合は、パフォーマンスの低下を避けるためにクリーンアップを検討すべきです。
- 出力結果の「Mounted on」列は、そのファイルシステムがマウントされている場所（マウントポイント）を示しています。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html