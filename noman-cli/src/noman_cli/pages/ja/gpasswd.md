# gpasswd

`gpasswd`はグループ管理のためのコマンドで、グループのメンバーやグループ管理者の追加・削除などを行います。

## オプション

### **-a (--add) ユーザー**

指定したユーザーをグループに追加します。

```bash
$ sudo gpasswd -a yamada developers
ユーザー「yamada」を「developers」グループに追加しました
```

### **-d (--delete) ユーザー**

指定したユーザーをグループから削除します。

```bash
$ sudo gpasswd -d yamada developers
ユーザー「yamada」を「developers」グループから削除しました
```

### **-A (--administrators) ユーザー1,ユーザー2,...**

グループ管理者を設定します。グループ管理者はroot権限なしでグループメンバーを管理できます。

```bash
$ sudo gpasswd -A tanaka,suzuki developers
```

### **-M (--members) ユーザー1,ユーザー2,...**

グループのメンバーリストを設定します（既存のメンバーリストは上書きされます）。

```bash
$ sudo gpasswd -M yamada,tanaka,suzuki developers
```

### **-r (--remove-password)**

グループのパスワードを削除します。

```bash
$ sudo gpasswd -r developers
```

## 使用例

### グループにユーザーを追加する

```bash
$ sudo gpasswd -a yamada developers
ユーザー「yamada」を「developers」グループに追加しました
```

### 複数のユーザーをグループに設定する

```bash
$ sudo gpasswd -M yamada,tanaka,suzuki developers
```

### グループ管理者を設定する

```bash
$ sudo gpasswd -A tanaka developers
```

## よくある質問

### Q1. `gpasswd`と`usermod`の違いは何ですか？
A. `gpasswd`はグループ管理に特化したコマンドで、グループ管理者の設定などができます。`usermod`はユーザーアカウント全般の変更に使用され、グループ追加はその一機能です。

### Q2. 一般ユーザーでもグループ管理ができますか？
A. グループ管理者として設定されたユーザーは、そのグループのメンバー管理ができます。ただし、すべての操作にroot権限が必要なわけではありません。

### Q3. グループのメンバーリストを確認するには？
A. `gpasswd`ではなく、`getent group グループ名`または`grep グループ名 /etc/group`で確認できます。

## 追加情報

- `-M`オプションを使うと既存のメンバーリストが上書きされるので注意が必要です。既存メンバーを残したまま追加する場合は`-a`を使用してください。
- グループパスワードは現在のLinuxシステムではあまり使用されていません。
- macOSでは`gpasswd`コマンドは標準では利用できません。代わりに`dscl`コマンドを使用してグループ管理を行います。

## 参考情報

man ページを参照してください。オンラインでは各ディストリビューションのマニュアルページで確認できます。