# `rg` コマンド概要

`rg`（ripgrep）は高速なテキスト検索ツールで、ファイル内の文字列パターンを検索します。`grep`の代替として開発され、Rustで書かれているため非常に高速です。

## オプション

### **-i, --ignore-case**:
大文字と小文字を区別せずに検索します。

例：
```bash
# 「hello」という単語を大文字小文字を区別せずに検索
rg -i hello
```

### **-v, --invert-match**:
パターンに一致しない行を表示します。

例：
```bash
# 「error」を含まない行を表示
rg -v error logfile.txt
```

### **-w, --word-regexp**:
単語全体に一致するパターンのみを検索します。

例：
```bash
# 「log」という単語のみを検索（「blog」や「logging」は含まない）
rg -w log
```

### **-c, --count**:
マッチした行数のみを表示します。

例：
```bash
# 各ファイルで「TODO」が出現する回数を表示
rg -c TODO
```

### **-l, --files-with-matches**:
マッチしたファイル名のみを表示します。

例：
```bash
# 「password」を含むファイルの一覧を表示
rg -l password
```

### **-A, --after-context**:
マッチした行の後の指定行数も表示します。

例：
```bash
# 「error」を含む行とその後2行を表示
rg -A 2 error logfile.txt
```

### **-B, --before-context**:
マッチした行の前の指定行数も表示します。

例：
```bash
# 「error」を含む行とその前3行を表示
rg -B 3 error logfile.txt
```

### **-C, --context**:
マッチした行の前後の指定行数を表示します。

例：
```bash
# 「error」を含む行とその前後2行ずつを表示
rg -C 2 error logfile.txt
```

### **-t, --type**:
特定のファイルタイプのみを検索します。

例：
```bash
# JavaScriptファイルのみで「function」を検索
rg -t js function
```

### **-g, --glob**:
グロブパターンでファイルをフィルタリングします。

例：
```bash
# 「*.log」ファイルのみで「error」を検索
rg -g "*.log" error
```

## 使用例

```bash
# 基本的な検索
rg "function" src/
# 出力例
src/main.js:10:function calculateTotal(items) {
src/utils.js:5:function formatDate(date) {

# 複数のディレクトリを再帰的に検索
rg "TODO" src/ lib/
# 出力例
src/app.js:42:// TODO: Implement error handling
lib/helpers.js:15:// TODO: Refactor this function

# 隠しファイルも含めて検索
rg --hidden "password"
# 出力例
.config/settings.json:8:  "default_password": "changeme"

# 正規表現を使用した検索
rg "\d{3}-\d{3}-\d{4}" --only-matching
# 出力例
contact.txt:123-456-7890
```

## よくある質問

### Q1. `rg`と`grep`の違いは何ですか？
A. `rg`は`grep`より高速で、デフォルトで再帰検索や`.git`ディレクトリの無視などの機能があります。また、色付き出力やファイルタイプフィルタリングなどの機能も組み込まれています。

### Q2. 隠しファイルも検索するにはどうすればいいですか？
A. `--hidden`オプションを使用します。例：`rg --hidden pattern`

### Q3. バイナリファイルを検索から除外するにはどうすればいいですか？
A. デフォルトでバイナリファイルは検索されません。明示的に含めたい場合は`-a`または`--text`オプションを使用します。

### Q4. 特定のディレクトリを検索から除外するにはどうすればいいですか？
A. `--glob`オプションを使用します。例：`rg pattern --glob '!node_modules/'`

### Q5. 大きなファイルを効率的に検索するにはどうすればいいですか？
A. `rg`は既に非常に効率的ですが、`--mmap`オプションを使用するとメモリマッピングを利用して大きなファイルの検索が速くなる場合があります。

### Q6. 検索結果をファイルに保存するにはどうすればいいですか？
A. 標準的なリダイレクトを使用します。例：`rg pattern > results.txt`

### Q7. 複数のパターンを検索するにはどうすればいいですか？
A. `-e`または`--regexp`オプションを複数回使用します。例：`rg -e pattern1 -e pattern2`

### Q8. ファイルタイプのリストを表示するにはどうすればいいですか？
A. `--type-list`オプションを使用します。例：`rg --type-list`

### Q9. 検索結果の行番号を非表示にするにはどうすればいいですか？
A. `--no-line-number`オプションを使用します。例：`rg --no-line-number pattern`

### Q10. 検索パターンをファイルから読み込むにはどうすればいいですか？
A. `-f`または`--file`オプションを使用します。例：`rg -f patterns.txt`

## 追加のメモ

- `rg`はデフォルトで`.gitignore`ファイルに記載されたパターンを無視します。
- `--no-ignore`オプションを使用すると、`.gitignore`などの無視ファイルを無視できます。
- 非常に大きなプロジェクトでは、`-j`または`--threads`オプションでスレッド数を調整できます。
- `rg`は多くの環境で`apt`、`brew`、`chocolatey`などのパッケージマネージャーを通じてインストールできます。