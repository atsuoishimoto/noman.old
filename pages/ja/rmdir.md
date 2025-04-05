# rmdirコマンド概要
`rmdir`コマンドは、空のディレクトリを削除するためのUnixコマンドです。ディレクトリ内にファイルやサブディレクトリが存在する場合は削除できません。

## 主なオプション
- **-p (--parents)**: 指定したパスの親ディレクトリも必要に応じて削除します
  - 例: `rmdir -p dir1/dir2/dir3`

- **-v (--verbose)**: 処理内容を詳細に表示します
  - 例: `rmdir -v emptyfolder`

- **--ignore-fail-on-non-empty**: 空でないディレクトリを削除しようとした場合でもエラーを表示せず処理を続行します
  - 例: `rmdir --ignore-fail-on-non-empty folder1 folder2`

## 使用例

### 基本的な使用法
```bash
# 空のディレクトリ「emptyfolder」を削除
rmdir emptyfolder
```

### 複数のディレクトリを一度に削除
```bash
# 複数の空ディレクトリを一度に削除
rmdir folder1 folder2 folder3
```

### 親ディレクトリも含めて削除
```bash
# dir1/dir2/dir3を削除し、空になったdir1とdir2も削除
rmdir -p dir1/dir2/dir3
# 出力（-vオプションを使用した場合）:
# rmdir: removing directory, 'dir1/dir2/dir3'
# rmdir: removing directory, 'dir1/dir2'
# rmdir: removing directory, 'dir1'
```

### 詳細表示モード
```bash
# 削除処理の詳細を表示
rmdir -v emptyfolder
# 出力:
# rmdir: removing directory, 'emptyfolder'
```

## 追加情報
- `rmdir`は空のディレクトリのみを削除できます。ディレクトリ内にファイルがある場合は、まず`rm`コマンドでファイルを削除するか、`rm -r`を使用してディレクトリごと削除する必要があります。
- ディレクトリが空でない場合、`rmdir`は「Directory not empty」というエラーを表示します。
- 複雑なディレクトリ構造を削除する場合は、`rm -r`コマンドの方が便利なことが多いです。
- 存在しないディレクトリを削除しようとすると「No such file or directory」エラーが表示されます。