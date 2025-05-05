# rsync コマンド

ファイルやディレクトリをローカルまたはリモート間で同期します。

## 概要

`rsync`は、高速で多機能なファイルコピーおよび同期ツールで、ローカルまたはリモート接続を介して動作します。ソースとデスティネーション間の差分のみを転送することで、ディレクトリやホスト間でファイルを効率的に転送・同期するように設計されています。これにより、特に大きなファイルや頻繁に同期する場合には、通常のコピーコマンドよりも高速に処理できます。

## オプション

### **-a, --archive**

アーカイブモードで、ほぼすべての属性を保持します（-rlptgoDと同等）。バックアップ操作で最も一般的に使用されるオプションです。

```console
$ rsync -a /source/directory/ /destination/directory/
```

### **-v, --verbose**

詳細表示を増やし、転送されているファイルを表示します。

```console
$ rsync -av /source/directory/ /destination/directory/
sending incremental file list
file1.txt
file2.txt
directory/
directory/file3.txt

sent 1,234 bytes  received 42 bytes  2,552.00 bytes/sec
total size is 10,240  speedup is 8.04
```

### **-z, --compress**

転送中にファイルデータを圧縮して、帯域幅の使用量を削減します。

```console
$ rsync -avz /source/directory/ user@remote-host:/destination/directory/
```

### **-P, --partial --progress**

転送中の進行状況を表示し、部分的に転送されたファイルを保持します。

```console
$ rsync -avP large_file.iso /backup/
sending incremental file list
large_file.iso
    852,492,288 100%   85.23MB/s    0:00:09 (xfr#1, to-chk=0/1)
```

### **--delete**

ソースに存在しないデスティネーション内のファイルを削除し、デスティネーションをソースの完全なミラーにします。

```console
$ rsync -av --delete /source/directory/ /destination/directory/
```

### **-n, --dry-run**

実際に変更を加えずに試験実行を行います。

```console
$ rsync -avn --delete /source/directory/ /destination/directory/
sending incremental file list
./
file1.txt
file2.txt

sent 123 bytes  received 42 bytes  330.00 bytes/sec
total size is 10,240  speedup is 62.07 (DRY RUN)
```

## 使用例

### リモートサーバーへの同期

```console
$ rsync -avz ~/Documents/ user@remote-server:/backup/documents/
sending incremental file list
./
report.docx
presentation.pptx
data.xlsx

sent 2,345,678 bytes  received 1,234 bytes  469,382.40 bytes/sec
total size is 2,340,000  speedup is 0.99
```

### 除外ファイルを指定したバックアップの作成

```console
$ rsync -av --exclude='*.tmp' --exclude='cache/' /home/user/ /mnt/backup/home/
```

### ウェブサイトのミラーリング

```console
$ rsync -avz --delete user@remote-server:/var/www/html/ /local/mirror/
```

### 大きなファイル転送の再開

```console
$ rsync -avP --partial user@remote-server:large_file.iso /downloads/
```

## ヒント:

### 末尾のスラッシュを注意して使用する

ディレクトリをコピーする際、ソースの末尾にスラッシュ（`/source/`）をつけると「このディレクトリの内容をコピー」を意味し、スラッシュなし（`/source`）は「このディレクトリとその内容をコピー」を意味します。

### パスワードなし転送のためのSSH鍵の設定

頻繁にリモート転送を行う場合は、SSH鍵認証を設定して、パスワードの入力を省略できます。

### バックグラウンド転送のための帯域制限

```console
$ rsync --bwlimit=1000 -av /source/ /destination/
```
これにより転送速度が1000 KB/秒に制限され、すべての帯域幅を消費すべきでないバックグラウンド転送に役立ちます。

### ハードリンクを使用したスナップショットの作成

```console
$ rsync -a --link-dest=/backup/previous /source/ /backup/current/
```
これにより、変更されていないファイルを以前のバックアップにハードリンクすることで、容量効率の良いバックアップが作成できます。

## よくある質問

#### Q1. rsyncはscpやcpとどう違いますか？
A. `cp`や`scp`と異なり、rsyncはファイル間の差分のみを転送するため、同じデータの後続の転送がはるかに高速になります。また、ファイル属性の保存や同期処理のためのより多くのオプションを提供しています。

#### Q2. rsyncは中断された転送を再開できますか？
A. はい、`--partial`オプション（または`-P`）を使用すると、rsyncは部分的に転送されたファイルを最初からやり直すのではなく、再開できます。

#### Q3. rsyncがデスティネーションのファイルを削除しないようにするにはどうすればよいですか？
A. デフォルトでは、rsyncはファイルを削除しません。ソースからファイルを追加または更新するだけです。ソースに存在しないデスティネーション内のファイルを削除するには、`--delete`オプションを明示的に指定する必要があります。

#### Q4. rsyncが実際に何をするかを事前にテストするにはどうすればよいですか？
A. `--dry-run`または`-n`オプションを使用すると、実際に変更を加えることなく、何が転送されるかを確認できます。

#### Q5. rsyncは2つのリモートサーバー間でファイルを同期できますか？
A. はい、ただしサーバーの1つでrsyncを実行するか、`--rsync-path`オプションを使用してリモートマシン上のrsyncへのパスを指定する必要があります。

## References

https://download.samba.org/pub/rsync/rsync.html

## Revisions

- 2025/05/04 First revision