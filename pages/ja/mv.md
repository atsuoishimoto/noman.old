# `mv` コマンド概要
`mv`（move）コマンドは、ファイルやディレクトリを移動したり、名前を変更したりするために使用されます。

## 主なオプション
- **-i（interactive）**: 上書き確認を行います。既存のファイルを上書きする前に確認メッセージを表示します。
  - 例: `mv -i file1.txt file2.txt`

- **-f（force）**: 確認なしで強制的に上書きします。
  - 例: `mv -f source.txt destination.txt`

- **-v（verbose）**: 実行内容を詳細に表示します。
  - 例: `mv -v file1.txt Documents/`

- **-n（no-clobber）**: 既存のファイルを上書きしません。
  - 例: `mv -n file1.txt file2.txt`

- **-u（update）**: 移動先のファイルが存在しない場合、または移動元のファイルが移動先のファイルより新しい場合のみ移動します。
  - 例: `mv -u source.txt destination.txt`

## 使用例

### 基本的なファイル移動
```bash
# ファイルを別のディレクトリに移動
mv file.txt Documents/
# 出力なし（成功時）
```

### ファイル名の変更
```bash
# ファイル名を変更
mv oldname.txt newname.txt
# 出力なし（成功時）
```

### 複数ファイルの移動
```bash
# 複数のファイルを一度に移動
mv file1.txt file2.txt file3.txt Documents/
# 出力なし（成功時）
```

### 詳細表示オプション使用
```bash
# 詳細表示オプションを使用
mv -v report.txt Documents/
# 出力例
'report.txt' -> 'Documents/report.txt'
```

### 上書き確認オプション使用
```bash
# 上書き確認オプションを使用
mv -i file1.txt file2.txt
# 出力例（file2.txtが既に存在する場合）
overwrite file2.txt? (y/n) 
```

## 追加メモ
- ファイルを誤って上書きしないように、日常的な使用では `-i` オプションを使うことをお勧めします。
- `mv` コマンドはデフォルトでは確認なしで上書きするため、重要なファイルを扱う際は注意が必要です。
- エイリアスを設定して `mv` を常に `-i` オプション付きで使用するようにすることも一般的です（例: `alias mv='mv -i'`）。
- ディレクトリの移動や名前変更も同じ構文で行えます。