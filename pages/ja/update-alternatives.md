# update-alternatives コマンド

`update-alternatives`は、Debian系Linuxディストリビューションで使用される、システム上の代替コマンドやアプリケーションを管理するためのコマンドです。複数のバージョンのソフトウェアを共存させ、デフォルトで使用するものを切り替えることができます。

## オプション

### **--install**
新しい代替グループを作成するか、既存のグループに新しい選択肢を追加します。

```console
$ sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 100
update-alternatives: using /usr/bin/vim to provide /usr/bin/editor (editor) in auto mode
```

### **--config**
対話的にデフォルトの代替を選択します。

```console
$ sudo update-alternatives --config java
There are 3 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                            Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      auto mode
  1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      manual mode
  2            /usr/lib/jvm/java-8-openjdk-amd64/bin/java       1081      manual mode
  3            /usr/lib/jvm/java-17-openjdk-amd64/bin/java      1171      manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

### **--display**
特定の代替グループに関する情報を表示します。

```console
$ update-alternatives --display editor
editor - auto mode
  link best version is /usr/bin/vim
  link currently points to /usr/bin/vim
  link editor is /usr/bin/editor
  slave editor.1.gz is /usr/share/man/man1/editor.1.gz
  slave editor.fr.1.gz is /usr/share/man/fr/man1/editor.1.gz
  slave editor.it.1.gz is /usr/share/man/it/man1/editor.1.gz
  slave editor.ja.1.gz is /usr/share/man/ja/man1/editor.1.gz
  slave editor.pl.1.gz is /usr/share/man/pl/man1/editor.1.gz
  slave editor.ru.1.gz is /usr/share/man/ru/man1/editor.1.gz
/usr/bin/vim - priority 100
/bin/nano - priority 40
/usr/bin/emacs - priority 0
```

### **--remove**
代替グループから特定の選択肢を削除します。

```console
$ sudo update-alternatives --remove editor /usr/bin/emacs
update-alternatives: removing editor alternative /usr/bin/emacs
```

## 使用例

### Javaのバージョン切り替え

```console
$ sudo update-alternatives --config java
[対話的なメニューが表示され、使用するJavaバージョンを選択できます]
```

### 新しいエディタを代替として追加

```console
$ sudo update-alternatives --install /usr/bin/editor editor /usr/bin/code 90
update-alternatives: using /usr/bin/code to provide /usr/bin/editor (editor) in auto mode
```

### 現在の代替設定を確認

```console
$ update-alternatives --list java
/usr/lib/jvm/java-11-openjdk-amd64/bin/java
/usr/lib/jvm/java-8-openjdk-amd64/bin/java
/usr/lib/jvm/java-17-openjdk-amd64/bin/java
```

## ヒント:

### 優先度の理解
`--install`オプションで設定する優先度（priority）の値が高いほど、自動モードでその選択肢が選ばれやすくなります。手動で設定した場合は優先度に関係なく選択したものが使用されます。

### スレーブリンクの活用
メインの代替だけでなく、関連するマニュアルページなども一緒に切り替えたい場合は、`--slave`オプションを使用します。これにより、一貫性のある環境を維持できます。

### 自動モードと手動モード
自動モードでは、システムが最も優先度の高い選択肢を自動的に選びます。手動モードでは、ユーザーが明示的に選んだ選択肢が使用されます。

### 管理者権限の必要性
ほとんどの操作には管理者権限（sudo）が必要です。読み取り専用の操作（--display, --list）のみ一般ユーザーでも実行できます。

## よくある質問

#### Q1. update-alternativesとは何ですか？
A. システム上の複数のバージョンのソフトウェアを管理し、デフォルトで使用するものを切り替えるためのコマンドです。

#### Q2. 現在設定されている代替を確認するにはどうすればよいですか？
A. `update-alternatives --display <名前>` または `update-alternatives --list <名前>` を使用します。

#### Q3. 代替の優先度はどのように機能しますか？
A. 優先度は数値で表され、値が大きいほど優先されます。自動モードでは最も優先度の高い選択肢が選ばれます。

#### Q4. 手動で設定した代替を自動モードに戻すにはどうすればよいですか？
A. `sudo update-alternatives --auto <名前>` を実行します。

#### Q5. 代替グループの一覧を表示するにはどうすればよいですか？
A. `update-alternatives --get-selections` コマンドを使用すると、システム上のすべての代替グループとその現在の設定を確認できます。

## 参考資料

https://manpages.debian.org/buster/dpkg/update-alternatives.1.en.html

## 改訂

- 2025/04/26 管理者権限の必要性に関するヒントと代替グループ一覧表示に関するFAQを追加。
- 2025/04/26 初版作成。