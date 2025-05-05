# find command

Search for files in a directory hierarchy.

## Overview

The `find` command searches for files in a directory hierarchy based on various criteria such as name, type, size, or modification time. It's a powerful tool for locating files and performing operations on the matching results.

## Options

### **-iname pattern**

Searches for files whose name matches the pattern, ignoring case distinctions. This is similar to `-name` but performs a case-insensitive search.

```console
$ find . -iname "*.txt"
./notes.txt
./Documents/README.txt
./Documents/report.TXT
```

### **-name pattern**

Searches for files whose name matches the pattern, with case sensitivity.

```console
$ find . -name "*.txt"
./notes.txt
./Documents/README.txt
```

### **-type type**

Searches for files of a specific type. Common types include:
- `f` for regular files
- `d` for directories
- `l` for symbolic links

```console
$ find . -type d
.
./Documents
./Downloads
./Pictures
```

### **-size n[cwbkMG]**

Searches for files based on their size:
- `c` for bytes
- `k` for kilobytes
- `M` for megabytes
- `G` for gigabytes
- `+` prefix means "greater than"
- `-` prefix means "less than"

```console
$ find . -size +10M
./Videos/movie.mp4
./Downloads/installer.iso
```

### **-mtime n**

Searches for files modified n days ago. Use `+n` for "more than n days ago" and `-n` for "less than n days ago".

```console
$ find . -mtime -7
./Documents/recent-report.txt
./Downloads/recent-file.zip
```

## Usage Examples

### Finding files with specific permissions

```console
$ find /home -type f -perm 644
/home/user/file1.txt
/home/user/file2.txt
```

### Finding and executing commands on matching files

```console
$ find . -name "*.log" -exec rm {} \;
```

### Finding empty files

```console
$ find /var/log -type f -empty
/var/log/empty.log
```

### Finding files modified in the last 24 hours

```console
$ find /home/user -type f -mtime -1
/home/user/recent-document.txt
/home/user/today-notes.md
```

## Tips

### Use `-iname` for Case-Insensitive Searches

When you're not sure about the exact capitalization of filenames, use `-iname` instead of `-name` to match files regardless of case.

### Combine Multiple Criteria with Logical Operators

Use `-and`, `-or`, and `-not` (or `!`) to create complex search conditions:
```console
$ find . -type f -name "*.txt" -and -size +1M
```

### Limit Directory Depth with `-maxdepth`

Control how deep `find` searches with `-maxdepth`:
```console
$ find . -maxdepth 2 -name "*.jpg"
```

### Redirect Error Messages

Use `2>/dev/null` to hide "Permission denied" errors:
```console
$ find / -name "config.xml" 2>/dev/null
```

## Frequently Asked Questions

#### Q1. How do I find files by name?
A. Use `find /path/to/search -name "filename"` for case-sensitive searches or `find /path/to/search -iname "filename"` for case-insensitive searches.

#### Q2. How can I find files modified recently?
A. Use `find /path/to/search -mtime -n` where n is the number of days. For example, `-mtime -7` finds files modified in the last 7 days.

#### Q3. How do I find and delete files?
A. Use `find /path/to/search -name "pattern" -delete` or `find /path/to/search -name "pattern" -exec rm {} \;`

#### Q4. How can I exclude directories from my search?
A. Use `! -path "*/directory_to_exclude/*"` or `-not -path "*/directory_to_exclude/*"`

## References

https://www.gnu.org/software/findutils/manual/html_node/find_html/index.html

## Revisions

- 2025/05/04 First revision