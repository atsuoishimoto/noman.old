# envコマンド概要

`env`コマンドは、環境変数を表示したり、指定した環境変数の下でコマンドを実行したりするためのUnixコマンドです。

## 主なオプション

- **オプションなし**: 現在の環境変数をすべて表示します
  - 例: `env`

- **-i, --ignore-environment**: すべての継承された環境変数を無視して、空の環境でコマンドを実行します
  - 例: `env -i command`

- **-u, --unset=NAME**: 指定した環境変数を削除してからコマンドを実行します
  - 例: `env -u HOME command`

- **NAME=VALUE**: 一時的に環境変数を設定してコマンドを実行します
  - 例: `env DEBUG=1 ./script.sh`

## 使用例

```bash
# 現在の環境変数をすべて表示
env
# 出力例
PATH=/usr/local/bin:/usr/bin:/bin
HOME=/home/user
USER=username
SHELL=/bin/bash
...

# 特定の環境変数だけを表示（grepと組み合わせる）
env | grep PATH
# 出力例
PATH=/usr/local/bin:/usr/bin:/bin

# 一時的に環境変数を設定してコマンドを実行
env LANG=ja_JP.UTF-8 date
# 出力例
2023年 4月 1日 土曜日 12:00:00 JST

# 空の環境でコマンドを実行
env -i bash -c 'echo $PATH'
# 出力例
（空の出力、PATHが設定されていない）

# 特定の環境変数を削除してコマンドを実行
env -u HOME pwd
# 出力例
/current/directory
```

## 追加メモ

- `env`コマンドは、スクリプトやプログラムのデバッグに役立ちます。特定の環境変数の影響を確認したい場合に便利です。
- シェルスクリプトの先頭に `#!/usr/bin/env python` のように記述すると、環境のPATH変数に基づいてインタープリタを探すため、移植性が高まります。
- 環境変数の変更は、そのコマンド実行中のみ有効で、親シェルには影響しません。永続的に変更するには、`.bashrc`や`.profile`などの設定ファイルを編集する必要があります。