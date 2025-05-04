# more コマンド

ファイルの内容を1画面ずつ表示します。

## 概要

`more` コマンドはページャーの一種で、テキストファイルを1画面ずつ閲覧することができます。大きなファイルを端末に一度にすべて表示せずに確認したい場合に特に便利です。より高機能な `less` コマンドとは異なり、`more` はファイル内を前方向にのみ移動できます。

## オプション

### **-d, --silent**

役立つプロンプトを表示し、よりユーザーフレンドリーなエラーメッセージを提供します。

```console
$ more -d large_file.txt
--More--(50%) [スペースキーで続行、'q'で終了]
```

### **-f, --logical**

画面行ではなく論理行をカウントします（長い行を折り返しません）。

```console
$ more -f wide_content.txt
```

### **-p, --plain**

画面のクリアを無効にし、特殊文字を処理せずにテキストを表示します。

```console
$ more -p script.sh
```

### **-c, --clean-print**

画面の下部からスクロールして各ページを描画し、よりクリーンな表示を提供します。

```console
$ more -c document.txt
```

### **-s, --squeeze**

複数の空白行を1つの空白行に圧縮します。

```console
$ more -s log_with_gaps.txt
```

### **-u, --plain**

下線やその他の書式設定を抑制します。

```console
$ more -u formatted_text.txt
```

### **-number**

各画面に表示する行数を指定します。

```console
$ more -10 short_file.txt
```

### **+number**

指定した行番号からファイルの表示を開始します。

```console
$ more +100 large_file.txt
```

### **+/pattern**

指定したパターンを含む最初の行から表示を開始します。

```console
$ more +/ERROR log_file.txt
```

## 使用例

### 基本的な使い方

```console
$ more /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
--More--(28%)
```

### 複数ファイルの閲覧

```console
$ more file1.txt file2.txt
::::::::::::::
file1.txt
::::::::::::::
This is the content of file1.txt
--More--(75%)
```

### オプションの組み合わせ

```console
$ more -cs +/important document.txt
[「important」の最初の出現箇所から、クリーンスクリーンと空白行圧縮を適用して表示される]
```

### パイプとの併用

```console
$ ls -la | more
total 112
drwxr-xr-x  15 user  staff   480 5月  4 10:23 .
drwxr-xr-x   5 user  staff   160 4月 29 09:15 ..
-rw-r--r--   1 user  staff  8196 5月  3 14:22 file1.txt
--More--(42%)
```

## ヒント:

### ナビゲーションコマンド

`more` でファイルを閲覧中に使用できるキーボードコマンド:
- `Space` または `f`: 1画面進む
- `Enter`: 1行進む
- `b`: 1画面戻る（すべての実装で動作するとは限らない）
- `q` または `Q`: 終了
- `/pattern`: パターンを検索
- `n`: 前回の検索を繰り返す

### 大きなファイルでの使用

非常に大きなファイルを調べる場合、`more` は閲覧しながらファイルを読み込むため、ファイル全体を一度に読み込むよりもメモリ効率が良いです。

### `more` の代替

より高度な機能（後方ナビゲーションや優れた検索機能など）が必要な場合は、`more` の代わりに `less` の使用を検討してください。`less` コマンドは「less is more（lessの方が多機能）」というキャッチフレーズで、`more` の改良版として設計されました。

## よくある質問

#### Q1. `more` と `less` の違いは何ですか？
A. `more` はファイル内を前方向にのみ移動できますが、`less` は前後両方向に移動でき、より高度な機能を備えています。

#### Q2. `more` を終了するにはどうすればよいですか？
A. `q` または `Q` キーを押して終了します。

#### Q3. `more` でテキストを検索できますか？
A. はい、`/` に続けて検索パターンを入力し、Enterを押します。次の一致を見つけるには `n` を使用します。

#### Q4. `more` で行番号を表示するにはどうすればよいですか？
A. `less` とは異なり、`more` には行番号を表示する組み込みオプションはありません。

#### Q5. なぜ `more` が時々画面をクリアするのですか？
A. デフォルトでは、`more` は各ページを表示する前に画面をクリアします。この動作を防ぐには `-p` オプションを使用してください。

## 参考資料

https://man7.org/linux/man-pages/man1/more.1.html

## 改訂履歴

- 2025/05/04 初版作成