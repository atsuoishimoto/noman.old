# diff3 コマンド

3つのファイル間の違いを行ごとに比較して表示します。

## 概要

`diff3`は3つのファイルを比較し、それらの間の違いを行単位で表示するコマンドです。主に、共通の元ファイルから派生した2つの異なるバージョンを比較する場合に役立ちます。これはバージョン管理システムでのマージ作業や、複数の人が同じファイルを編集した場合の変更点の確認に便利です。

## オプション

### **-m (マージ出力)**

3つのファイルをマージした結果を出力します。競合がある場合は、マークを付けて表示します。

```console
$ diff3 -m my-file.txt old-file.txt their-file.txt
<<<<<<< my-file.txt
私の変更内容
||||||| old-file.txt
元の内容
=======
彼らの変更内容
>>>>>>> their-file.txt
```

### **-A, --show-all**

すべての変更を統合して表示します。競合部分は特殊なマーカーで区切られます。

```console
$ diff3 -A my-file.txt old-file.txt their-file.txt
すべての内容が表示される
<<<<<<< my-file.txt
私の変更内容
||||||| old-file.txt
元の内容
=======
彼らの変更内容
>>>>>>> their-file.txt
その後の共通部分
```

### **-e, --ed**

`ed`エディタ形式の出力を生成します。これはスクリプトとして使用して変更を適用できます。

```console
$ diff3 -e my-file.txt old-file.txt their-file.txt
w
q
```

### **-T, --initial-tab**

出力の各行の先頭にタブを挿入して、見やすくします。

```console
$ diff3 -T my-file.txt old-file.txt their-file.txt
	====
	1:1c
	  私の行
	2:1c
	  元の行
	3:1c
	  彼らの行
```

## 使用例

### 基本的な3ファイル比較

```console
$ diff3 file1.txt original.txt file2.txt
====
1:1c
  file1の変更された行
2:1c
  originalの元の行
3:1c
  file2の変更された行
```

### マージ結果をファイルに保存

```console
$ diff3 -m file1.txt original.txt file2.txt > merged.txt
$ cat merged.txt
ファイルの共通部分
<<<<<<< file1.txt
file1の変更部分
||||||| original.txt
originalの元の部分
=======
file2の変更部分
>>>>>>> file2.txt
その後の共通部分
```

### 競合のないマージ

```console
$ diff3 -m file1.txt original.txt file2.txt
# 競合がない場合は、マージされた内容がそのまま表示される
```

## ヒント:

### 引数の順序に注意

`diff3`の引数の順序は重要です。通常は「my-file original-file other-file」の順で指定します。元ファイル（original）を中央に置くことで、2つの派生ファイルとの比較が明確になります。

### バージョン管理システムとの連携

多くのバージョン管理システム（Git、Mercurialなど）は内部で`diff3`のようなアルゴリズムを使用しています。マージ競合を手動で解決する際の参考として`diff3`の出力を確認すると役立つことがあります。

### 大きなファイルの比較

大きなファイルを比較する場合は、`-T`オプションを使用すると出力が見やすくなります。また、結果をファイルにリダイレクトして後で確認することも検討してください。

## よくある質問

#### Q1. `diff`と`diff3`の違いは何ですか？
A. `diff`は2つのファイルを比較するのに対し、`diff3`は3つのファイルを比較します。`diff3`は共通の元ファイルから派生した2つのファイルの変更を比較するのに特に役立ちます。

#### Q2. マージ結果から競合マーカーを削除するには？
A. マージ結果から競合マーカーを削除するには、テキストエディタで手動で編集するか、`sed`や`awk`などのテキスト処理ツールを使用して削除できます。

#### Q3. `diff3`の出力形式を変更できますか？
A. はい、`-e`（ed形式）、`-x`（拡張ed形式）、`-3`（3列形式）、`-A`（すべて表示）など、様々な出力形式のオプションがあります。

#### Q4. macOSでの`diff3`は GNU版と違いがありますか？
A. macOSの`diff3`は BSD版であり、GNU版と比べていくつかのオプションが異なる場合があります。特に高度な機能を使用する場合は、`man diff3`でオプションを確認することをお勧めします。

## 参考資料

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-diff3.html

## 改訂履歴

- 2025/04/30 初版作成