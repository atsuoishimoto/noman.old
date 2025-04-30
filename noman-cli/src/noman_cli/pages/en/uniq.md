# uniq command

Filter out or report adjacent duplicate lines from input.

## Overview

The `uniq` command examines adjacent lines in a file or standard input and removes or identifies duplicate lines. It's important to note that `uniq` only detects adjacent duplicate lines, so input is typically sorted first using the `sort` command.

## Options

### **-c (count)**

Prefixes lines with the number of occurrences

```console
$ sort names.txt | uniq -c
      2 Alice
      1 Bob
      3 Charlie
```

### **-d (duplicates only)**

Only prints duplicate lines (one copy of each)

```console
$ sort names.txt | uniq -d
Alice
Charlie
```

### **-u (unique only)**

Only prints lines that appear exactly once

```console
$ sort names.txt | uniq -u
Bob
```

### **-i (ignore case)**

Ignores differences in case when comparing lines

```console
$ cat case.txt
Hello
HELLO
hello
$ sort case.txt | uniq -i
hello
```

### **-f N (skip fields)**

Skips the first N fields before checking for uniqueness

```console
$ cat data.txt
1 Apple Red
2 Apple Red
$ uniq -f 1 data.txt
1 Apple Red
```

### **-s N (skip chars)**

Skips the first N characters before checking for uniqueness

```console
$ cat codes.txt
ABC123
ABD123
$ uniq -s 2 codes.txt
ABC123
```

## Usage Examples

### Basic usage with sort

```console
$ cat fruits.txt
apple
banana
apple
orange
banana
$ sort fruits.txt | uniq
apple
banana
orange
```

### Counting all occurrences

```console
$ cat fruits.txt
apple
banana
apple
orange
banana
$ sort fruits.txt | uniq -c
      2 apple
      2 banana
      1 orange
```

### Finding only unique entries

```console
$ sort fruits.txt | uniq -u
orange
```

## Tips:

### Always Sort First

Since `uniq` only works on adjacent duplicate lines, always pipe the output of `sort` to `uniq` unless you're certain the input is already sorted.

### Combine with Other Commands

`uniq` works well in pipelines with `sort`, `grep`, and `wc` for powerful text processing:

```console
$ sort log.txt | uniq -c | sort -nr
```
This sorts lines, counts occurrences, and sorts by frequency (most frequent first).

### Use -c for Frequency Analysis

The `-c` option is particularly useful for analyzing how often items appear in logs or datasets.

## Frequently Asked Questions

#### Q1. Why isn't `uniq` removing all duplicates from my file?
A. `uniq` only removes adjacent duplicate lines. You need to sort the file first: `sort file.txt | uniq`.

#### Q2. How can I count the number of unique lines in a file?
A. Use: `sort file.txt | uniq | wc -l`

#### Q3. How do I find the most common lines in a file?
A. Use: `sort file.txt | uniq -c | sort -nr`

#### Q4. Can `uniq` ignore specific parts of lines when comparing?
A. Yes, use `-f` to skip fields or `-s` to skip characters at the beginning of lines.

## References

https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html

## Revisions

- 2025/04/30 First revision