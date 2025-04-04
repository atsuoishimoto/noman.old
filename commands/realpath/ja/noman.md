# realpathコマンドの概要

`realpath`コマンドは、指定されたファイルやディレクトリの絶対パス（フルパス）を表示します。シンボリックリンクを解決し、正規化されたパスを出力します。

## 主なオプション

- **-s, --strip, --no-symlinks**: シンボリックリンクを解決せず、そのままのパスを表示します
  - 例: `realpath -s /usr/bin/python`

- **-m, --canonicalize-missing**: 指定したパスの一部が存在しなくても処理を続行します
  - 例: `realpath -m /path/to/non/existent/file`

- **-e, --canonicalize-existing**: 指定したパスのすべての構成要素が存在する場合のみ処理します
  - 例: `realpath -e /existing/path`

- **-q, --quiet**: エラーメッセージを表示しません
  - 例: `realpath -q /non/existent/path`

- **-z, --zero**: 出力の各行を改行ではなくNULL文字で終了します（スクリプトで使用する場合に便利）
  - 例: `realpath -z file1 file2`

- **--relative-to=DIR**: 指定したディレクトリからの相対パスを表示します
  - 例: `realpath --relative-to=/home /home/user/documents`

## 使用例

```bash
# 基本的な使用法（ファイルの絶対パスを表示）
realpath myfile.txt
# 出力例
/home/user/projects/myfile.txt

# シンボリックリンクを解決せずにパスを表示
ln -s /etc/hosts hosts_link
realpath -s hosts_link
# 出力例
/home/user/hosts_link

# 存在しないファイルのパスを表示
realpath -m /home/user/non_existent_file.txt
# 出力例
/home/user/non_existent_file.txt

# 相対パスを表示
realpath --relative-to=/home /home/user/documents/file.txt
# 出力例
user/documents/file.txt
```

## 追加情報

- シェルスクリプト内でファイルの絶対パスを取得する際に特に便利です
- `readlink -f`コマンドと似た機能を持ちますが、`realpath`の方がより多くのオプションを提供します
- 複数のファイルを一度に指定すると、それぞれの絶対パスを1行ずつ出力します
- 存在しないパスを指定した場合、デフォルトではエラーになりますが、`-m`オプションを使用すると仮想的なパスを表示できます