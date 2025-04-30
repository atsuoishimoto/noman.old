# update-alternatives コマンド

システム上の複数のバージョンのコマンドやライブラリを管理し、デフォルトを設定するためのツールです。

## 概要

`update-alternatives` は Debian ベースのシステム（Ubuntu など）で使用されるコマンドで、同じ機能を持つ複数のプログラムやライブラリのバージョンを管理します。これにより、システム全体のデフォルトとして使用するバージョンを簡単に切り替えることができます。例えば、複数のバージョンの Java や Python がインストールされている場合に、どのバージョンをデフォルトとして使用するかを指定できます。

## オプション

### **--display**

特定のコマンドやライブラリの現在の設定を表示します。

```console
$ update-alternatives --display java
java - auto mode
  link best version is /usr/lib/jvm/java-11-openjdk-amd64/bin/java
  link currently points to /usr/lib/jvm/java-11-openjdk-amd64/bin/java
  link java is /usr/bin/java
  slave java.1.gz is /usr/share/man/man1/java.1.gz
/usr/lib/jvm/java-8-openjdk-amd64/bin/java - priority 1081
/usr/lib/jvm/java-11-openjdk-amd64/bin/java - priority 1111
```

### **--config**

対話的にデフォルトのプログラムを選択します。

```console
$ sudo update-alternatives --config editor
There are 4 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/vim.basic   50        auto mode
  1            /bin/nano            40        manual mode
  2            /usr/bin/vim.basic   50        manual mode
  3            /usr/bin/vim.tiny    10        manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

### **--install**

新しい選択肢を alternatives システムに追加します。

```console
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 20
update-alternatives: using /usr/bin/python3.9 to provide /usr/bin/python (python) in auto mode
```

### **--remove**

alternatives システムから選択肢を削除します。

```console
$ sudo update-alternatives --remove python /usr/bin/python3.8
update-alternatives: removing python (/usr/bin/python3.8) from auto mode
```

## 使用例

### Java のデフォルトバージョンを確認する

```console
$ update-alternatives --display java
java - auto mode
  link best version is /usr/lib/jvm/java-11-openjdk-amd64/bin/java
  link currently points to /usr/lib/jvm/java-11-openjdk-amd64/bin/java
  link java is /usr/bin/java
  slave java.1.gz is /usr/share/man/man1/java.1.gz
/usr/lib/jvm/java-8-openjdk-amd64/bin/java - priority 1081
/usr/lib/jvm/java-11-openjdk-amd64/bin/java - priority 1111
```

### デフォルトのエディタを変更する

```console
$ sudo update-alternatives --config editor
There are 4 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/vim.basic   50        auto mode
  1            /bin/nano            40        manual mode
  2            /usr/bin/vim.basic   50        manual mode
  3            /usr/bin/vim.tiny    10        manual mode

Press <enter> to keep the current choice[*], or type selection number: 1
update-alternatives: using /bin/nano to provide /usr/bin/editor (editor) in manual mode
```

### 新しいPythonバージョンをシステムに追加する

```console
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 30
update-alternatives: using /usr/bin/python3.10 to provide /usr/bin/python (python) in auto mode
```

## ヒント:

### 優先度の理解

`--install` オプションを使用する際、優先度（priority）の値が高いほど、自動モードでその選択肢が選ばれやすくなります。例えば、Python 3.10に優先度30を、Python 3.9に優先度20を設定すると、自動モードではPython 3.10が選択されます。

### グループ管理

Java のような複数の関連コマンド（java, javac, javadoc など）を管理する場合、`--slave` オプションを使用して一括で切り替えることができます。これにより、一貫性のある環境を維持できます。

### 自動モードと手動モード

自動モードでは、システムが最も高い優先度を持つ選択肢を自動的に選びます。手動モード（`--config` で選択した場合）では、優先度に関係なく、明示的に選んだ選択肢が使用されます。

## よくある質問

#### Q1. update-alternatives と環境変数の違いは何ですか？
A. `update-alternatives` はシステム全体の設定を変更し、すべてのユーザーに影響します。環境変数はユーザーごとに設定でき、ユーザー固有の環境を構築できます。

#### Q2. 変更を元に戻すにはどうすればよいですか？
A. `sudo update-alternatives --config コマンド名` を実行し、以前の選択肢を選ぶことで元に戻せます。または、`--auto コマンド名` を使用して自動モードに戻すこともできます。

#### Q3. alternatives システムで管理されているすべてのプログラムを確認するには？
A. `update-alternatives --get-selections` コマンドを実行すると、管理されているすべてのプログラムとその現在の設定が表示されます。

#### Q4. 特定のコマンドに対する全ての選択肢を一覧表示するには？
A. `update-alternatives --display コマンド名` を使用すると、そのコマンドに対して登録されているすべての選択肢と現在の設定が表示されます。

## 参考資料

https://manpages.debian.org/buster/dpkg/update-alternatives.1.en.html

## 改訂履歴

- 2025/04/30 初版作成