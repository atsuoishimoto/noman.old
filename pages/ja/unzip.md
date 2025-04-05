# unzipコマンド概要

`unzip`コマンドは、ZIP形式で圧縮されたファイルを展開（解凍）するためのコマンドです。Windows、macOS、Linuxなど様々なプラットフォームで使用される一般的な圧縮形式であるZIPファイルを扱うことができます。

## 主なオプション

- **-l**: ZIPファイルの内容を一覧表示します（展開せずに中身を確認）
  - 例: `unzip -l archive.zip`

- **-d**: 指定したディレクトリに展開します
  - 例: `unzip archive.zip -d /path/to/directory`

- **-o**: 既存のファイルを確認なしで上書きします
  - 例: `unzip -o archive.zip`

- **-n**: 既存のファイルを上書きしません
  - 例: `unzip -n archive.zip`

- **-j**: ディレクトリ構造を無視して、すべてのファイルを現在のディレクトリに展開します
  - 例: `unzip -j archive.zip`

- **-q**: 静かモード（詳細な出力を表示しない）
  - 例: `unzip -q archive.zip`

- **-p**: 内容を標準出力に出力します（テキストファイルの内容を確認する場合に便利）
  - 例: `unzip -p archive.zip file.txt`

## 使用例

### 基本的な使い方
```bash
# ZIPファイルを現在のディレクトリに展開
unzip archive.zip
# 出力例
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
  inflating: subfolder/file3.txt
```

### ZIPファイルの内容を確認
```bash
# ZIPファイルの内容を一覧表示（展開せずに）
unzip -l photos.zip
# 出力例
Archive:  photos.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
   245760  2023-04-01 10:30   photo1.jpg
   189440  2023-04-01 10:31   photo2.jpg
   302080  2023-04-01 10:32   vacation/photo3.jpg
 --------                   -------
   737280                   3 files
```

### 特定のディレクトリに展開
```bash
# 指定したディレクトリに展開
unzip documents.zip -d ~/Documents/extracted
# 出力例
Archive:  documents.zip
   creating: /home/user/Documents/extracted/reports/
  inflating: /home/user/Documents/extracted/reports/report1.pdf
  inflating: /home/user/Documents/extracted/reports/report2.pdf
```

### 特定のファイルのみを展開
```bash
# ZIPファイルから特定のファイルのみを展開
unzip archive.zip config.json
# 出力例
Archive:  archive.zip
  inflating: config.json
```

## 追加のヒント

- ZIPファイルにパスワードが設定されている場合は、`-P`オプションでパスワードを指定できます：`unzip -P password archive.zip`
- セキュリティ上の理由から、パスワードをコマンドラインに直接入力したくない場合は、オプションなしで実行すると対話的にパスワードを入力できます
- 日本語などの非ASCII文字を含むZIPファイルを展開する場合、文字化けすることがあります。その場合は`unzip -O CP932 archive.zip`（Windows向けの日本語エンコーディング）などのオプションを試してみてください
- `unzip`コマンドがインストールされていない場合は、Ubuntuなどのデビアン系では`sudo apt install unzip`、RedHatなどのRPM系では`sudo yum install unzip`でインストールできます