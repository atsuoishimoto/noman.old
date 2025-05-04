# du command

Estimate file space usage for files and directories.

## Overview

The `du` (disk usage) command estimates and displays the disk space used by files and directories. It's useful for finding large files or directories that consume significant disk space, helping you manage storage efficiently.

## Options

### **-h, --human-readable**

Display sizes in human-readable format (e.g., 1K, 234M, 2G) instead of blocks.

```console
$ du -h Documents
16K     Documents/notes
4.0K    Documents/templates
24K     Documents
```

### **-s, --summarize**

Display only a total for each argument (summarize).

```console
$ du -s Documents
24      Documents
```

### **-a, --all**

Show counts for all files, not just directories.

```console
$ du -a Documents
4       Documents/notes/todo.txt
8       Documents/notes/meeting.txt
16      Documents/notes
4       Documents/templates/letter.txt
4       Documents/templates
24      Documents
```

### **-c, --total**

Produce a grand total of all arguments after all arguments have been processed.

```console
$ du -c Documents Downloads
24      Documents
156     Downloads
180     total
```

### **--max-depth=N**

Print the total for a directory only if it is N or fewer levels below the command line argument.

```console
$ du --max-depth=1 /home/user
24      /home/user/Documents
156     /home/user/Downloads
84      /home/user/Pictures
1024    /home/user
```

### **-x, --one-file-system**

Skip directories on different file systems.

```console
$ du -x /home
```

## Usage Examples

### Finding the largest directories

```console
$ du -h --max-depth=1 /home/user | sort -hr
1.0G    /home/user
450M    /home/user/Videos
350M    /home/user/Downloads
120M    /home/user/Pictures
24M     /home/user/Documents
```

### Checking specific directory size with human-readable output

```console
$ du -sh /var/log
156M    /var/log
```

### Finding the 5 largest files/directories

```console
$ du -ha /home/user | sort -hr | head -5
1.0G    /home/user
450M    /home/user/Videos
350M    /home/user/Downloads
200M    /home/user/Videos/movie.mp4
120M    /home/user/Pictures
```

## Tips:

### Combine with sort for better insights

Pipe `du` output to `sort` with the `-h` (human-readable) and `-r` (reverse) options to list directories by size in descending order.

```console
$ du -h --max-depth=1 | sort -hr
```

### Exclude certain directories

Use the `--exclude` option to skip specific directories:

```console
$ du -h --exclude="node_modules" --max-depth=1
```

### Use with grep to find specific patterns

Combine with `grep` to filter results:

```console
$ du -ha | grep "\.mp4$"
```

## Frequently Asked Questions

#### Q1. What's the difference between `du` and `df`?
A. `du` shows disk usage of files and directories, while `df` shows disk space usage of entire filesystems.

#### Q2. Why does `du` sometimes show different sizes than what I see in a file manager?
A. `du` measures disk space used (including filesystem overhead), while file managers often show file size. Also, block sizes and allocation methods can cause differences.

#### Q3. How can I make `du` run faster on large directories?
A. Use `du -s` to only get summaries, or `--max-depth=N` to limit recursion depth.

#### Q4. Why do I get "permission denied" errors with `du`?
A. You need read permissions for all directories you're checking. Try running with `sudo` if you need to check system directories.

## macOS Considerations

On macOS, the BSD version of `du` has slightly different options:
- Use `-d` instead of `--max-depth`
- Some GNU options like `--exclude` are not available
- For human-readable output, you may need to use `du -h | awk '{print $1, $2}'` to get cleaner output

## References

https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html

## Revisions

- 2025/05/04 First revision