# `free` コマンド概要

`free`コマンドはシステムのメモリ使用状況を表示するためのコマンドです。物理メモリ（RAM）やスワップ領域の合計、使用中、空き容量などの情報を確認できます。

## 主なオプション

- **`-h`（human-readable）**: メモリサイズを読みやすい単位（KB、MB、GB）で表示します
  - 例: `free -h`

- **`-m`（megabytes）**: メモリサイズをメガバイト単位で表示します
  - 例: `free -m`

- **`-g`（gigabytes）**: メモリサイズをギガバイト単位で表示します
  - 例: `free -g`

- **`-s N`（seconds）**: N秒ごとに継続的にメモリ情報を更新して表示します
  - 例: `free -s 5`（5秒ごとに更新）

- **`-t`（total）**: 物理メモリとスワップの合計行を追加表示します
  - 例: `free -t`

- **`-w`（wide）**: 新しいフォーマットで表示します（buffers と cached を分けて表示）
  - 例: `free -w`

## 使用例

### 基本的な使用方法
```bash
# メモリ情報を表示
free
# 出力例
              total        used        free      shared  buff/cache   available
Mem:        8167872     3899460     1007328      772312     3261084     3177520
Swap:       2097148      123904     1973244
```

### 読みやすい単位で表示
```bash
# 人間が読みやすい単位でメモリ情報を表示
free -h
# 出力例
              total        used        free      shared  buff/cache   available
Mem:           7.8Gi       3.7Gi       962Mi       754Mi       3.1Gi       3.0Gi
Swap:          2.0Gi       121Mi       1.9Gi
```

### 継続的な監視
```bash
# 3秒ごとにメモリ情報を更新して表示
free -h -s 3
# 出力例（3秒ごとに更新される）
              total        used        free      shared  buff/cache   available
Mem:           7.8Gi       3.7Gi       962Mi       754Mi       3.1Gi       3.0Gi
Swap:          2.0Gi       121Mi       1.9Gi

              total        used        free      shared  buff/cache   available
Mem:           7.8Gi       3.7Gi       961Mi       754Mi       3.1Gi       3.0Gi
Swap:          2.0Gi       121Mi       1.9Gi
```

### メガバイト単位で合計行を表示
```bash
# メモリ情報をメガバイト単位で表示し、合計行も追加
free -m -t
# 出力例
              total        used        free      shared  buff/cache   available
Mem:           7975        3805         984        754        3185        3102
Swap:          2047         121        1926
Total:        10022        3926        2910
```

## 追加情報

- `buff/cache`列はバッファとキャッシュに使用されているメモリを示します。これは必要に応じて解放可能なメモリです。
- `available`列は、スワップを使わずに新しいアプリケーションを起動できる実質的に利用可能なメモリ量を示します。
- メモリ使用率が高くても、Linuxはキャッシュとして積極的にメモリを使用するため、必ずしもメモリ不足を意味するわけではありません。
- システムのパフォーマンス問題を診断する際は、`free`コマンドと`top`や`htop`コマンドを組み合わせて使用すると効果的です。