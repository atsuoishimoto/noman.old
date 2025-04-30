# pstree コマンド

プロセスツリーを表示します。

## 概要

`pstree`コマンドは、実行中のプロセスをツリー構造で表示します。親プロセスと子プロセスの関係が視覚的に理解しやすく表示されるため、システム上で何が実行されているかを把握するのに役立ちます。デフォルトでは、すべてのプロセスが表示されますが、特定のプロセスIDを指定して、そのプロセスから派生したツリーのみを表示することも可能です。

## オプション

### **-a**

コマンドライン引数を表示します。

```console
$ pstree -a
systemd
  ├─ModemManager
  ├─NetworkManager --no-daemon
  │   └─2*[{NetworkManager}]
  ├─accounts-daemon
  │   └─2*[{accounts-daemon}]
  ├─avahi-daemon --syslog
  │   └─avahi-daemon --syslog
```

### **-p**

各プロセスのPID（プロセスID）を表示します。

```console
$ pstree -p
systemd(1)─┬─ModemManager(852)
           ├─NetworkManager(853)─┬─{NetworkManager}(873)
           │                     └─{NetworkManager}(875)
           ├─accounts-daemon(856)─┬─{accounts-daemon}(857)
           │                      └─{accounts-daemon}(858)
```

### **-u**

各プロセスのユーザー名を表示します。

```console
$ pstree -u
systemd─┬─ModemManager(root)
        ├─NetworkManager(root)─┬─{NetworkManager}(root)
        │                      └─{NetworkManager}(root)
        ├─accounts-daemon(root)─┬─{accounts-daemon}(root)
        │                       └─{accounts-daemon}(root)
```

### **-h**

現在のプロセスとその親を強調表示します。

```console
$ pstree -h
systemd─┬─ModemManager
        ├─NetworkManager─┬─{NetworkManager}
        │                └─{NetworkManager}
        ├─accounts-daemon─┬─{accounts-daemon}
        │                 └─{accounts-daemon}
        └─bash───pstree
```

## 使用例

### 特定のユーザーのプロセスを表示

```console
$ pstree username
bash───vim
```

### 特定のプロセスIDから始まるツリーを表示

```console
$ pstree 1234
bash───python3───2*[{python3}]
```

### PIDとコマンドライン引数を同時に表示

```console
$ pstree -ap 1
systemd --system --deserialize 21
  ├─ModemManager
  ├─NetworkManager --no-daemon
  │   └─2*[{NetworkManager}]
  ├─accounts-daemon
  │   └─2*[{accounts-daemon}]
```

## ヒント:

### 同じプロセスの複数のインスタンスを圧縮表示

デフォルトでは、同じ名前の複数のプロセスは「2*[プロセス名]」のように圧縮されます。`-c`オプションを使用すると、この圧縮を無効にできます。

### プロセスツリーの深さを制限

`-n`オプションを使用すると、表示するツリーの深さを制限できます。例えば、`pstree -n 2`は2レベルまでのプロセスのみを表示します。

### グラフィカルな区切り文字を変更

`-A`、`-U`、`-V`オプションを使用して、ツリーの表示に使用される文字を変更できます。例えば、`pstree -A`はASCII文字のみを使用します。

## よくある質問

#### Q1. `pstree`と`ps`の違いは何ですか？
A. `ps`はプロセスを一覧形式で表示しますが、`pstree`はプロセス間の親子関係をツリー構造で視覚的に表示します。

#### Q2. 特定のプロセスから始まるツリーを表示するにはどうすればよいですか？
A. `pstree PID`のようにプロセスIDを指定すると、そのプロセスから始まるツリーが表示されます。

#### Q3. プロセスのコマンドライン引数を表示するにはどうすればよいですか？
A. `pstree -a`オプションを使用すると、各プロセスのコマンドライン引数が表示されます。

#### Q4. 同じプロセスの複数のインスタンスを個別に表示するにはどうすればよいですか？
A. `pstree -c`オプションを使用すると、同じプロセスの複数のインスタンスが個別に表示されます。

## macOSでの注意点

macOSには標準で`pstree`コマンドが含まれていません。Homebrewを使用してインストールできます：

```console
$ brew install pstree
```

macOSでは、代わりに`ps -e -o pid,ppid,user,command`や`ps axjf`コマンドを使用してプロセス階層を確認することもできます。

## 参照

https://man7.org/linux/man-pages/man1/pstree.1.html

## Revisions

- 2025/04/30 First revision