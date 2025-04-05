# `sort` コマンド概要

`sort`コマンドはテキストファイルの行を並べ替えるためのUnixコマンドです。デフォルトでは文字列を辞書順（アルファベット順）に並べ替えます。

## 主なオプション

- **`-n`**: 数値として並べ替え
  - 文字列ではなく数値として認識して並べ替えます

- **`-r`**: 逆順に並べ替え
  - 通常の並び順を逆にします（降順）

- **`-k FIELD`**: 特定のフィールド（列）で並べ替え
  - 区切り文字で分けられたテキストの特定の列を基準に並べ替えます

- **`-t DELIMITER`**: フィールド区切り文字を指定
  - デフォルトはタブやスペースですが、カンマなど他の区切り文字を指定できます

- **`-u`**: 重複行を削除
  - 並べ替え結果から重複する行を取り除きます

- **`-f`**: 大文字小文字を区別しない
  - 「A」と「a」を同じものとして扱います

- **`-b`**: 先頭の空白を無視
  - 行の先頭にある空白を無視して並べ替えます

## 使用例

### 基本的な使い方
```bash
# ファイルの内容をアルファベット順に並べ替え
$ cat fruits.txt
orange
apple
banana
$ sort fruits.txt
apple
banana
orange
```

### 数値順の並べ替え
```bash
# -nオプションで数値として並べ替え
$ cat numbers.txt
10
2
1
$ sort numbers.txt
1
10
2
$ sort -n numbers.txt
1
2
10
```

### 逆順に並べ替え
```bash
# -rオプションで逆順に並べ替え
$ sort -r fruits.txt
orange
banana
apple
```

### 特定のフィールドで並べ替え
```bash
# カンマ区切りのCSVファイルの2列目で並べ替え
$ cat data.csv
John,25,Tokyo
Mary,30,Osaka
Bob,20,Kyoto
$ sort -t, -k2 data.csv
Bob,20,Kyoto
John,25,Tokyo
Mary,30,Osaka
```

### 重複行の削除
```bash
# -uオプションで重複を削除
$ cat duplicates.txt
apple
banana
apple
orange
$ sort -u duplicates.txt
apple
banana
orange
```

## 追加情報

- `sort`は一時的な並べ替えを行うだけで、元のファイルは変更されません。結果を保存するには、リダイレクト（`>`）を使用します：
  ```bash
  sort fruits.txt > sorted_fruits.txt
  ```

- 複数のファイルを同時に並べ替えることもできます：
  ```bash
  sort file1.txt file2.txt
  ```

- 複数の条件で並べ替えたい場合は、複数の `-k` オプションを指定できます：
  ```bash
  sort -t, -k1,1 -k2,2n data.csv  # 1列目を文字列、2列目を数値として並べ替え
  ```

- パイプ（`|`）と組み合わせて使うことも多いコマンドです：
  ```bash
  ls -l | sort -k5n  # ファイルサイズ順にディレクトリ内容を表示
  ```