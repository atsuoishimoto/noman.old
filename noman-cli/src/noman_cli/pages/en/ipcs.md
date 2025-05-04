# ipcs command

Display information about active IPC facilities (shared memory, message queues, and semaphores).

## Overview

The `ipcs` command shows information about Inter-Process Communication (IPC) resources currently active in the system. It displays details about shared memory segments, message queues, and semaphore arrays that processes use to communicate with each other. This command is particularly useful for system administrators and developers debugging IPC-related issues.

## Options

### **-a, --all**

Show information about all IPC facilities (default behavior)

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

Show information about active message queues

```console
$ ipcs -q
------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    
```

### **-m, --shmems**

Show information about active shared memory segments

```console
$ ipcs -m
------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status      
0x00000000 0          root       644        80         2                       
0x00000000 32769      root       644        16384      2                       
```

### **-s, --semaphores**

Show information about active semaphore arrays

```console
$ ipcs -s
------ Semaphore Arrays --------
key        semid      owner      perms      nsems     
```

### **-t, --time**

Show last operation times for IPC facilities

```console
$ ipcs -t -m
------ Shared Memory Operation/Change Times --------
shmid      last-op                    last-changed              
0          Thu Jan  1 00:00:00 1970   Thu Jan  1 00:00:00 1970  
32769      Thu Jan  1 00:00:00 1970   Thu Jan  1 00:00:00 1970  
```

### **-p, --pid**

Show creator and last operator's PIDs

```console
$ ipcs -p -m
------ Shared Memory Creator/Last-op PIDs --------
shmid      owner      cpid       lpid      
0          root       0          0         
32769      root       0          0         
```

### **-c, --creator**

Show creator and owner

```console
$ ipcs -c -m
------ Shared Memory Segment Creators/Owners --------
shmid      perms      cpid       lpid      uid       gid      
0          644        0          0         0         0        
32769      644        0          0         0         0        
```

### **-l, --limits**

Show system resource limits

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

## Usage Examples

### Viewing all IPC resources with detailed information

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

### Checking shared memory segments with timestamps

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

### Viewing system-wide IPC limits

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

## Tips

### Understanding IPC Resources

IPC resources (shared memory, message queues, and semaphores) persist even after the creating process terminates. Use `ipcrm` to remove unused IPC resources that might be consuming system resources.

### Identifying Resource Leaks

If you see a large number of IPC resources owned by a specific user or process, it might indicate a resource leak in an application. Regular monitoring with `ipcs` can help identify such issues.

### Permissions Column

The "perms" column shows the octal permissions for the IPC resource, similar to file permissions. For example, "644" means the owner can read and write, while group and others can only read.

### Key Values

The "key" column shows the IPC key used to identify the resource. A key of "0x00000000" often indicates a private IPC resource that was created with IPC_PRIVATE.

## Frequently Asked Questions

#### Q1. What does the "nattch" column mean in shared memory output?
A. "nattch" shows the number of processes currently attached to the shared memory segment. A value of 0 means no process is using it, and it might be a candidate for cleanup.

#### Q2. How do I remove an IPC resource shown by ipcs?
A. Use the `ipcrm` command with the appropriate option and ID. For example, `ipcrm -m 12345` removes the shared memory segment with ID 12345.

#### Q3. What does it mean when ipcs shows no output?
A. It means there are no active IPC resources of the requested type in the system. This is normal on systems that don't heavily use IPC mechanisms.

#### Q4. How can I see who is using a specific IPC resource?
A. Use `ipcs -p` to see the creator and last operator PIDs for IPC resources.

## References

https://man7.org/linux/man-pages/man1/ipcs.1.html

## Revisions

- 2025/05/04 First revision