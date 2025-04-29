# script

`script` コマンドは、ターミナルセッションの全出力を記録し、ファイルに保存するためのツールです。デバッグやトレーニング、ドキュメント作成に役立ちます。

## オプション

### **-a, --append**

既存のファイルに追記します。デフォルトでは上書きされます。

```bash
$ script -a session.log
Script started, output appended to session.log.
```

### **-f, --flush**

各入力後にすぐにログファイルに書き込みます。クラッシュ時のデータ損失を防ぎます。

```bash
$ script -f session.log
Script started, output file is session.log.
```

### **-q, --quiet**

開始・終了メッセージを表示しません。

```bash
$ script -q session.log
```

### **-t, --timing[=ファイル]**

タイミング情報を別ファイルに記録します。後で `scriptreplay` コマンドで再生できます。

```bash
$ script -t timing.log session.log
Script started, output file is session.log.
```

## 使用例

### 基本的な使い方

```bash
$ script session.log
Script started, output file is session.log.
$ ls
Documents Downloads Pictures
$ exit
Script done, output file is session.log.
```

### セッションの再生

タイミング情報を記録した場合、`scriptreplay` コマンドでセッションを再生できます。

```bash
$ script -t timing.log session.log
Script started, output file is session.log.
$ ls -la
$ pwd
$ exit
Script done, output file is session.log.

$ scriptreplay timing.log session.log
# 記録されたセッションが再生される
```

## よくある質問

### Q1. `script` コマンドはどのような場合に使うのですか？
A. トラブルシューティングの記録、コマンドラインデモの作成、トレーニング資料の準備、システム管理作業の監査証跡の作成などに使用します。

### Q2. 記録を終了するにはどうすればいいですか？
A. `exit` コマンドを入力するか、`Ctrl+D` を押すことで記録を終了できます。

### Q3. パスワードなど機密情報も記録されますか？
A. はい、表示される全ての内容が記録されます。機密情報を入力する前に記録を一時停止するか、後で編集する必要があります。

### Q4. 記録したファイルはどのように確認できますか？
A. 通常のテキストファイルなので、`cat`、`less`、`more` などのコマンドや任意のテキストエディタで確認できます。

## 追加情報

- 長時間のセッションを記録する場合は、`-f` オプションを使用してバッファリングを無効にすることをお勧めします。
- macOSでは基本的な機能は同じですが、一部のオプションが異なる場合があります。
- 大量の出力がある場合、ログファイルが非常に大きくなる可能性があるため注意が必要です。
- 色付きの出力（ANSIエスケープシーケンス）も記録されるため、ファイルを表示する際に特殊な文字が含まれることがあります。

## 参考情報

https://man7.org/linux/man-pages/man1/script.1.html