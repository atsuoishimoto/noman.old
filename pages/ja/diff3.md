# diff3 コマンド

3つのファイルを行ごとに比較し、差分を表示します。

## 概要

`diff3` は3つのファイルを比較して、それらの間の差分を識別するユーティリティです。特にバージョン管理システムのように、ファイルの複数のバージョンからの変更をマージする際に役立ちます。このコマンドは、各ファイルに固有の行と、ファイル間で共通する行を表示します。

## オプション

### **-A, --show-all**

すべての変更を出力し、ファイル間の競合を括弧で囲みます。

```console
$ diff3 -A file1 file2 file3
<<<<<<< file1
This is in file1
||||||| file2
This is in file2
======= 
This is in file3
>>>>>>> file3
```

### **-e, --ed**

file1からfile3へのすべての変更をfile2に組み込むedスクリプトを作成します。

```console
$ diff3 -e file1 file2 file3
w
q
```

### **-m, --merge**

edスクリプトの代わりにマージされたファイルを直接出力します。

```console
$ diff3 -m file1 file2 file3
Common text
<<<<<<< file1
Text from file1
||||||| file2
Text from file2
=======
Text from file3
>>>>>>> file3
More common text
```

### **-T, --initial-tab**

出力行の先頭にタブを付けることで、タブを揃えます。

```console
$ diff3 -T file1 file2 file3
	====1
	line from file1
	====2
	line from file2
	====3
	line from file3
```

### **-x, --overlap-only**

重複する変更のみを表示します。

```console
$ diff3 -x file1 file2 file3
====
1:1c
line in file1
2:1c
line in file2
3:1c
line in file3
```

## 使用例

### 基本的な比較

```console
$ diff3 file1 file2 file3
====
1:1c
This is file1
2:1c
This is file2
3:1c
This is file3
```

### マージファイルの作成

```console
$ diff3 -m file1 file2 file3 > merged_file
$ cat merged_file
Common text
<<<<<<< file1
Text from file1
||||||| file2
Text from file2
=======
Text from file3
>>>>>>> file3
More common text
```

### 競合の自動解決

```console
$ diff3 --merge --easy-only file1 file2 file3 > merged_file
```

## ヒント:

### 出力フォーマットの理解

標準出力では、`diff3`は差分ブロックの始まりを`====`でマークし、その後に行番号と変更タイプが続きます。例えば、`1:1c`はfile1の1行目が変更されたことを意味しています。

### 効果的なファイルのマージ

`-m`（マージ）を使用する場合、競合は`<<<<<<<`、`|||||||`、`=======`、`>>>>>>>`でマークされます。これらのセクションを手動で編集して競合を解決する必要があります。

### 競合解決の自動化

`--easy-only`と`--merge`を一緒に使用すると、競合しない変更を自動的に組み込み、真の競合のみを手動解決のために残すことができます。

### バージョン管理との連携

`diff3`は、Gitのようなバージョン管理システムでブランチ間のマージ競合を解決する際に、舞台裏でよく使用されます。

## よくある質問

#### Q1. `diff`と`diff3`の違いは何ですか？
A. `diff`は2つのファイルを比較しますが、`diff3`は3つのファイルを比較するため、複数のソースからの変更をマージするのに役立ちます。

#### Q2. `diff3`の出力をどのように解釈すればよいですか？
A. 出力には各ファイルの行番号と内容が表示されます。`====`でマークされた行は差分を示し、その後に各ファイルの行番号と内容が続きます。

#### Q3. `diff3`は競合を自動的に解決できますか？
A. 部分的にはできます。`--merge --easy-only`を使用すると、競合しない変更は自動的に解決されますが、真の競合は手動で解決する必要があります。

#### Q4. マージされた出力をファイルに保存するにはどうすればよいですか？
A. リダイレクションを使用します：`diff3 -m file1 file2 file3 > merged_file`

## 参考資料

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-diff3.html

## 改訂履歴

- 2025/05/04 初版作成