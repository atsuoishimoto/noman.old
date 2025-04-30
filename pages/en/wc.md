# wc command

Count lines, words, and bytes in files.

## Overview

The `wc` (word count) command counts the number of lines, words, and bytes in files. It's commonly used to get statistics about text files or to count specific elements in command output when combined with pipes.

## Options

### **-l (lines)**

Counts only the number of lines in each file

```console
$ wc -l document.txt
      42 document.txt
```

### **-w (words)**

Counts only the number of words in each file

```console
$ wc -w document.txt
     320 document.txt
```

### **-c (bytes)**

Counts only the number of bytes in each file

```console
$ wc -c document.txt
    1850 document.txt
```

### **-m (characters)**

Counts only the number of characters in each file (may differ from bytes in multi-byte character encodings)

```console
$ wc -m document.txt
    1842 document.txt
```

## Usage Examples

### Counting multiple files at once

```console
$ wc *.txt
      42     320    1850 document.txt
      15      98     520 notes.txt
      10      45     280 readme.txt
      67     463    2650 total
```

### Using wc with pipes

```console
$ ls -l | wc -l
      25
```

### Combining options

```console
$ wc -lw document.txt
      42     320 document.txt
```

## Tips:

### Quick Line Count for Multiple Files

Use `wc -l *` to quickly count lines in all files in the current directory. This is useful for comparing file sizes or checking how many entries are in log files.

### Counting Specific Patterns

Combine `wc` with `grep` to count specific patterns: `grep "error" logfile.txt | wc -l` counts how many lines contain "error".

### Default Behavior

When run without options, `wc` displays line count, word count, and byte count in that order. Remember this sequence to interpret the output correctly.

## Frequently Asked Questions

#### Q1. What's the difference between `-c` and `-m` options?
A. `-c` counts bytes while `-m` counts characters. They differ when working with multi-byte character encodings like UTF-8, where a single character might use multiple bytes.

#### Q2. How can I count only the total number of lines across multiple files?
A. Use `wc -l file1 file2 file3` and look at the "total" line, or pipe multiple files: `cat file1 file2 file3 | wc -l`.

#### Q3. Why does `wc -l` sometimes show a different count than the number of lines I see in a text editor?
A. `wc` counts newline characters. If the last line of a file doesn't end with a newline, `wc` might show one fewer line than you expect.

#### Q4. How can I count words in a string without creating a file?
A. Use echo with a pipe: `echo "your text here" | wc -w`

## References

https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html

## Revisions

- 2025/04/30 First revision