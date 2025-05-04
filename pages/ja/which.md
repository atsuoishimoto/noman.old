# which コマンド

PATH環境変数を検索してコマンドの場所を特定します。

## 概要

`which`コマンドは、PATHに含まれる実行可能ファイルの場所を見つけます。コマンドラインでプログラム名を入力した際にどのバージョンが実行されるかを判断するのに役立ち、実行ファイルへのフルパスを表示します。

## オプション

### **-a, --all**

PATHに含まれる一致する全ての実行ファイルを表示します（最初の一つだけではなく）。

```console
$ which -a python
/usr/bin/python
/usr/local/bin/python
```

### **-s, --silent, --quiet**

通常の出力を抑制します。実行ファイルが見つかった場合は終了ステータス0を、見つからなかった場合は1を返します。

```console
$ which -s python
$ echo $?
0
```

### **-v, --version**

バージョン情報を表示して終了します。

```console
$ which --version
GNU which v2.21, Copyright (C) 1999 - 2015 Carlo Wood.
```

## 使用例

### 基本的な使い方

```console
$ which ls
/bin/ls
```

### 複数のコマンドを一度に検索

```console
$ which bash python grep
/bin/bash
/usr/bin/python
/bin/grep
```

### 他のコマンドと組み合わせる

```console
$ file $(which python)
/usr/bin/python: symbolic link to python3
```

## ヒント:

### コマンドが存在するか確認する

条件文と組み合わせて、コマンドを使用する前に利用可能かどうかを確認できます：

```console
$ if which git >/dev/null; then echo "Gitがインストールされています"; else echo "Gitがインストールされていません"; fi
Gitがインストールされています
```

### より詳細な情報を得るために`type`と組み合わせる

`type`コマンドはコマンドについてより詳細な情報（ビルトイン、エイリアス、実行ファイルなど）を提供します：

```console
$ type ls
ls is aliased to `ls --color=auto'
```

### PATHの順序が重要

PATHで最初に一致する実行ファイルが実行されます。`which -a`を使用すると、可能な全ての一致を確認できます。

## よくある質問

#### Q1. `which`と`whereis`の違いは何ですか？
A. `which`はPATH内の実行ファイルの場所のみを表示しますが、`whereis`はマニュアルページやソースファイルも検索します。

#### Q2. なぜ`which`はシェルのビルトインやエイリアスを見つけられないのですか？
A. `which`はPATH内の実行ファイルのみを検索します。シェルのビルトイン、エイリアス、関数については、代わりに`type`コマンドを使用してください。

#### Q3. PATH内のコマンドの全てのインスタンスを見つけるにはどうすればよいですか？
A. `which -a コマンド名`を使用すると、最初の一つだけでなく、一致する全ての実行ファイルを表示できます。

#### Q4. なぜ`which`が何も返さないことがあるのですか？
A. `which`が何も返さない場合、そのコマンドはPATH内に存在しないか、シェルのビルトインやエイリアスである可能性があります。

## macOSに関する注意点

macOSでは、`which`コマンドの動作がLinuxシステムとは異なる場合があります。macOSバージョンでは`--all`などのGNUオプションをすべてサポートしていません（ただし`-a`は機能します）。システム間でより一貫した動作を得るには、POSIX準拠の代替手段である`command -v`の使用を検討してください。

## 参考資料

https://man7.org/linux/man-pages/man1/which.1.html

## 改訂履歴

2025/05/04 初版作成