# scp コマンドの概要

`scp`（Secure Copy）は、SSHプロトコルを使用してコンピュータ間でファイルを安全に転送するためのコマンドラインツールです。ローカルマシンとリモートサーバー間、または2つのリモートサーバー間でファイルやディレクトリをコピーできます。

## 主なオプション

- **-r**: ディレクトリを再帰的にコピーします
  - 例: `scp -r /local/directory user@remote:/path/to/destination`

- **-P**: 接続先のSSHポート番号を指定します（デフォルトは22）
  - 例: `scp -P 2222 file.txt user@remote:/path/to/destination`

- **-p**: 元のファイルの修正時刻、アクセス時刻、権限を保持します
  - 例: `scp -p file.txt user@remote:/path/to/destination`

- **-C**: 転送中にデータを圧縮します（低速ネットワークで有用）
  - 例: `scp -C large_file.zip user@remote:/path/to/destination`

- **-q**: 進行状況の表示を抑制し、静かに実行します
  - 例: `scp -q file.txt user@remote:/path/to/destination`

## 使用例

### ローカルからリモートへのファイル転送
```bash
# ローカルファイルをリモートサーバーに転送する
scp file.txt user@remote.server:/home/user/
# 出力例
file.txt                  100%  1234     1.2MB/s   00:01
```

### リモートからローカルへのファイル転送
```bash
# リモートサーバーからローカルマシンにファイルをダウンロードする
scp user@remote.server:/home/user/file.txt ./
# 出力例
file.txt                  100%  1234     1.2MB/s   00:01
```

### ディレクトリの再帰的コピー
```bash
# ディレクトリ全体をコピーする
scp -r /local/directory user@remote.server:/home/user/
# 出力例
file1.txt                 100%  1234     1.2MB/s   00:01
file2.txt                 100%  5678     1.5MB/s   00:03
```

### 異なるポート番号を使用
```bash
# ポート2222を使用してファイルを転送
scp -P 2222 file.txt user@remote.server:/home/user/
# 出力例
file.txt                  100%  1234     1.2MB/s   00:01
```

### リモートサーバー間のファイル転送
```bash
# あるリモートサーバーから別のリモートサーバーにファイルをコピー
scp user1@server1:/path/to/file user2@server2:/path/to/destination
# 出力例
file.txt                  100%  1234     1.2MB/s   00:01
```

## 追加情報

- 初めて接続するサーバーの場合、ホストキーの確認メッセージが表示されます。「yes」と入力して続行します。
- パスワード認証の代わりにSSH鍵認証を設定すると、より安全で便利です。
- ワイルドカード（`*`）を使用して複数のファイルを一度に転送できます：`scp *.txt user@remote:/path/`
- 大きなファイルを転送する場合は、`-C`（圧縮）オプションを使用すると転送速度が向上することがあります。
- 接続が頻繁に切断される不安定なネットワークでは、代わりに`rsync`コマンドの使用を検討してください。