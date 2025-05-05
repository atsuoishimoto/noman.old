# uniq command

Filter out or report adjacent duplicate lines from input.

## Overview

The `uniq` command processes text input and filters out or identifies repeated lines that appear consecutively. It requires sorted input to work properly, as it only compares adjacent lines. Commonly used with the `sort` command, `uniq` helps eliminate duplicates or count how many times each line appears in a file.

## Options

### **-c, --count**

Prefix lines with the number of occurrences

```console
$ cat names.txt
Alice
Bob
Bob
Charlie
Charlie
Charlie
$ sort names.txt | uniq -c
      1 Alice
      2 Bob
      3 Charlie
```

### **-d, --repeated**

Only print duplicate lines, one for each group

```console
$ cat names.txt
Alice
Bob
Bob
Charlie
Charlie
Charlie
$ sort names.txt | uniq -d
Bob
Charlie
```

### **-u, --unique**

Only print unique lines (not duplicated in input)

```console
$ cat names.txt
Alice
Bob
Bob
Charlie
Charlie
Charlie
$ sort names.txt | uniq -u
Alice
```

### **-i, --ignore-case**

Ignore differences in case when comparing lines

```console
$ cat mixed-case.txt
apple
Apple
banana
BANANA
$ sort mixed-case.txt | uniq -i
apple
banana
```

### **-f N, --skip-fields=N**

Skip comparing the first N fields

```console
$ cat data.txt
1 John Smith
1 Jane Doe
2 John Smith
$ uniq -f 1 data.txt
1 John Smith
1 Jane Doe
2 John Smith
```

### **-s N, --skip-chars=N**

Skip comparing the first N characters

```console
$ cat codes.txt
ABC123
ABC456
DEF123
$ uniq -s 3 codes.txt
ABC123
DEF123
```

## Usage Examples

### Counting unique words in a file

```console
$ cat words.txt
hello
world
hello
computer
world
$ sort words.txt | uniq -c
      1 computer
      2 hello
      2 world
```

### Finding only unique entries

```console
$ cat log.txt
ERROR: Connection failed
INFO: Starting application
ERROR: Connection failed
INFO: Application ready
$ sort log.txt | uniq -u
INFO: Application ready
INFO: Starting application
```

### Combining with other commands in a pipeline

```console
$ cat access.log | grep "404" | cut -d' ' -f1 | sort | uniq -c
     15 192.168.1.5
      3 192.168.1.7
     22 192.168.1.10
```

## Tips:

### Always Sort First

The `uniq` command only detects adjacent duplicate lines, so always use `sort` before `uniq` to ensure all duplicates are detected:

```console
$ sort file.txt | uniq
```

### Count Occurrences of All Lines

To see how many times each unique line appears in a file, use:

```console
$ sort file.txt | uniq -c | sort -nr
```
This sorts by frequency (most frequent first).

### Finding Non-Unique Lines

To find only lines that appear more than once:

```console
$ sort file.txt | uniq -d
```

## Frequently Asked Questions

#### Q1. Why doesn't `uniq` remove all duplicates in my file?
A. `uniq` only removes adjacent duplicate lines. You must sort the file first with `sort file.txt | uniq`.

#### Q2. How can I count the number of unique lines in a file?
A. Use `sort file.txt | uniq | wc -l` to count unique lines.

#### Q3. Can `uniq` ignore specific parts of lines when comparing?
A. Yes, use `-f N` to skip N fields or `-s N` to skip N characters at the beginning of each line.

#### Q4. How do I find the most common lines in a file?
A. Use `sort file.txt | uniq -c | sort -nr` to list lines by frequency (most frequent first).

## References

https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html

## Revisions

- 2025/05/04 First revision