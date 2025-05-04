# iotop コマンド

システム上のプロセスによるI/O使用状況を監視します。

## 概要

`iotop`は、プロセスのリアルタイムディスクI/O使用情報を表示するtopに似たユーティリティです。どのプロセスがディスクを使用しているか、どれだけ読み書きしているか、そしてそのI/O優先度を表示します。このツールは、高いディスクアクティビティを引き起こしているプロセスを特定するのに特に役立ちます。

## オプション

### **-o, --only**

実際にI/Oを実行しているプロセスやスレッドのみを表示します

```console
$ sudo iotop -o
Total DISK READ:         0.00 B/s | Total DISK WRITE:         7.56 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
   1234 be/4 root        0.00 B/s    7.56 K/s  0.00 %  0.00 % systemd-journald
```

### **-b, --batch**

非対話モードで実行します。ログ記録に便利です

```console
$ sudo iotop -b -n 3
Total DISK READ:         0.00 B/s | Total DISK WRITE:        15.69 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
      1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd
    346 be/4 root        0.00 B/s    7.84 K/s  0.00 %  0.00 % systemd-journald
[...]
```

### **-n NUM, --iter=NUM**

終了前の繰り返し回数を設定します（非対話モード用）

```console
$ sudo iotop -b -n 2
[ディスクI/O統計の2回の繰り返しを表示]
```

### **-d SEC, --delay=SEC**

繰り返し間の遅延を秒単位で設定します（デフォルトは1.0）

```console
$ sudo iotop -d 5
[5秒ごとに表示を更新]
```

### **-p PID, --pid=PID**

指定したプロセスIDのみを監視します

```console
$ sudo iotop -p 1234
[PID 1234のプロセスのI/O統計のみを表示]
```

### **-a, --accumulated**

帯域幅ではなく累積I/Oを表示します

```console
$ sudo iotop -a
[iotop起動以降の各プロセスが実行した総I/Oを表示]
```

## 使用例

### 基本的な監視

```console
$ sudo iotop
Total DISK READ:         0.00 B/s | Total DISK WRITE:        23.45 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       7.84 K/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
      1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd
    346 be/4 root        0.00 B/s    7.84 K/s  0.00 %  0.00 % systemd-journald
[...]
```

### アクティブなI/Oプロセスのみを監視してファイルにログを記録

```console
$ sudo iotop -bo -n 60 -d 10 > disk_activity.log
[I/Oを実行しているプロセスの10秒間隔で60回のスナップショットを記録]
```

### 特定のプロセスの監視

```console
$ sudo iotop -p 1234,5678
[PID 1234と5678のプロセスのI/O統計のみを表示]
```

## ヒント:

### sudoで実行

`iotop`はI/O統計にアクセスするためにroot権限が必要です。常に`sudo`を付けるかrootユーザーとして実行してください。

### 忙しいシステムでは-oを使用

多くのプロセスが動作しているシステムでは、`-o`オプションを使用して実際にI/O操作を実行しているプロセスのみを表示すると、問題のあるプロセスを特定しやすくなります。

### キーボードショートカット

対話モードで実行中に以下のキーが使えます：
- `o` --onlyオプションの切り替え
- `p` プロセス表示の切り替え（スレッドではなく）
- `a` 累積I/Oモードの切り替え
- `q` 終了

### ログ記録と組み合わせる

断続的なI/O問題のトラブルシューティングには、`iotop`をバッチモードで実行し、出力をログファイルにリダイレクトして後で分析できるようにしましょう。

## よくある質問

#### Q1. 「iotop: command not found」と表示されるのはなぜですか？
A. `iotop`はデフォルトではインストールされていない場合があります。ディストリビューションのパッケージマネージャを使用してインストールしてください（例：Debian/Ubuntuでは`apt install iotop`、RHEL/CentOSでは`yum install iotop`）。

#### Q2. iotopを実行すると「Permission denied」と表示されるのはなぜですか？
A. `iotop`はI/O統計にアクセスするためにroot権限が必要です。`sudo iotop`として実行するか、rootユーザーとして実行してください。

#### Q3. ディスクI/Oスパイクを引き起こしているプロセスを確認するにはどうすればよいですか？
A. `sudo iotop -o`を実行して、アクティブにI/O操作を実行しているプロセスのみを表示します。

#### Q4. SWAPINとIO列は何を意味していますか？
A. SWAPINはプロセスがスワップインに費やした時間の割合を示し、IOはプロセスがI/O待ちに費やした時間の割合を示します。

## 参考資料

https://man7.org/linux/man-pages/man8/iotop.8.html

## 改訂履歴

- 2025/05/04 初回改訂