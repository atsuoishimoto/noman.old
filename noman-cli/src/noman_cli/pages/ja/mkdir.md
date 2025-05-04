# mkdir コマンド

ディレクトリを作成します。

## 概要

`mkdir`（make directory）コマンドは、新しいディレクトリ（フォルダ）を作成するために使用されます。単一のディレクトリから複数の階層構造を持つディレクトリまで、様々なディレクトリを作成できます。

## オプション

### **-p（--parents）**

親ディレクトリが存在しない場合でも、必要に応じて親ディレクトリを作成します。

```console
$ mkdir -p projects/website/css
$ ls -l projects/
total 0
drwxr-xr-x  2 user  staff  64 May  3 10:00 website
```

### **-m（--mode）**

新しく作成するディレクトリのパーミッション（アクセス権限）を設定します。

```console
$ mkdir -m 700 private_dir
$ ls -l
total 0
drwx------  2 user  staff  64 May  3 10:05 private_dir
```

### **-v（--verbose）**

作成したディレクトリの情報を表示します。

```console
$ mkdir -v new_folder
mkdir: created directory 'new_folder'
```

## 使用例

### 基本的なディレクトリ作成

```console
$ mkdir documents
$ ls
documents
```

### 複数のディレクトリを一度に作成

```console
$ mkdir photos videos music
$ ls
music  photos  videos
```

### 階層構造のディレクトリを作成

```console
$ mkdir -p projects/webapp/src/components
$ ls -R projects
projects:
webapp

projects/webapp:
src

projects/webapp/src:
components
```

## ヒント:

### パスに空白を含むディレクトリ名

空白を含むディレクトリ名を作成する場合は、引用符で囲むか、バックスラッシュでエスケープします。

```console
$ mkdir "My Documents"
# または
$ mkdir My\ Documents
```

### 既存のディレクトリ

既に存在するディレクトリを作成しようとすると、エラーが発生します。`-p`オプションを使用すると、既存のディレクトリがあってもエラーにならず、存在しない部分だけ作成します。

### 日付付きディレクトリの作成

バックアップなどのために日付付きディレクトリを作成する場合：

```console
$ mkdir $(date +%Y-%m-%d)
$ ls
2025-05-03
```

## よくある質問

#### Q1. 既に存在するディレクトリを作成しようとするとどうなりますか？
A. エラーメッセージ「mkdir: cannot create directory 'dirname': File exists」が表示されます。`-p`オプションを使用すると、このエラーは表示されません。

#### Q2. ディレクトリに特定のパーミッションを設定するにはどうすればよいですか？
A. `-m`オプションを使用します。例えば、`mkdir -m 755 dirname`とすると、所有者に読み書き実行権限、グループとその他のユーザーに読み実行権限を与えます。

#### Q3. 複数の階層のディレクトリを一度に作成するにはどうすればよいですか？
A. `-p`オプションを使用します。例：`mkdir -p dir1/dir2/dir3`

#### Q4. 作成したディレクトリの所有者を変更するにはどうすればよいですか？
A. `mkdir`では所有者を変更できません。ディレクトリ作成後に`chown`コマンドを使用して所有者を変更します。

## 参考

https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html

## 改訂履歴

- 2025/05/03 初版作成