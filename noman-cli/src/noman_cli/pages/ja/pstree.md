# pstree コマンド

プロセスの親子関係を示すツリーを表示します。

## 概要

`pstree` コマンドは実行中のプロセスをツリー形式で表示し、プロセス間の親子関係を簡単に確認できるようにします。どのプロセスがどのプロセスを生成したかを視覚的に表現し、プロセス間の接続関係を明確に示します。

## オプション

### **-a, --arguments**

各プロセスのコマンドライン引数を表示します。

```console
$ pstree -a
systemd
  ├─ModemManager
  ├─NetworkManager --no-daemon
  ├─accounts-daemon
  ├─avahi-daemon --syslog
  │   └─avahi-daemon --syslog
  └─sshd -D
      └─sshd
          └─sshd
              └─bash
```

### **-p, --show-pids**

プロセス名と一緒にPID（プロセスID）を表示します。

```console
$ pstree -p
systemd(1)─┬─ModemManager(823)
           ├─NetworkManager(824)
           ├─accounts-daemon(825)
           ├─avahi-daemon(826)───avahi-daemon(845)
           └─sshd(1025)───sshd(1789)───sshd(1823)───bash(1824)
```

### **-h, --highlight-all**

現在のプロセスとその祖先を強調表示します。

```console
$ pstree -h
systemd─┬─ModemManager
        ├─NetworkManager
        ├─accounts-daemon
        ├─avahi-daemon───avahi-daemon
        └─sshd───sshd───sshd───bash
```

### **-u, --uid-changes**

ユーザーID（uid）の変更を表示します。

```console
$ pstree -u
systemd─┬─ModemManager
        ├─NetworkManager
        ├─accounts-daemon
        ├─avahi-daemon───avahi-daemon
        └─sshd───sshd───sshd───bash(user)
```

### **-n, --numeric-sort**

同じ親を持つプロセスを名前ではなくPID順にソートします。

```console
$ pstree -n
systemd─┬─ModemManager
        ├─NetworkManager
        ├─accounts-daemon
        ├─avahi-daemon───avahi-daemon
        └─sshd───sshd───sshd───bash
```

## 使用例

### 特定ユーザーのプロセスツリーを表示

```console
$ pstree username
bash───vim
```

### 特定のPIDのプロセスツリーを表示

```console
$ pstree 1234
bash───firefox───Web Content
```

### 複数のオプションを組み合わせて詳細な出力を得る

```console
$ pstree -apu
systemd(1)
  ├─ModemManager(823)
  ├─NetworkManager(824) --no-daemon
  ├─accounts-daemon(825)
  ├─avahi-daemon(826) --syslog
  │   └─avahi-daemon(845) --syslog
  └─sshd(1025) -D
      └─sshd(1789)
          └─sshd(1823)
              └─bash(1824)(user)
```

## ヒント:

### 親子プロセス関係の特定

トラブルシューティング時に `pstree -p` を使用すると、特定の子プロセスがどの親プロセスから生成されたかを素早く特定できます。これによりプロセス階層の理解が容易になります。

### リソースを多く消費するプロセスグループの特定

`ps` コマンドと組み合わせることで、リソースを多く消費するプロセスだけでなく、そのプロセスファミリー全体を特定できます：`pstree -p $(ps -eo pid,pcpu --sort=-pcpu | head -2 | tail -1 | awk '{print $1}')`

### 大規模システム向けのコンパクトビュー

多数のプロセスが実行されているシステムでは、`pstree -c` を使用すると、同一のサブツリーを圧縮せずにより簡潔な表示が得られます。

## よくある質問

#### Q1. `pstree` と `ps` の違いは何ですか？
A. `ps` はプロセスをフラットなフォーマットでリスト表示するのに対し、`pstree` は親子関係を示す階層的なツリー構造で表示します。

#### Q2. `pstree` でプロセスIDを確認できますか？
A. はい、`pstree -p` を使用するとプロセス名と一緒にPIDを表示できます。

#### Q3. 特定ユーザーのプロセスツリーを確認するにはどうすればよいですか？
A. `pstree ユーザー名` を実行すると、そのユーザーが所有するプロセスのみが表示されます。

#### Q4. プロセスツリーでコマンドライン引数を確認できますか？
A. はい、`pstree -a` を使用すると各プロセスのコマンドライン引数が表示されます。

## 参考資料

https://man7.org/linux/man-pages/man1/pstree.1.html

## 改訂履歴

- 2025/05/04 初版作成