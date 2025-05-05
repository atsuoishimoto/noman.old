# stat コマンド

ファイルやファイルシステムの詳細な状態情報を表示します。

## 概要

`stat`コマンドは、ファイルやファイルシステムに関する詳細情報を表示します。アクセス権限、所有者、サイズ、タイムスタンプ、iノード情報などが含まれます。`ls -l`よりも包括的な情報を提供します。

## オプション

### **-f, --file-system**

ファイル情報の代わりにファイルシステムの情報を表示します。

```console
$ stat -f /home
  File: "/home"
    ID: 2f400000000000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 244033764   Free: 146937542   Available: 134209270
Inodes: Total: 62259200    Free: 60948748
```

### **-c, --format=FORMAT**

デフォルトの出力形式の代わりに指定したFORMATを使用します。

```console
$ stat -c "%n %s %y" file.txt
file.txt 1024 2025-05-01 14:30:45.123456789 +0000
```

### **-t, --terse**

情報を簡潔な形式で表示します。

```console
$ stat -t file.txt
file.txt 1024 8 81a4 1000 1000 fe01 1620000000 1620000000 1620000000 4096 8 0 0
```

### **-L, --dereference**

シンボリックリンクの情報を表示する際にリンク先をたどります。

```console
$ stat -L symlink.txt
  File: 'symlink.txt'
  Size: 1024      	Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d	Inode: 12345      Links: 1
Access: (0644/-rw-r--r--)  Uid: (1000/username)   Gid: (1000/groupname)
Access: 2025-05-01 10:00:00.000000000 +0000
Modify: 2025-05-01 10:00:00.000000000 +0000
Change: 2025-05-01 10:00:00.000000000 +0000
 Birth: 2025-05-01 10:00:00.000000000 +0000
```

## 使用例

### 基本的なファイル情報

```console
$ stat file.txt
  File: file.txt
  Size: 1024      	Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d	Inode: 12345      Links: 1
Access: (0644/-rw-r--r--)  Uid: (1000/username)   Gid: (1000/groupname)
Access: 2025-05-01 10:00:00.000000000 +0000
Modify: 2025-05-01 10:00:00.000000000 +0000
Change: 2025-05-01 10:00:00.000000000 +0000
 Birth: 2025-05-01 10:00:00.000000000 +0000
```

### カスタムフォーマットで特定の情報を表示

```console
$ stat -c "ファイル: %n, サイズ: %s バイト, 更新日時: %y" file.txt
ファイル: file.txt, サイズ: 1024 バイト, 更新日時: 2025-05-01 10:00:00.000000000 +0000
```

### ファイルシステム情報

```console
$ stat -f /
  File: "/"
    ID: 2f400000000000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 244033764   Free: 146937542   Available: 134209270
Inodes: Total: 62259200    Free: 60948748
```

## ヒント:

### 必要な情報だけを取得する

`-c`オプションとフォーマット指定子を使用して、必要な情報だけを抽出できます。例えば、`stat -c "%s" file.txt`はファイルサイズのみを表示します。

### ファイルのタイムスタンプを比較する

`stat`を使用して、ファイルが最後にアクセスされた時間、変更された時間、またはメタデータが変更された時間を確認できます。これはトラブルシューティングやファイル操作の検証に役立ちます。

### iノード情報を確認する

`stat`で表示されるiノード番号は、2つのファイルが同じデータにハードリンクされているかどうかを識別するのに役立ちます（同じiノード番号を持ちます）。

### macOSでの違い

macOSでは、フォーマットオプションが異なります。サイズには`%z`、更新時間には`%m`などのフォーマット指定子と共に`-f`を使用します。GNU形式の長いオプションは利用できません。

## よくある質問

#### Q1. `stat`と`ls -l`の違いは何ですか？
A. `stat`は`ls -l`よりも詳細な情報を提供し、正確なタイムスタンプ、iノード番号、デバイスIDなどが含まれます。ファイルメタデータ分析により包括的です。

#### Q2. ファイルサイズだけを確認するにはどうすればよいですか？
A. Linuxでは`stat -c "%s" ファイル名`、macOSでは`stat -f "%z" ファイル名`を使用します。

#### Q3. ファイルが最後に変更された時間を確認するにはどうすればよいですか？
A. Linuxでは`stat -c "%y" ファイル名`、macOSでは`stat -f "%m" ファイル名`を使用します（後者はエポックからの秒数を表示します）。

#### Q4. `stat`をディレクトリに使用できますか？
A. はい、`stat`はファイルと同様にディレクトリでも機能し、そのメタデータを表示します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html

## 改訂履歴

- 2025/05/04 初版作成