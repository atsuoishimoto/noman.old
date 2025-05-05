# tree コマンド

ディレクトリの内容をツリー状のフォーマットで表示し、ディレクトリとファイルの階層構造を視覚化します。

## 概要

`tree` コマンドは、ディレクトリの内容を再帰的にツリー状のフォーマットで表示します。ファイルとディレクトリをインデントと接続線で表示することで階層構造を表現し、ファイルがどのように整理されているかを明確に把握できます。

## オプション

### **-a, --all**

隠しファイル（ドットで始まるファイル）を含むすべてのファイルを表示します

```console
$ tree -a
.
├── .git
│   ├── HEAD
│   ├── config
│   └── hooks
├── README.md
└── src
    ├── .env
    └── main.js

3 directories, 5 files
```

### **-d, --dirs-only**

ファイルを除き、ディレクトリのみをリストします

```console
$ tree -d
.
├── docs
├── node_modules
│   ├── express
│   └── lodash
└── src
    └── components

5 directories
```

### **-L, --level [level]**

ディレクトリの再帰の深さを指定したレベルに制限します

```console
$ tree -L 2
.
├── docs
├── node_modules
│   ├── express
│   └── lodash
├── package.json
└── src
    ├── components
    └── index.js

5 directories, 2 files
```

### **-I, --ignore [pattern]**

パターンに一致するファイル/ディレクトリを無視します（シェルのグロブパターンを使用）

```console
$ tree -I "node_modules"
.
├── docs
├── package.json
└── src
    ├── components
    │   └── Button.js
    └── index.js

3 directories, 3 files
```

### **-C, --color**

カラー出力を有効にします

```console
$ tree -C
```

### **-F, --classify**

エントリに識別子を追加します（ディレクトリには/、実行可能ファイルには*など）

```console
$ tree -F
.
├── docs/
├── package.json
└── src/
    ├── components/
    │   └── Button.js
    └── index.js*

3 directories, 3 files
```

### **-h, --human-readable**

サイズを人間が読みやすい形式で表示します（例：1K、234M、2G）

```console
$ tree -h
.
├── [4.0K]  docs
├── [ 340]  package.json
└── [4.0K]  src
    ├── [4.0K]  components
    │   └── [1.2K]  Button.js
    └── [ 256]  index.js

3 directories, 3 files
```

## 使用例

### 基本的なディレクトリリスト

```console
$ tree
.
├── docs
│   └── README.md
├── package.json
└── src
    ├── components
    │   └── Button.js
    └── index.js

3 directories, 3 files
```

### 深さを制限して特定のファイルタイプのみを表示

```console
$ tree -L 2 --prune -P "*.js"
.
├── package.json
└── src
    ├── components
    └── index.js

2 directories, 2 files
```

### 人間が読みやすい形式でファイルサイズを表示

```console
$ tree -h --du
.
├── [4.0K]  docs
│   └── [ 340]  README.md
├── [ 340]  package.json
└── [5.5K]  src
    ├── [4.3K]  components
    │   └── [1.2K]  Button.js
    └── [ 256]  index.js

3 directories, 3 files
```

## ヒント:

### ツリー出力をファイルに保存する

ドキュメント作成のために出力をファイルにリダイレクトできます：
```console
$ tree > directory_structure.txt
```

### 複数のパターンを除外する

複数の `-I` オプションを使用するか、パイプで区切ったパターンを使用します：
```console
$ tree -I "node_modules|*.log|.git"
```

### 大きなディレクトリを見つける

`-h` と `--du` を組み合わせて、ディレクトリサイズを表示し、容量を多く消費しているディレクトリを特定します：
```console
$ tree -h --du -d
```

### カスタム出力フォーマット

ディレクトリ構造をプログラム的に処理する必要がある場合は、JSON出力用の `-J` またはXML出力用の `-X` を使用します。

## よくある質問

#### Q1. システムにtreeをインストールするにはどうすればよいですか？
A. Debian/Ubuntuでは `sudo apt install tree`、macOSのHomebrewでは `brew install tree`、CentOS/RHELでは `sudo yum install tree` を実行します。

#### Q2. 表示するディレクトリの深さを制限するにはどうすればよいですか？
A. `-L` オプションの後に深さのレベルを指定します：`tree -L 2` は2レベルの深さまでしか表示しません。

#### Q3. 特定のディレクトリを出力から除外するにはどうすればよいですか？
A. `-I` オプションの後にパターンを指定します：`tree -I "node_modules"` はnode_modulesディレクトリを除外します。

#### Q4. ディレクトリのみを表示するにはどうすればよいですか？
A. `-d` オプションを使用します：`tree -d` はファイルを除いてディレクトリのみを表示します。

#### Q5. 隠しファイルを表示するにはどうすればよいですか？
A. `-a` オプションを使用します：`tree -a` は隠しファイルを含むすべてのファイルを表示します。

## References

https://linux.die.net/man/1/tree

## Revisions

- 2025/05/04 初回リビジョン