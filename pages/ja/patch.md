# patch コマンド

ファイルに差分（パッチ）を適用するユーティリティ。

## 概要

`patch`コマンドは、差分ファイル（パッチファイル）を使用して元のファイルを更新するためのツールです。ソフトウェア開発やシステム管理において、コードの変更を配布したり適用したりする際によく使用されます。`diff`コマンドで生成された差分を適用するのに最適です。

## オプション

### **-p[数字]**

パッチファイル内のパス名から取り除く階層の数を指定します。

```console
$ patch -p1 < changes.patch
patching file src/main.c
```

### **-b, --backup**

パッチを適用する前にオリジナルファイルのバックアップを作成します。

```console
$ patch -b file.txt < file.patch
patching file file.txt
$ ls
file.txt file.txt.orig file.patch
```

### **-R, --reverse**

パッチを逆方向に適用します（変更を元に戻す）。

```console
$ patch -R file.txt < file.patch
patching file file.txt
```

### **-d DIR, --directory=DIR**

指定したディレクトリに移動してからパッチを適用します。

```console
$ patch -d src/ < changes.patch
patching file main.c
```

## 使用例

### 基本的なパッチの適用

```console
$ diff -u original.txt modified.txt > changes.patch
$ patch < changes.patch
patching file original.txt
```

### 特定のファイルにパッチを適用

```console
$ patch file.txt < changes.patch
patching file file.txt
```

### 複数のファイルを含むパッチの適用

```console
$ patch -p0 < project.patch
patching file src/main.c
patching file include/header.h
```

## ヒント:

### パッチの確認

パッチを適用する前に、`--dry-run`オプションを使用して実際に変更を加えずにパッチの適用をシミュレーションできます。

```console
$ patch --dry-run < changes.patch
patching file src/main.c
```

### 拒否されたパッチの処理

パッチの適用に失敗した場合、`.rej`拡張子を持つ拒否ファイルが作成されます。これらのファイルを確認して手動で変更を適用することができます。

### パッチの作成

パッチファイルは通常、`diff -u`コマンドを使用して作成します。これにより、コンテキスト情報を含む統一形式の差分が生成されます。

```console
$ diff -u original.txt modified.txt > changes.patch
```

## よくある質問

#### Q1. パッチファイルとは何ですか？
A. パッチファイルは、ファイルの元のバージョンと変更後のバージョンの間の差分を含むテキストファイルです。通常、`diff`コマンドで生成されます。

#### Q2. パッチの適用に失敗した場合はどうすればよいですか？
A. パッチの適用に失敗すると、`.rej`ファイルが作成されます。このファイルを確認して、変更を手動で適用することができます。また、`-f`オプションを使用して強制的に適用することもできますが、注意が必要です。

#### Q3. パッチを元に戻すにはどうすればよいですか？
A. `-R`または`--reverse`オプションを使用して、同じパッチファイルで変更を元に戻すことができます。

#### Q4. パッチファイルの形式にはどのようなものがありますか？
A. 一般的なパッチ形式には、コンテキスト形式（`diff -c`）、統一形式（`diff -u`）、通常形式（`diff`）があります。統一形式が最も一般的で推奨されています。

## 参考

https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html

## Revisions

- 2025/04/30 初版作成