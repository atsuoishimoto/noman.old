# mkfifo command

Create named pipes (FIFOs) with specified names.

## Overview

The `mkfifo` command creates special files known as named pipes or FIFOs (First In, First Out). These pipes act as communication channels between processes, allowing data to flow from one process to another without using temporary files or network connections.

## Options

### **-m, --mode=MODE**

Set the permission mode for the created FIFO (default is 0666 - read/write for all)

```console
$ mkfifo -m 0600 private_pipe
$ ls -l private_pipe
prw-------  1 user  staff  0 Apr 30 10:15 private_pipe
```

### **-Z, --context=CTX**

Set the SELinux security context of created FIFOs (only on systems with SELinux)

```console
$ mkfifo -Z user_u:object_r:tmp_t:s0 selinux_pipe
```

### **--help**

Display help information and exit

```console
$ mkfifo --help
Usage: mkfifo [OPTION]... NAME...
Create named pipes (FIFOs) with the given NAMEs.
...
```

## Usage Examples

### Creating a basic named pipe

```console
$ mkfifo my_pipe
$ ls -l my_pipe
prw-r--r--  1 user  staff  0 Apr 30 10:20 my_pipe
```

### Using a named pipe for process communication

```console
# Terminal 1: Create pipe and write to it
$ mkfifo message_pipe
$ echo "Hello from process 1" > message_pipe

# Terminal 2: Read from the pipe (blocks until data is available)
$ cat < message_pipe
Hello from process 1
```

### Creating multiple pipes at once

```console
$ mkfifo pipe1 pipe2 pipe3
$ ls -l pipe*
prw-r--r--  1 user  staff  0 Apr 30 10:25 pipe1
prw-r--r--  1 user  staff  0 Apr 30 10:25 pipe2
prw-r--r--  1 user  staff  0 Apr 30 10:25 pipe3
```

## Tips

### Understanding Blocking Behavior

Named pipes block when opened for reading until another process opens them for writing (and vice versa). This is important to remember to avoid deadlocks in your scripts.

### Cleaning Up Pipes

Unlike regular pipes created with `|`, named pipes persist in the filesystem until explicitly deleted with `rm`. Always clean up pipes when you're done with them.

### Pipe Size Limitations

Data written to a named pipe is buffered by the kernel up to a certain limit (typically 64KB on Linux). Writing more data will block until a reader consumes some of it.

### Using with Command Substitution

Be careful when using named pipes with command substitution `$(...)` as it can lead to deadlocks if not managed properly.

## Frequently Asked Questions

#### Q1. What's the difference between a named pipe and a regular pipe (`|`)?
A. Regular pipes (`|`) exist only while the connected processes are running and have no presence in the filesystem. Named pipes created with `mkfifo` persist in the filesystem and can be used by unrelated processes at different times.

#### Q2. Can multiple processes read from or write to the same named pipe?
A. Yes, multiple processes can open a named pipe for reading or writing, but data written by one process will be read by only one reader (not duplicated to all readers).

#### Q3. How do I remove a named pipe when I'm done with it?
A. Use the standard `rm` command: `rm my_pipe`. Named pipes are removed from the filesystem just like regular files.

#### Q4. What happens if I try to read from an empty pipe?
A. The reading process will block (wait) until another process writes data to the pipe or until the pipe is closed by all writers.

## References

https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html

## Revisions

- 2025/04/30 First revision