# apt-file コマンド

Debian系ディストリビューションでパッケージに含まれるファイルを検索するツール。

## 概要

`apt-file`は、Debian系Linuxディストリビューション（UbuntuやDebian）で、インストール済みまたはリポジトリ内のパッケージに含まれるファイルを検索するためのコマンドラインツールです。特定のファイルがどのパッケージに含まれているかを調べたり、インストールされていないパッケージ内のファイルを探したりする際に便利です。

## オプション

### **search**

指定したパターンに一致するファイルを含むパッケージを検索します。

```console
$ apt-file search libssl.so
libssl-dev: /usr/lib/x86_64-linux-gnu/libssl.so
libssl1.1: /usr/lib/x86_64-linux-gnu/libssl.so.1.1
```

### **list**

指定したパッケージに含まれるすべてのファイルを表示します。

```console
$ apt-file list vim
vim: /usr/bin/vim
vim: /usr/share/applications/vim.desktop
vim: /usr/share/doc/vim/changelog.Debian.gz
vim: /usr/share/doc/vim/copyright
vim: /usr/share/man/man1/vim.1.gz
```

### **update**

apt-fileのデータベースを更新します。初回使用時や最新の情報を取得するために実行します。

```console
$ sudo apt-file update
Processing 1 index files...
Processing index: 100%
```

### **-x, --regexp**

正規表現を使用してファイルを検索します。

```console
$ apt-file -x search "bin/python[0-9]"
python3.8: /usr/bin/python3.8
python3.9: /usr/bin/python3.9
python3.10: /usr/bin/python3.10
```

### **-i, --ignore-case**

大文字と小文字を区別せずに検索します。

```console
$ apt-file -i search makefile
build-essential: /usr/share/build-essential/essential-packages-list
make: /usr/share/doc/make/Makefile.example
```

## 使用例

### 特定のファイルを含むパッケージを検索

```console
$ apt-file search /usr/bin/python3
python3: /usr/bin/python3
```

### 複数のファイルパターンを検索

```console
$ apt-file search "bin/gcc" | grep -v "cpp"
gcc: /usr/bin/gcc
gcc-9: /usr/bin/gcc-9
gcc-10: /usr/bin/gcc-10
```

### インストールされていないライブラリを探す

```console
$ apt-file search libncurses.so
libncurses-dev: /usr/lib/x86_64-linux-gnu/libncurses.so
```

## ヒント:

### 初回使用時はデータベースの更新が必要

初めて`apt-file`を使用する前に、`sudo apt-file update`を実行してデータベースを更新する必要があります。これにより、最新のパッケージ情報が取得されます。

### パッケージのインストール

`apt-file`自体はデフォルトではインストールされていないため、使用前に`sudo apt install apt-file`でインストールする必要があります。

### 検索結果の絞り込み

検索結果が多すぎる場合は、`grep`と組み合わせて結果を絞り込むことができます。例：`apt-file search libssl | grep "\.so$"`

### 依存関係の解決

「コマンドが見つかりません」などのエラーが出た場合、`apt-file search`を使って必要なパッケージを特定できます。

## よくある質問

#### Q1. apt-fileとdpkgの違いは何ですか？
A. `dpkg -S`はインストール済みのパッケージのみを検索しますが、`apt-file`はリポジトリ内のすべてのパッケージ（インストールされていないものも含む）を検索できます。

#### Q2. apt-fileのデータベースはどのくらいの頻度で更新すべきですか？
A. システムの更新（`apt update`）を行った後や、最新のパッケージ情報が必要な場合に`apt-file update`を実行するとよいでしょう。

#### Q3. apt-fileの検索が遅い場合はどうすればよいですか？
A. 検索パターンをより具体的にすることで結果が絞られ、検索速度が向上します。また、正規表現を使用する場合は、できるだけ効率的なパターンを使用してください。

#### Q4. apt-fileはどのディストリビューションで使えますか？
A. Debian、Ubuntu、Linux Mintなど、Debian系のディストリビューションで使用できます。

## 参考文献

https://manpages.debian.org/buster/apt-file/apt-file.1.en.html

## 改訂履歴

- 2025/04/30 初版作成