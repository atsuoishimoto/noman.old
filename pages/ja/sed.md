# sed コマンド概要

`sed`（Stream EDitor）は、テキストファイルやストリームを処理するための強力なテキスト変換ツールです。パターンマッチングを使用してテキストを検索・置換することができます。

## オプション

### **-e**：複数の編集コマンドを指定

複数の編集操作を一度に実行できます。

```bash
$ echo "Hello World" | sed -e 's/Hello/Hi/' -e 's/World/Everyone/'
Hi Everyone
```

### **-i**：ファイルを直接編集

ファイルを直接変更します（元のファイルを上書き）。

```bash
$ sed -i 's/old/new/g' file.txt
# file.txtの「old」を「new」に置き換えて保存
```

### **-n**：自動出力を抑制

マッチした行のみを出力します（デフォルトではすべての行が出力されます）。

```bash
$ sed -n '/pattern/p' file.txt
# 「pattern」を含む行のみを表示
```

## 使用例

### 基本的な置換

```bash
$ echo "The quick brown fox" | sed 's/brown/red/'
The quick red fox
# 最初に出現する「brown」を「red」に置換
```

### グローバル置換（g フラグ）

```bash
$ echo "brown paper brown bag" | sed 's/brown/white/g'
white paper white bag
# すべての「brown」を「white」に置換
```

### 特定の行を削除

```bash
$ cat file.txt
Line 1
Line 2
Line 3
Line 4

$ sed '2d' file.txt
Line 1
Line 3
Line 4
# 2行目を削除
```

### 特定のパターンを含む行を削除

```bash
$ sed '/pattern/d' file.txt
# 「pattern」を含む行を削除
```

### 範囲指定での編集

```bash
$ sed '2,4s/old/new/g' file.txt
# 2行目から4行目までの「old」を「new」に置換
```

## よくある質問

### Q1. sedの基本的な構文は？
A. 基本構文は `sed 'コマンド' ファイル` です。コマンドには `s/検索パターン/置換テキスト/フラグ` などがあります。

### Q2. 元のファイルを変更せずに結果を確認するには？
A. デフォルトでは、`sed`は標準出力に結果を表示し、元のファイルは変更しません。変更を適用するには `-i` オプションを使用します。

### Q3. 特定の行だけを編集するには？
A. `sed '行番号s/old/new/'` のように行番号を指定できます。例：`sed '3s/old/new/' file.txt`

### Q4. 正規表現を使用できますか？
A. はい、`sed`は基本的な正規表現をサポートしています。例えば `sed 's/[0-9]\+/NUM/g'` は数字を「NUM」に置き換えます。

## 追加情報

- MacOSの`sed`はBSD版で、GNU版と若干動作が異なります。特に `-i` オプションでは、MacOSでは `-i ''` のように空の拡張子を指定する必要があります。
- 複雑な置換には、`&`を使って一致したパターン全体を参照できます：`sed 's/hello/& world/'`
- バックアップを作成しながら編集するには：`sed -i.bak 's/old/new/g' file.txt`（file.txt.bakというバックアップが作成されます）