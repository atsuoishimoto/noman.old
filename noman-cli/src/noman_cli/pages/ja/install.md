# install コマンド

ファイルをコピーし、モード、所有者、グループを設定するコマンドです。

## 概要

`install` コマンドは、ファイルをコピーして、同時にパーミッション（アクセス権限）、所有者、グループを設定できるユーティリティです。主にソフトウェアのインストールスクリプトで使用され、実行可能ファイルやライブラリ、設定ファイルなどを適切な場所に配置する際に便利です。`cp` コマンドの拡張版と考えることができます。

## オプション

### **-m, --mode=MODE**

コピー先のファイルのパーミッションを設定します。

```console
$ install -m 755 myprogram /usr/local/bin/
# myprogram を /usr/local/bin/ にコピーし、実行権限を付与する
```

### **-o, --owner=OWNER**

コピー先のファイルの所有者を設定します（通常はroot権限が必要）。

```console
$ sudo install -o root myfile /etc/
# myfile を /etc/ にコピーし、所有者を root に設定する
```

### **-g, --group=GROUP**

コピー先のファイルのグループを設定します（通常はroot権限が必要）。

```console
$ sudo install -g wheel myfile /usr/local/etc/
# myfile を /usr/local/etc/ にコピーし、グループを wheel に設定する
```

### **-d, --directory**

指定したディレクトリを作成します（存在しない場合）。

```console
$ install -d -m 755 /path/to/new/directory
# 新しいディレクトリを作成し、パーミッションを 755 に設定する
```

### **-s, --strip**

バイナリファイルからシンボルテーブルを削除します。

```console
$ install -s myprogram /usr/local/bin/
# シンボル情報を削除してバイナリサイズを小さくしてからコピーする
```

## 使用例

### 実行可能ファイルのインストール

```console
$ sudo install -m 755 myprogram /usr/local/bin/
# myprogram を /usr/local/bin/ にコピーし、実行権限を付与する
```

### 設定ファイルのインストール

```console
$ sudo install -m 644 -o root -g wheel config.conf /etc/
# config.conf を /etc/ にコピーし、パーミッションを 644、所有者を root、グループを wheel に設定する
```

### 複数のディレクトリを一度に作成

```console
$ install -d -m 755 dir1 dir2 dir3
# dir1、dir2、dir3 ディレクトリを作成し、パーミッションを 755 に設定する
```

### バックアップの作成

```console
$ install -b config.conf /etc/
# config.conf を /etc/ にコピーし、既存のファイルがある場合はバックアップを作成する
```

## ヒント:

### cp コマンドとの違い

`install` コマンドは `cp` コマンドと似ていますが、一度の操作でパーミッション設定や所有者変更ができるため、システムファイルのインストールに適しています。

### Makefile での利用

ソフトウェアの `Makefile` では、`install` コマンドがよく使われます。これにより、ビルドしたバイナリを適切な権限で正しい場所にインストールできます。

### ディレクトリ構造の作成

`install -d` は `mkdir -p` と似ていますが、同時にパーミッションも設定できるため、セキュアなディレクトリ構造を作成する際に便利です。

## よくある質問

#### Q1. install コマンドと cp コマンドの主な違いは何ですか？
A. `install` はファイルのコピーと同時にパーミッション、所有者、グループを設定できます。また、ディレクトリの作成やバイナリのストリップなど、ソフトウェアインストール向けの機能があります。

#### Q2. sudo を使わずに install コマンドを実行できますか？
A. はい、自分が所有するディレクトリ内であれば `sudo` なしで実行できます。ただし、所有者やグループを変更する場合や、システムディレクトリにファイルをコピーする場合は `sudo` が必要です。

#### Q3. install コマンドでディレクトリ全体をコピーできますか？
A. いいえ、`install` は基本的に単一ファイルのコピーに対応しています。ディレクトリ全体をコピーするには、`cp -r` や `rsync` などの他のコマンドを使用するか、シェルスクリプトで個別のファイルに対して `install` を実行する必要があります。

#### Q4. install -d と mkdir -p の違いは何ですか？
A. どちらも必要に応じて親ディレクトリを作成しますが、`install -d` はパーミッションも同時に設定できます。`mkdir -p` の後に `chmod` を実行するのと同等です。

## macOS での注意点

macOSの `install` コマンドは GNU バージョンと若干異なる場合があります。特に、一部のオプション（`--compare`、`--preserve-timestamps` など）がサポートされていない可能性があります。macOS で GNU 互換の `install` コマンドを使用したい場合は、Homebrew などのパッケージマネージャで `coreutils` をインストールし、`ginstall` として使用できます。

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html

## 改訂履歴

- 2025/04/30 初版作成