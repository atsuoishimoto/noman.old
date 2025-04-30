# iotop コマンド

I/O 使用量をプロセスごとに監視するリアルタイムモニタリングツール。

## 概要

`iotop` は Linux システム上でプロセスごとの I/O（入出力）使用状況をリアルタイムで表示するコマンドです。ディスク I/O のボトルネックを特定したり、どのプロセスがディスクを最も使用しているかを確認したりするのに役立ちます。`top` コマンドに似ていますが、CPU やメモリではなく I/O 使用量に特化しています。

## オプション

### **-o, --only**

I/O を実際に行っているプロセスのみを表示します。

```console
$ sudo iotop -o
Total DISK READ:       0.00 B/s | Total DISK WRITE:       7.63 K/s
Current DISK READ:     0.00 B/s | Current DISK WRITE:     0.00 B/s
  PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
 1234  be/4  root        0.00 B    7.63 K/s  0.00 %  0.00 % systemd-journald
```

### **-b, --batch**

バッチモードで実行します。非対話的な出力形式で、ログファイルへのリダイレクトに適しています。

```console
$ sudo iotop -b -n 3
Total DISK READ:       0.00 B/s | Total DISK WRITE:      15.27 K/s
Current DISK READ:     0.00 B/s | Current DISK WRITE:     0.00 B/s
  PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
    1  be/4  root        0.00 B    0.00 B/s  0.00 %  0.00 % systemd
  ...
```

### **-n NUM, --iter=NUM**

指定した回数だけ更新して終了します。バッチモードと組み合わせて使用すると便利です。

```console
$ sudo iotop -b -n 2
Total DISK READ:       0.00 B/s | Total DISK WRITE:      15.27 K/s
...
Total DISK READ:       0.00 B/s | Total DISK WRITE:      12.45 K/s
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
Total DISK READ:       1.02 M/s | Total DISK WRITE:      156.68 K/s
Current DISK READ:     0.00 B/s | Current DISK WRITE:     23.44 K/s
  PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
 1234  be/4  postgres   1.02 M/s    0.00 B/s  0.00 %  0.12 % postgres: autovacuum worker process
  567  be/4  www-data   0.00 B/s  156.68 K/s  0.00 %  0.05 % apache2 -k start
```

### 特定のプロセスの I/O 使用状況を監視してログに記録

```console
$ sudo iotop -b -o -p 1234,5678 -n 10 > io_log.txt
# プロセスID 1234と5678の I/O 使用状況を10回記録してio_log.txtに保存
```

### 累積 I/O 統計を表示

```console
$ sudo iotop -a
# 起動してから累積された I/O 統計が表示される
# 通常モードでは「A」キーを押すことでも切り替え可能
```

## ヒント:

### 対話モードでのキーボードショートカット

対話モードでは、以下のキーを使用して表示を制御できます：
- `o`: I/O を行っているプロセスのみ表示/すべて表示を切り替え
- `p`: PID でソート
- `a`: 累積 I/O 統計の表示/非表示を切り替え
- `q`: 終了

### root 権限が必要

`iotop` は通常、root 権限が必要です。一般ユーザーで実行する場合は `sudo` を使用してください。

### 長時間の I/O モニタリング

長時間の I/O 使用状況を分析するには、バッチモードとリダイレクトを組み合わせて使用します：
```bash
sudo iotop -b -o -n 60 -d 60 > io_usage.log
```
これにより、1時間にわたって1分ごとに I/O を行っているプロセスの情報が記録されます。

## よくある質問

#### Q1. `iotop` をインストールするにはどうすればよいですか？
A. Debian/Ubuntu では `sudo apt install iotop`、CentOS/RHEL では `sudo yum install iotop` でインストールできます。

#### Q2. `iotop` が「CONFIG_TASK_DELAY_ACCT not enabled in kernel」というエラーを表示する場合はどうすればよいですか？
A. このエラーはカーネルに必要な機能が有効になっていないことを示しています。カーネルを再コンパイルするか、より新しいバージョンのディストリビューションを使用する必要があります。

#### Q3. 特定のプロセスだけを監視するにはどうすればよいですか？
A. `-p PID` または `--pid=PID` オプションを使用して、特定のプロセス ID を指定できます。複数のプロセスを監視する場合はカンマで区切ります（例：`-p 1234,5678`）。

#### Q4. `iotop` の出力を理解するにはどうすればよいですか？
A. 主な列は以下の通りです：
- DISK READ/WRITE: プロセスのディスク読み書き速度
- SWAPIN: スワップインの割合
- IO>: プロセスが I/O 待ちで費やした時間の割合
- COMMAND: プロセス名とコマンドライン引数

## 参考資料

https://linux.die.net/man/1/iotop

## Revisions

- 2025/04/30 初版作成