# chgrp コマンドの概要

`chgrp`コマンドは、ファイルやディレクトリのグループ所有権を変更するためのUnixコマンドです。ユーザーがファイルやディレクトリを共有する際に、適切なグループアクセス権を設定するのに役立ちます。

## 主なオプション

- **-R, --recursive**: 指定したディレクトリとその中のすべてのファイルやサブディレクトリに対して再帰的にグループを変更します
  - 例: `chgrp -R developers project/`

- **-v, --verbose**: 処理されるすべてのファイルについて詳細情報を表示します
  - 例: `chgrp -v staff document.txt`

- **-c, --changes**: `-v`と似ていますが、実際に変更があった場合のみ出力します
  - 例: `chgrp -c admin config.ini`

- **-h, --no-dereference**: シンボリックリンク自体のグループを変更し、リンク先のファイルは変更しません
  - 例: `chgrp -h developers symlink_file`

## 使用例

### 基本的な使用方法
```bash
# ファイルのグループを「staff」に変更
chgrp staff document.txt

# 確認
ls -l document.txt
# 出力例
-rw-r--r--  1 username staff  2048 4月 10 14:30 document.txt
```

### 再帰的にグループを変更
```bash
# プロジェクトディレクトリとその中身すべてのグループを「developers」に変更
chgrp -R developers project/

# 詳細表示で確認
ls -l project/
# 出力例
drwxr-xr-x  3 username developers  4096 4月 10 14:35 project/
```

### 詳細表示モード
```bash
# 変更内容を表示しながらグループを変更
chgrp -v admin config.ini
# 出力例
「config.ini」のグループを「users」から「admin」に変更しました
```

## 追加メモ

- グループ名の代わりにグループIDを使用することもできます（例: `chgrp 1000 file.txt`）
- ファイルのグループを変更するには、そのファイルの所有者であるか、root権限が必要です
- `/etc/group`ファイルには、システム上のすべてのグループ情報が格納されています
- `chown`コマンドを使用すると、所有者とグループを同時に変更できます（例: `chown user:group file.txt`）