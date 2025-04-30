# ssh-add コマンド

SSH 認証エージェントに秘密鍵を追加・管理するコマンドです。

## 概要

`ssh-add` は SSH 認証エージェント（ssh-agent）に SSH 秘密鍵を追加するためのコマンドです。これにより、SSH 接続時にパスフレーズを毎回入力する必要がなくなります。また、鍵の一覧表示や削除などの管理機能も提供します。

## オプション

### **-l**（リスト表示）

認証エージェントに登録されている鍵の一覧を表示します。

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD user@hostname (RSA)
```

### **-d**（削除）

指定した鍵を認証エージェントから削除します。

```console
$ ssh-add -d ~/.ssh/id_rsa
Identity removed: /Users/username/.ssh/id_rsa (user@hostname)
```

### **-D**（全削除）

認証エージェントに登録されているすべての鍵を削除します。

```console
$ ssh-add -D
All identities removed.
```

### **-t**（有効期限設定）

鍵の有効期限を秒単位で設定します。

```console
$ ssh-add -t 3600 ~/.ssh/id_rsa
Identity added: /Users/username/.ssh/id_rsa (user@hostname)
Lifetime set to 3600 seconds
```

## 使用例

### 標準の鍵を追加する

```console
$ ssh-add
Enter passphrase for /Users/username/.ssh/id_rsa: 
Identity added: /Users/username/.ssh/id_rsa (user@hostname)
```

### 特定の鍵ファイルを追加する

```console
$ ssh-add ~/.ssh/my_custom_key
Enter passphrase for /Users/username/.ssh/my_custom_key: 
Identity added: /Users/username/.ssh/my_custom_key (user@hostname)
```

### 鍵のフィンガープリントを表示する

```console
$ ssh-add -l -E md5
2048 MD5:aa:bb:cc:dd:ee:ff:00:11:22:33:44:55:66:77:88:99 user@hostname (RSA)
```

## ヒント:

### ssh-agent の起動確認

`ssh-add` を使用する前に、ssh-agent が実行されていることを確認してください。実行されていない場合は、`eval $(ssh-agent)` コマンドで起動できます。

### ログイン時に自動で鍵を追加

`.bashrc` や `.zshrc` などのシェル設定ファイルに `ssh-add` コマンドを追加することで、ログイン時に自動的に鍵を追加できます。

### パスフレーズなしでの使用

```console
$ ssh-add -k ~/.ssh/id_rsa
```

macOS では `-k` オプションを使用すると、キーチェーンに保存されたパスフレーズを使用して鍵を追加できます。

## よくある質問

#### Q1. ssh-add と ssh-agent の違いは何ですか？
A. `ssh-agent` は認証情報を保持するバックグラウンドプロセスで、`ssh-add` はそのエージェントに鍵を追加するためのコマンドです。

#### Q2. ログアウト後も鍵を保持するにはどうすればよいですか？
A. macOS では `-K` オプションを使用してキーチェーンに保存できます。Linux では `keychain` などのツールを使用するか、systemd や screen/tmux で ssh-agent を永続化する方法があります。

#### Q3. 追加した鍵が使われているか確認するにはどうすればよいですか？
A. `ssh -v user@host` コマンドを実行すると、詳細なデバッグ情報が表示され、どの鍵が試行されているかを確認できます。

## macOS での注意点

macOS では、Sierra (10.12.2) 以降、デフォルトでキーチェーンと連携するようになりました。以下のオプションが特に重要です：

- `-K`: 追加した鍵のパスフレーズをキーチェーンに保存します
- `-A`: ローカルの ssh-agent から転送先のマシンの ssh-agent に鍵を転送します
- `-k`: キーチェーンから鍵のパスフレーズを読み込みます

macOS Monterey 以降では、`~/.ssh/config` に以下の設定を追加することで、キーチェーンとの連携を強化できます：

```
Host *
  UseKeychain yes
  AddKeysToAgent yes
```

## 参考資料

https://man.openbsd.org/ssh-add.1

## 改訂履歴

- 2025/04/30 macOS での注意点を追加。
- 2025/04/30 初版作成。