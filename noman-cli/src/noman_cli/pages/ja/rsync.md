# rsyncコマンド概要

rsyncは、ファイルやディレクトリを効率的に同期・コピーするためのコマンドです。通常のコピーと異なり、差分のみを転送するため高速で、リモートマシンとのファイル転送にも使用できます。

## 主なオプション

- **-a (--archive)**: アーカイブモード。権限、所有者、タイムスタンプなどの属性を保持します
  - 例: `rsync -a /source/ /destination/`

- **-v (--verbose)**: 詳細な情報を表示します
  - 例: `rsync -av /source/ /destination/`

- **-z (--compress)**: 転送中にデータを圧縮します（ネットワーク転送時に便利）
  - 例: `rsync -avz /source/ user@remote:/destination/`

- **-r (--recursive)**: ディレクトリを再帰的にコピーします
  - 例: `rsync -r /source/ /destination/`

- **--delete**: 送信先にあって送信元にないファイルを削除します（完全同期）
  - 例: `rsync -av --delete /source/ /destination/`

- **-n (--dry-run)**: 実際にコピーせずに何が行われるかをシミュレーションします
  - 例: `rsync -avn /source/ /destination/`

- **-P (--partial --progress)**: 進捗状況を表示し、部分的に転送されたファイルを保持します
  - 例: `rsync -avP /source/ /destination/`

## 使用例

### ローカルディレクトリの同期
```bash
# ソースディレクトリからデスティネーションディレクトリへファイルをコピー
rsync -av /home/user/documents/ /backup/documents/

# 出力例
sending incremental file list
./
file1.txt
file2.txt
folder/
folder/document.pdf

sent 2,048 bytes  received 48 bytes  4,192.00 bytes/sec
total size is 10,240  speedup is 4.88
```

### リモートサーバーへのファイル転送
```bash
# ローカルからリモートサーバーへファイルを転送
rsync -avz ~/projects/ user@remote-server:/home/user/projects/

# 出力例
sending incremental file list
./
index.html
css/
css/style.css
js/
js/script.js

sent 15,872 bytes  received 312 bytes  3,236.80 bytes/sec
total size is 156,672  speedup is 9.67
```

### 進捗状況を表示しながらの大きなファイル転送
```bash
# 進捗状況を表示しながら大きなファイルを転送
rsync -avP large_file.iso user@remote-server:/home/user/downloads/

# 出力例
sending incremental file list
large_file.iso
    852,017,152 100%  25.78MB/s    0:00:31 (xfr#1, to-chk=0/1)

sent 852,032,640 bytes  received 42 bytes  27,485,570.39 bytes/sec
total size is 852,017,152  speedup is 1.00
```

## 追加メモ

- ソースディレクトリの末尾に `/` をつけると、ディレクトリの内容だけがコピーされます。`/` がない場合は、ディレクトリ自体もコピーされます。
- `-e` オプションで SSH などの通信プロトコルを指定できます：`rsync -avz -e ssh /source/ user@remote:/destination/`
- バックアップに使用する場合は `--backup` と `--backup-dir` オプションを使うと、上書きされるファイルのバックアップを作成できます。
- 大きなファイルを転送する際に中断した場合、再開すると差分のみを転送するため効率的です。
- `--exclude` オプションで特定のファイルやパターンを除外できます：`rsync -av --exclude='*.log' /source/ /destination/`