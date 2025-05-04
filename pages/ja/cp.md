# cp コマンド

ファイルやディレクトリをソースから宛先へコピーします。

## 概要

`cp` コマンドはファイルやディレクトリをコピーするために使用します。単一のファイルを別のファイルへ、複数のファイルをディレクトリへ、またはディレクトリ全体をその内容と共にコピーすることができます。デフォルトでは、`cp` は `-f` オプションが使用されない限り既存のファイルを上書きせず、また `-R` または `-r` オプションが指定されない限りディレクトリを再帰的にコピーしません。

## オプション

### **-a, --archive**

すべてのファイル属性を保持し、ディレクトリを再帰的にコピーするアーカイブモードです。`-dR --preserve=all` と同等です。

```console
$ cp -a documents/ backup/
# documents ディレクトリの内容をすべての属性を保持して backup にコピーする
```

### **-r, -R, --recursive**

ディレクトリを再帰的にコピーします。すべてのサブディレクトリとその内容も含まれます。

```console
$ cp -r projects/ backup/
# projects ディレクトリとその中身を再帰的に backup にコピーする
```

### **-i, --interactive**

既存のファイルを上書きする前に確認を求めます。各ファイルごとに判断できます。

```console
$ cp -i report.txt backup/
cp: overwrite 'backup/report.txt'? y
# 上書きするかどうかを確認している
```

### **-f, --force**

書き込みのために開けない場合、宛先ファイルを削除して強制的にコピーします。

```console
$ cp -f important.txt backup/
# 強制的に important.txt を backup ディレクトリにコピーする
```

### **-v, --verbose**

コピーする前に各ファイル名を表示し、処理中のファイルを確認できます。

```console
$ cp -v *.txt documents/
'report.txt' -> 'documents/report.txt'
'notes.txt' -> 'documents/notes.txt'
# コピーされるファイルとその宛先が表示される
```

### **-p, --preserve**

モード、所有権、タイムスタンプなどのファイル属性を保持します。

```console
$ cp -p config.ini backup/
# ファイル属性を保持して config.ini を backup ディレクトリにコピーする
```

### **-u, --update**

ソースファイルが宛先ファイルより新しい場合、または宛先ファイルが存在しない場合にのみコピーします。

```console
$ cp -u *.txt backup/
# 新しいファイルまたは存在しないファイルのみをコピーする
```

## 使用例

### 単一ファイルのコピー

```console
$ cp report.txt backup/report.txt
# report.txt を backup ディレクトリにコピーする
```

### 複数のファイルをディレクトリにコピー

```console
$ cp file1.txt file2.txt file3.txt destination/
# 複数のファイルを destination ディレクトリにコピーする
```

### 詳細出力付きの再帰的コピー

```console
$ cp -rv projects/ backup/
'projects/main.c' -> 'backup/projects/main.c'
'projects/lib/utils.c' -> 'backup/projects/lib/utils.c'
'projects/lib/utils.h' -> 'backup/projects/lib/utils.h'
# コピーされる各ファイルの情報が表示される
```

### 属性を保持したコピー

```console
$ cp -ap documents/ archive/
# documents ディレクトリの内容をすべての属性を保持して archive にコピーする
```

## ヒント:

### 末尾のスラッシュを注意して使用する

ディレクトリをコピーする際、ソースの末尾にスラッシュをつけると「このディレクトリの内容をコピー」という意味になります：
- `cp -r dir1 dir2` は dir2 が存在する場合、dir2/dir1 を作成します
- `cp -r dir1/ dir2` は dir1 の内容を dir2 にコピーします

### 上書き前にバックアップを作成する

`--backup` オプションを使用して、ファイルを上書きする前にバックアップを作成できます：

```console
$ cp --backup=numbered important.txt destination/
# 上書き前に番号付きバックアップを作成する
```

### シンボリックリンクの扱い

デフォルトでは、`cp` はシンボリックリンクをたどります。リンク先ではなくリンク自体をコピーするには、`-P` または `--no-dereference` を使用します。

## よくある質問

#### Q1. 既存のファイルを上書きせずにファイルをコピーするにはどうすればよいですか？
A. `cp -n ソース 宛先` を使用します。これにより既存のファイルの上書きを防ぎます。

#### Q2. 隠しファイルをコピーするにはどうすればよいですか？
A. 隠しファイル（ドットで始まるファイル）は通常通りコピーされます。隠しファイルを含むすべてのファイルをコピーするには、`cp -r .* * 宛先/` のようなパターンを使用するか、隠しファイルを明示的に指定します。

#### Q3. ファイルなしでディレクトリ構造だけをコピーするにはどうすればよいですか？
A. `cp` には直接のオプションがありません。`find` と `mkdir` または `rsync --include='*/' --exclude='*'` を使用する必要があるかもしれません。

#### Q4. 権限を保持してファイルをコピーするにはどうすればよいですか？
A. モード、所有権、タイムスタンプを保持するには `cp -p` を使用し、すべての属性を保持するには `cp -a` を使用します。

## References

https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html

## Revisions

- 2025/05/04 初回リビジョン