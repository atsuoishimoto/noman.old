# chmod コマンド

ファイルやディレクトリのモードビット（アクセス権限）を変更します。

## 概要

`chmod`コマンドは、Unix系オペレーティングシステムにおいてファイルやディレクトリのアクセス権限を変更するために使用されます。ファイルモードビットを変更することで、誰がファイルを読み取り、書き込み、実行できるかを制御します。このコマンドはファイルのセキュリティとアクセス制御の管理に不可欠です。

## オプション

### **-R, --recursive**

権限を再帰的に変更し、指定されたディレクトリ内のすべてのファイルとサブディレクトリに影響を与えます。

```console
$ chmod -R 755 projects/
```

### **-v, --verbose**

処理されるすべてのファイルについて、行われる変更を示す診断メッセージを表示します。

```console
$ chmod -v 644 document.txt
mode of 'document.txt' changed from 0600 (rw-------) to 0644 (rw-r--r--)
```

### **-c, --changes**

verboseと似ていますが、実際に変更が行われた場合のみ報告します。

```console
$ chmod -c 644 document.txt
mode of 'document.txt' changed from 0600 (rw-------) to 0644 (rw-r--r--)
```

### **-f, --silent, --quiet**

ほとんどのエラーメッセージを抑制します。

```console
$ chmod -f 644 nonexistent.txt
```

## 使用例

### 数値（8進数）モードの使用

```console
$ chmod 755 script.sh
$ ls -l script.sh
-rwxr-xr-x 1 user group 1024 May 4 10:00 script.sh
```

### シンボリックモードの使用

```console
$ chmod u+x script.sh
$ ls -l script.sh
-rwxr--r-- 1 user group 1024 May 4 10:00 script.sh
```

### 再帰的に権限を変更する

```console
$ chmod -R go-w documents/
$ ls -l documents/
total 8
-rw-r--r-- 1 user group 1024 May 4 10:00 file1.txt
-rw-r--r-- 1 user group 2048 May 4 10:00 file2.txt
drwxr-xr-x 2 user group 4096 May 4 10:00 subfolder
```

## ヒント:

### 権限表記の理解

- 数値（8進数）モード: 
  - 1桁目: 所有者の権限（4=読取、2=書込、1=実行）
  - 2桁目: グループの権限
  - 3桁目: その他のユーザーの権限
  - 例: 755 = rwxr-xr-x（所有者は読取/書込/実行可能、グループとその他は読取/実行可能）

- シンボリックモード:
  - u: ユーザー/所有者、g: グループ、o: その他、a: すべて
  - +: 権限追加、-: 権限削除、=: 権限を正確に設定
  - r: 読取、w: 書込、x: 実行
  - 例: u+x（所有者に実行権限を追加）

### 一般的な権限パターン

- 755 (rwxr-xr-x): ディレクトリと実行可能スクリプトの標準
- 644 (rw-r--r--): 通常ファイルの標準
- 600 (rw-------): プライベートファイル（所有者のみ読取/書込可能）
- 777 (rwxrwxrwx): 全員がフルアクセス可能（注意して使用）

### 変更前の確認

特に再帰的オプションを使用する場合は、変更を行う前に`ls -l`で現在の権限を確認することをお勧めします。

## よくある質問

#### Q1. ファイルを実行可能にするにはどうすればよいですか？
A. `chmod +x ファイル名`または`chmod u+x ファイル名`を使用して、所有者のみが実行できるようにします。

#### Q2. シンボリックモードと数値モードの違いは何ですか？
A. シンボリックモード（u+xなど）はより直感的で、相対的な変更が可能です。数値モード（755など）は絶対的な権限を設定し、より簡潔です。

#### Q3. ファイルの所有者のみに読み取りと書き込みの権限を与えるにはどうすればよいですか？
A. `chmod 600 ファイル名`または`chmod u=rw,go= ファイル名`を使用します。

#### Q4. chmodでファイルの所有権を変更できますか？
A. いいえ、chmodは権限のみを変更します。ファイルの所有権を変更するには`chown`を使用してください。

#### Q5. 「Permission denied」エラーを修正するにはどうすればよいですか？
A. `chmod`でファイルの権限を変更するか、`sudo`を使用して昇格した権限でコマンドを実行します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html

## 改訂履歴

- 2025/05/04 初版作成