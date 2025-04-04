# cpコマンド概要
`cp`コマンドはファイルやディレクトリをコピーするためのUnixコマンドです。元のファイルを保持したまま、別の場所に複製を作成します。

## 主なオプション
- **-r, -R, --recursive**: ディレクトリとその中身を再帰的にコピーします
  - 例: `cp -r ソースディレクトリ 宛先ディレクトリ`

- **-i, --interactive**: 上書き前に確認を求めます（対話モード）
  - 例: `cp -i file1.txt file2.txt`

- **-v, --verbose**: 実行中の操作を詳細に表示します
  - 例: `cp -v file1.txt file2.txt`

- **-p, --preserve**: ファイルの属性（所有者、グループ、タイムスタンプなど）を保持します
  - 例: `cp -p file1.txt file2.txt`

- **-u, --update**: 宛先ファイルが存在しない場合、または元ファイルより古い場合のみコピーします
  - 例: `cp -u file1.txt file2.txt`

## 使用例

### 基本的なファイルのコピー
```bash
# 1つのファイルを別の名前でコピー
cp document.txt document_backup.txt

# 複数のファイルをディレクトリにコピー
cp file1.txt file2.txt destination_directory/
```

### ディレクトリのコピー
```bash
# ディレクトリとその中身を再帰的にコピー
cp -r source_directory/ destination_directory/

# 詳細表示しながらディレクトリをコピー
cp -rv source_directory/ destination_directory/
```

### 上書き確認
```bash
# 上書き前に確認を求める
cp -i important.txt backup/important.txt
# 出力例（ファイルが存在する場合）:
# overwrite backup/important.txt? (y/n) 
```

### 属性を保持したコピー
```bash
# タイムスタンプや権限などの属性を保持してコピー
cp -p config.ini /etc/config.ini
```

## 追加メモ
- ワイルドカード（`*`）を使用して複数のファイルを一度にコピーできます：`cp *.txt destination/`
- 宛先が存在するディレクトリの場合、ファイルはそのディレクトリ内にコピーされます
- 宛先が存在しないファイル名の場合、ファイルはその名前でコピーされます
- `-f`（強制）オプションを使うと、確認なしで上書きします（注意して使用してください）
- 大量のファイルや大きなディレクトリをコピーする場合は、`-v`オプションを使うと進行状況を確認できます