# visudo コマンド

sudoers ファイルを安全に編集するためのコマンド。

## 概要

`visudo` は、システム管理者が sudo の設定ファイル（/etc/sudoers）を安全に編集するためのコマンドです。このコマンドは、編集中に他のユーザーが同時に変更できないようにファイルをロックし、保存前に構文チェックを行うことで、設定ミスによるシステムアクセス不能を防ぎます。

## オプション

### **-c**

sudoers ファイルの構文チェックのみを行います。

```console
$ sudo visudo -c
/etc/sudoers: OK
```

### **-f ファイル**

デフォルトの /etc/sudoers ではなく、指定したファイルを編集します。

```console
$ sudo visudo -f /etc/sudoers.d/custom
```

### **-s**

厳格なパーサーモードを有効にします。警告も全てエラーとして扱われます。

```console
$ sudo visudo -s
```

### **-q**

静かモード。構文エラーのみを表示します。

```console
$ sudo visudo -q
```

## 使用例

### 基本的な使用方法

```console
$ sudo visudo
# 標準のエディタで /etc/sudoers ファイルが開かれる
```

### 別のエディタを使用する

```console
$ sudo EDITOR=nano visudo
# nanoエディタで /etc/sudoers ファイルが開かれる
```

### カスタム設定ファイルの作成

```console
$ sudo visudo -f /etc/sudoers.d/developers
# /etc/sudoers.d/developers ファイルを編集する
```

## ヒント:

### エディタの変更

デフォルトでは `visudo` は vi エディタを使用しますが、`EDITOR` または `VISUAL` 環境変数を設定することで別のエディタを使用できます。

```console
$ sudo EDITOR=nano visudo
```

### sudoers.d ディレクトリの活用

個別の設定ファイルを `/etc/sudoers.d/` ディレクトリに作成することで、メインの sudoers ファイルを変更せずに設定を追加できます。

```console
$ sudo visudo -f /etc/sudoers.d/myconfig
```

### 構文エラーの防止

`visudo` は保存時に構文チェックを行い、エラーがある場合は警告を表示します。これにより、誤った設定でシステムがロックされることを防ぎます。

## よくある質問

#### Q1. なぜ直接 /etc/sudoers ファイルを編集せず、visudo を使うべきですか？
A. `visudo` は構文チェックを行い、複数のユーザーによる同時編集を防ぐため、システムがロックされるリスクを減らします。

#### Q2. visudo で使用するエディタを変更するにはどうすればよいですか？
A. `EDITOR` または `VISUAL` 環境変数を設定します。例: `sudo EDITOR=nano visudo`

#### Q3. sudoers ファイルを編集中に構文エラーがあった場合はどうなりますか？
A. `visudo` は保存時にエラーを検出し、修正するか無視するかの選択肢を提供します。無視を選んでも、ファイルは保存されません。

#### Q4. sudoers.d ディレクトリとは何ですか？
A. `/etc/sudoers.d/` は追加の sudo 設定ファイルを格納するディレクトリです。メインの sudoers ファイルを変更せずに設定を追加できます。

## macOS での注意点

macOSでは、sudoers ファイルは `/private/etc/sudoers` にあります。また、macOS のアップデート後に変更が上書きされる可能性があるため、`/private/etc/sudoers.d/` ディレクトリに独自の設定ファイルを作成することをお勧めします。

## 参考文献

https://www.sudo.ws/docs/man/visudo.man/

## 改訂履歴

- 2025/04/30 初版作成