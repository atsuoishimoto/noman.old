# pstree

プロセスの親子関係を階層的なツリー構造で表示するコマンドです。システム上で実行中のプロセスの関係性を視覚的に確認できます。

## オプション

### **-a**

すべてのプロセスを表示します（デフォルトでは一部のプロセスが省略されることがあります）。

```bash
$ pstree -a
systemd
  ├─ModemManager
  │   └─2*[{ModemManager}]
  ├─NetworkManager --no-daemon
  │   └─3*[{NetworkManager}]
  ├─accounts-daemon
  │   └─2*[{accounts-daemon}]
  ├─avahi-daemon
  │   └─avahi-daemon
  ...
```

### **-p**

各プロセスのPID（プロセスID）を表示します。

```bash
$ pstree -p
systemd(1)─┬─ModemManager(823)─┬─{ModemManager}(841)
           │                   └─{ModemManager}(843)
           ├─NetworkManager(824)─┬─{NetworkManager}(845)
           │                     ├─{NetworkManager}(846)
           │                     └─{NetworkManager}(847)
           ...
```

### **-u**

各プロセスのユーザー名も表示します。

```bash
$ pstree -u
systemd─┬─ModemManager(root)─┬─{ModemManager}(root)
        │                    └─{ModemManager}(root)
        ├─NetworkManager(root)─┬─{NetworkManager}(root)
        │                      ├─{NetworkManager}(root)
        │                      └─{NetworkManager}(root)
        ...
```

### **-g**

各プロセスのグループIDも表示します。

```bash
$ pstree -g
systemd─┬─ModemManager(823)─┬─{ModemManager}(823)
        │                   └─{ModemManager}(823)
        ├─NetworkManager(824)─┬─{NetworkManager}(824)
        │                     ├─{NetworkManager}(824)
        │                     └─{NetworkManager}(824)
        ...
```

### **-n**

出力を数値順（PID順）でソートします。

```bash
$ pstree -n
systemd─┬─systemd-journald
        ├─systemd-udevd
        ├─systemd-networkd
        ├─systemd-resolved
        ├─accounts-daemon
        ...
```

## 使用例

### 特定のユーザーのプロセスツリーを表示

```bash
$ pstree username
bash───vim
```

### PIDとユーザー名を含めた詳細なプロセスツリーを表示

```bash
$ pstree -pu
systemd(1,root)─┬─ModemManager(823,root)─┬─{ModemManager}(841,root)
                │                        └─{ModemManager}(843,root)
                ├─NetworkManager(824,root)─┬─{NetworkManager}(845,root)
                │                          ├─{NetworkManager}(846,root)
                │                          └─{NetworkManager}(847,root)
                ...
```

### 特定のプロセスのサブツリーのみを表示

```bash
$ pstree -p 1234
bash(1234)───ssh(1250)───bash(1300)───vim(1400)
```

## よくある質問

### Q1. pstreeとpsコマンドの違いは何ですか？
A. `ps`コマンドはプロセスを一覧形式で表示しますが、`pstree`はプロセスの親子関係を階層的なツリー構造で視覚的に表示します。

### Q2. 特定のプロセスだけを表示するにはどうすればいいですか？
A. `pstree PID`または`pstree ユーザー名`のように、特定のPIDやユーザー名を指定することで、そのプロセスまたはユーザーのプロセスのみを表示できます。

### Q3. 同じプロセスが複数ある場合はどのように表示されますか？
A. 同じプロセスが複数ある場合は、`3*[プロセス名]`のように表示されます。これは同じプロセスが3つあることを示しています。

### Q4. macOSでpstreeを使うにはどうすればいいですか？
A. macOSには標準で`pstree`コマンドがインストールされていません。Homebrewを使って`brew install pstree`でインストールするか、代わりに`ps -e -o pid,ppid,user,args | sort`などのコマンドを使用できます。

## 追加情報

- `pstree`は大規模なシステムでプロセスの関係を把握するのに非常に役立ちます。
- `-h`オプションを使用すると、現在のプロセス（pstreeを実行しているプロセス）がハイライト表示されます。
- 出力が長すぎる場合は、`pstree | less`のようにパイプして閲覧すると便利です。
- 同じプロセスが多数ある場合（例：ウェブサーバーの子プロセス）、`-c`オプションを使用すると、それらを個別に表示できます。

## 参考情報

https://man7.org/linux/man-pages/man1/pstree.1.html