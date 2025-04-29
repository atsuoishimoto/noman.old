# `tail` コマンド概要

`tail`コマンドはファイルの末尾部分を表示するためのコマンドです。デフォルトでは、ファイルの最後の10行を表示します。ログファイルの監視や最新の変更を確認する際に特に便利です。

## 主なオプション

- **-n, --lines=N**: 表示する行数を指定します（デフォルトは10行）
  - 例: `tail -n 5 file.txt` （最後の5行を表示）

- **-f, --follow**: ファイルの更新をリアルタイムで監視し、新しく追加された行を表示し続けます
  - 例: `tail -f log.txt` （ログファイルの更新をリアルタイムで監視）

- **-c, --bytes=N**: 最後のN文字（バイト）を表示します
  - 例: `tail -c 20 file.txt` （最後の20バイトを表示）

- **+N**: ファイルのN行目から最後までを表示します
  - 例: `tail +100 file.txt` （100行目から最後まで表示）

## 使用例

```bash
# ファイルの最後の10行を表示（デフォルト）
tail file.txt
# 出力例
This is line 91
This is line 92
This is line 93
This is line 94
This is line 95
This is line 96
This is line 97
This is line 98
This is line 99
This is line 100

# 最後の3行だけを表示
tail -n 3 file.txt
# 出力例
This is line 98
This is line 99
This is line 100

# 複数のファイルの末尾を表示
tail -n 2 file1.txt file2.txt
# 出力例
==> file1.txt <==
Last line of file1
End of file1

==> file2.txt <==
Last line of file2
End of file2

# ログファイルをリアルタイムで監視
tail -f /var/log/syslog
# 出力例（新しいログが追加されるたびに表示が更新される）
Apr 10 15:23:01 server systemd[1]: Starting Daily apt upgrade and clean activities...
Apr 10 15:23:01 server systemd[1]: apt-daily-upgrade.service: Succeeded.
Apr 10 15:23:01 server systemd[1]: Finished Daily apt upgrade and clean activities.
...（新しいログが追加されると自動的に表示される）
```

## 追加情報

- `tail -f`はサーバーのログ監視に非常に便利です。Ctrl+Cで監視を終了できます。
- `tail -f`と`grep`を組み合わせると、特定のパターンを含む新しい行だけを監視できます：`tail -f log.txt | grep "error"`
- 複数のファイルを同時に監視するには：`tail -f file1.txt file2.txt`
- 最新のログを確認するために、システム管理者が最もよく使うコマンドの一つです。