# xdg-open コマンド

`xdg-open`は、ファイルやURLをデフォルトのアプリケーションで開くLinuxコマンドです。ファイルの種類に応じて適切なプログラムを自動的に選択します。

## オプション

### **ファイルを開く**
指定したファイルをそのファイルタイプに関連付けられたデフォルトアプリケーションで開きます。

```console
$ xdg-open document.pdf
```

### **URLを開く**
指定したURLをデフォルトのウェブブラウザで開きます。

```console
$ xdg-open https://www.google.com
```

### **ディレクトリを開く**
指定したディレクトリをファイルマネージャで開きます。

```console
$ xdg-open ~/Documents
```

## 使用例

### ローカルHTMLファイルを開く

```console
$ xdg-open index.html
```

### メールクライアントを起動する

```console
$ xdg-open mailto:user@example.com
```

### 画像ファイルを開く

```console
$ xdg-open image.jpg
```

## ヒント:

### バックグラウンドで実行する
コマンドの後に `&` を付けると、プログラムがバックグラウンドで起動し、ターミナルを継続して使用できます。

```console
$ xdg-open document.pdf &
```

### スクリプト内での使用
シェルスクリプト内で使用する場合は、出力をリダイレクトして不要なメッセージを抑制できます。

```console
$ xdg-open file.txt > /dev/null 2>&1 &
```

### 複数のファイルを一度に開く
複数のファイルを一度に開くには、それぞれに対して個別のxdg-openコマンドを実行する必要があります。

## よくある質問

#### Q1. `xdg-open`とは何ですか？
A. `xdg-open`は、ファイルやURLをそのタイプに適したデフォルトアプリケーションで開くLinuxコマンドです。

#### Q2. Windowsや macOSにも同様のコマンドはありますか？
A. はい、Windowsでは`start`、macOSでは`open`コマンドが同様の機能を提供します。

#### Q3. デフォルトアプリケーションを変更するにはどうすればよいですか？
A. デスクトップ環境の設定から「デフォルトアプリケーション」または「ファイルの関連付け」を変更できます。コマンドラインでは`xdg-mime`コマンドを使用できます。

#### Q4. エラーが発生した場合はどうすればよいですか？
A. 多くの場合、ファイルタイプに対応するアプリケーションが見つからないことが原因です。適切なアプリケーションをインストールするか、ファイルの関連付けを設定してください。

## macOSに関する注意点

macOSでは`xdg-open`の代わりに`open`コマンドを使用します。機能は同様ですが、構文が若干異なります。

```console
$ open document.pdf
$ open https://www.google.com
$ open ~/Documents
```

## 参考文献

https://www.freedesktop.org/wiki/Software/xdg-utils/

## 改訂履歴

- 2025/04/26 初版作成。