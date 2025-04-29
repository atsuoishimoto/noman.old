# xdg-mime コマンド

xdg-mime は Linux デスクトップ環境でファイルタイプの関連付けを管理するコマンドです。ファイルの MIME タイプの確認や、特定の MIME タイプに対するデフォルトアプリケーションの設定ができます。

## オプション

### **query filetype**
ファイルの MIME タイプを確認します。

```console
$ xdg-mime query filetype document.pdf
application/pdf
```

### **query default**
特定の MIME タイプに対するデフォルトアプリケーションを確認します。

```console
$ xdg-mime query default application/pdf
evince.desktop
```

### **default**
MIME タイプに対するデフォルトアプリケーションを設定します。

```console
$ xdg-mime default okular.desktop application/pdf
```

### **install**
新しい MIME タイプ情報をシステムにインストールします。

```console
$ xdg-mime install --mode user mytype.xml
```

## 使用例

### ファイルの MIME タイプを確認する

```console
$ xdg-mime query filetype ~/Downloads/report.docx
application/vnd.openxmlformats-officedocument.wordprocessingml.document
```

### PDF ファイルのデフォルトアプリケーションを変更する

```console
$ xdg-mime default org.gnome.Evince.desktop application/pdf
```

### 複数の MIME タイプに同じアプリケーションを設定する

```console
$ xdg-mime default org.gnome.Nautilus.desktop inode/directory
$ xdg-mime default org.gnome.Nautilus.desktop application/x-gnome-saved-search
```

## ヒント:

### MIME タイプの確認方法
ファイルの正確な MIME タイプがわからない場合は、`xdg-mime query filetype ファイル名` を使用して確認できます。これは新しいファイル形式のアプリケーション関連付けを設定する際に役立ちます。

### デスクトップファイルの場所
`.desktop` ファイルは通常 `/usr/share/applications/` または `~/.local/share/applications/` にあります。正確なファイル名が必要な場合は、これらのディレクトリを確認してください。

### 変更の反映
変更が即座に反映されない場合は、デスクトップ環境を再起動するか、`update-desktop-database` コマンドを実行してみてください。

## よくある質問

#### Q1. xdg-mime とは何ですか？
A. xdg-mime は Linux デスクトップ環境でファイルタイプとアプリケーションの関連付けを管理するためのコマンドラインツールです。

#### Q2. 特定のファイルタイプのデフォルトアプリケーションを変更するにはどうすればよいですか？
A. `xdg-mime default アプリケーション名.desktop MIMEタイプ` を使用します。例えば、`xdg-mime default firefox.desktop text/html` とすると、HTML ファイルのデフォルトブラウザが Firefox に設定されます。

#### Q3. 変更はどこに保存されますか？
A. ユーザーレベルの変更は `~/.config/mimeapps.list` ファイルに保存されます。システム全体の設定は `/usr/share/applications/mimeinfo.cache` などに保存されます。

#### Q4. 設定した関連付けをリセットするにはどうすればよいですか？
A. `~/.config/mimeapps.list` ファイルから該当する行を削除するか、別のアプリケーションを同じ MIME タイプのデフォルトとして設定します。

## 参考資料

https://portland.freedesktop.org/doc/xdg-mime.html

## Revisions

- 2025/04/26 初版作成。