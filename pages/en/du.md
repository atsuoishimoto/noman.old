# du command

Display disk usage statistics for files and directories.

## Overview

The `du` (disk usage) command estimates and displays the amount of disk space used by files and directories. It's particularly useful for finding which files or directories are consuming the most space on your system, helping you manage storage effectively.

## Options

### **-h, --human-readable**

Display sizes in human-readable format (e.g., KB, MB, GB) instead of blocks

```console
$ du -h Documents
4.0K    Documents/notes
16K     Documents/images
24K     Documents
```

### **-s, --summarize**

Display only a total for each argument (summarize)

```console
$ du -s Documents
24      Documents
```

### **-c, --total**

Produce a grand total of all arguments

```console
$ du -c Documents Downloads
24      Documents
36      Downloads
60      total
```

### **-a, --all**

Show sizes for all files, not just directories

```console
$ du -a Documents
4.0K    Documents/notes/todo.txt
4.0K    Documents/notes
8.0K    Documents/images/photo.jpg
8.0K    Documents/images
24K     Documents
```

### **--max-depth=N**

Print the total for a directory only if it is N or fewer levels below the command line argument

```console
$ du --max-depth=1 Documents
4.0K    Documents/notes
16K     Documents/images
24K     Documents
```

## Usage Examples

### Finding the largest directories in your home folder

```console
$ du -h --max-depth=1 ~ | sort -hr
1.2G    /home/user
450M    /home/user/Downloads
320M    /home/user/Videos
280M    /home/user/Documents
```

### Checking specific directory size with human-readable output

```console
$ du -sh /var/log
156M    /var/log
```

### Finding the top 5 largest files/directories

```console
$ du -ha /home/user | sort -hr | head -5
1.2G    /home/user
450M    /home/user/Downloads
320M    /home/user/Videos
280M    /home/user/Documents
150M    /home/user/Downloads/ubuntu.iso
```

## Tips

### Combine with Sort for Better Analysis

Pipe `du` output to `sort` with the `-h` and `-r` flags to sort by size in descending order: `du -h | sort -hr`

### Exclude Certain Directories

Use the `--exclude` option to skip directories: `du -h --exclude="node_modules"`

### Use with Find for Specific File Types

Combine with `find` to analyze disk usage for specific file types: `find . -name "*.log" -exec du -ch {} \; | grep total`

### Beware of Permissions

Running `du` on system directories may require sudo privileges, and some files might be inaccessible without proper permissions.

## Frequently Asked Questions

#### Q1. What's the difference between `du` and `df`?
A. `du` shows disk usage of files and directories, while `df` displays free disk space on the entire filesystem.

#### Q2. Why does `du` sometimes show different sizes than what I see in a file manager?
A. `du` measures actual disk space used (including filesystem overhead), while file managers often show logical file sizes.

#### Q3. How can I check the size of a specific folder?
A. Use `du -sh folder_name` to get a summarized, human-readable size of that folder.

#### Q4. Why is `du` slow on large directories?
A. `du` needs to traverse every file and directory to calculate sizes, which can be time-consuming for large directory structures.

## References

https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html

## Revisions

- 2025/04/30 First revision