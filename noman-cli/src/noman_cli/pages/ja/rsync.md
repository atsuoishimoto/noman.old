# rsync コマンド

ファイルやディレクトリを効率的に同期・コピーするためのツール。

## 概要

rsync（remote synchronization）は、ローカルまたはリモートのファイルやディレクトリを同期するためのコマンドです。増分バックアップ機能を持ち、変更されたファイルのみを転送することで効率的なデータ転送を実現します。ネットワーク帯域幅を節約し、大量のデータを扱う場合に特に有用です。

## オプション

### **-a (アーカイブモード)**

ディレクトリの再帰的コピー、シンボリックリンクの保持、ファイル権限・タイムスタンプ・所有者などのメタデータを保持します。

```console
$ rsync -a /home/user/documents/ /backup/documents/
```

### **-v (詳細表示)**

転送されるファイルの一覧と進捗状況を表示します。

```console
$ rsync -av /home/user/documents/ /backup/documents/
sending incremental file list
./
file1.txt
file2.txt
directory/
directory/file3.txt

sent 1,234 bytes  received 42 bytes  2,552.00 bytes/sec
total size is 10,240  speedup is 8.02
```

### **-z (圧縮)**

転送中にデータを圧縮します。ネットワーク経由の転送で特に有用です。

```console
$ rsync -avz /home/user/documents/ user@remote-server:/backup/documents/
```

### **--delete**

送信先にあって送信元にないファイルを削除し、完全な同期を行います。

```console
$ rsync -av --delete /home/user/documents/ /backup/documents/
```

### **-P (進捗表示と部分転送の再開)**

進捗バーを表示し、中断された転送を再開できるようにします。

```console
$ rsync -avP large_file.iso user@remote-server:/backup/
sending incremental file list
large_file.iso
    873,123,456 67% 25.4MB/s    0:01:23
```

## 使用例

### ローカルディレクトリの同期

```console
$ rsync -av ~/documents/ /media/backup/documents/
sending incremental file list
./
report.docx
presentation.pptx
images/
images/photo1.jpg
images/photo2.jpg

sent 15,234,567 bytes  received 1,234 bytes  10,156,534.00 bytes/sec
total size is 15,200,000  speedup is 0.99
```

### リモートサーバーへのバックアップ

```console
$ rsync -avz --delete ~/projects/ user@server.example.com:/backup/projects/
sending incremental file list
./
index.html
css/style.css
js/script.js

sent 45,678 bytes  received 987 bytes  18,666.00 bytes/sec
total size is 45,000  speedup is 0.97
```

### 特定のファイルタイプのみ同期

```console
$ rsync -av --include="*.jpg" --include="*.png" --exclude="*" ~/pictures/ /media/backup/pictures/
sending incremental file list
./
vacation.jpg
family.png
portrait.jpg

sent 8,765,432 bytes  received 123 bytes  5,843,703.33 bytes/sec
total size is 8,700,000  speedup is 0.99
```

## ヒント:

### ドライランで確認

`--dry-run`（または `-n`）オプションを使用すると、実際にファイルを転送せずに何が行われるかを確認できます。重要な同期やバックアップ前に試すと安全です。

```console
$ rsync -avn --delete ~/documents/ /backup/documents/
```

### SSHポートの指定

デフォルト以外のSSHポートを使用する場合は、`-e`オプションで指定できます。

```console
$ rsync -avz -e "ssh -p 2222" ~/documents/ user@server.example.com:/backup/
```

### 帯域制限

`--bwlimit`オプションを使用して転送速度を制限できます。値はKB/秒で指定します。

```console
$ rsync -av --bwlimit=1000 large_file.iso user@server.example.com:/backup/
```

## よくある質問

#### Q1. rsyncとscpの違いは何ですか？
A. rsyncは増分転送機能があり、変更されたファイルのみを転送するため効率的です。また、中断された転送の再開や同期機能があります。scpはシンプルなファイルコピーツールで、常に全ファイルを転送します。

#### Q2. rsyncでディレクトリをコピーする際のスラッシュ（/）の意味は？
A. 送信元パスの末尾にスラッシュを付けると、ディレクトリの内容のみがコピーされます。スラッシュがない場合は、ディレクトリ自体も含めてコピーされます。

#### Q3. バックグラウンドでrsyncを実行するには？
A. `nohup rsync -av source/ destination/ &`のように実行すると、ターミナルを閉じても処理が継続します。

#### Q4. 特定のファイルやディレクトリを除外するには？
A. `--exclude="pattern"`オプションを使用します。例：`rsync -av --exclude="*.tmp" --exclude="cache/" source/ destination/`

## macOSでの注意点

macOSでrsyncを使用する場合、デフォルトのバージョンは古い場合があります。Homebrewを使用して最新版をインストールすることをお勧めします：

```console
$ brew install rsync
```

また、macOSのファイルシステムには特殊な属性（リソースフォーク、拡張属性など）があります。これらを保持するには`-E`オプションを追加してください：

```console
$ rsync -avE source/ destination/
```

## 参考情報

https://rsync.samba.org/documentation.html

## 改訂履歴

- 2025/04/30 macOSでの注意点を追加。
- 2025/04/30 初版作成。