# wc command

Count lines, words, and bytes in files.

## Overview

The `wc` (word count) command counts the number of lines, words, and bytes in specified files. It's commonly used to get statistics about text files, check file sizes, or count specific elements in text data. By default, it displays line count, word count, and byte count for each file, followed by the filename.

## Options

### **-c, --bytes**

Count bytes in the file.

```console
$ wc -c file.txt
    1234 file.txt
```

### **-m, --chars**

Count characters in the file.

```console
$ wc -m file.txt
    1234 file.txt
```

### **-l, --lines**

Count lines in the file.

```console
$ wc -l file.txt
     100 file.txt
```

### **-w, --words**

Count words in the file.

```console
$ wc -w file.txt
     234 file.txt
```

### **-L, --max-line-length**

Display the length of the longest line.

```console
$ wc -L file.txt
      80 file.txt
```

## Usage Examples

### Default output (lines, words, bytes)

```console
$ wc file.txt
     100     234    1234 file.txt
```

### Counting lines in multiple files

```console
$ wc -l file1.txt file2.txt
     100 file1.txt
     150 file2.txt
     250 total
```

### Using with pipes to count output from other commands

```console
$ ls -l | wc -l
      12
```

### Counting words in all text files in a directory

```console
$ wc -w *.txt
     234 file1.txt
     345 file2.txt
     579 total
```

## Tips

### Count Non-Empty Lines

To count only non-empty lines, you can combine `grep` with `wc`:

```console
$ grep -c . file.txt
```

### Quick File Size Check

Use `wc -c` for a quick check of file size in bytes, which is faster than using `ls -l` when you only need the size.

### Count Specific Patterns

Combine with `grep` to count specific patterns:

```console
$ grep "error" logfile.txt | wc -l
```

### Handling Large Files

For very large files, `wc` is efficient as it streams the file rather than loading it entirely into memory.

## Frequently Asked Questions

#### Q1. What does the output of `wc` mean?
A. The default output shows three numbers followed by the filename: line count, word count, and byte count.

#### Q2. How do I count only the number of lines in a file?
A. Use `wc -l filename`.

#### Q3. Can I count characters instead of bytes?
A. Yes, use `wc -m filename` to count characters, which may differ from bytes in UTF-8 encoded files.

#### Q4. How do I count words in text from standard input?
A. Pipe the text to `wc -w`, for example: `echo "hello world" | wc -w`.

#### Q5. Why might line counts from `wc -l` and `grep -c` differ?
A. `wc -l` counts all newlines, while `grep -c` without options counts matching lines. Empty lines affect this difference.

## References

https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html

## Revisions

- 2025/05/04 First revision