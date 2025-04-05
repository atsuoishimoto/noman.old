# grepコマンド概要

`grep`は、ファイルやテキスト入力から特定のパターン（文字列や正規表現）を検索するためのコマンドです。名前は「Global Regular Expression Print」に由来しています。

## 主なオプション

- **-i**: 大文字と小文字を区別せずに検索します
  - 例: `grep -i "hello" file.txt`

- **-v**: マッチしない行を表示します（反転検索）
  - 例: `grep -v "error" log.txt`

- **-r, -R**: ディレクトリ内のファイルを再帰的に検索します
  - 例: `grep -r "TODO" ./src/`

- **-l**: マッチしたファイル名のみを表示します
  - 例: `grep -l "function" *.js`

- **-n**: マッチした行の行番号も表示します
  - 例: `grep -n "import" *.py`

- **-c**: マッチした行数のみを表示します
  - 例: `grep -c "ERROR" error.log`

- **-A n**: マッチした行の後ろn行も表示します（After）
  - 例: `grep -A 2 "exception" log.txt`

- **-B n**: マッチした行の前n行も表示します（Before）
  - 例: `grep -B 2 "exception" log.txt`

- **-C n**: マッチした行の前後n行を表示します（Context）
  - 例: `grep -C 2 "exception" log.txt`

- **-E**: 拡張正規表現を使用します
  - 例: `grep -E "apple|orange" fruits.txt`

## 使用例

```bash
# 基本的な使い方：ファイル内で「error」を含む行を検索
grep "error" log.txt
# 出力例
2023-04-01 12:34:56 error: connection refused

# 大文字小文字を区別せずに検索
grep -i "error" log.txt
# 出力例
2023-04-01 12:34:56 error: connection refused
2023-04-01 13:45:23 ERROR: timeout occurred

# 複数ファイルから検索し、ファイル名も表示
grep "function" *.js
# 出力例
app.js:function initialize() {
utils.js:function formatDate(date) {

# 行番号付きで表示
grep -n "import" main.py
# 出力例
3:import os
4:import sys
10:import datetime

# 再帰的にディレクトリ内を検索
grep -r "TODO" ./project/
# 出力例
./project/src/main.js:// TODO: Implement error handling
./project/docs/readme.md:TODO: Complete documentation

# マッチした行の前後1行を表示
grep -C 1 "exception" error.log
# 出力例
trying to connect to server
exception occurred: connection timeout
retrying in 5 seconds
```

## 追加メモ

- パイプ（`|`）と組み合わせて使うと非常に便利です。例えば `ps aux | grep "firefox"` でFirefoxプロセスを検索できます。
- 正規表現を使うことで、より複雑なパターンマッチングが可能です。例えば `grep "^[0-9]"` で数字で始まる行を検索できます。
- 検索パターンに空白やメタ文字が含まれる場合は、引用符で囲むことをお勧めします。
- 大量のファイルを検索する場合は、`grep -l` でマッチするファイル名だけを先に確認すると効率的です。
- 最近のLinuxディストリビューションでは、`grep`の出力は通常カラー表示されますが、`--color=auto`オプションで明示的に指定することもできます。