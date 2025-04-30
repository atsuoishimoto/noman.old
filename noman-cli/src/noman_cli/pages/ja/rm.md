# rm コマンド

ファイルやディレクトリを削除します。

## 概要

`rm`（remove）コマンドは、ファイルシステムからファイルやディレクトリを削除するために使用されます。デフォルトでは、ディレクトリの削除や確認プロンプトの表示は行われません。削除されたファイルは通常のゴミ箱には移動せず、完全に削除されるため注意が必要です。

## オプション

### **-f, --force**

確認プロンプトを表示せずに強制的に削除します。存在しないファイルやアクセス権限のないファイルに対してもエラーメッセージを表示しません。

```console
$ rm -f 不要なファイル.txt
```

### **-i, --interactive**

削除前に確認プロンプトを表示します。

```console
$ rm -i document.txt
rm: remove regular file 'document.txt'? y
```

### **-r, -R, --recursive**

ディレクトリとその中身を再帰的に削除します。

```console
$ rm -r プロジェクト/
```

### **-v, --verbose**

削除処理の詳細を表示します。

```console
$ rm -v document.txt
removed 'document.txt'
```

## 使用例

### 複数のファイルを削除

```console
$ rm file1.txt file2.txt file3.txt
```

### 確認プロンプト付きでディレクトリを削除

```console
$ rm -ri 古いプロジェクト/
rm: descend into directory '古いプロジェクト/'? y
rm: remove regular file '古いプロジェクト/README.md'? y
rm: remove directory '古いプロジェクト/'? y
```

### ワイルドカードを使用して特定のパターンのファイルを削除

```console
$ rm -v *.tmp
removed 'temp1.tmp'
removed 'temp2.tmp'
removed 'backup.tmp'
```

## ヒント:

### 削除前のバックアップ

重要なファイルを削除する前に、バックアップを作成することをお勧めします。

```console
$ cp -r 重要なディレクトリ/ 重要なディレクトリ_backup/
$ rm -r 重要なディレクトリ/
```

### 安全な削除のためのエイリアス設定

`rm`コマンドに`-i`オプションを常に使用するエイリアスを設定すると、誤削除を防ぐことができます。

```console
$ alias rm='rm -i'
```

### 「rm -rf /」は絶対に使用しない

ルートディレクトリ（`/`）に対して再帰的強制削除を行うと、システム全体が破壊される可能性があります。

## よくある質問

#### Q1. 削除したファイルを復元できますか？
A. 通常の`rm`コマンドで削除したファイルは、特別なデータ復旧ツールなしでは復元できません。`rm`はファイルをゴミ箱に移動するのではなく、完全に削除します。

#### Q2. ディレクトリを削除するにはどうすればよいですか？
A. ディレクトリを削除するには`rm -r ディレクトリ名`を使用します。空のディレクトリであれば`rmdir ディレクトリ名`も使えます。

#### Q3. 「Operation not permitted」エラーが表示される場合はどうすればよいですか？
A. ファイルの所有者でない場合や、特別な保護属性が設定されている場合に発生します。`sudo rm`で管理者権限で実行するか、ファイルの権限を確認してください。

## macOSでの注意点

macOSでは、一部のシステムファイルはSystem Integrity Protection（SIP）によって保護されており、`sudo`を使用しても削除できない場合があります。また、macOSでは`-P`オプションを使用して安全な上書き削除を行うことができますが、SSDでは効果が限定的です。

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html

## 改訂履歴

- 2025/04/30 初版作成