# getopt

`getopt`は、コマンドラインオプションを解析するためのユーティリティです。シェルスクリプト内でコマンドライン引数を標準化された方法で処理するのに役立ちます。

## オプション

### **-o, --options**

短いオプション（一文字）を指定します。

```bash
$ getopt -o a:bc file1 file2
 -a 'file1' -b -c -- 'file2'
```

### **-l, --longoptions**

長いオプション（単語）を指定します。

```bash
$ getopt -o a:bc -l alpha:,beta,gamma file1 file2
 -a 'file1' -b -c -- 'file2'
```

### **-n, --name**

エラーメッセージに表示するプログラム名を指定します。

```bash
$ getopt -n myscript -o a:bc file1 file2
 -a 'file1' -b -c -- 'file2'
```

### **-q, --quiet**

エラーメッセージを抑制します。

```bash
$ getopt -q -o a:bc -- -x file1
 -- '-x' 'file1'
```

### **-u, --unquoted**

出力を引用符で囲まないようにします。

```bash
$ getopt -u -o a:bc -- -a file1
 -a file1 --
```

## 使用例

### 基本的なシェルスクリプトでの使用例

```bash
#!/bin/bash
# オプションを解析
OPTS=$(getopt -o ab:c -l alpha,beta:,gamma -- "$@")
eval set -- "$OPTS"

# オプションを処理
while true; do
  case "$1" in
    -a | --alpha) ALPHA=true; shift ;;
    -b | --beta) BETA="$2"; shift 2 ;;
    -c | --gamma) GAMMA=true; shift ;;
    --) shift; break ;;
    *) echo "不明なオプション: $1"; exit 1 ;;
  esac
done

# 残りの引数を処理
echo "ALPHA=$ALPHA"
echo "BETA=$BETA"
echo "GAMMA=$GAMMA"
echo "残りの引数: $@"
```

### 複雑なオプション処理の例

```bash
#!/bin/bash
# 値を必要とするオプションと値を必要としないオプションを混在させる
OPTS=$(getopt -o a:bc::d -l alpha:,beta,charlie::,delta -- "$@")
eval set -- "$OPTS"

while true; do
  case "$1" in
    -a | --alpha) echo "alphaオプション: $2"; shift 2 ;;
    -b | --beta) echo "betaオプションが指定されました"; shift ;;
    -c | --charlie) 
      case "$2" in
        "") echo "charlieオプション（値なし）"; shift 2 ;;
        *) echo "charlieオプション: $2"; shift 2 ;;
      esac ;;
    -d | --delta) echo "deltaオプションが指定されました"; shift ;;
    --) shift; break ;;
    *) echo "エラー: 不明なオプション: $1"; exit 1 ;;
  esac
done

echo "残りの引数: $@"
```

## よくある質問

### Q1. `getopt`と`getopts`の違いは何ですか？
A. `getopt`は外部コマンドで、長いオプション（`--option`形式）をサポートしています。一方、`getopts`はシェル組み込みコマンドで、短いオプション（`-o`形式）のみをサポートしますが、より移植性が高いです。

### Q2. オプションが値を取るかどうかを指定するには？
A. `-o`オプションで、オプション文字の後に`:` を付けると値が必要、`::` を付けると値が任意になります。例：`-o a:b::c`

### Q3. `eval set -- "$OPTS"`の目的は何ですか？
A. `getopt`の出力を`eval set`することで、元のコマンドライン引数を整形された形式に置き換え、後続の処理を簡単にします。

### Q4. エラー処理はどうすればよいですか？
A. `getopt`はオプションが無効な場合にエラーを返します。スクリプトでは通常、`getopt`の戻り値をチェックし、エラーが発生した場合は処理を中止します。

## 追加情報

- `getopt`の新しいバージョン（enhanced getopt）と古いバージョンがあり、機能が異なります。Linux では通常、拡張版が使用されます。
- macOSのデフォルトの`getopt`は機能が限られているため、GNU版の`getopt`をインストールすることをお勧めします（`brew install gnu-getopt`でインストール可能）。
- 複雑なオプション処理が必要な場合は、より強力な`argparse`などのPythonライブラリの使用も検討してください。
- オプション指定の標準的な形式は、単一文字オプションには`-`（例：`-a`）、単語オプションには`--`（例：`--alpha`）を使用します。

## 参考資料

https://www.gnu.org/software/libc/manual/html_node/Getopt.html