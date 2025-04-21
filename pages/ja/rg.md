# rg (ripgrep)

ripgrepは高速な検索ツールで、ファイル内の文字列パターンを検索します。grepの代替として設計され、より高速で使いやすい機能を提供します。

## オプション

### **-i, --ignore-case**

大文字と小文字を区別せずに検索します。

```bash
$ rg -i "hello"
example.txt:10:Hello World
example.txt:15:hello everyone
```

### **-v, --invert-match**

パターンに一致しない行を表示します。

```bash
$ rg -v "error" log.txt
log.txt:1:System started
log.txt:3:Process completed successfully
```

### **-w, --word-regexp**

単語全体に一致するパターンのみを検索します。

```bash
$ rg -w "log"
logger.js:5:function log(message) {
config.json:10:"log": true
```

### **-A, --after-context**

一致した行の後に指定した行数を表示します。

```bash
$ rg -A 2 "error"
app.js:25:throw new Error("Something went wrong");
app.js:26:  console.log("This won't execute");
app.js:27:}
```

### **-B, --before-context**

一致した行の前に指定した行数を表示します。

```bash
$ rg -B 1 "function main"
main.js:9:// Entry point
main.js:10:function main() {
```

### **-C, --context**

一致した行の前後に指定した行数を表示します。

```bash
$ rg -C 1 "important"
document.txt:14:The previous line
document.txt:15:This is important information
document.txt:16:The next line
```

### **-t, --type**

特定のファイルタイプのみを検索します。

```bash
$ rg -t js "function"
app.js:5:function initialize() {
utils.js:10:function formatDate(date) {
```

### **-g, --glob**

指定したグロブパターンに一致するファイルのみを検索します。

```bash
$ rg -g "*.md" "TODO"
README.md:30:TODO: Update documentation
CONTRIBUTING.md:15:TODO: Add more examples
```

## 使用例

### 複数のパターンで検索

```bash
$ rg -e "error" -e "warning" log.txt
log.txt:15:warning: disk space low
log.txt:42:error: connection failed
log.txt:67:warning: timeout occurred
```

### 再帰的に特定のディレクトリを検索

```bash
$ rg "api.connect" src/
src/network/client.js:25:  api.connect(endpoint);
src/services/auth.js:10:  await api.connect(authServer);
```

### 隠しファイルを含めて検索

```bash
$ rg --hidden "password"
.config:5:password=test123
config.js:10:const password = process.env.PASSWORD;
```

## よくある質問

### Q1. ripgrepとgrepの違いは何ですか？
A. ripgrepはgrepよりも高速で、デフォルトで再帰的に検索し、.gitignoreファイルを尊重し、自動的にバイナリファイルをスキップします。また、より多くの検索オプションと色付き出力を提供します。

### Q2. 特定のディレクトリやファイルを検索から除外するにはどうすればいいですか？
A. `--ignore-file`オプションを使用するか、プロジェクトルートに`.ignore`ファイルを作成して除外パターンを指定できます。また、`-g '!pattern'`を使用して特定のパターンを除外することもできます。

### Q3. 正規表現を使用できますか？
A. はい、ripgrepはデフォルトで正規表現をサポートしています。例えば、`rg '\d{3}-\d{2}-\d{4}'`は社会保障番号のようなパターンを検索します。

### Q4. 検索結果をファイルに保存するにはどうすればいいですか？
A. 標準的なリダイレクトを使用できます：`rg "pattern" > results.txt`

## 追加情報

- ripgrepは非常に高速で、大規模なコードベースでも効率的に動作します。
- デフォルトでは、ripgrepは`.gitignore`ファイルに記載されたパターンを無視します。この動作を変更するには`--no-ignore`オプションを使用します。
- macOSでは、Homebrewを使用してインストールできます：`brew install ripgrep`
- 検索結果が多すぎる場合は、`-l`または`--files-with-matches`オプションを使用して、一致するファイル名のみを表示することができます。
- `--type-list`オプションを使用すると、サポートされているすべてのファイルタイプを確認できます。

## 参考

https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md