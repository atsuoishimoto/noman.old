# sudoedit コマンド

特権ユーザーとしてファイルを安全に編集し、ファイルの所有権と権限を維持します。

## 概要

`sudoedit`（`sudo -e` としても利用可能）は、ユーザー自身のエディタ設定を使用しながら、特権が必要なファイルを編集できるようにするコマンドです。`sudo vim` で直接編集する場合と異なり、`sudoedit` はファイルの一時コピーを作成し、そのコピーをユーザーが好みのエディタで編集した後、変更を元のファイルに反映します。これにより、ファイルの元の所有権と権限が保持されます。

## オプション

### **-u ユーザー名/ID** / **--user=ユーザー名/ID**

root ではなく指定したユーザーとしてファイルを編集します

```console
$ sudoedit -u www-data /var/www/html/index.html
```

### **-H** / **--set-home**

HOME 環境変数をターゲットユーザーのホームディレクトリに設定します

```console
$ sudoedit -H /etc/ssh/sshd_config
```

### **-C 数値** / **--close-from=数値**

コマンド実行前に指定した数値以上のすべてのファイルディスクリプタを閉じます

```console
$ sudoedit -C 3 /etc/hosts
```

### **-E** / **--preserve-env**

編集時にユーザーの環境変数を保持します

```console
$ sudoedit -E /etc/nginx/nginx.conf
```

## 使用例

### 基本的なファイル編集

```console
$ sudoedit /etc/ssh/sshd_config
[デフォルトエディタでファイルが開かれる]
```

### sudo -e の使用（sudoedit と同等）

```console
$ sudo -e /etc/fstab
[デフォルトエディタでファイルが開かれる]
```

### 複数ファイルの同時編集

```console
$ sudoedit /etc/hosts /etc/hostname
[デフォルトエディタで最初のファイル、次に2番目のファイルが開かれる]
```

## ヒント:

### 好みのエディタの設定

`sudoedit` は SUDO_EDITOR、VISUAL、または EDITOR 環境変数（この順序）を使用して、どのエディタを使用するかを決定します。シェル設定ファイルでこれらのいずれかを設定しましょう：

```console
$ echo 'export EDITOR=vim' >> ~/.bashrc
```

### 保存前の差分確認

重要なシステムファイルを編集する場合、変更が適用される前に diff コマンドを使用して変更内容を確認できます：

```console
$ diff /etc/ssh/sshd_config /tmp/sshd_config.tmp
```

### セキュリティ上の利点

`sudoedit` は `sudo vim` よりも安全です。特権で過ごす時間を最小限に抑え、エディタのプラグインが root 権限で悪意のあるコードを実行する可能性を防ぎます。

## よくある質問

#### Q1. `sudoedit` と `sudo vim` の違いは何ですか？
A. `sudoedit` はファイルの一時コピーを作成し、通常の権限でそれを編集した後、sudo 権限でコピーを元に戻します。これは `sudo vim` でエディタ全体を root として実行するよりも安全です。

#### Q2. `sudoedit` で使用するエディタを指定するにはどうすればよいですか？
A. シェル設定ファイル（例：~/.bashrc）で SUDO_EDITOR、VISUAL、または EDITOR 環境変数を設定します。

#### Q3. `sudoedit` で複数のファイルを一度に編集できますか？
A. はい、編集したいすべてのファイルを引数として列挙するだけです：`sudoedit file1 file2 file3`

#### Q4. なぜ `sudoedit` が「sudoedit: no writable temporary directory found」というエラーで失敗することがありますか？
A. これは `sudoedit` が適切な権限を持つ一時ディレクトリを見つけられない場合に発生します。TMPDIR 環境変数を書き込み可能なディレクトリに設定してみてください。

## macOSに関する注意点

macOSでは、`sudoedit` はLinuxと同様に動作しますが、デフォルトのエディタが異なる場合があります。macOSは通常、デフォルトエディタとしてnanoを使用します。これを変更するには、~/.zshrcまたは~/.bash_profileファイルでEDITOR環境変数を設定してください。

## 参考資料

https://www.sudo.ws/docs/man/sudoedit.man/

## 改訂履歴

- 2025/05/04 初版作成