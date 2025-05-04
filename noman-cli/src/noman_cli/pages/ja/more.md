# more コマンド

ファイルの内容を1画面ずつ表示します。

## 概要

`more`コマンドはページャーの一種で、テキストファイルを1画面ずつ表示することができます。特に大きなファイルを閲覧する際に便利で、コンテンツをページごとに表示し、簡単なキーボードコマンドでファイル内を移動できます。より高機能な`less`コマンドとは異なり、`more`はファイル内の前方向への移動のみをサポートしています。

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

画面のクリアや一部の端末で干渉する可能性のある制御シーケンスを無効にします。

```console
$ more -p script.sh
```

### **-c, --clean-print**

スクロールの代わりに画面を再描画し、よりクリーンな表示を提供します。

```console
$ more -c document.txt
```

### **-s, --squeeze**

複数の空白行を1行に圧縮します。

```console
$ more -s log_file.txt
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

### 基本的な使用法

```console
$ more /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
--More--(28%)
```

### 複数ファイルの表示

```console
$ more file1.txt file2.txt
::::::::::::::
file1.txt
::::::::::::::
This is file 1 content
--More--(50%)
```

### 特定のパターンから開始

```console
$ more +/important document.txt
Here is the important information you were looking for...
--More--(75%)
```

### オプションの組み合わせ

```console
$ more -cs +10 large_log.txt
[10行目からクリーンな画面再描画と空白行圧縮で表示]
--More--(15%)
```

## ヒント:

### ナビゲーションコマンド

`more`でファイルを表示中に、以下のキーボードコマンドが使用できます：
- `Space` - 1画面進む
- `Enter` - 1行進む
- `b` - 1画面戻る（すべての実装で動作するとは限りません）
- `q` - 終了する
- `/pattern` - パターンを検索
- `n` - 前回の検索を繰り返す

### コマンド出力のパイプ

大きな出力を画面ごとに表示するために、コマンドの出力を`more`にパイプできます：

```console
$ ls -la /usr/bin | more
```

### 環境変数

`MORE`環境変数を設定してデフォルトオプションを指定できます：

```console
$ export MORE="-d"
$ more large_file.txt
```

## よくある質問

#### Q1. `more`と`less`の違いは何ですか？
A. `more`はファイル内の前方向への移動のみをサポートしますが、`less`は前後両方向の移動が可能で、より多くの機能を持っています。`less`は一般的に`more`の改良版と考えられています（そのため名前が「less」となっています）。

#### Q2. `more`を終了するにはどうすればよいですか？
A. `q`キーを押すと終了してコマンドプロンプトに戻ります。

#### Q3. `more`でテキストを検索できますか？
A. はい、`/`に続けて検索パターンを入力してEnterを押します。次の一致を見つけるには`n`を使用します。

#### Q4. `more`で行番号を表示するにはどうすればよいですか？
A. `less`と異なり、`more`には行番号を表示するための組み込みオプションがありません。行番号が必要な場合は、代わりに`less -N`の使用を検討してください。

## macOSに関する注意点

macOSでは、`more`コマンドはGNU/Linuxバージョンとは若干異なります。`-d`などの一部のオプションは動作が異なるか、利用できない場合があります。プラットフォーム間でより一貫した動作を得るには、より機能が豊富で一貫性のある`less`コマンドの使用を検討してください。

## 参考資料

https://man7.org/linux/man-pages/man1/more.1.html

## 改訂履歴

- 2025/05/04 初版作成