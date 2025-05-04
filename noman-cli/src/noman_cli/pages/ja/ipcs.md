# ipcs コマンド

アクティブなIPCファシリティ（共有メモリ、メッセージキュー、セマフォ）に関する情報を表示します。

## 概要

`ipcs`コマンドは、システム上で現在アクティブなプロセス間通信（IPC）リソースに関する情報を表示します。プロセスが相互に通信するために使用する共有メモリセグメント、メッセージキュー、セマフォ配列の詳細を表示します。このコマンドは、システム管理者やIPC関連の問題をデバッグする開発者にとって特に役立ちます。

## オプション

### **-a, --all**

すべてのIPCファシリティに関する情報を表示します（デフォルトの動作）

```console
$ ipcs -a
------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x00000000 0          root       644        80         2                       
0x00000000 32769      root       644        16384      2                       

------ Semaphore Arrays --------
key        semid      owner      perms      nsems     
```

### **-q, --queues**

アクティブなメッセージキューに関する情報を表示します

```console
$ ipcs -q
------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    
```

### **-m, --shmems**

アクティブな共有メモリセグメントに関する情報を表示します

```console
$ ipcs -m
------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x00000000 0          root       644        80         2                       
0x00000000 32769      root       644        16384      2                       
```

### **-s, --semaphores**

アクティブなセマフォ配列に関する情報を表示します

```console
$ ipcs -s
------ Semaphore Arrays --------
key        semid      owner      perms      nsems     
```

### **-t, --time**

IPCファシリティの最終操作時間を表示します

```console
$ ipcs -t -m
------ Shared Memory Operation/Change Times --------
shmid      last-op                    last-changed              
0          Thu Jan  1 00:00:00 1970   Thu Jan  1 00:00:00 1970  
32769      Thu Jan  1 00:00:00 1970   Thu Jan  1 00:00:00 1970  
```

### **-p, --pid**

作成者と最後の操作者のPIDを表示します

```console
$ ipcs -p -m
------ Shared Memory Creator/Last-op PIDs --------
shmid      owner      cpid       lpid      
0          root       0          0         
32769      root       0          0         
```

### **-c, --creator**

作成者と所有者を表示します

```console
$ ipcs -c -m
------ Shared Memory Segment Creators/Owners --------
shmid      perms      cpid       lpid      uid       gid      
0          644        0          0         0         0        
32769      644        0          0         0         0        
```

### **-l, --limits**

システムリソースの制限を表示します

```console
$ ipcs -l
------ Messages Limits --------
max queues system wide = 32000
max size of message (bytes) = 8192
default max size of queue (bytes) = 16384

------ Shared Memory Limits --------
max number of segments = 4096
max seg size (kbytes) = 18014398509465599
max total shared memory (kbytes) = 18014398509481980
min seg size (bytes) = 1

------ Semaphore Limits --------
max number of arrays = 32000
max semaphores per array = 32000
max semaphores system wide = 1024000000
max ops per semop call = 500
semaphore max value = 32767
```

## 使用例

### 詳細情報を含むすべてのIPCリソースの表示

```console
$ ipcs -a
------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x00000000 0          root       644        80         2                       
0x00000000 32769      root       644        16384      2                       

------ Semaphore Arrays --------
key        semid      owner      perms      nsems     
```

### タイムスタンプ付きの共有メモリセグメントの確認

```console
$ ipcs -mt
------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x00000000 0          root       644        80         2                       
0x00000000 32769      root       644        16384      2                       

------ Shared Memory Operation/Change Times --------
shmid      last-op                    last-changed              
0          Thu Jan  1 00:00:00 1970   Thu Jan  1 00:00:00 1970  
32769      Thu Jan  1 00:00:00 1970   Thu Jan  1 00:00:00 1970  
```

### システム全体のIPC制限の表示

```console
$ ipcs -l
------ Messages Limits --------
max queues system wide = 32000
max size of message (bytes) = 8192
default max size of queue (bytes) = 16384

------ Shared Memory Limits --------
max number of segments = 4096
max seg size (kbytes) = 18014398509465599
max total shared memory (kbytes) = 18014398509481980
min seg size (bytes) = 1

------ Semaphore Limits --------
max number of arrays = 32000
max semaphores per array = 32000
max semaphores system wide = 1024000000
max ops per semop call = 500
semaphore max value = 32767
```

## ヒント:

### IPCリソースの理解

IPCリソース（共有メモリ、メッセージキュー、セマフォ）は、作成プロセスが終了した後も存続します。システムリソースを消費している可能性のある未使用のIPCリソースを削除するには、`ipcrm`を使用してください。

### リソースリークの特定

特定のユーザーやプロセスが所有する大量のIPCリソースが表示される場合、アプリケーションでリソースリークが発生している可能性があります。`ipcs`による定期的な監視で、このような問題を特定できます。

### パーミッション列

「perms」列は、ファイルパーミッションと同様に、IPCリソースの8進数パーミッションを示します。例えば、「644」は、所有者が読み書き可能で、グループとその他のユーザーは読み取りのみ可能であることを意味します。

### キー値

「key」列は、リソースを識別するために使用されるIPCキーを示します。「0x00000000」のキーは、多くの場合、IPC_PRIVATEで作成されたプライベートIPCリソースを示します。

## よくある質問

#### Q1. 共有メモリ出力の「nattch」列は何を意味しますか？
A. 「nattch」は、現在共有メモリセグメントにアタッチしているプロセスの数を示します。値が0の場合、そのセグメントを使用しているプロセスがないことを意味し、クリーンアップの候補となる可能性があります。

#### Q2. ipcsで表示されるIPCリソースを削除するにはどうすればよいですか？
A. 適切なオプションとIDを指定して`ipcrm`コマンドを使用します。例えば、`ipcrm -m 12345`はID 12345の共有メモリセグメントを削除します。

#### Q3. ipcsが何も出力しない場合、何を意味しますか？
A. システム内に要求されたタイプのアクティブなIPCリソースがないことを意味します。これは、IPCメカニズムを多用しないシステムでは正常です。

#### Q4. 特定のIPCリソースを誰が使用しているかを確認するにはどうすればよいですか？
A. `ipcs -p`を使用して、IPCリソースの作成者と最後の操作者のPIDを確認できます。

## 参考文献

https://man7.org/linux/man-pages/man1/ipcs.1.html

## 改訂履歴

- 2025/05/04 初回改訂