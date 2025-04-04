# truncateコマンドの概要

`truncate`コマンドは、ファイルのサイズを指定したサイズに変更するためのコマンドです。ファイルを拡大したり縮小したりすることができます。

## 主なオプション

- **-s, --size=SIZE**: ファイルを指定したサイズに設定します
  - 例: `truncate -s 100 file.txt` (ファイルを100バイトにする)
  - サイズ指定には単位を付けることができます: K (キロバイト)、M (メガバイト)、G (ギガバイト)など
  - `+`や`-`を付けると、現在のサイズから相対的に変更できます

- **-c, --no-create**: 存在しないファイルを作成しません
  - 例: `truncate -c -s 0 file.txt` (file.txtが存在しない場合は作成しない)

- **-r, --reference=RFILE**: 指定したファイルと同じサイズに設定します
  - 例: `truncate -r reference.txt target.txt` (target.txtをreference.txtと同じサイズにする)

## 使用例

```bash
# 新しいファイルを作成して100バイトのサイズに設定
truncate -s 100 newfile.txt

# 既存のファイルを0バイト（空）にする
truncate -s 0 logfile.txt

# ファイルサイズを1メガバイトに設定
truncate -s 1M largefile.dat

# 現在のサイズから500バイト増やす
truncate -s +500 growing.txt

# 現在のサイズから1キロバイト減らす
truncate -s -1K shrinking.txt

# 別のファイルと同じサイズにする
truncate -r reference.txt target.txt
```

## 追加メモ

- ファイルを縮小すると、余分なデータは失われます（削除されます）
- ファイルを拡大すると、新しく追加された部分はゼロ（null）バイトで埋められます
- ログファイルを素早く空にするのに便利です（`truncate -s 0 logfile.log`）
- `-s 0`は、ファイルを削除せずに内容だけを空にする最も一般的な使い方です
- 存在しないファイルを指定すると、デフォルトでは新しく作成されます（`-c`オプションで防止可能）