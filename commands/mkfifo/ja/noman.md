# mkfifo コマンドの概要

`mkfifo`は、名前付きパイプ（FIFO: First In First Out）を作成するためのUnixコマンドです。これにより、異なるプロセス間でデータを受け渡しするための特殊なファイルを作成できます。

## 主なオプション

- **-m, --mode=MODE**: パイプのパーミッション（アクセス権限）を設定します
  - 例: `mkfifo -m 644 mypipe`

- **-Z, --context=CTX**: SELinuxセキュリティコンテキストを設定します（SELinux対応システムのみ）
  - 例: `mkfifo -Z user_u:object_r:user_tmp_t:s0 mypipe`

## 使用例

### 基本的な名前付きパイプの作成

```bash
# 名前付きパイプ「mypipe」を作成
mkfifo mypipe

# 確認（lsコマンドでは「p」がパイプを示す）
ls -l mypipe
# 出力例
prw-r--r-- 1 user group 0 Apr 10 12:34 mypipe
```

### パイプを使ったプロセス間通信

```bash
# ターミナル1で実行：パイプからデータを読み込む
cat mypipe

# ターミナル2で実行：パイプにデータを書き込む
echo "Hello through the pipe" > mypipe
# ターミナル1に「Hello through the pipe」と表示される
```

### 特定のパーミッションでパイプを作成

```bash
# 所有者のみ読み書き可能なパイプを作成
mkfifo -m 600 securepipe

# 確認
ls -l securepipe
# 出力例
prw------- 1 user group 0 Apr 10 12:40 securepipe
```

## 追加情報

- 名前付きパイプは、関連のないプロセス間でデータを受け渡しするのに便利です。
- パイプからの読み取りは、誰かがパイプに書き込むまでブロック（待機）されます。
- パイプへの書き込みも、誰かがパイプから読み取るまでブロックされることがあります。
- 通常のファイルとは異なり、パイプはデータを一時的に保持するだけで、ディスクに永続的に保存されません。
- パイプを削除するには通常のファイルと同様に `rm` コマンドを使用します。