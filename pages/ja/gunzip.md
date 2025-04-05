# gunzipコマンド概要

`gunzip`は圧縮ファイル（通常は`.gz`拡張子を持つファイル）を解凍するためのUNIXコマンドです。主にgzipで圧縮されたファイルを元に戻すために使用されます。

## 主なオプション

- **-c, --stdout**: 解凍したデータを標準出力に出力します。元の圧縮ファイルは削除されません。
  - 例: `gunzip -c file.gz > file`

- **-f, --force**: 強制的に解凍を実行します。既に同名のファイルが存在する場合でも上書きします。
  - 例: `gunzip -f already_exists.gz`

- **-k, --keep**: 解凍後も元の圧縮ファイルを保持します（通常は解凍後に削除されます）。
  - 例: `gunzip -k important_archive.gz`

- **-l, --list**: 圧縮ファイルの内容を表示します（解凍せずに情報のみ表示）。
  - 例: `gunzip -l files.gz`

- **-r, --recursive**: ディレクトリを再帰的に処理し、見つかった全ての`.gz`ファイルを解凍します。
  - 例: `gunzip -r directory/`

- **-t, --test**: 圧縮ファイルの整合性をテストします（実際に解凍は行いません）。
  - 例: `gunzip -t suspicious.gz`

## 使用例

```bash
# 基本的な使い方：ファイルの解凍
gunzip file.gz
# 結果：file.gzが解凍されてfileというファイルが作成され、元のfile.gzは削除される

# 複数ファイルの解凍
gunzip file1.gz file2.gz file3.gz
# 結果：指定した全てのファイルが解凍される

# 元のファイルを保持したまま解凍
gunzip -k important.gz
# 結果：important.gzが解凍されてimportantというファイルが作成され、important.gzも保持される

# 圧縮ファイルの内容を確認
gunzip -l large_archive.gz
# 出力例：
#         compressed        uncompressed  ratio uncompressed_name
#                1024               4096  75.0% large_archive

# 標準出力への解凍（パイプラインで他のコマンドに渡す場合に便利）
gunzip -c data.gz | grep "keyword"
# 結果：data.gzを解凍した内容から"keyword"を含む行が表示される
```

## 追加情報

- `gunzip`は実際には`gzip -d`と同等です。`gzip`コマンドの解凍モードとして機能します。
- ファイル名に`.gz`拡張子がない場合でも、`gunzip`は自動的に`.gz`を追加して探そうとします。
- 複数のファイルを一度に解凍する場合、一部のファイルでエラーが発生しても処理は続行されます。
- `.tar.gz`や`.tgz`ファイル（tarボールと呼ばれる）は、`tar -xzf file.tar.gz`コマンドで一度に解凍・展開できます。
- 大きなファイルを解凍する場合、十分なディスク容量があることを事前に確認しておくことをお勧めします。