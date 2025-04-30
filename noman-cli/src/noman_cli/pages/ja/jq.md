# jq コマンド

JSONデータを柔軟に処理・変換するためのコマンドラインツール。

## 概要

`jq`はJSONデータを操作するための強力なコマンドラインプロセッサです。JSONの整形表示、フィルタリング、変換、抽出などの操作を行うことができます。複雑なJSONデータを簡単に扱えるようにする「JSONのsed」とも呼ばれています。

## オプション

### **-r, --raw-output**

出力時に文字列の引用符を取り除きます。

```console
$ echo '{"name": "Taro"}' | jq '.name'
"Taro"

$ echo '{"name": "Taro"}' | jq -r '.name'
Taro
```

### **-c, --compact-output**

出力を1行にまとめて表示します。

```console
$ echo '{"name": "Taro", "age": 30}' | jq '.'
{
  "name": "Taro",
  "age": 30
}

$ echo '{"name": "Taro", "age": 30}' | jq -c '.'
{"name":"Taro","age":30}
```

### **-s, --slurp**

複数のJSONオブジェクトを1つの配列にまとめます。

```console
$ echo '{"id": 1}\n{"id": 2}' | jq '.'
{
  "id": 1
}
{
  "id": 2
}

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

### **-f, --from-file**

フィルタをファイルから読み込みます。

```console
$ echo 'map(.id)' > filter.jq
$ echo '[{"id": 1, "name": "Taro"}, {"id": 2, "name": "Hanako"}]' | jq -f filter.jq
[
  1,
  2
]
```

## 使用例

### 特定のキーの値を抽出する

```console
$ echo '{"user": {"name": "Taro", "age": 30}}' | jq '.user.name'
"Taro"
```

### 配列から特定の要素を抽出する

```console
$ echo '{"users": [{"name": "Taro"}, {"name": "Hanako"}]}' | jq '.users[1].name'
"Hanako"
```

### 配列をフィルタリングする

```console
$ echo '[{"name": "Taro", "age": 30}, {"name": "Hanako", "age": 25}]' | jq '.[] | select(.age > 28)'
{
  "name": "Taro",
  "age": 30
}
```

### 配列の要素を変換する

```console
$ echo '[{"name": "Taro"}, {"name": "Hanako"}]' | jq 'map({username: .name})'
[
  {
    "username": "Taro"
  },
  {
    "username": "Hanako"
  }
]
```

## ヒント:

### パイプとの組み合わせ

curlなどのコマンドと組み合わせてAPIレスポンスを処理できます。

```console
$ curl -s https://api.example.com/users | jq '.[] | select(.active == true)'
# アクティブなユーザーのみを表示する
```

### 複雑なフィルタの構築

複数のフィルタを組み合わせて複雑な処理を行えます。

```console
$ echo '{"users": [{"name": "Taro", "age": 30}, {"name": "Hanako", "age": 25}]}' | jq '.users | map(select(.age > 28)) | .[].name'
"Taro"
```

### 出力形式の変換

JSONからCSVなどの他の形式に変換できます。

```console
$ echo '[{"name": "Taro", "age": 30}, {"name": "Hanako", "age": 25}]' | jq -r '.[] | [.name, .age] | @csv'
"Taro",30
"Hanako",25
```

## よくある質問

#### Q1. jqのフィルタ式はどのような構文ですか？
A. jqのフィルタ式はドット(`.`)で始まり、JSONのパスを指定します。例えば、`.users[0].name`は最初のユーザーの名前を取得します。

#### Q2. 複数のJSONファイルを一度に処理できますか？
A. はい、`jq -s`オプションを使用して複数のJSONを1つの配列として処理できます。または、`jq -f filter.jq file1.json file2.json`のように複数のファイルを指定することもできます。

#### Q3. jqで条件付きフィルタリングを行うにはどうすればよいですか？
A. `select()`関数を使用します。例えば、`.[] | select(.age > 30)`は30歳より上のレコードを選択します。

#### Q4. macOSにjqをインストールするにはどうすればよいですか？
A. Homebrewを使用して`brew install jq`でインストールできます。

## 参考

https://stedolan.github.io/jq/manual/

## Revisions

- 2025/04/30 First revision