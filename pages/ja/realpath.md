# realpath コマンド

ファイルやディレクトリの絶対パス（正規化されたフルパス）を表示します。

## 概要

`realpath`コマンドは、指定されたファイルやディレクトリの絶対パスを表示します。シンボリックリンクを解決し、相対パスを絶対パスに変換することができます。これにより、ファイルの実際の場所を正確に把握することができます。

## オプション

### **-s, --strip, --no-symlinks**

シンボリックリンクを解決せず、絶対パスのみを表示します。

```console
$ ln -s /etc/hosts symlink_to_hosts
$ realpath -s symlink_to_hosts
/home/user/symlink_to_hosts
```

### **-e, --canonicalize-existing**

パス上のすべてのコンポーネント（ディレクトリなど）が存在する必要があります。存在しない場合はエラーになります。

```console
$ realpath -e /path/to/nonexistent
realpath: /path/to/nonexistent: No such file or directory
```

### **-m, --canonicalize-missing**

パス上に存在しないコンポーネントがあっても処理を続行します。

```console
$ realpath -m /path/to/nonexistent
/path/to/nonexistent
```

### **-L, --logical**

シンボリックリンクを解決します（デフォルトの動作）。

```console
$ ln -s /etc/hosts symlink_to_hosts
$ realpath -L symlink_to_hosts
/etc/hosts
```

### **-P, --physical**

すべてのシンボリックリンクを解決します。

```console
$ realpath -P symlink_to_hosts
/etc/hosts
```

### **--relative-to=DIR**

指定したディレクトリからの相対パスを表示します。

```console
$ realpath --relative-to=/etc /etc/hosts
hosts
```

### **--relative-base=DIR**

指定したディレクトリを基準として相対パスを表示します。指定したディレクトリの子ディレクトリでない場合は絶対パスを表示します。

```console
$ realpath --relative-base=/etc /etc/hosts
hosts
$ realpath --relative-base=/etc /var/log
/var/log
```

## 使用例

### 基本的な使用方法

```console
$ realpath file.txt
/home/user/documents/file.txt
```

### シンボリックリンクの解決

```console
$ ln -s /etc/hosts symlink_to_hosts
$ realpath symlink_to_hosts
/etc/hosts
```

### 相対パスの絶対パスへの変換

```console
$ realpath ../projects
/home/user/projects
```

### 複数のファイルの絶対パスを表示

```console
$ realpath file1.txt file2.txt dir1
/home/user/file1.txt
/home/user/file2.txt
/home/user/dir1
```

## ヒント:

### スクリプト内での使用

シェルスクリプト内で`realpath`を使用すると、スクリプトの実行場所に関係なく、ファイルの絶対パスを取得できるため、ファイル操作が安全になります。

### 存在しないファイルのパス

デフォルトでは、`realpath`は存在しないファイルに対してエラーを返します。存在しないファイルのパスを取得するには`-m`オプションを使用します。

### 相対パスの活用

`--relative-to`オプションを使うと、あるパスから別のパスへの相対パスを簡単に取得できます。これはファイルの移動やリンク作成時に役立ちます。

## よくある質問

#### Q1. `realpath`と`readlink -f`の違いは何ですか？
A. 両方とも絶対パスを表示しますが、`realpath`はより多くのオプションを提供し、GNU coreutils の一部です。`readlink -f`は一部の古いシステムでは動作が異なる場合があります。

#### Q2. 存在しないファイルの絶対パスを取得するにはどうすればよいですか？
A. `realpath -m /path/to/nonexistent`を使用します。`-m`オプションは存在しないコンポーネントがあっても処理を続行します。

#### Q3. シンボリックリンクを解決せずに絶対パスを取得するにはどうすればよいですか？
A. `realpath -s symlink`を使用します。これにより、シンボリックリンク自体の絶対パスが表示されます。

#### Q4. macOSでrealpathを使用するには？
A. macOSのデフォルトインストールには`realpath`が含まれていない場合があります。Homebrewを使用して`coreutils`パッケージをインストールすることで利用できます: `brew install coreutils`

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html

## 改訂履歴

- 2025/04/30 初版作成