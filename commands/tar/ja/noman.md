# `tar` コマンド概要

`tar`（テープアーカイブの略）は、複数のファイルやディレクトリを1つのアーカイブファイルにまとめたり、アーカイブから元のファイルを取り出したりするためのコマンドです。圧縮機能も備えており、ファイルの保存や転送に便利です。

## 主なオプション

- **`-c`（create）**: 新しいアーカイブを作成します
  - 例: `tar -cf archive.tar file1 file2`

- **`-x`（extract）**: アーカイブからファイルを取り出します
  - 例: `tar -xf archive.tar`

- **`-f`（file）**: 操作対象のアーカイブファイル名を指定します（ほぼ必須のオプション）
  - 例: `tar -cf archive.tar files/`

- **`-v`（verbose）**: 処理中のファイル名を表示します
  - 例: `tar -cvf archive.tar files/`

- **`-z`（gzip）**: gzip圧縮を使用します（.tar.gzファイル用）
  - 例: `tar -czf archive.tar.gz files/`

- **`-j`（bzip2）**: bzip2圧縮を使用します（.tar.bz2ファイル用）
  - 例: `tar -cjf archive.tar.bz2 files/`

- **`-t`（list）**: アーカイブの内容を一覧表示します
  - 例: `tar -tf archive.tar`

## 使用例

### アーカイブの作成

```bash
# ディレクトリをtarアーカイブに圧縮（gzip形式）
tar -czf backup.tar.gz /home/user/documents/
# 処理中のファイル名が表示される
/home/user/documents/
/home/user/documents/file1.txt
/home/user/documents/file2.txt
```

### アーカイブの展開

```bash
# tarアーカイブを現在のディレクトリに展開
tar -xf archive.tar
# gzip圧縮されたアーカイブを展開
tar -xzf archive.tar.gz
```

### アーカイブの内容確認

```bash
# アーカイブ内のファイル一覧を表示
tar -tf archive.tar
# 出力例
documents/
documents/file1.txt
documents/file2.txt
```

### 特定のファイルのみ展開

```bash
# アーカイブから特定のファイルだけを展開
tar -xf archive.tar documents/file1.txt
```

## 追加のヒント

- オプションの前のハイフン（`-`）は省略可能です（例: `tar cf archive.tar files/`）
- 最近のLinuxディストリビューションでは、ファイル拡張子から自動的に圧縮形式を判断できます（例: `tar -xf archive.tar.gz`）
- 大きなディレクトリを圧縮する場合は、`-v`オプションを使うと進行状況が分かりやすくなります
- 展開先を指定するには`-C`オプションを使用します（例: `tar -xf archive.tar -C /path/to/extract/`）
- `.tgz`ファイルは`.tar.gz`ファイルの短縮形です。同じ方法で扱えます