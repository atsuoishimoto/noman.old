# egrep コマンド概要

`egrep`は拡張正規表現を使用してテキストパターンを検索するコマンドです。`grep -E`と同等の機能を持ち、複雑なパターンマッチングを簡潔な構文で実行できます。

## 主なオプション

- **-i**: 大文字と小文字を区別せずに検索します
  - 例: `egrep -i "pattern" file.txt`

- **-v**: パターンに一致しない行を表示します（反転マッチ）
  - 例: `egrep -v "pattern" file.txt`

- **-c**: 一致した行数のみを表示します
  - 例: `egrep -c "pattern" file.txt`

- **-n**: 一致した行の行番号も表示します
  - 例: `egrep -n "pattern" file.txt`

- **-l**: パターンが含まれるファイル名のみを表示します
  - 例: `egrep -l "pattern" *.txt`

- **-r, -R**: ディレクトリを再帰的に検索します
  - 例: `egrep -r "pattern" /path/to/directory`

## 使用例

### 基本的な使用法
```bash
# ファイル内で「apple」または「orange」を検索
egrep "apple|orange" fruits.txt
# 出力例
apple is red
orange is orange
```

### 複数のパターンと行番号表示
```bash
# 「user」または「admin」を含む行を行番号付きで表示
egrep -n "user|admin" users.log
# 出力例
2: user1 logged in
5: admin access granted
7: user2 logged out
```

### 再帰的な検索
```bash
# プロジェクト内のすべてのJavaファイルから「TODO」を検索
egrep -r "TODO" --include="*.java" ./project/
# 出力例
./project/src/Main.java:45: // TODO: Fix this bug
./project/src/User.java:23: // TODO: Implement authentication
```

### 複雑な正規表現
```bash
# 数字で始まる行を検索
egrep "^[0-9]" data.txt
# 出力例
1. First item
2. Second item
9999 - Special code
```

## 追加情報

- `egrep`は`grep -E`の別名であり、最近のシステムでは`grep -E`の使用が推奨されています。
- 拡張正規表現では、`|`（OR）、`+`（1回以上の繰り返し）、`?`（0または1回の出現）、`()`（グループ化）などの特殊文字をエスケープなしで使用できます。
- 検索パターンに空白やシェルの特殊文字が含まれる場合は、引用符（`""`）で囲むことをお勧めします。
- 大量のファイルを検索する場合は、`--include`や`--exclude`オプションを使用して対象を絞り込むと効率的です。