# `split` コマンド概要

`split`コマンドは、大きなファイルを小さな部分に分割するためのUnixコマンドです。ファイルサイズが大きすぎて扱いにくい場合や、メール添付などで分割が必要な場合に便利です。

## 主なオプション

- **-b, --bytes=SIZE**: 指定したバイトサイズごとにファイルを分割
  - 例: `split -b 1M largefile` (1MBごとに分割)

- **-l, --lines=NUMBER**: 指定した行数ごとにファイルを分割
  - 例: `split -l 1000 largefile` (1000行ごとに分割)

- **-d, --numeric-suffixes[=FROM]**: 数字のサフィックスを使用（アルファベットの代わりに）
  - 例: `split -d largefile` (xaa, xabではなく、x00, x01などの形式で出力)

- **-a, --suffix-length=N**: サフィックスの長さを指定
  - 例: `split -a 3 largefile` (xaaa, xaab, ...のように3文字のサフィックス)

- **--additional-suffix=SUFFIX**: 出力ファイル名に追加するサフィックスを指定
  - 例: `split -b 1M --additional-suffix=.txt largefile` (x00.txt, x01.txt, ...)

- **PREFIX**: 出力ファイル名のプレフィックスを指定（デフォルトは「x」）
  - 例: `split -b 1M largefile part_` (part_aa, part_ab, ...)

## 使用例

### 基本的な使用方法（デフォルトで1000行ごとに分割）

```bash
# 大きなファイルを分割
split largefile
# 出力
# xaa, xab, xac, ... というファイルが生成される
```

### サイズによる分割

```bash
# 10MBごとに分割し、数字のサフィックスを使用
split -b 10M -d largefile chunk_
# 出力
# chunk_00, chunk_01, chunk_02, ... というファイルが生成される
```

### 行数による分割

```bash
# 500行ごとに分割
split -l 500 logfile log_part_
# 出力
# log_part_aa, log_part_ab, ... というファイルが生成される
```

### 分割したファイルの結合

```bash
# 分割したファイルを元に戻す
cat x* > original_file_restored
```

## 追加情報

- 分割されたファイルは自動的に連番が振られますが、デフォルトではアルファベット順（aa, ab, ac...）です。`-d`オプションを使うと数字順（00, 01, 02...）になります。
- 分割したファイルを元に戻すには、`cat`コマンドを使って全ての分割ファイルを連結します。
- バイナリファイルを分割する場合は、`-b`オプションを使用するのが安全です。テキストファイルなら`-l`オプションが便利です。
- サイズ指定には、K（キロバイト）、M（メガバイト）、G（ギガバイト）などの単位を使用できます。