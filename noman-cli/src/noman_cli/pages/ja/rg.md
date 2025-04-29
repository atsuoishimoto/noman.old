# rg コマンド

`rg`（ripgrep）は高速な検索ツールで、ファイル内の文字列パターンを正規表現で検索します。gitやVSCodeなどでも採用されている高性能な`grep`代替ツールです。

## オプション

### **-i, --ignore-case**
大文字と小文字を区別せずに検索します。

```console
$ rg -i error
./log.txt:10:ERROR: Failed to connect to database
./log.txt:15:error: timeout occurred
./config.js:5:// errorHandler configuration
```

### **-v, --invert-match**
パターンに一致しない行を表示します。

```console
$ rg -v success ./log.txt
./log.txt:10:ERROR: Failed to connect to database
./log.txt:15:error: timeout occurred
./log.txt:20:Warning: retry attempt 3
```

### **-A, --after-context**
マッチした行の後に指定した行数を表示します。

```console
$ rg -A 2 error
./log.txt:15:error: timeout occurred
./log.txt-16:  at line 42 in network.js
./log.txt-17:  retrying in 5 seconds
```

### **-B, --before-context**
マッチした行の前に指定した行数を表示します。

```console
$ rg -B 1 error
./log.txt-14:Attempting connection...
./log.txt:15:error: timeout occurred
```

### **-C, --context**
マッチした行の前後に指定した行数を表示します。

```console
$ rg -C 1 error
./log.txt-14:Attempting connection...
./log.txt:15:error: timeout occurred
./log.txt-16:  at line 42 in network.js
```

### **-l, --files-with-matches**
マッチしたファイル名のみを表示します。

```console
$ rg -l error
./log.txt
./config.js
```

### **--no-ignore**
`.gitignore`や`.ignore`などで指定された無視ファイルも検索対象に含めます。

```console
$ rg --no-ignore password
./node_modules/config.js:5:const password = 'default123';
./config.backup:10:password=test123
```

## 使用例

### 複数のファイルタイプを検索

```console
$ rg -t js -t ts 'function main'
./src/main.js:5:function main() {
./src/utils.ts:10:export function main(): void {
```

### 再帰的に特定のディレクトリを検索

```console
$ rg 'TODO' ./src
./src/app.js:15:// TODO: Implement error handling
./src/components/Button.js:42:// TODO: Add accessibility features
```

### 正規表現を使用した検索

```console
$ rg '\d{3}-\d{4}' --type=txt
./contacts.txt:5:Phone: 555-1234
./orders.txt:12:Contact: 123-4567
```

## ヒント:

### 検索速度の最適化
`rg`はデフォルトで`.git`ディレクトリや`.gitignore`で指定されたファイルを無視するため、大規模なプロジェクトでも高速に検索できます。

### 複雑な検索パターン
`-e`オプションを使用すると、複数の検索パターンを指定できます：`rg -e 'pattern1' -e 'pattern2'`

### 検索結果の色分け
`rg`はデフォルトでマッチした部分を色付きで表示します。`--color never`で無効化、`--color always`で常に有効化できます。

### 隠しファイルの検索
`-u`（`--unrestricted`）オプションを使うと隠しファイルも検索対象に含めることができます。`-uu`でさらに多くのファイルを、`-uuu`で全てのファイルを対象にします。

## よくある質問

#### Q1. `rg`と`grep`の違いは何ですか？
A. `rg`は`grep`より高速で、デフォルトで再帰検索や`.gitignore`の尊重、色付き出力などの機能があります。また、マルチスレッドで動作するため大規模なプロジェクトでの検索が速いです。

#### Q2. 特定のファイルタイプだけを検索するには？
A. `-t`または`--type`オプションを使用します。例：`rg -t js pattern`でJavaScriptファイルのみ検索します。

#### Q3. バイナリファイルを検索対象から除外するには？
A. デフォルトでバイナリファイルは検索されません。明示的に指定する場合は`--no-binary`オプションを使用します。

#### Q4. 大きなファイルを効率的に検索するには？
A. `rg`は自動的に大きなファイルも効率的に処理しますが、`--mmap`オプションを使うとメモリマッピングを利用してさらに高速化できる場合があります。

## macOSでの注意点

macOSでは、Homebrewを使用してインストールするのが一般的です：
```console
$ brew install ripgrep
```

macOSのファイルシステム（APFS/HFS+）は大文字小文字を区別しないため、検索時に注意が必要です。正確に大文字小文字を区別したい場合は、明示的に`-s`または`--case-sensitive`オプションを使用してください。

## 参考資料

https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md

## 改訂履歴

- 2025/04/26 --no-ignoreオプションの説明を追加。macOSでの注意点を追加。
- 2025/04/26 初回作成