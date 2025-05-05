# xdg-mime コマンド

デスクトップ環境でファイルタイプの関連付けを照会・設定します。

## 概要

`xdg-mime`は、Linuxデスクトップ環境でファイルタイプの関連付けを管理するためのコマンドラインツールです。特定のファイルタイプ（MIMEタイプ）に関連付けられたアプリケーションの照会、ファイルタイプのデフォルトアプリケーションの設定、システムへの新しいMIMEタイプ情報の追加などが可能です。

## オプション

### **query default [mimetype]**

特定のMIMEタイプに対するデフォルトアプリケーションを照会します。

```console
$ xdg-mime query default text/plain
gedit.desktop
```

### **query filetype [file]**

ファイルのMIMEタイプを判定します。

```console
$ xdg-mime query filetype document.pdf
application/pdf
```

### **default [application.desktop] [mimetype(s)]**

1つまたは複数のMIMEタイプに対するデフォルトアプリケーションを設定します。

```console
$ xdg-mime default firefox.desktop text/html
```

### **install [--mode mode] [--novendor] mimetypes-file**

ファイルから新しいMIMEタイプ情報をインストールします。

```console
$ xdg-mime install --mode user myapplication-mime.xml
```

## 使用例

### PDFファイルを開くアプリケーションを確認する

```console
$ xdg-mime query default application/pdf
evince.desktop
```

### Firefoxをデフォルトブラウザとして設定する

```console
$ xdg-mime default firefox.desktop x-scheme-handler/http x-scheme-handler/https
```

### ファイルのMIMEタイプを確認する

```console
$ xdg-mime query filetype myimage.jpg
image/jpeg
```

### テキストファイル用に別のテキストエディタを設定する

```console
$ xdg-mime default code.desktop text/plain
```

## ヒント:

### デスクトップエントリファイルの場所

デスクトップエントリファイル（`.desktop`）は通常、`/usr/share/applications/`または`~/.local/share/applications/`にあります。デフォルトアプリケーションを設定する際には、これらのファイルを参照する必要があります。

### システム全体とユーザー固有の設定

システム全体の変更を行うには`--mode system`（root権限が必要）を、ユーザー固有の設定には`--mode user`（デフォルト）を使用します。

### 利用可能なデスクトップファイルを見つける

デフォルト設定に使用できるデスクトップファイルを確認するには、次のようにリストアップできます：
```console
$ ls /usr/share/applications/*.desktop
```

### MIMEタイプの参照

一般的なMIMEタイプには、テキストファイル用の`text/plain`、PDF用の`application/pdf`、JPEG画像用の`image/jpeg`、MP4ビデオ用の`video/mp4`などがあります。

## よくある質問

#### Q1. 特定のファイルを開くアプリケーションを調べるにはどうすればよいですか？
A. `xdg-mime query default $(xdg-mime query filetype ファイル名)`を使用して、まずファイルのMIMEタイプを判定し、次にそのMIMEタイプに関連付けられているアプリケーションを照会します。

#### Q2. ファイルの関連付けをシステムのデフォルトにリセットするにはどうすればよいですか？
A. xdg-mimeには直接のリセットコマンドはありません。`~/.config/mimeapps.list`の関連エントリを削除するか、手動で希望するデフォルトに設定する必要があります。

#### Q3. 新しいファイル関連付けが機能しないのはなぜですか？
A. 一部のデスクトップ環境ではMIME関連付けをキャッシュしています。ログアウトして再度ログインするか、ファイルマネージャーを再起動してみてください。また、`.desktop`ファイルが存在し、適切にフォーマットされていることを確認してください。

#### Q4. 1つのファイルタイプに複数のアプリケーションを関連付けることはできますか？
A. `xdg-mime`はデフォルトアプリケーションのみを設定します。代替アプリケーションは、デスクトップ環境のファイルプロパティダイアログで設定できます。

## 参照

https://portland.freedesktop.org/doc/xdg-mime.html

## 改訂履歴

- 2025/05/04 初回改訂