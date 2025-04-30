# mv コマンド

ファイルやディレクトリを移動（名前変更）するためのコマンド。

## 概要

`mv`（move）コマンドは、ファイルやディレクトリを別の場所に移動したり、名前を変更したりするために使用します。基本的な構文は `mv 元ファイル 移動先` です。移動先が既存のディレクトリの場合、ファイルはそのディレクトリ内に移動されます。移動先が存在しないか、ファイル名の場合は、名前の変更として機能します。

## オプション

### **-i（interactive）**

上書き前に確認を求めます。

```console
$ mv -i file.txt existing-file.txt
mv: overwrite 'existing-file.txt'? y
```

### **-f（force）**

確認なしで強制的に上書きします。

```console
$ mv -f file.txt existing-file.txt
```

### **-n（no-clobber）**

既存のファイルを上書きしません。

```console
$ mv -n file.txt existing-file.txt
```

### **-v（verbose）**

実行内容を詳細に表示します。

```console
$ mv -v file.txt documents/
'file.txt' -> 'documents/file.txt'
```

### **-b（backup）**

上書きする前にバックアップを作成します。

```console
$ mv -b file.txt existing-file.txt
```

## 使用例

### ファイルの移動

```console
$ mv document.txt ~/Documents/
```

ファイル `document.txt` をホームディレクトリの Documents フォルダに移動している。

### ファイル名の変更

```console
$ mv old-name.txt new-name.txt
```

ファイル名を `old-name.txt` から `new-name.txt` に変更している。

### 複数ファイルの移動

```console
$ mv file1.txt file2.txt file3.txt destination/
```

複数のファイルを一度に指定のディレクトリに移動している。

### ディレクトリの移動

```console
$ mv source_directory/ destination_directory/
```

ディレクトリ全体を別の場所に移動している。

## ヒント:

### バックアップを作成しながら移動

```console
$ mv -b important.txt new-location/
```

重要なファイルを移動する際は `-b` オプションを使用してバックアップを作成すると安全です。

### ワイルドカードの活用

```console
$ mv *.jpg Photos/
```

特定のパターンに一致するすべてのファイル（この例では JPG 画像）を一度に移動できます。

### 上書き確認の習慣化

重要なファイルを扱う際は `-i` オプションを使用して、誤って上書きしないよう確認する習慣をつけましょう。

## よくある質問

#### Q1. `mv` コマンドでファイルを誤って上書きしてしまった場合、元に戻せますか？
A. 通常は戻せません。`-b` オプションを使用していない限り、上書きされたデータは失われます。重要なファイルを扱う際は `-i` オプションを使用するか、バックアップを作成することをお勧めします。

#### Q2. ディレクトリ内のすべてのファイルを移動するには？
A. `mv directory/* destination/` のようにワイルドカード（`*`）を使用できます。ただし、隠しファイル（ドットで始まるファイル）は含まれないため注意が必要です。

#### Q3. `mv` と `cp` の違いは何ですか？
A. `mv` はファイルを移動または名前変更し、元の場所からファイルが削除されます。一方、`cp` はファイルをコピーするため、元のファイルはそのまま残ります。

#### Q4. 移動先に同名のファイルが存在する場合どうなりますか？
A. デフォルトでは確認なしに上書きされます。`-i` オプションを使用すると確認メッセージが表示され、`-n` オプションを使用すると上書きを防止できます。

## 参考

https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html

## 改訂履歴

- 2025/04/30 初版作成