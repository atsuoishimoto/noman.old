# for コマンド

`for` はシェルスクリプトで繰り返し処理を行うためのループ構文です。指定したリストの各要素に対して、同じコマンドを繰り返し実行することができます。

## 構文

### **基本構文**
リスト内の各要素に対して処理を繰り返します。

```bash
for 変数 in リスト; do
  コマンド
done
```

### **C言語風構文** (Bash専用)
C言語のような構文でループを記述できます。

```bash
for ((初期値; 条件; 増分)); do
  コマンド
done
```

## 使用例

### 基本的な使い方

```console
$ for i in 1 2 3; do
    echo "数字: $i"
  done
数字: 1
数字: 2
数字: 3
```

### ファイル一覧に対する処理

```console
$ for file in *.txt; do
    echo "ファイル名: $file"
  done
ファイル名: document.txt
ファイル名: notes.txt
ファイル名: readme.txt
```

### 数値範囲を使ったループ

```console
$ for i in {1..5}; do
    echo "$i回目の処理"
  done
1回目の処理
2回目の処理
3回目の処理
4回目の処理
5回目の処理
```

### C言語風構文の例

```console
$ for ((i=1; i<=3; i++)); do
    echo "カウント: $i"
  done
カウント: 1
カウント: 2
カウント: 3
```

## よくある質問

#### Q1. `for` ループでファイル名に空白が含まれる場合はどうすればよいですか？
A. `IFS`（Internal Field Separator）を変更するか、配列を使用します。

```console
$ IFS=$'\n'  # 改行だけを区切り文字に設定
$ for file in $(ls); do
    echo "処理中: $file"
  done
```

#### Q2. 特定の間隔で数値を増やすにはどうすればよいですか？
A. 波括弧展開で増分を指定できます。

```console
$ for i in {0..10..2}; do  # 0から10まで2ずつ増加
    echo $i
  done
0
2
4
6
8
10
```

#### Q3. `for` ループを途中で抜けるにはどうすればよいですか？
A. `break` コマンドを使用します。条件付きでスキップするには `continue` を使用します。

```console
$ for i in {1..10}; do
    if [ $i -eq 5 ]; then
      break  # 5になったらループを抜ける
    fi
    echo $i
  done
1
2
3
4
```

## 追加情報

* シェルスクリプトでは、`for` ループは配列処理やファイル操作の自動化に非常に便利です。
* macOSでは基本的な `for` 構文は同じですが、デフォルトシェルが `zsh` であることに注意してください。
* 処理が複雑な場合は、可読性のために変数名を意味のある名前にすることをお勧めします。

## 参考資料

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## 改訂履歴

2025/04/26 フォーマットを統一し、出力例を追加しました。追加情報セクションを新設しました。