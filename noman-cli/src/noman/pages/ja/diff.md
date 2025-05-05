# diff コマンド

ファイルを行ごとに比較します。

## 概要

`diff` コマンドは2つのファイルやディレクトリを比較し、その違いを表示します。ファイルの変更内容の確認、パッチファイルの作成、設定ファイルの比較などによく使用されます。出力結果は、ファイルを同一にするために変更が必要な行を示します。

## オプション

### **-u, --unified**

統一フォーマットで差分を出力し、変更箇所の前後に文脈を表示します。これは最も読みやすく、一般的に使用されるフォーマットです。

```console
$ diff -u file1.txt file2.txt
--- file1.txt	2025-05-04 10:00:00.000000000 -0400
+++ file2.txt	2025-05-04 10:30:00.000000000 -0400
@@ -1,3 +1,4 @@
 This is a test file.
-It has some content.
+It has some modified content.
 The end of the file.
+A new line was added.
```

### **-i, --ignore-case**

ファイル比較時に大文字と小文字の違いを無視します。

```console
$ diff -i uppercase.txt lowercase.txt
[大文字小文字のみが異なる場合は出力なし]
```

### **-b, --ignore-space-change**

空白の量の変化を無視します。

```console
$ diff -b spaced.txt compact.txt
[スペースの違いのみの場合は出力なし]
```

### **-w, --ignore-all-space**

行を比較する際にすべての空白を無視します。

```console
$ diff -w file1.txt file2.txt
[空白のみが異なる場合は出力なし]
```

### **-r, --recursive**

見つかったサブディレクトリを再帰的に比較します。

```console
$ diff -r dir1 dir2
Only in dir1: unique_file1.txt
Only in dir2: unique_file2.txt
diff -r dir1/common.txt dir2/common.txt
1c1
< Original content
---
> Modified content
```

### **-q, --brief**

ファイルが異なるかどうかのみを報告し、違いの詳細は表示しません。

```console
$ diff -q file1.txt file2.txt
Files file1.txt and file2.txt differ
```

## 使用例

### 基本的なファイル比較

```console
$ diff file1.txt file2.txt
2c2
< It has some content.
---
> It has some modified content.
3a4
> A new line was added.
```

### パッチファイルの作成

```console
$ diff -u original.txt modified.txt > changes.patch
$ patch original.txt < changes.patch
patching file original.txt
```

### ディレクトリの比較

```console
$ diff -r project_v1 project_v2
Only in project_v2: new_feature.py
diff -r project_v1/main.py project_v2/main.py
10c10,12
< print("Hello World")
---
> print("Hello World!")
> print("Version 2.0")
> print("Copyright 2025")
```

### 横並び比較

```console
$ diff -y file1.txt file2.txt
This is a test file.                 This is a test file.
It has some content.               | It has some modified content.
The end of the file.                 The end of the file.
                                   > A new line was added.
```

## ヒント:

### 読みやすさを向上させるためのカラー表示

多くのシステムには `colordiff` がインストールされており、diff出力にカラーハイライトを追加できます：

```console
$ colordiff -u file1.txt file2.txt
```

### コンテキスト制御

`-U NUM` または `--unified=NUM` で表示されるコンテキストの量を制御できます：

```console
$ diff -U1 file1.txt file2.txt
```

### バージョン管理ファイルを無視する

ディレクトリを比較する際に、`--exclude=PATTERN` を使用して特定のファイルを無視できます：

```console
$ diff -r --exclude=".git" dir1 dir2
```

### バージョン管理システムでの使用

バージョン管理システムには独自のdiffツールがありますが、外部diffを使用することもできます：

```console
$ git diff --no-index --external-diff=diff -u file1.txt file2.txt
```

## よくある質問

#### Q1. diffの出力に表示される記号の意味は何ですか？
A. 通常の出力では、`a`は追加、`d`は削除、`c`は変更を意味します。`<`で始まる行は最初のファイルからの行、`>`は2番目のファイルからの行、`---`は変更を区切ります。

#### Q2. diffの出力をより読みやすくするにはどうすればよいですか？
A. 統一フォーマット（`-u`）または横並びフォーマット（`-y`）を使用してください。カラー出力には、可能であれば`colordiff`を使用します。

#### Q3. 後で適用できるパッチファイルを作成するにはどうすればよいですか？
A. `diff -u 元のファイル 変更後のファイル > パッチファイル.patch`を使用し、その後`patch 元のファイル < パッチファイル.patch`で適用します。

#### Q4. diffはバイナリファイルを比較できますか？
A. デフォルトでは、diffはテキストファイル用です。バイナリファイルの場合は、`cmp`や`xxdiff`、`hexdump`とdiffを組み合わせた特殊なツールの使用を検討してください。

## 参考資料

https://www.gnu.org/software/diffutils/manual/html_node/diff.html

## 改訂履歴

- 2025/05/04 初版作成