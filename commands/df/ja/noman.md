# dfコマンドの概要
dfコマンドは、システム上のディスクの空き容量と使用状況を表示するためのUnixコマンドです。ファイルシステムごとの総容量、使用量、空き容量を確認できます。

## 主なオプション
- **-h**: 人間が読みやすい形式（KB、MB、GBなど）でサイズを表示します
  - 例: `df -h`

- **-T**: 各ファイルシステムのタイプも表示します
  - 例: `df -T`

- **-i**: ディスクブロックではなく、iノード情報（ファイル数の制限に関連）を表示します
  - 例: `df -i`

- **-a**: 通常表示されない特殊なファイルシステム（/proc、/sysなど）も含めてすべて表示します
  - 例: `df -a`

- **特定のディレクトリやマウントポイント**: 特定のディレクトリやマウントポイントの情報のみを表示します
  - 例: `df /home`

## 使用例

```bash
# 基本的な使用方法
df
# 出力例
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       41251136 8123456  31096292  21% /
tmpfs            1021876       0   1021876   0% /dev/shm
/dev/sda2      103081248 6291456  91530380   7% /home
```

```bash
# 人間が読みやすい形式で表示
df -h
# 出力例
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        40G  7.8G   30G  21% /
tmpfs           1.0G     0  1.0G   0% /dev/shm
/dev/sda2        99G  6.0G   88G   7% /home
```

```bash
# ファイルシステムタイプも表示
df -T
# 出力例
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4      41251136 8123456  31096292  21% /
tmpfs          tmpfs      1021876       0   1021876   0% /dev/shm
/dev/sda2      ext4     103081248 6291456  91530380   7% /home
```

```bash
# iノード情報を表示
df -i
# 出力例
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      2621440 254321 2367119   10% /
tmpfs           255469      1  255468    1% /dev/shm
/dev/sda2      6553600  42123 6511477    1% /home
```

## 追加メモ
- 最も一般的な使用法は `df -h` で、これにより容量が読みやすい単位（GB、MBなど）で表示されます
- ディスク容量が不足している場合、`df -h` を使って素早く問題のあるパーティションを特定できます
- 特定のディレクトリの容量を確認したい場合は、そのパスを引数として指定します（例: `df -h /var/log`）
- iノードの枯渇はディスク容量が十分あっても問題を引き起こす可能性があるため、時々 `df -i` で確認すると良いでしょう