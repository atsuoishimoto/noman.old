# scp コマンド

ネットワーク上のホスト間でSSHを使用してファイルを安全にコピーします。

## 概要

`scp`（secure copy）は、暗号化されたSSH接続を介してコンピュータ間でファイルを安全に転送できるコマンドラインユーティリティです。`cp`コマンドの機能とSSHのセキュリティを組み合わせており、リモートサーバーとの間でファイルをコピーする安全な方法を提供します。

## オプション

### **-r, --recursive**

ディレクトリを再帰的にコピーします

```console
$ scp -r documents/ user@remote:/home/user/backup/
documents/file1.txt                 100%  123     1.2KB/s   00:00    
documents/file2.txt                 100%  456     2.3KB/s   00:00
documents/subfolder/file3.txt       100%  789     3.4KB/s   00:00
```

### **-P, --port**

リモートホストに接続する際の異なるポートを指定します

```console
$ scp -P 2222 file.txt user@remote:/home/user/
file.txt                            100%  123     1.2KB/s   00:00
```

### **-p**

元のファイルから更新時刻、アクセス時刻、モードを保持します

```console
$ scp -p important.txt user@remote:/home/user/
important.txt                       100%  123     1.2KB/s   00:00
```

### **-q, --quiet**

静かモード：進捗メーターと警告/診断メッセージを無効にします

```console
$ scp -q large_file.zip user@remote:/home/user/
```

### **-C, --compress**

ファイル転送中に圧縮を有効にします

```console
$ scp -C large_file.zip user@remote:/home/user/
large_file.zip                      100%  10MB    5.0MB/s   00:02
```

### **-l, --limit-bandwidth**

使用する帯域幅を制限します（Kbit/s単位で指定）

```console
$ scp -l 1000 large_file.zip user@remote:/home/user/
large_file.zip                      100%  10MB    1.0MB/s   00:10
```

## 使用例

### ローカルファイルをリモートサーバーにコピーする

```console
$ scp document.txt user@remote.server:/path/to/destination/
document.txt                        100%  123     1.2KB/s   00:00
```

### リモートサーバーからローカルマシンにファイルをコピーする

```console
$ scp user@remote.server:/path/to/file.txt ./
file.txt                            100%  123     1.2KB/s   00:00
```

### 2つのリモートサーバー間でコピーする

```console
$ scp user1@server1:/path/to/file.txt user2@server2:/path/to/destination/
file.txt                            100%  123     1.2KB/s   00:00
```

### 複数のファイルを一度にコピーする

```console
$ scp file1.txt file2.txt user@remote:/home/user/
file1.txt                           100%  123     1.2KB/s   00:00
file2.txt                           100%  456     2.3KB/s   00:00
```

## ヒント:

### パスワードなしの転送にSSH鍵を使用する

SSH鍵認証を設定して、転送ごとにパスワードを入力する必要をなくしましょう。これは頻繁な転送において、より安全で便利な方法です。

### ファイル名の特殊文字をエスケープする

スペースや特殊文字を含むファイルを転送する場合は、引用符を使用するか文字をエスケープしてください：
```console
$ scp "file with spaces.txt" user@remote:/home/user/
```

### 新しい接続のフィンガープリントを確認する

中間者攻撃を防ぐため、新しいサーバーに接続する際は常にSSHフィンガープリントを確認しましょう。

### 低速接続には圧縮を使用する

`-C`オプションは圧縮を有効にし、特にテキストファイルの場合、低速ネットワーク接続での転送速度を大幅に向上させることができます。

## よくある質問

#### Q1. scpは通常のcpとどう違いますか？
A. `scp`はSSH暗号化を使用してネットワーク経由で動作しますが、`cp`はローカルでのみ動作します。`scp`は認証が必要で、安全で暗号化されたファイル転送を提供します。

#### Q2. 中断されたファイル転送をscpで再開できますか？
A. いいえ、`scp`は中断された転送の再開をサポートしていません。その機能が必要な場合は、`-P`オプション付きの`rsync`の使用を検討してください。

#### Q3. ディレクトリ全体を転送するにはどうすればよいですか？
A. `-r`（再帰的）オプションを使用します：`scp -r /path/to/directory user@remote:/destination/`

#### Q4. 標準以外のSSHポートを指定するにはどうすればよいですか？
A. `-P`オプションを使用します：`scp -P 2222 file.txt user@remote:/home/user/`

## 参考文献

https://man.openbsd.org/scp.1

## 改訂履歴

- 2025/05/04 初版作成