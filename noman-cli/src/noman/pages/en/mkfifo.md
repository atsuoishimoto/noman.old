# mkfifo command

Creates named pipes (FIFOs) with the specified names.

## Overview

The `mkfifo` command creates special files known as named pipes or FIFOs (First-In-First-Out). These pipes allow communication between processes without using temporary files. Unlike regular pipes created with the `|` symbol, named pipes persist in the filesystem until deleted, allowing unrelated processes to communicate.

## Options

### **-m, --mode=MODE**

Set the permission mode for the created FIFO (default is 0666 minus umask)

```console
$ mkfifo -m 0600 private_pipe
$ ls -l private_pipe
prw-------  1 user  staff  0 May  4 10:15 private_pipe
```

### **-Z, --context=CTX**

Set the SELinux security context of created FIFOs to CTX

```console
$ mkfifo -Z user_u:object_r:user_fifo_t:s0 selinux_pipe
```

### **--help**

Display help information and exit

```console
$ mkfifo --help
Usage: mkfifo [OPTION]... NAME...
Create named pipes (FIFOs) with the given NAMEs.
...
```

### **--version**

Output version information and exit

```console
$ mkfifo --version
mkfifo (GNU coreutils) 8.32
...
```

## Usage Examples

### Basic FIFO Creation

```console
$ mkfifo my_pipe
$ ls -l my_pipe
prw-r--r--  1 user  staff  0 May  4 10:20 my_pipe
```

### Using a Named Pipe for Process Communication

```console
# Terminal 1: Create pipe and write to it
$ mkfifo message_pipe
$ echo "Hello from process 1" > message_pipe

# Terminal 2: Read from the pipe
$ cat < message_pipe
Hello from process 1
```

### Creating Multiple FIFOs at Once

```console
$ mkfifo pipe1 pipe2 pipe3
$ ls -l pipe*
prw-r--r--  1 user  staff  0 May  4 10:25 pipe1
prw-r--r--  1 user  staff  0 May  4 10:25 pipe2
prw-r--r--  1 user  staff  0 May  4 10:25 pipe3
```

## Tips

### Understanding Blocking Behavior

When a process attempts to read from an empty FIFO, it blocks until data is available. Similarly, writing to a FIFO blocks until another process reads the data. This behavior is important to understand when designing inter-process communication.

### Using with Redirection

Named pipes work well with standard input/output redirection. You can redirect output from one command to a named pipe and input from the named pipe to another command.

### Cleaning Up

Named pipes persist in the filesystem until explicitly removed with `rm`. Remember to clean up pipes when they're no longer needed to avoid confusion.

### Permissions Matter

Set appropriate permissions on your named pipes, especially in multi-user environments, to control which processes can read from or write to them.

## Frequently Asked Questions

#### Q1. What's the difference between a named pipe and a regular pipe?
A. A regular pipe (using `|`) exists only while the connected processes are running. A named pipe exists as a file in the filesystem until deleted, allowing unrelated processes to communicate.

#### Q2. Can I use named pipes for bidirectional communication?
A. No, named pipes are unidirectional. For bidirectional communication, you need to create two named pipes.

#### Q3. Why does my process hang when writing to a named pipe?
A. Writing to a named pipe blocks until another process reads from it. Make sure you have a reader process or open the pipe in non-blocking mode.

#### Q4. How do I remove a named pipe?
A. Use the `rm` command, just like with regular files: `rm my_pipe`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html

## Revisions

2025/05/04 First revision