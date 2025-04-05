# gzipコマンド概要

gzipは、ファイルを圧縮・展開するためのUNIXコマンドです。ファイルサイズを小さくして保存容量を節約したり、ネットワーク転送を高速化したりするために使用されます。

## 主なオプション

- **-d**: 圧縮ファイルを展開（解凍）します
  - 例: `gzip -d file.gz`

- **-c**: 圧縮/展開結果を標準出力に出力します（元のファイルはそのまま保持）
  - 例: `gzip -c file > file.gz`

- **-k**: 圧縮/展開後も元のファイルを保持します
  - 例: `gzip -k file`

- **-l**: 圧縮ファイルの情報を表示します
  - 例: `gzip -l file.gz`

- **-[1-9]**: 圧縮レベルを指定します（1が最速・低圧縮率、9が最高圧縮率・低速）
  - 例: `gzip -9 file`

- **-r**: ディレクトリを再帰的に処理します
  - 例: `gzip -r directory`

## 使用例

### 基本的な圧縮
```bash
# ファイルを圧縮（元のファイルは削除される）
gzip data.txt
# 結果: data.txt.gz が作成される
```

### 複数ファイルの圧縮
```bash
# 複数のファイルを一度に圧縮
gzip file1.txt file2.txt file3.txt
# 結果: file1.txt.gz, file2.txt.gz, file3.txt.gz が作成される
```

### 圧縮ファイルの展開
```bash
# 圧縮ファイルを展開
gzip -d data.txt.gz
# または
gunzip data.txt.gz
# 結果: data.txt が復元される
```

### 元ファイルを保持しながら圧縮
```bash
# -k オプションで元ファイルを保持
gzip -k important_data.txt
# 結果: important_data.txt と important_data.txt.gz の両方が存在
```

### 圧縮情報の表示
```bash
# 圧縮ファイルの情報を表示
gzip -l archive.gz
# 出力例:
#         compressed        uncompressed  ratio uncompressed_name
#                 453               1024  55.7% archive
```

### 高圧縮率での圧縮
```bash
# 最高圧縮率（レベル9）で圧縮
gzip -9 large_file.txt
# 結果: 時間はかかるが、より小さいサイズの large_file.txt.gz が作成される
```

## 追加情報

- gzipは単一ファイルのみを圧縮します。複数のファイルをまとめて一つのアーカイブにしたい場合は、先に`tar`コマンドでアーカイブ化してから`gzip`で圧縮するのが一般的です（例: `tar -czf archive.tar.gz directory/`）。

- 圧縮ファイルの拡張子は通常`.gz`ですが、gzipコマンドは自動的に付加します。

- `zcat`、`zless`、`zgrep`などの関連コマンドを使うと、圧縮ファイルを展開せずに内容を確認できます。

- 大きなファイルを圧縮する場合、圧縮レベルが高いほどCPU使用率が上がり、処理時間が長くなることに注意してください。日常的な使用では、デフォルトのレベル6が速度と圧縮率のバランスが良いでしょう。