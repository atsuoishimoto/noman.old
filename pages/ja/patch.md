# patch コマンド

差分ファイルを元のファイルに適用します。

## 概要

`patch`コマンドは、ファイルに変更（パッチ）を適用するためのコマンドです。パッチファイル（通常は`diff`コマンドで作成されたもの）を読み込み、その指示に従って元のファイルを修正します。これは、バグ修正、アップデート、ソースコードやテキストファイルの変更を適用する際によく使用されます。

## オプション

### **-p 数値, --strip=数値**

パッチファイル内のファイル名から、指定した数値分の先頭のスラッシュを含む最小のプレフィックスを削除します。

```console
$ patch -p1 < changes.patch
patching file src/main.c
```

### **-b, --backup**

パッチを適用する前に元のファイルのバックアップを作成します。

```console
$ patch -b file.txt < changes.patch
patching file file.txt
```

### **-R, --reverse**

パッチが古いファイルと新しいファイルを入れ替えて作成されたと仮定し、実質的にパッチを逆適用します。

```console
$ patch -R file.txt < changes.patch
patching file file.txt
```

### **-i パッチファイル, --input=パッチファイル**

標準入力ではなく、指定したファイルからパッチを読み込みます。

```console
$ patch -i changes.patch
patching file file.txt
```

### **-d ディレクトリ, --directory=ディレクトリ**

パッチを適用する前に指定したディレクトリに移動します。

```console
$ patch -d src/ -i ../changes.patch
patching file main.c
```

### **-u, --unified**

パッチファイルを統合差分（現在最も一般的な形式）として解釈します。

```console
$ patch -u file.txt < changes.patch
patching file file.txt
```

## 使用例

### 基本的なパッチの適用

```console
$ diff -u original.txt modified.txt > changes.patch
$ patch original.txt < changes.patch
patching file original.txt
```

### 複数ファイルへのパッチ適用

```console
$ patch -p0 < project.patch
patching file src/main.c
patching file include/header.h
```

### バックアップを作成してパッチを適用

```console
$ patch -b file.txt < changes.patch
patching file file.txt
$ ls
file.txt  file.txt.orig  changes.patch
```

### ドライラン（適用せずに確認）

```console
$ patch --dry-run -p1 < changes.patch
checking file src/main.c
```

## ヒント:

### パッチレベルの理解

`-p`オプション（ストリップレベル）は、プロジェクトにパッチを適用する際に重要です。パッチに`a/src/file.c`のようなパスが含まれている場合、`-p1`を使用すると`a/`プレフィックスが削除され、`src/file.c`を探すようになります。

### 失敗したパッチの処理

パッチがきれいに適用できない場合、patchは拒否されたハンク（変更部分）を含む`.rej`ファイルを作成します。自動的に適用できなかった変更を手動で適用するために、これらのファイルを確認してください。

### パッチを適用する前のテスト

特に重要なファイルに対しては、実際に適用する前に`--dry-run`を使用してパッチがきれいに適用されるかどうかを常にテストしてください。

### パッチの方向

`-R`（逆適用）を使用するかどうか不明な場合は、まず通常通りパッチを適用してみてください。「reversed patch detected」（逆パッチが検出された）というエラーが出た場合は、`-R`を試してみてください。

## よくある質問

#### Q1. 統合差分（unified diff）とコンテキスト差分（context diff）の違いは何ですか？
A. 統合差分（diffの`-u`オプション）は、変更された行をコンテキスト付きで`+`と`-`の接頭辞を付けて1つのブロックで表示します。一方、コンテキスト差分は変更前と変更後のブロックを別々に表示します。統合差分はよりコンパクトで、現在一般的に使用されています。

#### Q2. 適用したパッチを元に戻すにはどうすればよいですか？
A. 同じパッチファイルを使用して`patch -R`を実行すると、変更を元に戻すことができます。`-b`でバックアップを作成した場合は、それらから復元することもできます。

#### Q3. 「Hunk #1 FAILED」とはどういう意味ですか？
A. パッチの一部（ハンク）が適用できなかったことを意味します。通常、パッチが作成された後にターゲットファイルが変更されたために発生します。失敗した変更については`.rej`ファイルを確認してください。

#### Q4. 複数のファイルにパッチを適用するにはどうすればよいですか？
A. パッチファイルに複数のファイルの変更が含まれている場合、patchを実行すると自動的にすべての影響を受けるファイルに変更が適用されます。

## 参考資料

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html

## macOSでの注意点

macOSに付属のpatchコマンドはGNU patchとは若干動作が異なる場合があります。特に、パスの扱いやオプションの一部が異なることがあるため、複雑なパッチを適用する場合は注意が必要です。HomebrewなどでインストールしたGNU patchを使用することで、Linux環境と同じ動作を期待できます。

## 改訂履歴

- 2025/05/04 初版作成