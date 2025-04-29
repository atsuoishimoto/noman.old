# jq コマンド概要

`jq`は、JSONデータを処理・操作するためのコマンドラインツールです。JSONデータのフィルタリング、変換、整形を簡単に行うことができます。

## オプション

### **-r, --raw-output**

出力時に引用符を取り除き、生のテキストとして表示します。

```bash
$ echo '{"name": "Taro"}' | jq '.name'
"Taro"

$ echo '{"name": "Taro"}' | jq -r '.name'
Taro
```

### **-c, --compact-output**

JSONを整形せず、コンパクトな形式で出力します。

```bash
$ echo '{"name": "Taro", "age": 30}' | jq '.'
{
  "name": "Taro",
  "age": 30
}

$ echo '{"name": "Taro", "age": 30}' | jq -c '.'
{"name":"Taro","age":30}
```

### **-f, --from-file**

フィルタをファイルから読み込みます。

```bash
$ echo 'select(.age > 25)' > filter.jq
$ echo '[{"name": "Taro", "age": 30}, {"name": "Hanako", "age": 20}]' | jq -f filter.jq
{
  "name": "Taro",
  "age": 30
}
```

### **-s, --slurp**

複数のJSONオブジェクトを配列として扱います。

```bash
$ echo '{"name": "Taro"} {"name": "Hanako"}' | jq -s '.'
[
  {
    "name": "Taro"
  },
  {
    "name": "Hanako"
  }
]
```

## 使用例

### 基本的なフィルタリング

```bash
$ echo '{"user": {"name": "Taro", "age": 30, "email": "taro@example.com"}}' | jq '.user.name'
"Taro"
```

### 配列の処理

```bash
$ echo '{"users": [{"name": "Taro"}, {"name": "Hanako"}, {"name": "Jiro"}]}' | jq '.users[].name'
"Taro"
"Hanako"
"Jiro"
```

### 条件フィルタリング

```bash
$ echo '[{"name": "Taro", "age": 30}, {"name": "Hanako", "age": 25}, {"name": "Jiro", "age": 35}]' | jq '.[] | select(.age > 28)'
{
  "name": "Taro",
  "age": 30
}
{
  "name": "Jiro",
  "age": 35
}
```

### データ変換

```bash
$ echo '[{"name": "Taro", "age": 30}, {"name": "Hanako", "age": 25}]' | jq 'map({名前: .name, 年齢: .age})'
[
  {
    "名前": "Taro",
    "年齢": 30
  },
  {
    "名前": "Hanako",
    "年齢": 25
  }
]
```

## よくある質問

### Q1. jqの基本的な使い方は？
A. パイプ（`|`）を使ってJSONデータを渡し、フィルタ式を指定します。例：`cat data.json | jq '.fieldname'`

### Q2. 特定のキーだけを抽出するには？
A. ドット表記を使います。例えば、`jq '.name'`は「name」キーの値を抽出します。

### Q3. 配列から特定の要素を取得するには？
A. インデックスを使います。例：`jq '.users[0]'`は配列の最初の要素を取得します。

### Q4. 複数のフィールドを選択するには？
A. `{}`を使って新しいオブジェクトを作成します。例：`jq '{name: .name, age: .age}'`

### Q5. jqのフィルタを保存して再利用できますか？
A. はい、`-f`オプションを使ってファイルからフィルタを読み込めます。

## 追加情報

- jqはパイプラインを使った複雑な処理も可能です。例：`.[] | select(.active == true) | .name`
- 出力をCSVやTSVに変換することもできます：`jq -r '.[] | [.name, .age] | @csv'`
- 複雑なJSONデータを扱う場合は、まず`jq '.'`で整形表示して構造を確認すると便利です。
- jqのフィルタ式は独自の言語で書かれており、学習曲線がありますが、一度マスターすると非常に強力です。
- オンラインでjqを試せるサイト（[jqplay.org](https://jqplay.org/)など）を活用すると学習に役立ちます。