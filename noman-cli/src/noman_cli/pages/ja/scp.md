# scp コマンド

ネットワーク経由でファイルやディレクトリを安全にコピーします。

## 概要

`scp`（Secure Copy Protocol）は、SSHプロトコルを使用してローカルマシンとリモートマシン間、またはリモートマシン同士でファイルを安全に転送するためのコマンドです。データは暗号化されて送信されるため、セキュリティが確保されます。

## オプション

### **-r**（再帰的コピー）

ディレクトリとその中身を再帰的にコピーします。

```console
$ scp -r ~/Documents/project user@remote-host:/home/user/backup/
project/                                   100%  4096     1.2MB/s   00:00    
file1.txt                                  100%  1024     0.5MB/s   00:00
file2.txt                                  100%  2048     0.8MB/s   00:00
```

### **-P**（ポート指定）

デフォルト（22）以外のSSHポートを指定します。

```console
$ scp -P 2222 file.txt user@remote-host:/home/user/
file.txt                                   100%  1024     0.5MB/s   00:00
```

### **-p**（パーミッション保持）

元のファイルの修正時刻、アクセス時刻、モードを保持します。

```console
$ scp -p important.conf user@remote-host:/etc/
important.conf                             100%  2048     0.8MB/s   00:00
```

### **-C**（圧縮）

転送中にデータを圧縮します。低速ネットワークで有用です。

```console
$ scp -C large_file.zip user@remote-host:~/
large_file.zip                             100%  10MB     2.5MB/s   00:04
```

### **-q**（静かモード）

進行状況メーターやエラー以外のメッセージを表示しません。

```console
$ scp -q file.txt user@remote-host:~/
```

## 使用例

### ローカルからリモートへのファイルコピー

```console
$ scp document.txt user@remote-host:/path/to/destination/
document.txt                               100%  1024     0.5MB/s   00:00
```

### リモートからローカルへのファイルコピー

```console
$ scp user@remote-host:/path/to/file.txt ./
file.txt                                   100%  2048     0.8MB/s   00:00
```

### リモートからリモートへのファイルコピー

```console
$ scp user1@host1:/path/file.txt user2@host2:/path/
file.txt                                   100%  1024     0.5MB/s   00:00
```

### ワイルドカードを使用した複数ファイルのコピー

```console
$ scp user@remote-host:/path/*.txt ./
file1.txt                                  100%  1024     0.5MB/s   00:00
file2.txt                                  100%  2048     0.8MB/s   00:00
```

## ヒント:

### SSH鍵認証の利用

パスワード入力を省略するためにSSH鍵認証を設定しておくと、自動化スクリプトでの利用が容易になります。

### 大きなファイルの転送

大きなファイルを転送する場合は、`-C`オプションで圧縮するか、事前にファイルを圧縮してから転送すると効率的です。

### 安全な接続の確認

初めて接続するホストの場合、フィンガープリントの確認を求められます。セキュリティのため、これを確認することが重要です。

### 帯域制限

`-l`オプションを使用して帯域幅を制限できます（例：`scp -l 1000`で約1Mbps）。共有ネットワークでの大きなファイル転送時に有用です。

## よくある質問

#### Q1. scpとrsyncの違いは何ですか？
A. scpは単純なファイルコピーに適していますが、rsyncは差分転送や同期機能があり、大量のファイルや定期的な同期に適しています。

#### Q2. パスワードなしでscpを使うにはどうすればいいですか？
A. SSH鍵ペアを生成し、`ssh-copy-id user@remote-host`でリモートホストに公開鍵を登録します。

#### Q3. 特定のSSH設定ファイルを使用するには？
A. `-F`オプションで設定ファイルを指定できます：`scp -F /path/to/ssh_config file.txt user@host:~/`

#### Q4. 転送速度が遅い場合はどうすればいいですか？
A. `-C`オプションで圧縮を有効にするか、Cipher指定（`-c aes128-ctr`など）で高速な暗号化アルゴリズムを選択できます。

## macOSでの注意点

macOSでは、Homebrewを使って最新版のOpenSSHをインストールすることができます。デフォルトのバージョンでは一部の新しいオプションが使えない場合があります。また、macOSのファイルシステム属性（拡張属性）は転送されないため、重要な場合は`tar`でアーカイブしてから転送することをお勧めします。

## 参考

https://man.openbsd.org/scp.1

## 改訂履歴

- 2025/04/30 初版作成