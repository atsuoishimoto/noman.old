# `uniq` コマンドの概要

`uniq` コマンドは、連続する重複行を検出し、削除するためのUNIXコマンドです。デフォルトでは、ソート済みのテキストから隣接する重複行を1つだけ残して削除します。

## 主なオプション

- **-c, --count**: 各行の前に、その行が何回出現したかを表示します
  - 例: `uniq -c file.txt`

- **-d, --repeated**: 重複する行のみを表示します（各重複グループから1行）
  - 例: `uniq -d file.txt`

- **-D, --all-repeated**: 重複する行をすべて表示します
  - 例: `uniq -D file.txt`

- **-u, --unique**: 重複しない行のみを表示します
  - 例: `uniq -u file.txt`

- **-i, --ignore-case**: 大文字と小文字を区別せずに比較します
  - 例: `uniq -i file.txt`

- **-f N, --skip-fields=N**: 比較する際に最初のN個のフィールド（空白で区切られた部分）をスキップします
  - 例: `uniq -f 1 file.txt`

- **-s N, --skip-chars=N**: 比較する際に各行の最初のN文字をスキップします
  - 例: `uniq -s 3 file.txt`

## 使用例

```bash
# 入力ファイルの内容
cat fruits.txt
# 出力
apple
apple
banana
orange
orange
orange
grape

# 基本的な使用法（重複行を削除）
uniq fruits.txt
# 出力
apple
banana
orange
grape

# 出現回数を表示
uniq -c fruits.txt
# 出力
      2 apple
      1 banana
      3 orange
      1 grape

# 重複する行のみを表示
uniq -d fruits.txt
# 出力
apple
orange

# 重複しない行のみを表示
uniq -u fruits.txt
# 出力
banana
grape

# 大文字小文字を区別せずに重複を削除
cat mixed_case.txt
# 出力
Apple
apple
BANANA
banana
Orange

uniq -i mixed_case.txt
# 出力
Apple
BANANA
Orange
```

## 追加情報

- `uniq` コマンドは隣接する行のみを比較するため、通常は `sort` コマンドと組み合わせて使用します。例: `sort file.txt | uniq`

- ファイル全体から重複を完全に削除するには: `sort file.txt | uniq` または `sort -u file.txt`

- 特定のフィールドのみに基づいて重複を削除したい場合は、`-f` オプションが便利です。例えば、CSVファイルの2列目を無視して重複を削除する場合: `uniq -f 1 file.csv`

- `uniq` はデフォルトでは標準出力に結果を表示しますが、`>` リダイレクトを使用して結果をファイルに保存できます。例: `uniq file.txt > unique_lines.txt`