# du コマンド

ファイルやディレクトリの使用ディスク容量を推定します。

## 概要

`du`（disk usage）コマンドは、ファイルやディレクトリが使用しているディスク容量を推定して表示します。大容量のファイルやディレクトリを見つけて、ストレージを効率的に管理するのに役立ちます。

## オプション

### **-h, --human-readable**

サイズを人間が読みやすい形式（例：1K、234M、2G）でブロック数ではなく表示します。

```console
$ du -h Documents
16K     Documents/notes
4.0K    Documents/templates
24K     Documents
```

### **-s, --summarize**

各引数の合計のみを表示します（要約表示）。

```console
$ du -s Documents
24      Documents
```

### **-a, --all**

ディレクトリだけでなく、すべてのファイルのサイズを表示します。

```console
$ du -a Documents
4       Documents/notes/todo.txt
8       Documents/notes/meeting.txt
16      Documents/notes
4       Documents/templates/letter.txt
4       Documents/templates
24      Documents
```

### **-c, --total**

すべての引数を処理した後、総合計を表示します。

```console
$ du -c Documents Downloads
24      Documents
156     Downloads
180     total
```

### **--max-depth=N**

コマンドライン引数から N レベル以下のディレクトリの合計のみを表示します。

```console
$ du --max-depth=1 /home/user
24      /home/user/Documents
156     /home/user/Downloads
84      /home/user/Pictures
1024    /home/user
```

### **-x, --one-file-system**

異なるファイルシステム上のディレクトリをスキップします。

```console
$ du -x /home
```

## 使用例

### 最大のディレクトリを見つける

```console
$ du -h --max-depth=1 /home/user | sort -hr
1.0G    /home/user
450M    /home/user/Videos
350M    /home/user/Downloads
120M    /home/user/Pictures
24M     /home/user/Documents
```

### 特定のディレクトリサイズを人間が読みやすい形式で確認する

```console
$ du -sh /var/log
156M    /var/log
```

### 最も大きい5つのファイル/ディレクトリを見つける

```console
$ du -ha /home/user | sort -hr | head -5
1.0G    /home/user
450M    /home/user/Videos
350M    /home/user/Downloads
200M    /home/user/Videos/movie.mp4
120M    /home/user/Pictures
```

## ヒント:

### sortと組み合わせてより良い洞察を得る

`du`の出力を`sort`コマンドに`-h`（人間が読みやすい）と`-r`（逆順）オプションでパイプすると、ディレクトリを降順でサイズ順に表示できます。

```console
$ du -h --max-depth=1 | sort -hr
```

### 特定のディレクトリを除外する

`--exclude`オプションを使用して特定のディレクトリをスキップできます：

```console
$ du -h --exclude="node_modules" --max-depth=1
```

### grepと組み合わせて特定のパターンを見つける

`grep`と組み合わせて結果をフィルタリングできます：

```console
$ du -ha | grep "\.mp4$"
```

## よくある質問

#### Q1. `du`と`df`の違いは何ですか？
A. `du`はファイルやディレクトリのディスク使用量を表示しますが、`df`はファイルシステム全体のディスク容量使用状況を表示します。

#### Q2. なぜ`du`が表示するサイズがファイルマネージャで見るサイズと異なることがありますか？
A. `du`はディスク上で使用されている容量（ファイルシステムのオーバーヘッドを含む）を測定しますが、ファイルマネージャはファイルサイズを表示することが多いです。また、ブロックサイズや割り当て方法によっても違いが生じることがあります。

#### Q3. 大きなディレクトリで`du`をより速く実行するにはどうすればよいですか？
A. `du -s`を使用して要約のみを取得するか、`--max-depth=N`を使用して再帰の深さを制限します。

#### Q4. `du`で「permission denied」エラーが出るのはなぜですか？
A. チェックするすべてのディレクトリに対する読み取り権限が必要です。システムディレクトリをチェックする必要がある場合は、`sudo`で実行してみてください。

## macOSでの注意点

macOSでは、BSDバージョンの`du`が使用されており、オプションが若干異なります：
- `--max-depth`の代わりに`-d`を使用します
- `--exclude`のようなGNUオプションは利用できません
- 人間が読みやすい出力を得るには、`du -h | awk '{print $1, $2}'`を使用するとより見やすくなります

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html

## 改訂履歴

- 2025/05/04 初版作成