# awk コマンド概要

`awk` はテキスト処理のためのプログラミング言語であり、パターンマッチングとテキスト操作に特化したコマンドです。ファイルやパイプからのデータを行単位で処理し、フィールド（列）ごとに操作できます。

## オプション

### **-F** (フィールドセパレータ)

入力データのフィールド区切り文字を指定します。デフォルトは空白（スペースまたはタブ）です。

```bash
$ echo "apple,orange,banana" | awk -F, '{print $2}'
orange
```

### **-v** (変数設定)

awk プログラム内で使用する変数に値を設定します。

```bash
$ awk -v name="Taro" '{print "Hello, " name "! This is line " NR}' sample.txt
Hello, Taro! This is line 1
Hello, Taro! This is line 2
```

### **-f** (ファイル指定)

awk プログラムをファイルから読み込みます。

```bash
$ cat program.awk
{print $1, $3}
$ awk -f program.awk data.txt
# data.txtの各行の1列目と3列目が表示される
```

## 使用例

### 基本的な列の抽出

```bash
$ cat data.txt
John 25 Tokyo
Mary 30 Osaka
Bob 22 Kyoto
$ awk '{print $1, $3}' data.txt
John Tokyo
Mary Osaka
Bob Kyoto
```

### 条件付き処理

```bash
$ awk '$2 > 25 {print $1 "さんは" $2 "歳です"}' data.txt
Mary さんは30歳です
```

### 合計値の計算

```bash
$ cat numbers.txt
10
20
30
40
$ awk '{sum += $1} END {print "合計: " sum}' numbers.txt
合計: 100
```

### CSVファイルの特定列を抽出

```bash
$ cat data.csv
名前,年齢,都市
田中,25,東京
佐藤,30,大阪
鈴木,22,京都
$ awk -F, '{print $1 "さんは" $3 "に住んでいます"}' data.csv
名前さんは都市に住んでいます
田中さんは東京に住んでいます
佐藤さんは大阪に住んでいます
鈴木さんは京都に住んでいます
```

## よくある質問

### Q1. awk の基本的な構文は？
A. 基本構文は `awk 'パターン {アクション}' ファイル名` です。パターンに一致する行に対してアクションが実行されます。

### Q2. 特定の列だけを表示するには？
A. `awk '{print $1, $3}' ファイル名` のように、`$n` で n 番目の列を指定できます。

### Q3. 行番号を表示するには？
A. 組み込み変数 `NR` を使用します：`awk '{print NR, $0}' ファイル名`

### Q4. ヘッダー行をスキップするには？
A. `awk 'NR > 1 {print $1}' ファイル名` のように、NR（行番号）を使って条件付けできます。

## 追加情報

- `$0` は行全体を表します
- `NF` は各行のフィールド（列）数を表す変数です
- `BEGIN {...}` はファイル処理前に実行されるブロックです
- `END {...}` はファイル処理後に実行されるブロックです
- 複雑な処理には、条件文（if-else）やループ（for, while）も使用できます
- 正規表現を使ったパターンマッチングも強力な機能です：`awk '/pattern/ {print}'`