# sftpコマンド概要

sftpは「SSH File Transfer Protocol」の略で、SSHプロトコルを使用してリモートサーバーとの間でファイルを安全に転送するためのコマンドです。通常のFTPと違い、暗号化された接続を使用するため、データ転送がより安全です。

## 主なオプション

- **-P port**: 接続先のSSHポート番号を指定します（デフォルトは22）
  - 例: `sftp -P 2222 user@example.com`

- **-i identity_file**: 認証に使用する秘密鍵ファイルを指定します
  - 例: `sftp -i ~/.ssh/my_key user@example.com`

- **-b batchfile**: バッチファイルからコマンドを読み込んで実行します
  - 例: `sftp -b commands.txt user@example.com`

- **-r**: ディレクトリを再帰的にアップロード/ダウンロードします
  - 例: `get -r remote_dir local_dir`（sftpセッション内で使用）

## 基本的な使い方

### 接続方法

```bash
# ユーザー名とホスト名を指定して接続
sftp user@example.com

# 接続成功時の出力例
Connected to example.com.
sftp>
```

### sftpセッション内のコマンド

```bash
# リモートディレクトリの内容を表示
sftp> ls
# 出力例
file1.txt  documents/  images/

# ローカルディレクトリの内容を表示
sftp> lls
# 出力例
Downloads/  Desktop/  local_file.txt

# カレントディレクトリの変更（リモート）
sftp> cd documents

# カレントディレクトリの変更（ローカル）
sftp> lcd Downloads

# ファイルのダウンロード
sftp> get file1.txt
# 出力例
Fetching /home/user/file1.txt to file1.txt

# ファイルのアップロード
sftp> put local_file.txt
# 出力例
Uploading local_file.txt to /home/user/local_file.txt

# ディレクトリの再帰的ダウンロード
sftp> get -r documents
# 出力例
Fetching /home/user/documents/ to documents/

# セッションの終了
sftp> exit
```

## 追加情報

- sftpはインタラクティブモードとバッチモードの両方で使用できます。バッチモードは自動化スクリプトに便利です。

- ワイルドカードを使用したファイル転送も可能です：
  ```bash
  sftp> get *.txt
  ```

- 転送速度を確認するには `-v`（詳細表示）オプションを使用します：
  ```bash
  sftp -v user@example.com
  ```

- 多くのsftpコマンドはFTPと似ていますが、すべての通信が暗号化されるため、公共のネットワークでも安全に使用できます。

- パスワード認証よりも公開鍵認証（`-i`オプション）を使用する方が安全で便利です。