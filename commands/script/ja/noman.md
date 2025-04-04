# `script` コマンドの概要

`script` コマンドは、ターミナルセッションの全出力を記録し、ファイルに保存するためのユーティリティです。コマンドの実行履歴やその出力結果を後で確認したり、他の人と共有したりする際に便利です。

## 主なオプション

- **`-a`, `--append`**: 既存のファイルに追記します（上書きではなく）
  - 例: `script -a session.log`

- **`-f`, `--flush`**: 各コマンド実行後にバッファをフラッシュし、リアルタイムでログを更新します
  - 例: `script -f realtime.log`

- **`-q`, `--quiet`**: 開始・終了メッセージを表示しません
  - 例: `script -q silent.log`

- **`-t`, `--timing[=ファイル]`**: タイミング情報を別ファイルに記録します
  - 例: `script -t timing.log session.log`

- **`-c`, `--command "コマンド"`**: 指定したコマンドのみを実行して記録します
  - 例: `script -c "ls -la" command_output.log`

## 使用例

### 基本的な使い方

```bash
# script コマンドを開始
script my_session.log

# 開始メッセージが表示される
Script started, file is my_session.log

# いくつかのコマンドを実行
ls -la
pwd
echo "Hello World"

# 記録を終了
exit

# または Ctrl+D を押す
# 終了メッセージが表示される
Script done, file is my_session.log
```

### 特定のコマンドだけを記録

```bash
# ls -la コマンドの出力だけを記録
script -c "ls -la" directory_listing.log

# 記録されたファイルの内容を確認
cat directory_listing.log
# 出力例:
# total 32
# drwxr-xr-x  5 user  staff   160 Apr 10 12:34 .
# drwxr-xr-x  3 user  staff    96 Apr 10 12:30 ..
# -rw-r--r--  1 user  staff  2048 Apr 10 12:32 file1.txt
# -rw-r--r--  1 user  staff  1024 Apr 10 12:33 file2.txt
```

### タイミング情報を記録して再生

```bash
# タイミング情報を記録
script -t timing.log session.log

# コマンドを実行
ls -la
sleep 2
echo "Hello after 2 seconds"
exit

# 記録を再生（scriptreplay コマンドを使用）
scriptreplay timing.log session.log
# 実行したコマンドが、実際の操作と同じタイミングで再生される
```

## 追加情報

- `script` コマンドはシェルスクリプトの実行ログを取るだけでなく、インタラクティブなセッション全体（プロンプト、コマンド入力、出力など）を記録します。
- 記録されたファイルには制御文字も含まれるため、`cat` で表示すると読みにくい場合があります。`less` コマンドで確認するとより見やすくなります。
- システム管理者がトラブルシューティングの手順を記録したり、コマンドラインでの作業を他の人に説明したりする際に非常に役立ちます。
- セキュリティ上の注意点として、パスワードなどの機密情報を入力する場合は記録が残ることを意識してください。