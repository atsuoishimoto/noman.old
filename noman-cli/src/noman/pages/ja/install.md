# install コマンド

ファイルをコピーして属性を設定します。

## 概要

`install` コマンドは、ファイルを指定した場所にコピーしながら、権限や所有者を設定します。プログラム、スクリプト、設定ファイルをシステム内の適切な場所にインストールするために、スクリプトやMakefileでよく使用されます。

## オプション

### **-d, --directory**

ファイルをコピーする代わりに、ディレクトリ（必要に応じて親ディレクトリも）を作成します。

```console
$ install -d /tmp/new_directory
$ ls -ld /tmp/new_directory
drwxr-xr-x 2 user user 4096 May 4 10:15 /tmp/new_directory
```

### **-m, --mode=MODE**

コピー先のファイルやディレクトリのパーミッションモード（chmodと同様）を設定します。

```console
$ install -m 755 script.sh /usr/local/bin/
$ ls -l /usr/local/bin/script.sh
-rwxr-xr-x 1 root root 256 May 4 10:20 /usr/local/bin/script.sh
```

### **-o, --owner=OWNER**

コピー先のファイルの所有者を設定します（スーパーユーザー権限が必要）。

```console
$ sudo install -o nobody script.sh /usr/local/bin/
$ ls -l /usr/local/bin/script.sh
-rwxr-xr-x 1 nobody root 256 May 4 10:25 /usr/local/bin/script.sh
```

### **-g, --group=GROUP**

コピー先のファイルのグループを設定します（スーパーユーザー権限が必要）。

```console
$ sudo install -g staff script.sh /usr/local/bin/
$ ls -l /usr/local/bin/script.sh
-rwxr-xr-x 1 root staff 256 May 4 10:30 /usr/local/bin/script.sh
```

### **-s, --strip**

実行ファイルからシンボルテーブルを削除します。

```console
$ install -s myprogram /usr/local/bin/
```

### **-v, --verbose**

コピーする前に各ファイルの名前を表示します。

```console
$ install -v script.sh /usr/local/bin/
'script.sh' -> '/usr/local/bin/script.sh'
```

## 使用例

### 特定の権限でスクリプトをインストールする

```console
$ sudo install -m 755 -o root -g root myscript.sh /usr/local/bin/
$ ls -l /usr/local/bin/myscript.sh
-rwxr-xr-x 1 root root 512 May 4 10:35 /usr/local/bin/myscript.sh
```

### 複数のディレクトリを一度に作成する

```console
$ install -d -m 750 /tmp/project/{bin,lib,doc}
$ ls -ld /tmp/project/bin /tmp/project/lib /tmp/project/doc
drwxr-x--- 2 user user 4096 May 4 10:40 /tmp/project/bin
drwxr-x--- 2 user user 4096 May 4 10:40 /tmp/project/doc
drwxr-x--- 2 user user 4096 May 4 10:40 /tmp/project/lib
```

### 複数のファイルをディレクトリにインストールする

```console
$ install -m 644 config.json settings.ini /etc/myapp/
$ ls -l /etc/myapp/
-rw-r--r-- 1 root root 1024 May 4 10:45 config.json
-rw-r--r-- 1 root root 512 May 4 10:45 settings.ini
```

## ヒント:

### Makefileでの使用

`install` コマンドはソフトウェアインストール用のMakefileでよく使用されます。権限と所有権を一度に処理できるため、`cp` よりも好まれます。

### ディレクトリツリーの作成

`-d` を使用すると、存在しない親ディレクトリが自動的に作成されます。これは `mkdir -p` と同様の動作です。

### デフォルトの権限

`-m` でモードを指定しない場合、通常、実行可能ファイルには 755 (rwxr-xr-x)、実行不可能ファイルには 644 (rw-r--r--) がデフォルトとして設定されます。

### バックアップオプション

`-b` または `--backup` を使用すると、上書きする前に既存の宛先ファイルのバックアップを作成できます。

## よくある質問

#### Q1. `install` と `cp` の違いは何ですか？
A. `cp` は単にファイルをコピーするだけですが、`install` はファイルをコピーし、一つのコマンドで権限、所有権、その他の属性を設定します。システムにファイルをインストールするために特別に設計されています。

#### Q2. `install` を使ってディレクトリを作成できますか？
A. はい、`install -d` を使用すると、特定の権限を持つディレクトリを作成できます。これは `mkdir -p` に似ていますが、権限をより細かく制御できます。

#### Q3. `install` を使うにはroot権限が必要ですか？
A. システムディレクトリにインストールする場合や、`-o` または `-g` オプションで所有権を変更する場合にのみ、root権限が必要です。

#### Q4. `install` はファイル属性を保持できますか？
A. `cp -p` とは異なり、`install` は既存の属性を保持するのではなく、特定の属性を設定するように設計されています。元のファイルの属性を保持したい場合は、`cp -p` を使用してください。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html

## 改訂履歴

- 2025/05/04 初版作成