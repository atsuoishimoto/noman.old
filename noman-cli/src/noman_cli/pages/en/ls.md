# ls command

List information about files and directories in the specified location.

## Overview

The `ls` command displays the contents of a directory, showing files and directories. By default, it lists the contents of the current working directory in alphabetical order, excluding hidden files (those starting with a dot). It's one of the most frequently used commands for navigating and exploring the filesystem.

## Options

### **-l** (Long format)

Displays detailed information about each file including permissions, number of links, owner, group, size, and modification time.

```console
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-a** (All files)

Shows all files, including hidden files (those starting with a dot).

```console
$ ls -a
.  ..  .hidden  document.txt  projects
```

### **-h** (Human-readable)

When used with `-l`, displays file sizes in human-readable format (KB, MB, GB).

```console
$ ls -lh
total 16K
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

### **-d** (Directory)

Lists directories themselves, not their contents. Useful when you want to see information about the directory rather than what's inside it.

```console
$ ls -ld projects
drwxr-xr-x  3 user  staff  96 Apr 9 14:22 projects
```

### **-s** (Size)

Shows the allocated size of each file in blocks.

```console
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t** (Time)

Sorts files by modification time, with newest files first.

```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-r** (Reverse)

Reverses the order of the sort. When combined with other sorting options like `-t`, it reverses that order.

```console
$ ls -ltr
total 16
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
```

## Usage Examples

### Combining multiple options

```console
$ ls -lha
total 20K
drwxr-xr-x  4 user  staff  128B Apr 30 10:15 .
drwxr-xr-x 18 user  staff  576B Apr 29 09:30 ..
-rw-r--r--  1 user  staff   74B Apr 28 14:22 .hidden
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

### Listing files by pattern

```console
$ ls *.txt
document.txt  notes.txt  readme.txt
```

### Listing files in multiple directories

```console
$ ls -l /usr/bin /usr/local/bin
/usr/bin:
[output shows contents of /usr/bin directory]

/usr/local/bin:
[output shows contents of /usr/local/bin directory]
```

## Tips

### Color-coded Output

On many systems, you can use `ls --color=auto` to get color-coded output that distinguishes between different file types. On macOS, use `ls -G` instead.

### Sorting by File Size

Use `ls -lS` to sort files by size, with largest files first. Add `-r` (e.g., `ls -lSr`) to reverse the order.

### Finding Recently Modified Files

Combine `-t` with `-l` and limit results with `head`: `ls -lt | head -5` shows the five most recently modified files.

### Recursive Listing

Use `ls -R` to list all files in the current directory and all subdirectories recursively. Be careful in large directory structures as this can produce a lot of output.

## Frequently Asked Questions

#### Q1. How do I list only directories?
A. Use `ls -d */` to list only directories in the current location.

#### Q2. How can I see file sizes in a readable format?
A. Use `ls -lh` to display file sizes in KB, MB, or GB instead of bytes.

#### Q3. How do I sort files by modification time?
A. Use `ls -lt` to sort by modification time with newest files first. Use `ls -ltr` to show oldest files first.

#### Q4. How can I list files with their absolute paths?
A. Use `ls -d $PWD/*` to show the full path of each file.

## macOS Specifics

On macOS, some GNU ls options may not be available. Instead of `--color=auto`, use `-G` for colored output. The `-h` option works the same way for human-readable sizes. For extended attributes, macOS provides the `-@` option which shows extended file attributes.

## References

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html

## Revisions

- 2025/04/30 First revision