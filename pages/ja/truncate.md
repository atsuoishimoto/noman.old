# truncate コマンド

ファイルのサイズを指定したサイズに変更します。

## 概要

`truncate`コマンドは、ファイルのサイズを指定したサイズに変更するためのコマンドです。ファイルを拡大または縮小することができ、新しいファイルを作成することも可能です。主に、特定のサイズのテストファイルを作成したり、ログファイルを空にしたりする場合に便利です。

## オプション

### **-s, --size=SIZE**

ファイルのサイズを指定します。数値の前に「+」や「-」を付けると、現在のサイズから相対的に変更できます。

```console
$ # 10MBのテストファイルを作成する
$ truncate -s 10M test.txt
$ ls -lh test.txt
-rw-r--r-- 1 user group 10M 4月 30 12:34 test.txt
```

### **-c, --no-create**

存在しないファイルを作成しません。

```console
$ # 存在しないファイルは作成しない
$ truncate -c -s 5M nonexistent.txt
truncate: 'nonexistent.txt' を開けません: そのようなファイルやディレクトリはありません
```

### **-o, --io-blocks**

SIZE をIO ブロックサイズとして扱います。

```console
$ # IOブロックサイズ（通常512バイト）を単位として指定
$ truncate -o -s 10 blockfile.txt
$ ls -lh blockfile.txt
-rw-r--r-- 1 user group 5.0K 4月 30 12:35 blockfile.txt
```

### **-r, --reference=RFILE**

指定したRFILEと同じサイズにします。

```console
$ # 既存のファイルと同じサイズにする
$ truncate -s 1M reference.txt
$ truncate -r reference.txt target.txt
$ ls -lh reference.txt target.txt
-rw-r--r-- 1 user group 1.0M 4月 30 12:36 reference.txt
-rw-r--r-- 1 user group 1.0M 4月 30 12:36 target.txt
```

## 使用例

### ファイルを特定のサイズに設定

```console
$ # 空のファイルを作成（サイズ0）
$ truncate -s 0 empty.txt

$ # 100MBのテストファイルを作成
$ truncate -s 100M large_file.txt
$ ls -lh large_file.txt
-rw-r--r-- 1 user group 100M 4月 30 12:37 large_file.txt
```

### ファイルサイズを相対的に変更

```console
$ # 既存のファイルに5MBを追加
$ truncate -s +5M large_file.txt
$ ls -lh large_file.txt
-rw-r--r-- 1 user group 105M 4月 30 12:38 large_file.txt

$ # 既存のファイルから10MBを削除
$ truncate -s -10M large_file.txt
$ ls -lh large_file.txt
-rw-r--r-- 1 user group 95M 4月 30 12:38 large_file.txt
```

### ログファイルを空にする

```console
$ # ログファイルを空にする（サイズを0にする）
$ truncate -s 0 app.log
$ ls -lh app.log
-rw-r--r-- 1 user group 0 4月 30 12:39 app.log
```

## ヒント:

### スパースファイルの作成

`truncate`で大きなファイルを作成すると、実際のディスク使用量は少なくなります。これはスパースファイルと呼ばれ、実際にデータが書き込まれるまでディスク容量を消費しません。

### サイズの単位

サイズ指定には、K（キロバイト）、M（メガバイト）、G（ギガバイト）などの単位を使用できます。例えば、`-s 10M`は10メガバイトを意味します。

### ログローテーション

`truncate -s 0`を使用すると、ログファイルを削除せずに内容だけを空にできます。これにより、ファイルのパーミッションや所有権を保持したままログをクリアできます。

## よくある質問

#### Q1. `truncate`と`touch`の違いは何ですか？
A. `touch`は主にファイルのタイムスタンプを更新するためのコマンドで、存在しない場合は空のファイルを作成しますが、サイズを変更する機能はありません。一方、`truncate`は明示的にファイルサイズを変更するためのコマンドです。

#### Q2. `truncate`でファイルを縮小すると、データはどうなりますか？
A. ファイルを縮小すると、指定したサイズを超える部分のデータは失われます。この操作は元に戻せないので注意が必要です。

#### Q3. `truncate`で作成した大きなファイルは実際にディスク容量を消費しますか？
A. いいえ、`truncate`で作成したファイルはスパースファイルとなり、実際にデータが書き込まれるまでディスク容量をほとんど消費しません。`du -h`コマンドで確認すると、実際の使用量が表示されます。

#### Q4. ファイルを拡大した場合、追加された部分には何が入りますか？
A. 拡大された部分には通常、ヌル（0）バイトが埋められます。これらは読み込むと0として扱われます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html

## Revisions

- 2025/04/30 初版作成