# groupadd

`groupadd`コマンドは、システムに新しいグループを作成するためのコマンドです。ユーザーアカウント管理の一部として、ファイルやディレクトリへのアクセス権限を管理するのに役立ちます。

## オプション

### **-g GID**

グループIDを指定します。指定しない場合は利用可能な次のGIDが自動的に割り当てられます。

```bash
$ sudo groupadd -g 1001 developers
```

### **-r**

システムグループを作成します。システムグループは通常、デーモンやシステムサービス用に使用されます。

```bash
$ sudo groupadd -r webservice
```

### **-f**

グループがすでに存在する場合でもエラーを表示せず、正常終了します（force）。

```bash
$ sudo groupadd -f marketing
```

### **-K KEY=VALUE**

/etc/login.defsのデフォルト設定を上書きします。

```bash
$ sudo groupadd -K GID_MIN=5000 newgroup
```

## 使用例

### 基本的なグループ作成

```bash
$ sudo groupadd developers
```

新しい「developers」グループが作成されました。

### 特定のGIDでグループを作成

```bash
$ sudo groupadd -g 2000 project_team
```

GID 2000で「project_team」グループを作成しました。

### システムグループの作成

```bash
$ sudo groupadd -r nginx
```

nginxサービス用のシステムグループを作成しました。

## よくある質問

### Q1. 一般ユーザーでもgroupaddコマンドを実行できますか？
A. いいえ、通常は管理者権限（root権限）が必要です。`sudo`を使用して実行してください。

### Q2. 既存のグループ情報を確認するにはどうすればいいですか？
A. `cat /etc/group`コマンドや`getent group グループ名`コマンドで確認できます。

### Q3. グループを削除するにはどうすればいいですか？
A. `groupdel グループ名`コマンドを使用します。

### Q4. 作成したグループにユーザーを追加するにはどうすればいいですか？
A. `usermod -aG グループ名 ユーザー名`コマンドを使用します。

## 追加情報

- グループ名は通常、英数字のみを使用し、スペースを含めないようにします。
- システムによっては、グループ名の長さに制限があります（通常は32文字以下）。
- グループを作成しても、自動的にユーザーは追加されません。ユーザーを追加するには別途コマンドが必要です。
- 既存のGIDを指定すると、エラーになります。

## macOSでの注意点

macOSでは`groupadd`コマンドは標準では利用できません。代わりに以下の方法でグループを作成します：

```bash
$ sudo dscl . -create /Groups/グループ名
$ sudo dscl . -create /Groups/グループ名 PrimaryGroupID 1000
```

または、Apple提供の`dseditgroup`コマンドを使用します：

```bash
$ sudo dseditgroup -o create グループ名
```

## 参考情報

https://www.man7.org/linux/man-pages/man8/groupadd.8.html