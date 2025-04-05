# zipコマンド概要
zipコマンドは、ファイルを圧縮して.zipアーカイブを作成するためのUnixコマンドです。複数のファイルやディレクトリを一つのアーカイブにまとめて、サイズを小さくすることができます。

## 主なオプション
- **-r**: ディレクトリを再帰的に圧縮します（ディレクトリ内のすべてのファイルとサブディレクトリを含めます）
  - 例: `zip -r archive.zip directory/`

- **-q**: 静かモード（quiet mode）で実行し、処理中のメッセージを表示しません
  - 例: `zip -q archive.zip file1 file2`

- **-u**: アーカイブを更新します（新しいファイルを追加したり、変更されたファイルを更新したりします）
  - 例: `zip -u archive.zip newfile.txt`

- **-d**: アーカイブから指定したファイルを削除します
  - 例: `zip -d archive.zip oldfile.txt`

- **-e**: パスワード保護されたアーカイブを作成します
  - 例: `zip -e archive.zip file1 file2`

- **-j**: ディレクトリ構造を保存せず、ファイル名のみを使用します（junkパス）
  - 例: `zip -j archive.zip directory/file1 directory/file2`

## 使用例

### 基本的な使用方法
```bash
# 複数のファイルを圧縮
zip archive.zip file1.txt file2.txt file3.txt
# 出力例
  adding: file1.txt (stored 0%)
  adding: file2.txt (stored 0%)
  adding: file3.txt (deflated 45%)
```

### ディレクトリを再帰的に圧縮
```bash
# ディレクトリとその中身をすべて圧縮
zip -r backup.zip ~/Documents/project/
# 出力例
  adding: Documents/project/ (stored 0%)
  adding: Documents/project/file1.txt (deflated 35%)
  adding: Documents/project/images/ (stored 0%)
  adding: Documents/project/images/photo.jpg (stored 0%)
```

### パスワード保護されたアーカイブの作成
```bash
# パスワード保護付きで圧縮
zip -e secure.zip confidential.pdf
# 出力例
Enter password: 
Verify password: 
  adding: confidential.pdf (deflated 12%)
```

### アーカイブの更新
```bash
# 既存のアーカイブに新しいファイルを追加
zip -u archive.zip newfile.txt updatedfile.txt
# 出力例
  adding: newfile.txt (stored 0%)
  updating: updatedfile.txt (deflated 32%)
```

## 追加メモ
- Windowsとの互換性が高く、クロスプラットフォームでファイル共有する際に便利です。
- 大量のファイルを圧縮する場合は、`-9`オプションで最高圧縮率を指定できますが、処理時間が長くなります。
- セキュリティが重要な場合は、zipの暗号化は比較的弱いので、より強力な暗号化が必要な場合は`gpg`などの他のツールを検討してください。
- 日本語ファイル名を含むアーカイブを作成する場合、文字化けを防ぐために適切な文字エンコーディングを指定することが重要な場合があります。