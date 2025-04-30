# egrep コマンド

テキストファイル内でパターンを検索するための拡張正規表現を使用するコマンド。

## 概要

`egrep`は`grep -E`と同等で、拡張正規表現を使ってファイル内のテキストパターンを検索するコマンドです。複雑な検索パターンを簡潔に表現できるため、テキスト処理やログ分析などで広く使われています。

## オプション

### **-i**

大文字と小文字を区別せずに検索します。

```console
$ egrep -i "error" logfile.txt
Error: Connection failed
WARNING: error in configuration file
System error detected at line 42
```

### **-v**

パターンに一致しない行を表示します（反転マッチ）。

```console
$ egrep -v "success" logfile.txt
Error: Connection failed
Warning: Timeout occurred
Process terminated unexpectedly
```

### **-n**

マッチした行の行番号も表示します。

```console
$ egrep -n "error" logfile.txt
3:Error: Connection failed
7:System error detected at line 42
15:Cannot proceed due to error condition
```

### **-c**

マッチした行数のみを表示します。

```console
$ egrep -c "error" logfile.txt
3
```

### **-l**

マッチしたファイル名のみを表示します（複数ファイル検索時に便利）。

```console
$ egrep -l "error" *.log
app.log
system.log
```

## 使用例

### 複数のパターンを検索（OR検索）

```console
$ egrep "error|warning|critical" logfile.txt
Error: Connection failed
Warning: Timeout occurred
CRITICAL: System shutdown initiated
```

### 特定の単語で始まる行を検索

```console
$ egrep "^Error" logfile.txt
Error: Connection failed
Error: Database unreachable
```

### 特定の単語で終わる行を検索

```console
$ egrep "failed$" logfile.txt
Connection attempt failed
Authentication failed
```

### 特定の形式の日付を含む行を検索

```console
$ egrep "[0-9]{4}-[0-9]{2}-[0-9]{2}" logfile.txt
2025-04-30: System update completed
2025-04-29: Backup failed
```

## ヒント:

### 正規表現の基本記号

- `|` - OR演算子（例：`pattern1|pattern2`）
- `()` - グループ化
- `?` - 直前の文字が0回または1回出現
- `+` - 直前の文字が1回以上出現
- `*` - 直前の文字が0回以上出現
- `[]` - 文字クラス（例：`[0-9]`は任意の数字）
- `^` - 行の先頭にマッチ
- `$` - 行の末尾にマッチ

### 検索結果の色付け

`--color=auto`オプションを使うと、マッチした部分が色付けされて見やすくなります。

### エスケープシーケンス

特殊文字（`*`, `?`, `|`など）を検索する場合は、バックスラッシュ（`\`）でエスケープする必要があります。

## よくある質問

#### Q1. `egrep`と`grep -E`の違いは何ですか？
A. 機能的には同じです。`egrep`は`grep -E`のエイリアスであり、拡張正規表現を使用するためのショートカットです。最近のシステムでは`grep -E`の使用が推奨されています。

#### Q2. 複数のファイルから検索するにはどうすればいいですか？
A. ファイル名にワイルドカードを使用するか、複数のファイル名を指定します。例：`egrep "pattern" file1.txt file2.txt`または`egrep "pattern" *.txt`

#### Q3. 検索結果を別のファイルに保存するにはどうすればいいですか？
A. リダイレクト演算子（`>`）を使用します。例：`egrep "pattern" file.txt > results.txt`

#### Q4. 再帰的にディレクトリ内を検索するにはどうすればいいですか？
A. `-r`オプションを使用します。例：`egrep -r "pattern" /path/to/directory`

## macOSでの注意点

macOSの`egrep`はBSD版であり、GNU版と若干の違いがあります。特に複雑な正規表現を使用する場合、動作が異なる可能性があります。また、macOSでは`grep -E`の使用が推奨されており、将来的に`egrep`は非推奨になる可能性があります。

## 参考

https://www.gnu.org/software/grep/manual/grep.html

## 改訂

- 2025/04/30 初版作成