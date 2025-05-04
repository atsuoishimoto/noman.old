# ipcs command

Display information about active IPC facilities (shared memory, message queues, and semaphores).

## Overview

The `ipcs` command shows information about Inter-Process Communication (IPC) resources currently active in the system. It displays details about shared memory segments, message queues, and semaphore arrays that processes use to communicate with each other. This command is useful for system administrators and developers to monitor and troubleshoot IPC resource usage.

## Options

### **-m (Shared Memory)**

Shows information about active shared memory segments

```console
$ ipcs -m
------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x00000000 0          root       644        80         2          dest         
0x00000000 32769      postgres   600        56         2          dest
```

### **-q (Message Queues)**

Shows information about active message queues

```console
$ ipcs -q
------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    
0x41424344 0          user       644        80           2
```

### **-s (Semaphores)**

Shows information about active semaphore sets

```console
$ ipcs -s
------ Semaphore Arrays --------
key        semid      owner      perms      nsems     
0x00000000 0          postgres   600        17
```

### **-a (All)**

Shows information about all IPC facilities

```console
$ ipcs -a
# Shows all shared memory segments, message queues, and semaphores
```

### **-t (Time)**

Shows creation/last operation times for IPC facilities

```console
$ ipcs -t -m
------ Shared Memory Segment Creators/Owners --------
shmid      owner      cpid       lpid      
0          root       1          1         
32769      postgres   1234       1234
```

## Usage Examples

### Displaying detailed information about shared memory

```console
$ ipcs -m -i 32769
Shared Memory Segment shmid=32769
uid=999 gid=999 cuid=999 cgid=999
mode=0600, access_perms=0600
bytes=56, lpid=1234, cpid=1234, nattch=2
att_time=Wed May  4 10:30:45 2025  
det_time=Wed May  4 10:30:45 2025  
change_time=Wed May  4 10:30:45 2025
```

### Showing all IPC resources with permissions

```console
$ ipcs -p
------ Shared Memory Creator/Last-op --------
shmid      owner      cpid       lpid      
0          root       1          1         
32769      postgres   1234       1234      

------ Message Queues: Creator/Last-op --------
msqid      owner      cpid       lpid      
0          user       2345       2346      

------ Semaphore Arrays: Creator/Last-op --------
semid      owner      cpid       lpid      
0          postgres   1234       1234
```

## Tips:

### Identifying Resource Leaks

If you see a large number of IPC resources owned by a specific process or user, it might indicate a resource leak. Use `ipcs -a` regularly to monitor IPC usage.

### Cleaning Up Stale Resources

Use `ipcrm` command to remove unused IPC resources. For example, `ipcrm -m <shmid>` removes a shared memory segment.

### Understanding Permissions

The "perms" column shows octal permissions similar to file permissions. For example, "600" means the owner has read and write access, but group and others have no access.

### Finding Processes Using IPC Resources

Use `ipcs -p` to see which processes created or last accessed each IPC resource, helping you track down which applications are using system IPC facilities.

## Frequently Asked Questions

#### Q1. What is IPC and why would I need to monitor it?
A. Inter-Process Communication (IPC) allows processes to communicate with each other. Monitoring IPC is important for diagnosing performance issues, resource leaks, or deadlocks in applications that use shared resources.

#### Q2. How do I remove an IPC resource that's no longer needed?
A. Use the `ipcrm` command. For example, `ipcrm -m <shmid>` removes a shared memory segment, `ipcrm -q <msqid>` removes a message queue, and `ipcrm -s <semid>` removes a semaphore array.

#### Q3. What do the different columns in the ipcs output mean?
A. Key columns include: "key" (IPC resource identifier), "id" (system-assigned ID), "owner" (user who created it), "perms" (access permissions), and resource-specific information like "bytes" for shared memory or "nsems" for semaphores.

#### Q4. How can I see which processes are using a specific IPC resource?
A. Use `ipcs -p` to see the creator process ID (cpid) and last accessing process ID (lpid) for each IPC resource.

## References

https://man7.org/linux/man-pages/man1/ipcs.1.html

## Revisions

- 2025/05/04 First revision