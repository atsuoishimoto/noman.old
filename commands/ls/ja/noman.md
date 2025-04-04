# `ls` コマンドの概要
`ls`コマンドはディレクトリの内容を一覧表示するためのUnixコマンドです。ファイルやフォルダの情報を確認する際に最も基本的で頻繁に使用されるコマンドの一つです。

## 主なオプション
- **`-l`**: 詳細な一覧形式で表示（ロングフォーマット）
  - ファイルの権限、所有者、サイズ、更新日時などの詳細情報を表示します

- **`-a`**: 隠しファイル（ドットで始まるファイル）も含めてすべてのファイルを表示
  - 通常は表示されない `.` で始まるファイルやディレクトリも表示します

- **`-h`**: ファイルサイズを人間が読みやすい形式（KB、MB、GBなど）で表示
  - `-l` オプションと組み合わせて使用すると効果的です

- **`-t`**: 更新日時順にファイルを並べ替えて表示
  - 最近変更されたファイルが先頭に表示されます

- **`-r`**: 逆順で表示
  - 他のソートオプションと組み合わせて使用できます（例：`-tr` で最も古いファイルから表示）

- **`-S`**: ファイルサイズ順（大きい順）に並べ替えて表示

- **`--color`**: ファイルタイプによって色分けして表示
  - ディレクトリ、実行可能ファイル、シンボリックリンクなどが区別しやすくなります

## 使用例

```bash
# 基本的な使用法（現在のディレクトリの内容を表示）
$ ls
Documents  Downloads  Pictures  Videos

# 詳細情報を表示
$ ls -l
total 16
drwxr-xr-x  2 user group  4096 4月 10 15:30 Documents
drwxr-xr-x  2 user group  4096 4月  9 10:15 Downloads
drwxr-xr-x  2 user group  4096 4月  8 20:45 Pictures
drwxr-xr-x  2 user group  4096 4月  7 18:20 Videos

# 隠しファイルを含めて表示
$ ls -a
.  ..  .bash_history  .config  Documents  Downloads  Pictures  Videos

# 詳細情報と人間が読みやすいサイズ表示
$ ls -lh
total 16K
drwxr-xr-x  2 user group  4.0K 4月 10 15:30 Documents
drwxr-xr-x  2 user group  4.0K 4月  9 10:15 Downloads
drwxr-xr-x  2 user group  4.0K 4月  8 20:45 Pictures
drwxr-xr-x  2 user group  4.0K 4月  7 18:20 Videos

# 最近更新されたファイル順に表示
$ ls -lt
total 16
drwxr-xr-x  2 user group  4096 4月 10 15:30 Documents
drwxr-xr-x  2 user group  4096 4月  9 10:15 Downloads
drwxr-xr-x  2 user group  4096 4月  8 20:45 Pictures
drwxr-xr-x  2 user