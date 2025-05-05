# echo コマンド

テキストや変数を標準出力に表示します。

## 概要

`echo`コマンドはテキストや変数の値をターミナルに出力します。シェルスクリプトでメッセージを表示したり、変数の内容を確認したり、他のコマンドにパイプで渡す出力を生成したりするのによく使われます。echoは最も基本的なUnixコマンドの一つで、テキスト出力に欠かせないものです。

## オプション

### **-n**

通常echoが出力の最後に追加する改行を抑制します。

```console
$ echo -n "Hello"
Hello$
```

### **-e**

バックスラッシュエスケープシーケンスの解釈を有効にします。

```console
$ echo -e "Hello\nWorld"
Hello
World
```

### **--help**

ヘルプ情報を表示して終了します。

```console
$ echo --help
Usage: echo [SHORT-OPTION]... [STRING]...
  or:  echo LONG-OPTION
Echo the STRING(s) to standard output.

  -n             do not output the trailing newline
  -e             enable interpretation of backslash escapes
  -E             disable interpretation of backslash escapes (default)
      --help     display this help and exit
      --version  output version information and exit
```

## 使用例

### テキストの表示

```console
$ echo Hello World
Hello World
```

### 変数の値の表示

```console
$ name="John"
$ echo "My name is $name"
My name is John
```

### -eオプションでエスケープシーケンスを使用

```console
$ echo -e "タブ:\t| 改行:\n| バックスラッシュ:\\"
タブ:	| 改行:
| バックスラッシュ:\
```

### -nオプションで改行を抑制

```console
$ echo -n "名前を入力してください: "
名前を入力してください: $
```

### 出力をファイルにリダイレクト

```console
$ echo "これはテストです" > test.txt
$ cat test.txt
これはテストです
```

## ヒント:

### 引用符の違いが重要

シングルクォート（`'`）は変数展開やエスケープシーケンスの解釈を防ぎますが、ダブルクォート（`"`）はそれらを許可します：

```console
$ name="John"
$ echo "こんにちは $name"
こんにちは John
$ echo 'こんにちは $name'
こんにちは $name
```

### コマンド置換との組み合わせ

echoをコマンド置換と組み合わせてコマンド出力をフォーマットできます：

```console
$ echo "現在の日付: $(date)"
現在の日付: Tue May 4 10:15:30 JST 2025
```

### -eオプションでのエスケープシーケンス

よく使われるエスケープシーケンス：
- `\n` - 改行
- `\t` - タブ
- `\b` - バックスペース
- `\\` - バックスラッシュ
- `\a` - アラート（ベル）

## よくある質問

#### Q1. echoとprintfの違いは何ですか？
A. `echo`は`printf`よりもシンプルですが、機能は少ないです。`echo`は基本的な出力に適していますが、`printf`はC言語のprintf関数と同様に、より多くのフォーマット制御を提供します。

#### Q2. 改行なしでechoするにはどうすればいいですか？
A. `-n`オプションを使用します：`echo -n "テキスト"`

#### Q3. タブや改行などの特殊文字を表示するにはどうすればいいですか？
A. `-e`オプションとエスケープシーケンスを使用します：`echo -e "1行目\n2行目\tタブ付き"`

#### Q4. 一部のシェルでecho -eが機能しないのはなぜですか？
A. 一部のシェル実装（dashの一部バージョンなど）では、デフォルトで`-e`オプションがサポートされていません。その場合は、代わりに`printf`を使用してください。

## macOSでの注意点

macOSのデフォルトシェル（zshやbash）では、GNU版のechoとは若干動作が異なる場合があります。特に、一部のエスケープシーケンスの解釈が異なることがあります。確実にクロスプラットフォームで動作させたい場合は、`printf`コマンドの使用を検討してください。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html

## 改訂履歴

- 2025/05/04 初版作成