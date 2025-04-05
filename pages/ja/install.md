# `install` コマンドの概要

`install` コマンドは、ファイルをコピーし、同時に権限やオーナーシップを設定するためのコマンドです。通常のコピー（`cp`）と違い、ファイルモードや所有者、グループを指定できます。

## 主なオプション

- **-m, --mode=MODE**: コピー先のファイルに権限を設定する
  - 例: `install -m 755 script.sh /usr/local/bin/`

- **-o, --owner=OWNER**: コピー先のファイルの所有者を設定する
  - 例: `install -o root myfile /etc/`

- **-g, --group=GROUP**: コピー先のファイルのグループを設定する
  - 例: `install -g admin myfile /var/log/`

- **-d, --directory**: 指定したディレクトリを作成する（ファイルのコピーは行わない）
  - 例: `install -d -m 755 /opt/myapp/logs`

- **-s, --strip**: 実行可能ファイルからデバッグシンボルを削除する
  - 例: `install -s myprogram /usr/local/bin/`

- **-v, --verbose**: 実行中の処理を詳細に表示する
  - 例: `install -v -m 644 config.txt /etc/`

## 使用例

### 基本的な使い方（ファイルのコピーと権限設定）

```bash
# スクリプトを実行可能な形で /usr/local/bin にコピー
install -m 755 myscript.sh /usr/local/bin/

# 出力は通常ないが、成功すると終了コード 0 を返す
```

### 所有者とグループを指定してファイルをコピー

```bash
# 設定ファイルを root:wheel の所有権で /etc にコピー
sudo install -m 644 -o root -g wheel config.conf /etc/

# 出力は通常ないが、成功すると終了コード 0 を返す
```

### ディレクトリの作成

```bash
# 権限 755 でディレクトリを作成
install -d -m 755 /opt/myapp/data

# 出力は通常ないが、成功すると終了コード 0 を返す
```

### 複数ファイルを一度にコピー

```bash
# 複数のファイルを /usr/local/bin にコピー
install -m 755 script1.sh script2.sh script3.sh /usr/local/bin/

# 出力は通常ないが、成功すると終了コード 0 を返す
```

## 追加メモ

- `install` コマンドは主にソフトウェアのインストールスクリプトやMakefileで使用されることが多いです。
- `cp` コマンドと違い、コピー先のディレクトリが存在しない場合はエラーになります（`-d` オプションで事前に作成する必要があります）。
- 権限変更だけなら `chmod`、所有者変更だけなら `chown` を使う方がシンプルですが、`install` はこれらの操作を一度に行えるため便利です。
- 多くの場合、システムファイルを操作するため `sudo` と組み合わせて使用します。