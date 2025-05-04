# split コマンド

ファイルを複数の小さな部分に分割します。

## 概要

`split`コマンドは、ファイルを複数の小さなファイルに分割します。大きなファイルを扱いやすく、転送しやすく、または保存しやすくするために役立ちます。デフォルトでは、'xaa'、'xab'などの名前のファイルを作成し、それぞれに元のファイルから指定された行数またはバイト数が含まれます。

## オプション

### **-b, --bytes=SIZE**

行ではなくバイト単位で分割します。SIZEは数字の後に乗数を付けることができます：k (1024)、m (1024²)、g (1024³)など。

```console
$ split -b 1M largefile.dat chunk_
$ ls chunk_*
chunk_aa  chunk_ab  chunk_ac
```

### **-l, --lines=NUMBER**

出力ファイルごとに特定の行数で分割します（デフォルトは1000行）。

```console
$ split -l 100 data.csv part_
$ ls part_*
part_aa  part_ab  part_ac  part_ad
```

### **-d, --numeric-suffixes[=FROM]**

アルファベットの接尾辞ではなく、数値の接尾辞を使用します。FROMから開始します（デフォルトは0）。

```console
$ split -d -l 100 data.txt section_
$ ls section_*
section_00  section_01  section_02
```

### **-a, --suffix-length=N**

長さNの接尾辞を生成します（デフォルトは2）。

```console
$ split -a 3 -l 100 data.txt part_
$ ls part_*
part_aaa  part_aab  part_aac  part_aad
```

### **--additional-suffix=SUFFIX**

ファイル名に追加の接尾辞SUFFIXを付加します。

```console
$ split -l 100 --additional-suffix=.txt data.csv part_
$ ls part_*
part_aa.txt  part_ab.txt  part_ac.txt
```

### **-n, --number=CHUNKS**

サイズまたは数に基づいてCHUNKS個のファイルに分割します。

```console
$ split -n 3 largefile.dat chunk_
$ ls chunk_*
chunk_aa  chunk_ab  chunk_ac
```

## 使用例

### 大きなログファイルをサイズで分割する

```console
$ split -b 10M large_log.log log_chunk_
$ ls -lh log_chunk_*
-rw-r--r-- 1 user group 10M May 4 10:15 log_chunk_aa
-rw-r--r-- 1 user group 10M May 4 10:15 log_chunk_ab
-rw-r--r-- 1 user group 5.2M May 4 10:15 log_chunk_ac
```

### CSVファイルを行数で分割し、番号付き出力にする

```console
$ split -d -l 1000 --additional-suffix=.csv large_dataset.csv dataset_
$ ls dataset_*
dataset_00.csv  dataset_01.csv  dataset_02.csv
```

### ファイルを等分に分割する

```console
$ split -n l/4 bigfile.txt equal_part_
$ ls -lh equal_part_*
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_aa
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_ab
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_ac
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_ad
```

## ヒント:

### 分割ファイルの再結合

`split`コマンドで分割したファイルを再結合するには、`cat`コマンドを正しい順序でファイルに使用します：
```console
$ cat chunk_* > original_file_restored
```

### 適切な分割サイズの選択

転送用（メール添付ファイルなど）にファイルを分割する場合は、宛先のサイズ制限を考慮してください。例えば、10MB未満である必要があるファイルには`-b 10M`を使用します。

### 圧縮との併用

より効率的にするために、圧縮後に分割します：
```console
$ gzip -c largefile > largefile.gz
$ split -b 10M largefile.gz largefile.gz.part_
```

## よくある質問

#### Q1. ファイルを等サイズのチャンクに分割するにはどうすればよいですか？
A. `split -n l/N filename`を使用します。Nは希望する等分の数です。

#### Q2. ファイルを分割して元のファイル拡張子を維持するにはどうすればよいですか？
A. `--additional-suffix`オプションを使用します：`split -l 1000 file.csv part_ --additional-suffix=.csv`

#### Q3. `-b`と`-n`の違いは何ですか？
A. `-b`は正確なバイトサイズで分割しますが、`-n`は特定の数のチャンクに分割し、サイズが異なる可能性があります。

#### Q4. 実際にファイルを分割せずに、splitが何をするかをプレビューできますか？
A. いいえ、`split`にはプレビューやドライランオプションはありません。分割を計画するために、まず`wc -l`を使用して行数を数えることができます。

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html

## 改訂履歴

- 2025/05/04 初版作成