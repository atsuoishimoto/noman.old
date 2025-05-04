# touch コマンド

ファイルのタイムスタンプを作成または更新します。

## 概要

`touch`コマンドは、ファイルのタイムスタンプを変更したり、存在しない場合は空のファイルを作成したりするために使用されます。既存ファイルのアクセス時間や更新時間を現在の時刻に更新したり、新しい空のファイルを作成したりする場合によく使われます。

## オプション

### **-a, --time=atime, --time=access, --time=use**

アクセス時間のみを変更します。

```console
$ ls -l file.txt
-rw-r--r-- 1 user group 0 5月 01 10:00 file.txt
$ touch -a file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 5月 01 10:00 file.txt  # 注意: アクセス時間のみが変更され、ls -lでは表示されない
```

### **-c, --no-create**

存在しないファイルを作成しません。

```console
$ touch -c nonexistent.txt
$ ls nonexistent.txt
ls: 'nonexistent.txt' にアクセスできません: そのようなファイルやディレクトリはありません
```

### **-d, --date=文字列**

指定した文字列を解析し、現在時刻の代わりに使用します。

```console
$ touch -d "2023-12-25 12:00" file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 12月 25 2023 file.txt
```

### **-m, --time=mtime, --time=modify**

更新時間のみを変更します。

```console
$ touch -m file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 5月 04 15:30 file.txt  # 更新時間が更新された
```

### **-r, --reference=ファイル**

現在時刻の代わりに指定したファイルの時刻を使用します。

```console
$ ls -l reference.txt
-rw-r--r-- 1 user group 0 1月 15 2024 reference.txt
$ touch -r reference.txt file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 1月 15 2024 file.txt
```

## 使用例

### 複数の空ファイルを作成する

```console
$ touch file1.txt file2.txt file3.txt
$ ls
file1.txt  file2.txt  file3.txt
```

### 特定の時間にタイムスタンプを更新する

```console
$ touch -d "2 days ago" oldfile.txt
$ ls -l oldfile.txt
-rw-r--r-- 1 user group 0 5月 02 15:30 oldfile.txt
```

### 特定のパーミッションでファイルを作成する

```console
$ umask 022
$ touch newfile.txt
$ ls -l newfile.txt
-rw-r--r-- 1 user group 0 5月 04 15:30 newfile.txt
```

## ヒント:

### Makefileの依存関係に使用する

ソフトウェアをビルドする際、`touch`を使用してファイルのタイムスタンプを更新し、Makeのようなビルドシステムでの再ビルドをトリガーしたり回避したりできます。

### テスト用に特定のタイムスタンプを持つファイルを作成する

日付に依存する機能をテストする場合、`touch -d`を使用して特定のタイムスタンプを持つファイルを作成し、ソートやフィルタリングのテストに使用できます。

### タイムスタンプの一括更新

ワイルドカードを使用して複数のファイルのタイムスタンプを一度に更新できます：`touch *.txt`は現在のディレクトリ内のすべてのテキストファイルを更新します。

### ファイルの存在確認（変更なし）

`touch -c`を使用すると、存在しない場合に作成せずにファイルの存在を確認できます。

## よくある質問

#### Q1. すでに存在するファイルをtouchするとどうなりますか？
A. ファイルの内容を変更せずに、アクセス時間と更新時間を現在の時刻に更新します。

#### Q2. touchでディレクトリを作成できますか？
A. いいえ、`touch`はファイルのみ作成でき、ディレクトリは作成できません。ディレクトリを作成するには`mkdir`を使用してください。

#### Q3. 特定のタイムスタンプを持つファイルを作成するにはどうすればよいですか？
A. `touch -d "YYYY-MM-DD HH:MM:SS" ファイル名`を使用して特定のタイムスタンプを設定できます。

#### Q4. touchはファイルのパーミッションを変更しますか？
A. いいえ、`touch`はタイムスタンプのみに影響します。新しいファイルを作成する場合は、umask設定に基づいたデフォルトのパーミッションで作成されます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html

## 改訂履歴

- 2025/05/04 初版作成