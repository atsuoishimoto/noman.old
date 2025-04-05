# `tree` コマンド概要

`tree`コマンドはディレクトリ構造を視覚的にツリー形式で表示するツールです。ファイルやフォルダの階層関係を簡単に把握することができます。

## 主なオプション

- **`-L <数字>`**: 表示する階層の深さを指定します
  - 例: `tree -L 2` (2階層までのディレクトリ構造を表示)

- **`-d`**: ディレクトリのみを表示し、ファイルは表示しません
  - 例: `tree -d` (ファイルを除外してディレクトリ構造のみ表示)

- **`-a`**: 隠しファイル（.で始まるファイル）も含めて全てのファイルを表示します
  - 例: `tree -a` (隠しファイルも含めて表示)

- **`-I <パターン>`**: 指定したパターンに一致するファイルやディレクトリを除外します
  - 例: `tree -I "node_modules"` (node_modulesディレクトリを除外)

- **`--filelimit <数字>`**: 各ディレクトリに表示するファイル数を制限します
  - 例: `tree --filelimit 5` (各ディレクトリ内は最大5ファイルまで表示)

- **`-s`**: ファイルサイズを表示します
  - 例: `tree -s` (各ファイルのサイズも表示)

- **`-h`**: ファイルサイズを人間が読みやすい形式（KB、MB、GBなど）で表示します
  - 例: `tree -sh` (読みやすい形式でサイズを表示)

## 使用例

### 基本的な使用方法
```bash
# プロジェクトディレクトリの構造を表示
tree
# 出力例
.
├── README.md
├── index.html
├── css
│   └── style.css
├── js
│   └── script.js
└── images
    ├── logo.png
    └── banner.jpg

3 directories, 5 files
```

### 階層の深さを制限
```bash
# 2階層までの構造を表示
tree -L 2
# 出力例
.
├── README.md
├── index.html
├── css
│   └── style.css
├── js
│   └── script.js
└── images
    ├── logo.png
    └── banner.jpg

3 directories, 5 files
```

### ディレクトリのみ表示
```bash
# ディレクトリ構造のみを表示
tree -d
# 出力例
.
├── css
├── js
└── images

3 directories
```

### 特定のディレクトリを除外
```bash
# node_modulesディレクトリを除外して表示
tree -I "node_modules"
# 出力例
.
├── README.md
├── index.html
├── package.json
├── css
│   └── style.css
├── js
│   └── script.js
└── images
    ├── logo.png
    └── banner.jpg

3 directories, 6 files
```

### ファイルサイズを表示
```bash
# ファイルサイズを人間が読みやすい形式で表示
tree -sh
# 出力例
.
├── [4.0K]  README.md
├── [8.2K]  index.html
├── css
│   └── [2.1K]  style.css
├── js
│   └── [1.5K]  script.js
└── images
    ├── [45K]   logo.png
    └── [128K]  banner.jpg

3 directories, 5 files
```

## 追加情報

- `tree`コマンドは多くのLinuxディストリビューションでデフォルトではインストールされていないことがあります。Ubuntu/Debianでは`apt install tree`、CentOS/Fedoraでは`yum install tree`、macOSでは`brew install tree`でインストールできます。

- 大規模なディレクトリ構造を表示する場合は、`-L`オプションで深さを制限するか、`-I`オプションで不要なディレクトリを除外すると見やすくなります。

- JSONやXML形式で出力することもできます（`-J`や`-X`オプション）。これはプログラムで処理する場合に便利です。

- カラー表示をオフにしたい場合は`-n`オプションを使用します。これはスクリプト内で使用する際に便利です。