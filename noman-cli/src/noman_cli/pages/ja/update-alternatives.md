# update-alternatives コマンド

代替システム内のシンボリックリンクを管理し、デフォルトコマンドを決定します。

## 概要

`update-alternatives`は代替システム内のシンボリックリンクを作成、削除、維持、表示するためのコマンドです。このシステムにより、同じプログラムの複数のバージョンを共存させ、そのうちの1つをデフォルトとして指定できます。主にDebianベースのLinuxディストリビューションで、ユーザーがコマンドを実行したときにどのバージョンのプログラムが実行されるかを管理するために使用されます。

## オプション

### **--install** (`-i`)

新しい代替リンクグループを作成します

```console
$ sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 50
update-alternatives: using /usr/bin/vim to provide /usr/bin/editor (editor) in auto mode
```

### **--remove** (`-r`)

システムから代替を削除します

```console
$ sudo update-alternatives --remove editor /usr/bin/vim
update-alternatives: removing editor (/usr/bin/vim) from auto mode
```

### **--config** (`-c`)

リンクグループで利用可能な代替を表示し、対話的に選択できるようにします

```console
$ sudo update-alternatives --config editor
There are 3 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path              Priority   Status
------------------------------------------------------------
* 0            /usr/bin/vim       50        auto mode
  1            /usr/bin/nano      40        manual mode
  2            /usr/bin/emacs     30        manual mode
  3            /usr/bin/vim       50        manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

### **--display** (`-d`)

リンクグループに関する情報を表示します

```console
$ update-alternatives --display editor
editor - auto mode
  link best version is /usr/bin/vim
  link currently points to /usr/bin/vim
  link editor is /usr/bin/editor
  slave editor.1.gz is /usr/share/man/man1/editor.1.gz
  slave editor.fr.1.gz is /usr/share/man/fr/man1/editor.1.gz
  slave editor.it.1.gz is /usr/share/man/it/man1/editor.1.gz
  slave editor.pl.1.gz is /usr/share/man/pl/man1/editor.1.gz
  slave editor.ru.1.gz is /usr/share/man/ru/man1/editor.1.gz
/usr/bin/vim - priority 50
  slave editor.1.gz: /usr/share/man/man1/vim.1.gz
  slave editor.fr.1.gz: /usr/share/man/fr/man1/vim.1.gz
  slave editor.it.1.gz: /usr/share/man/it/man1/vim.1.gz
  slave editor.pl.1.gz: /usr/share/man/pl/man1/vim.1.gz
  slave editor.ru.1.gz: /usr/share/man/ru/man1/vim.1.gz
```

### **--auto** (`-a`)

リンクグループを自動モードに設定します（最も優先度の高い代替が使用されます）

```console
$ sudo update-alternatives --auto editor
update-alternatives: using /usr/bin/vim to provide /usr/bin/editor (editor) in auto mode
```

### **--set** (`-s`)

特定の代替をリンクグループの選択肢として設定します

```console
$ sudo update-alternatives --set editor /usr/bin/nano
update-alternatives: using /usr/bin/nano to provide /usr/bin/editor (editor) in manual mode
```

## 使用例

### 新しいJavaバージョンを代替に追加する

```console
$ sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-11-openjdk/bin/java 1100
update-alternatives: using /usr/lib/jvm/java-11-openjdk/bin/java to provide /usr/bin/java (java) in auto mode
```

### 異なるJavaバージョン間を切り替える

```console
$ sudo update-alternatives --config java
There are 3 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                           Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk/bin/java          1100      auto mode
  1            /usr/lib/jvm/java-8-openjdk/bin/java           1080      manual mode
  2            /usr/lib/jvm/java-17-openjdk/bin/java          1170      manual mode
  3            /usr/lib/jvm/java-11-openjdk/bin/java          1100      manual mode

Press <enter> to keep the current choice[*], or type selection number: 2
update-alternatives: using /usr/lib/jvm/java-17-openjdk/bin/java to provide /usr/bin/java (java) in manual mode
```

### 特定のコマンドのすべての代替を一覧表示する

```console
$ update-alternatives --list java
/usr/lib/jvm/java-8-openjdk/bin/java
/usr/lib/jvm/java-11-openjdk/bin/java
/usr/lib/jvm/java-17-openjdk/bin/java
```

## ヒント:

### 優先度の値を理解する

高い優先度の値（例えば50より100）は、自動モードでどの代替が選択されるかを決定します。新しい代替をインストールする際、それをデフォルトにしたい場合は、既存のものより高い優先度を割り当てます。

### 関連コマンドのグループを管理する

Javaのように複数の関連コマンド（java、javac、jar）を持つプログラムの場合、代替をインストールする際に`--slave`オプションを使用して一緒に管理できます。

### 現在のデフォルトを確認する

変更を加える前に、`--display`を使用して代替グループの現在の設定を確認しましょう。これにより、システムへの意図しない変更を避けることができます。

### 自動モードと手動モード

自動モードでは、システムは最も優先度の高い代替を自動的に選択します。手動モードでは、優先度に関係なく、手動で選択した代替が維持されます。

## よくある質問

#### Q1. update-alternativesとシンボリックリンクの違いは何ですか？
A. `update-alternatives`はシンボリックリンクを標準化された方法で管理する高レベルのシステムです。プログラムのバージョン間を切り替えるための一貫したインターフェースを提供し、利用可能な代替を追跡します。

#### Q2. どのプログラムが代替システムを使用しているか知るにはどうすればいいですか？
A. `update-alternatives --get-selections`で管理されているすべての代替を一覧表示できます。

#### Q3. 代替をシステムから完全に削除できますか？
A. はい、`update-alternatives --remove-all <名前>`を使用して、特定のコマンドのすべての代替を削除できます。

#### Q4. 代替を提供する新しいパッケージをインストールするとどうなりますか？
A. パッケージマネージャーは通常、インストール中に`update-alternatives`を呼び出して、事前定義された優先度で新しい代替をシステムに追加します。

#### Q5. 壊れた代替を修正するにはどうすればいいですか？
A. 代替が存在しないファイルを指している場合、`--remove`でそれを削除し、正しい代替を再インストールできます。

## 参考資料

https://manpages.debian.org/bullseye/dpkg/update-alternatives.1.en.html

## 改訂履歴

2025/05/04 初回改訂