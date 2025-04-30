# sort command

Sorts lines of text files alphabetically or numerically.

## Overview

The `sort` command arranges lines in text files or from standard input in alphabetical, numerical, or custom-defined order. It's commonly used for organizing data, preparing input for other commands, and performing simple data analysis tasks.

## Options

### **-n (Numeric Sort)**

Sorts lines numerically instead of alphabetically

```console
$ cat numbers.txt
10
2
1
$ sort -n numbers.txt
1
2
10
```

### **-r (Reverse Sort)**

Reverses the sort order

```console
$ sort -r names.txt
Zack
Victor
Amy
```

### **-k (Sort by Field)**

Sorts based on a specific field (column) in the input

```console
$ cat employees.txt
John 35 Developer
Alice 28 Designer
Bob 42 Manager
$ sort -k2 -n employees.txt
Alice 28 Designer
John 35 Developer
Bob 42 Manager
```

### **-u (Unique)**

Removes duplicate lines from the output

```console
$ cat duplicates.txt
apple
banana
apple
orange
$ sort -u duplicates.txt
apple
banana
orange
```

### **-f (Ignore Case)**

Performs case-insensitive sorting

```console
$ cat mixed.txt
Apple
banana
Carrot
$ sort -f mixed.txt
Apple
banana
Carrot
```

## Usage Examples

### Sorting a File and Saving the Result

```console
$ sort names.txt > sorted_names.txt
$ cat sorted_names.txt
Amy
Victor
Zack
```

### Combining Multiple Files and Sorting

```console
$ sort file1.txt file2.txt
[combined and sorted output of both files]
```

### Sorting by Multiple Fields

```console
$ cat data.csv
John,35,1000
Alice,28,1200
Bob,42,900
$ sort -t, -k2n -k3nr data.csv
Alice,28,1200
John,35,1000
Bob,42,900
```

## Tips

### Pipe with Other Commands

Combine `sort` with other commands like `uniq` to count occurrences:

```console
$ cat log.txt | sort | uniq -c
      3 ERROR
     12 INFO
      5 WARNING
```

### Memory Usage for Large Files

For very large files, use the `-S` option to specify buffer size or `--parallel` to utilize multiple cores:

```console
$ sort --parallel=4 -S 1G huge_file.txt
```

### Stable Sort

Use `-s` for a stable sort when you want to preserve the original order of lines that would otherwise be considered equal:

```console
$ sort -s -k1,1 data.txt
```

## Frequently Asked Questions

#### Q1. How do I sort a CSV file by a specific column?
A. Use `-t` to specify the delimiter and `-k` for the column: `sort -t, -k2 file.csv` sorts by the second column.

#### Q2. How can I sort IP addresses correctly?
A. Use version sort: `sort -V iplist.txt` will properly sort IP addresses and version numbers.

#### Q3. How do I sort by month names instead of alphabetically?
A. Use the `--month-sort` option or create a custom ordering with the `-k` option and a carefully crafted key definition.

#### Q4. Can sort handle very large files?
A. Yes, `sort` is designed to handle files larger than available memory using temporary files and efficient algorithms.

## References

https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html

## Revisions

- 2025/04/30 First revision