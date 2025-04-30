# xdg-open コマンド

指定したファイルやURLをデフォルトのアプリケーションで開きます。

## 概要

`xdg-open`は、ファイル、ディレクトリ、URLを適切なデフォルトアプリケーションで開くLinuxコマンドです。ファイルタイプに応じて、テキストエディタ、ウェブブラウザ、画像ビューアなど、システムに設定されたデフォルトのアプリケーションが自動的に起動されます。これはmacOSの`open`コマンドやWindowsの`start`コマンドに相当する機能です。

## オプション

`xdg-open`は基本的にオプションを必要とせず、単純に開きたいファイルやURLを引数として指定します。

### **基本的な使い方**

ファイルやURLを開くための基本的な構文です。

```console
$ xdg-open ファイル名またはURL
```

## 使用例

### ファイルを開く

```console
$ xdg-open document.pdf
# PDFビューアでdocument.pdfが開かれる
```

### ディレクトリを開く

```console
$ xdg-open ~/Documents
# ファイルマネージャでDocumentsディレクトリが開かれる
```

### ウェブサイトを開く

```console
$ xdg-open https://www.example.com
# デフォルトのウェブブラウザでexample.comが開かれる
```

### 画像ファイルを開く

```console
$ xdg-open image.jpg
# 画像ビューアでimage.jpgが開かれる
```

## ヒント:

### バックグラウンドで実行する

コマンドの後に`&`を付けると、アプリケーションがバックグラウンドで起動し、ターミナルを継続して使用できます。

```console
$ xdg-open document.pdf &
```

### スクリプト内での使用

シェルスクリプト内で`xdg-open`を使用する場合、ユーザーの操作を待たずに次の処理に進みたい場合は、バックグラウンド実行と出力のリダイレクトを組み合わせると効果的です。

```console
$ xdg-open document.pdf > /dev/null 2>&1 &
```

### デフォルトアプリケーションの変更

特定のファイルタイプに対するデフォルトアプリケーションを変更するには、デスクトップ環境の設定ツールを使用するか、`xdg-mime`コマンドを使用します。

```console
$ xdg-mime default vlc.desktop video/mp4
# MP4ファイルのデフォルトアプリケーションをVLCに設定
```

## よくある質問

#### Q1. `xdg-open`はどのLinuxディストリビューションで使用できますか？
A. ほとんどの主要なLinuxディストリビューション（Ubuntu、Fedora、Debian、CentOSなど）で利用可能です。xdg-utilsパッケージの一部として提供されています。

#### Q2. `xdg-open`がファイルを開かない場合はどうすればよいですか？
A. ファイルタイプに対応するデフォルトアプリケーションが設定されていない可能性があります。`xdg-mime query default ファイルタイプ`でデフォルトアプリケーションを確認し、必要に応じて`xdg-mime default`で設定してください。

#### Q3. macOSやWindowsに相当するコマンドはありますか？
A. macOSでは`open`コマンド、Windowsでは`start`コマンドが同様の機能を提供します。

#### Q4. スクリプト内で使用する際の注意点はありますか？
A. `xdg-open`はアプリケーションを起動した後、すぐに制御を返します。アプリケーションの終了を待つ必要がある場合は、追加の処理が必要です。

## macOSでの注意点

macOSでは`xdg-open`コマンドは標準では利用できません。代わりに`open`コマンドを使用してください。`open`コマンドは同様の機能を持ち、ファイルやURLをデフォルトのアプリケーションで開きます。

```console
$ open document.pdf
# PDFビューアでdocument.pdfが開かれる
```

## 参考情報

https://www.freedesktop.org/wiki/Software/xdg-utils/

## 改訂履歴

- 2025/04/30 初版作成