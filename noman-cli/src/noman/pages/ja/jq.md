# jq コマンド

JSONデータを軽量で柔軟なコマンドラインプロセッサで処理・変換します。

## 概要

`jq`はコマンドラインJSON処理ツールで、構造化データの切り出し、フィルタリング、マッピング、変換を簡単に行えます。JSONデータに対する`sed`のように機能し、複雑なスクリプトを書かなくても特定のフィールドの抽出、値の変換、配列のフィルタリングなどを行うことができます。

## オプション

### **-r, --raw-output**

文字列を引用符なしで出力し、より読みやすい結果を得られます。

```console
$ echo '{"name": "John"}' | jq -r '.name'
John
```

### **-s, --slurp**

複数のJSONオブジェクトを読み込み、それらを配列に結合します。

```console
$ echo '{"id": 1}\n{"id": 2}' | jq -s '.'
[
  {
    "id": 1
  },
  {
    "id": 2
  }
]
```

### **-f, --from-file FILENAME**

コマンドラインではなくファイルからフィルターを読み込みます。

```console
$ echo '{"name": "John", "age": 30}' | jq -f filter.jq
# filter.jqの内容: .name
"John"
```

### **-c, --compact-output**

整形されたJSONではなく、コンパクトなJSONを出力します。

```console
$ echo '{"name": "John", "age": 30}' | jq -c '.'
{"name":"John","age":30}
```

### **-n, --null-input**

入力を読み込まず、フィルターに基づいて結果を生成します。

```console
$ jq -n '{"hello": "world"}'
{
  "hello": "world"
}
```

## 使用例

### 特定のフィールドの抽出

```console
$ echo '{"user": {"name": "John", "age": 30}}' | jq '.user.name'
"John"
```

### 配列のフィルタリング

```console
$ echo '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]' | jq '.[] | select(.age > 28)'
{
  "name": "John",
  "age": 30
}
```

### データの変換

```console
$ echo '[{"name": "John"}, {"name": "Jane"}]' | jq 'map({username: .name})'
[
  {
    "username": "John"
  },
  {
    "username": "Jane"
  }
]
```

### 配列の操作

```console
$ echo '{"users": ["John", "Jane", "Bob"]}' | jq '.users[1]'
"Jane"
```

## ヒント:

### 複数のフィルターをパイプでつなぐ

複数のフィルターをパイプでつないで複雑な変換を実行できます：

```console
$ echo '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]' | jq '.[] | select(.age > 25) | .name'
"John"
```

### 組み込み関数を使用する

`jq`には`length`、`keys`、`has`、`map`など多くの組み込み関数があり、データ操作が容易になります：

```console
$ echo '{"a": 1, "b": 2, "c": 3}' | jq 'keys'
[
  "a",
  "b",
  "c"
]
```

### 変数を作成する

複雑なフィルターで再利用するために`as`キーワードを使用して変数を作成できます：

```console
$ echo '{"items": [{"price": 10}, {"price": 20}]}' | jq '.items | map(.price) | add as $total | {"total": $total, "count": length}'
{
  "total": 30,
  "count": 2
}
```

## よくある質問

#### Q1. jqでJSONをフォーマットするにはどうすればよいですか？
A. JSONを`jq '.'`にパイプするだけで整形された出力が得られます。

#### Q2. 引用符なしで値を抽出するにはどうすればよいですか？
A. `-r`または`--raw-output`オプションを使用すると、引用符なしで文字列を出力できます。

#### Q3. 条件に基づいて配列をフィルタリングするにはどうすればよいですか？
A. 条件付きの`select()`を使用します：`jq '.[] | select(.field == "value")'`

#### Q4. 複数のJSONファイルを処理するにはどうすればよいですか？
A. `-s`（slurp）オプションを使用して、複数の入力を配列に結合します。

#### Q5. 既存のデータから新しいJSONを作成するにはどうすればよいですか？
A. フィルター内でオブジェクトリテラルを作成します：`jq '{new_key: .old_key, calculated: (.value * 2)}'`

## 参考資料

https://stedolan.github.io/jq/manual/

## 改訂履歴

- 2025/05/04 初版作成