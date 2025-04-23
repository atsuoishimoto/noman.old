# mv

`mv`コマンドは、ファイルやディレクトリを移動（移動）したり、名前を変更したりするために使用されます。

## オプション

### **-i (interactive)**

上書き前に確認を求めます。既存のファイルを誤って上書きするのを防ぐのに役立ちます。

```bash
$ mv -i file.txt destination/
mv: overwrite 'destination/file.txt'? y
```

### **-f (force)**

上書き時に確認を求めずに強制的に実行します。

```bash
$ mv -f important.txt backup/
```

### **-v (verbose)**

実行中の操作を詳細に表示します。

```bash
$ mv -v document.txt reports/
'document.txt' -> 'reports/document.txt'
```

### **-n (no-clobber)**

既存のファイルを上書きしません。

```bash
$ mv -n file.txt destination/
```

## 使用例

### ファイルの移動

```bash
$ mv file.txt Documents/
```

これは`file.txt`を現在のディレクトリから`Documents`ディレクトリに移動する。

### ファイル名の変更

```bash
$ mv oldname.txt newname.txt
```

これは`oldname.txt`の名前を`newname.txt`に変更する。

### 複数ファイルの移動

```bash
$ mv file1.txt file2.txt file3.txt destination/
```

これは複数のファイルを一度に`destination`ディレクトリに移動する。

### ディレクトリの移動

```bash
$ mv directory1 directory2
```

これは`directory1`を`directory2`に移動する。`directory2`が存在しない場合は、`directory1`の名前が`directory2`に変更される。

## よくある質問

### Q1. `mv`コマンドでファイルを誤って上書きしないようにするにはどうすればいいですか？
A. `-i`オプションを使用すると、既存のファイルを上書きする前に確認を求められます。`mv -i file.txt destination/`のように使います。

### Q2. 複数のファイルを一度に移動できますか？
A. はい、`mv file1.txt file2.txt directory/`のように、最後の引数をディレクトリにして複数のファイルを指定できます。

### Q3. ファイル名に特殊文字やスペースがある場合はどうすればいいですか？
A. 引用符で囲むか、バックスラッシュでエスケープします。例：`mv "my file.txt" destination/`または`mv my\ file.txt destination/`

### Q4. `mv`コマンドを使ってファイルをバックアップするにはどうすればいいですか？
A. 元のファイル名に拡張子を追加します。例：`mv file.txt file.txt.bak`

## 追加情報

- `mv`コマンドはデフォルトでは確認なしに上書きするため、重要なファイルを扱う場合は`-i`オプションの使用をお勧めします。
- macOSでは、`mv`コマンドの動作はLinuxとほぼ同じですが、一部のファイルシステム属性（拡張属性など）の扱いが異なる場合があります。
- エイリアスを設定して`mv -i`をデフォルトにすることで、誤った上書きを防ぐことができます：`alias mv='mv -i'`

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html