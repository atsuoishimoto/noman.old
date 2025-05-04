# ls command

List directory contents.

## Overview

The `ls` command displays files and directories in the specified location. By default, it shows the contents of the current directory, sorted alphabetically. It's one of the most frequently used commands for navigating and examining the file system.

## Options

### **-l** (Long format)

Displays detailed information about each file including permissions, number of links, owner, group, size, and modification time.

```console
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-a** (All)

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

Lists directories themselves, not their contents.

```console
$ ls -d */
projects/  documents/  downloads/
```

### **-s** (Size)

Prints the allocated size of each file in blocks.

```console
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t** (Time)

Sorts files by modification time, newest first.

```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-r** (Reverse)

Reverses the order of the sort.

```console
$ ls -lr
total 16
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
```

## Usage Examples

### Combining multiple options

```console
$ ls -lha
total 20K
drwxr-xr-x  4 user  staff  128B Apr 10 15:35 .
drwxr-xr-x 18 user  staff  576B Apr 10 14:00 ..
-rw-r--r--  1 user  staff   74B Apr 10 15:32 .hidden
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

### Listing files by pattern

```console
$ ls *.txt
document.txt  notes.txt  readme.txt
```

### Sorting files by size (largest first)

```console
$ ls -lhS
total 16K
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

## Tips

### Color-coded Output

Many systems configure `ls` to display different file types in different colors. You can enforce this with `ls --color=auto` on Linux or `ls -G` on macOS.

### Recursive Listing

Use `ls -R` to list subdirectories recursively, showing the entire directory tree.

### Combining Sort Options

When combining sort options like `-t` (time) and `-r` (reverse), remember that `-r` always reverses the current sort order. For example, `ls -ltr` shows the oldest files first.

### Aliases

Many users create aliases like `ll` for `ls -l` and `la` for `ls -la` in their shell configuration files to save typing common combinations.

## Frequently Asked Questions

#### Q1. How do I list only directories?
A. Use `ls -d */` to list only directories in the current location.

#### Q2. How can I see file sizes in a readable format?
A. Use `ls -lh` to see file sizes in KB, MB, or GB instead of bytes.

#### Q3. How do I sort files by size?
A. Use `ls -lS` to sort files by size (largest first). Add `-r` (`ls -lSr`) to reverse the order.

#### Q4. How can I see the most recently modified files first?
A. Use `ls -lt` to sort by modification time with newest files first.

#### Q5. How do I list files with their inode numbers?
A. Use `ls -i` to display the index number (inode) of each file.

## macOS Considerations

On macOS, some GNU ls options may not be available or may work differently:
- Use `-G` instead of `--color` to enable colorized output
- The `-h` option works the same way as on Linux
- For extended attributes, use `ls -@` which is specific to macOS

## References

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html

## Revisions

- 2025/05/04 Added -d, -s, -t, -r options and macOS considerations.