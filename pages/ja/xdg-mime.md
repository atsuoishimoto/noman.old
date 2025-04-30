# xdg-mime コマンド

ファイルタイプとそれに関連付けられたアプリケーションを管理するコマンド。

## 概要

`xdg-mime` は Linux デスクトップ環境でファイルタイプ（MIME タイプ）とアプリケーションの関連付けを管理するためのコマンドです。ファイルの種類を調べたり、特定のファイルタイプを開くデフォルトアプリケーションを設定したりすることができます。このコマンドは XDG（X Desktop Group）標準の一部で、デスクトップ環境間での一貫性を提供します。

## オプション

### **query filetype**

ファイルの MIME タイプを調査します。

```console
$ xdg-mime query filetype document.pdf
application/pdf
```

### **query default**

特定の MIME タイプに関連付けられたデフォルトアプリケーションを表示します。

```console
$ xdg-mime query default application/pdf
org.gnome.evince.desktop
```

### **default**

特定の MIME タイプに対するデフォルトアプリケーションを設定します。

```console
$ xdg-mime default firefox.desktop text/html
```

### **install**

新しい MIME タイプ情報をシステムにインストールします。

```console
$ xdg-mime install mytype.xml
```

## 使用例

### ファイルの MIME タイプを確認する

```console
$ xdg-mime query filetype image.jpg
image/jpeg
```

### PDF ファイルのデフォルトアプリケーションを変更する

```console
$ xdg-mime default okular.desktop application/pdf
```

### 現在の HTML ファイルのデフォルトブラウザを確認する

```console
$ xdg-mime query default text/html
firefox.desktop
```

## ヒント:

### MIME タイプの詳細を調べる

`file --mime-type` コマンドも使用して、ファイルの MIME タイプを確認できます。これは xdg-mime が利用できない環境でも役立ちます。

```console
$ file --mime-type document.pdf
document.pdf: application/pdf
```

### デスクトップファイルの場所

`.desktop` ファイルは通常 `/usr/share/applications/` または `~/.local/share/applications/` ディレクトリにあります。デフォルトアプリケーションを設定する際には、これらのディレクトリにある正確なファイル名を使用する必要があります。

### 変更の反映

設定変更後、変更が反映されない場合は、アプリケーションを再起動するか、場合によってはログアウト/ログインが必要になることがあります。

## よくある質問

#### Q1. xdg-mime とは何ですか？
A. Linux デスクトップ環境でファイルタイプとアプリケーションの関連付けを管理するためのコマンドラインツールです。

#### Q2. 特定のファイルタイプに対するデフォルトアプリケーションを変更するにはどうすればよいですか？
A. `xdg-mime default アプリケーション名.desktop MIMEタイプ` を使用します。例えば、`xdg-mime default firefox.desktop text/html` のようにします。

#### Q3. ファイルの MIME タイプを調べるにはどうすればよいですか？
A. `xdg-mime query filetype ファイル名` を使用します。例えば、`xdg-mime query filetype document.pdf` のようにします。

#### Q4. 変更したデフォルトアプリケーションの設定はどこに保存されますか？
A. 通常、`~/.config/mimeapps.list` ファイルに保存されます。

#### Q5. xdg-mime コマンドはどのデスクトップ環境で動作しますか？
A. GNOME、KDE、Xfce など、XDG 標準に準拠したほとんどの Linux デスクトップ環境で動作します。

## 参考資料

https://portland.freedesktop.org/doc/xdg-mime.html

## 改訂履歴

- 2025/04/30 初版作成