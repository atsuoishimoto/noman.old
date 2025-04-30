# tree コマンド

ディレクトリ構造をツリー形式で表示します。

## 概要

`tree`コマンドは、ディレクトリとファイルの階層構造を視覚的に表示するツールです。ディレクトリ内のファイルやサブディレクトリを木構造（ツリー）形式で出力するため、プロジェクトの構造を把握したり、ファイル配置を確認したりする際に便利です。

## オプション

### **-L [level]**

表示する階層の深さを指定します。

```console
$ tree -L 2
.
├── documents
│   ├── personal
│   └── work
├── downloads
│   └── software
└── pictures
    ├── family
    └── vacation

7 directories, 0 files
```

### **-d**

ディレクトリのみを表示します。

```console
$ tree -d
.
├── documents
│   ├── personal
│   └── work
├── downloads
│   └── software
└── pictures
    ├── family
    └── vacation

7 directories
```

### **-a**

隠しファイル（ドットで始まるファイル）も表示します。

```console
$ tree -a
.
├── .config
│   └── .settings.json
├── documents
│   ├── personal
│   └── work
└── .gitignore

4 directories, 2 files
```

### **-I [pattern]**

指定したパターンに一致するファイルやディレクトリを除外します。

```console
$ tree -I "node_modules|.git"
.
├── package.json
├── public
│   └── index.html
└── src
    ├── App.js
    └── index.js

2 directories, 3 files
```

### **-C**

出力に色を付けます。

```console
$ tree -C
# 色付きで表示されます（実際の色はターミナルの設定によります）
```

## 使用例

### プロジェクトディレクトリの構造を表示

```console
$ tree my_project
my_project
├── README.md
├── src
│   ├── main.js
│   └── utils
│       └── helpers.js
└── tests
    └── main.test.js

3 directories, 3 files
```

### ファイルサイズを含めて表示

```console
$ tree -h
.
├── [4.0K]  documents
│   ├── [4.0K]  personal
│   └── [4.0K]  work
├── [2.1M]  image.jpg
└── [ 15K]  report.pdf

3 directories, 2 files
```

### JSONファイルのみを表示

```console
$ tree -P "*.json"
.
├── config.json
└── data
    └── settings.json

1 directory, 2 files
```

## ヒント:

### インストール方法

macOSでは、Homebrewを使ってインストールできます：`brew install tree`
Linuxでは、パッケージマネージャーを使用します：`apt install tree`（Debian/Ubuntu）または`yum install tree`（RHEL/CentOS）

### 出力をファイルに保存

`tree > structure.txt`のようにリダイレクトすることで、出力をファイルに保存できます。

### 大きなディレクトリでの使用

大きなディレクトリで実行すると出力が膨大になるため、`-L`オプションで深さを制限するか、`-I`オプションで不要なディレクトリを除外することをお勧めします。

## よくある質問

#### Q1. treeコマンドがインストールされていないとどうなりますか？
A. 「command not found」エラーが表示されます。お使いのOSのパッケージマネージャーを使ってインストールする必要があります。

#### Q2. 特定の拡張子のファイルだけを表示するにはどうすればいいですか？
A. `-P "*.拡張子"`オプションを使います。例えば、`tree -P "*.txt"`はテキストファイルのみを表示します。

#### Q3. ディレクトリの深さを制限するにはどうすればいいですか？
A. `-L 数字`オプションを使います。例えば、`tree -L 2`は2階層までのディレクトリとファイルを表示します。

#### Q4. 出力から特定のディレクトリを除外するにはどうすればいいですか？
A. `-I "パターン"`オプションを使います。例えば、`tree -I "node_modules|.git"`はnode_modulesと.gitディレクトリを除外します。

## macOSでの注意点

macOSのデフォルトバージョンのtreeコマンドは、Linuxバージョンと比べて一部のオプションが異なる場合があります。最新の機能を使用したい場合は、Homebrewを使って最新版をインストールすることをお勧めします。また、macOSでは隠しファイルの表示に関して、システムの設定によって動作が異なる場合があります。

## 参考

https://linux.die.net/man/1/tree

## 改訂履歴

- 2025/04/30 初版作成