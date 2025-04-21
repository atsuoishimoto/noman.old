# continue

`continue`はシェルスクリプトやプログラミングで使用される制御フロー命令で、ループ内の現在の反復をスキップして次の反復に進むために使用されます。

## オプション

`continue`コマンド自体にはオプションはありませんが、数値引数を取ることができます。

### **数値引数**

数値を指定すると、そのレベルのネストされたループに対して`continue`が適用されます。

```bash
$ for i in 1 2 3; do
>   for j in a b c; do
>     if [ "$j" = "b" ]; then
>       continue 2  # 外側のループ（iのループ）の次の反復に進む
>     fi
>     echo "$i $j"
>   done
> done
1 a
2 a
3 a
```

## 使用例

### 基本的な使用法

```bash
$ for i in 1 2 3 4 5; do
>   if [ $i -eq 3 ]; then
>     continue  # 3の場合は処理をスキップ
>   fi
>   echo "処理中: $i"
> done
処理中: 1
処理中: 2
処理中: 4
処理中: 5
```

### 条件に基づいた処理のスキップ

```bash
$ for file in *.txt; do
>   if [ ! -s "$file" ]; then
>     echo "$file は空なのでスキップします"
>     continue
>   fi
>   echo "$file を処理しています..."
>   # ここに処理コードが入る
> done
empty.txt は空なのでスキップします
document.txt を処理しています...
notes.txt を処理しています...
```

### while ループでの使用

```bash
$ i=0
$ while [ $i -lt 5 ]; do
>   i=$((i+1))
>   if [ $i -eq 3 ]; then
>     continue
>   fi
>   echo "i = $i"
> done
i = 1
i = 2
i = 4
i = 5
```

## よくある質問

### Q1. `continue`と`break`の違いは何ですか？
A. `continue`は現在の反復をスキップして次の反復に進みますが、`break`はループ全体を終了します。

### Q2. `continue`は複数のネストされたループで使えますか？
A. はい、数値引数を指定することで、どのレベルのループに対して`continue`を適用するか指定できます。例えば、`continue 2`は2つ目の外側のループに対して適用されます。

### Q3. `continue`はどのシェルでも使えますか？
A. はい、`continue`はBash、Zsh、sh、kshなど、ほとんどのUNIXシェルで使用できる標準的な制御構文です。

## 追加情報

- `continue`はループ内でのみ使用できます。ループの外で使用するとエラーになります。
- シェルスクリプトでは、`continue`の後に処理を続けたい場合は、別のブロックや条件分岐を使用する必要があります。
- 大きなループで特定の条件の項目をスキップする場合に便利ですが、過度に使用するとコードの可読性が低下する可能性があります。

## 参考情報

https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html