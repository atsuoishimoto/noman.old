# iotop コマンド
プロセスごとの I/O 使用状況をリアルタイムで監視するツール。

## 概要
`iotop` は Linux システム上でプロセスやスレッドの I/O（入出力）使用状況をリアルタイムで監視するためのコマンドラインユーティリティです。ディスク I/O のボトルネックを特定したり、どのプロセスがディスクリソースを最も使用しているかを確認するのに役立ちます。`top` コマンドに似ていますが、CPU やメモリではなく I/O 使用状況に特化しています。

## オプション
### **-o, --only**
I/O を実際に行っているプロセスのみを表示します。

```console
$ sudo iotop -o
合計 DISK READ:       0.00 B/s | 合計 DISK WRITE:       7.56 K/s
現在 DISK READ:       0.00 B/s | 現在 DISK WRITE:       0.00 B/s
  PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
 1234  be/4  root        0.00 B/s    7.56 K/s  0.00 %  0.00 % systemd-journald
```

### **-b, --batch**
バッチモードで実行します。非対話的な出力形式で、ログファイルへの出力やスクリプト内での使用に適しています。

```console
$ sudo iotop -b -n 3
合計 DISK READ:       0.00 B/s | 合計 DISK WRITE:      15.72 K/s
現在 DISK READ:       0.00 B/s | 現在 DISK WRITE:       0.00 B/s
  PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
    1  be/4  root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd --system
...
```

### **-n NUM, --iter=NUM**
指定した回数だけ更新して終了します。バッチモードと組み合わせて使用すると便利です。

```console
$ sudo iotop -b -n 2
合計 DISK READ:       0.00 B/s | 合計 DISK WRITE:      12.46 K/s
現在 DISK READ:       0.00 B/s | 現在 DISK WRITE:       0.00 B/s
...
合計 DISK READ:       0.00 B/s | 合計 DISK WRITE:      14.32 K/s
現在 DISK READ:       0.00 B/s | 現在 DISK WRITE:       0.00 B/s
...
```

### **-d SEC, --delay=SEC**
更新間隔を秒単位で指定します（デフォルトは1秒）。

```console
$ sudo iotop -d 5
# 5秒ごとに画面が更新される
```

## 使用例
### 実際に I/O を行っているプロセスのみを表示
```console
$ sudo iotop -o
合計 DISK READ:       1.21 M/s | 合計 DISK WRITE:     256.84 K/s
現在 DISK READ:       0.00 B/s | 現在 DISK WRITE:      12.56 K/s
  PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
 5432  be/4  postgres    1.21 M/s   245.32 K/s  0.00 %  2.34 % postgres: writer process
 1234  be/4  www-data    0.00 B/s    11.52 K/s  0.00 %  0.12 % apache2 -k start
```

### 特定のユーザーのプロセスのみを表示
```console
$ sudo iotop -u postgres
合計 DISK READ:       0.85 M/s | 合計 DISK WRITE:     178.45 K/s
現在 DISK READ:       0.00 B/s | 現在 DISK WRITE:       8.72 K/s
  PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
 5432  be/4  postgres    0.85 M/s   178.45 K/s  0.00 %  1.87 % postgres: writer process
 5433  be/4  postgres    0.00 B/s     0.00 B/s  0.00 %  0.00 % postgres: wal writer process
 5434  be/4  postgres    0.00 B/s     0.00 B/s  0.00 %  0.00 % postgres: autovacuum launcher
```

### バッチモードで出力をファイルに保存
```console
$ sudo iotop -b -n 10 -d 5 > io_activity.log
# 5秒間隔で10回の測定結果をio_activity.logファイルに保存する
```

## ヒント:
### 管理者権限が必要
`iotop` の実行には通常、root 権限（sudo）が必要です。権限がない場合は「Permission denied」エラーが表示されます。

### キーボードショートカット
対話モードでは、以下のキーが使用できます：
- `o`: `-o` オプションと同様に、I/O を行っているプロセスのみの表示を切り替え
- `p`: プロセスごとの表示とスレッドごとの表示を切り替え
- `a`: 累積 I/O の表示を切り替え
- `q`: 終了

### 累積モードの活用
`a` キーを押すと累積モードになり、プログラムの起動以降の合計 I/O 量を確認できます。長時間実行されるプロセスの I/O パターンを分析するのに役立ちます。

## よくある質問
#### Q1. `iotop` と `top` の違いは何ですか？
A. `top` は CPU やメモリ使用率を中心に監視するのに対し、`iotop` はディスク I/O 使用状況に特化しています。ディスク I/O がボトルネックになっている場合に `iotop` が特に役立ちます。

#### Q2. `iotop` が「DISK READ/WRITE」と「IO>」の両方を表示するのはなぜですか？
A. 「DISK READ/WRITE」は実際のディスク読み書き速度を示し、「IO>」はプロセスが I/O 待ちで費やした時間の割合を示します。両方を見ることで、I/O 使用パターンをより詳細に理解できます。

#### Q3. `iotop` をインストールするにはどうすればよいですか？
A. Debian/Ubuntu では `sudo apt install iotop`、RHEL/CentOS では `sudo yum install iotop` または `sudo dnf install iotop` でインストールできます。

#### Q4. `iotop` が「CONFIG_TASK_DELAY_ACCT not enabled in kernel」というエラーを表示する場合はどうすればよいですか？
A. このエラーは、カーネルが必要な機能をサポートしていないことを示しています。カーネルを再コンパイルするか、より新しいバージョンのカーネルを使用する必要があります。

## 参考情報
https://github.com/Tomas-M/iotop

## 改訂履歴
- 2025/04/29 初版作成