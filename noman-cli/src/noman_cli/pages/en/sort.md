# sort command

Sort lines of text files alphabetically or numerically.

## Overview

The `sort` command arranges lines in text files or from standard input in alphabetical, numerical, or custom-defined order. It can merge multiple sorted files, remove duplicate lines, and perform various other sorting operations. This utility is commonly used in data processing pipelines and for organizing text-based information.

## Options

### **-n, --numeric-sort**

Sort numerically instead of alphabetically. Recognizes numbers at the start of fields.

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

### **-r, --reverse**

Reverse the result of comparisons, sorting in descending order.

```console
$ sort -r fruits.txt
watermelon
orange
banana
apple
```

### **-k, --key=POS1[,POS2]**

Sort based on a specific field (column) in the input.

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

### **-t, --field-separator=SEP**

Specify a field separator character (default is whitespace).

```console
$ cat data.csv
name,age,role
John,35,Developer
Alice,28,Designer
Bob,42,Manager
$ sort -t, -k2 -n data.csv
name,age,role
Alice,28,Designer
John,35,Developer
Bob,42,Manager
```

### **-u, --unique**

Output only the first of an equal run (remove duplicates).

```console
$ cat duplicates.txt
apple
banana
apple
orange
banana
$ sort -u duplicates.txt
apple
banana
orange
```

### **-f, --ignore-case**

Ignore case when sorting alphabetically.

```console
$ cat mixed-case.txt
Apple
banana
Carrot
apple
$ sort -f mixed-case.txt
Apple
apple
banana
Carrot
```

### **-h, --human-numeric-sort**

Compare human-readable numbers (e.g., 2K, 1M).

```console
$ cat sizes.txt
1K
5M
10G
2K
$ sort -h sizes.txt
1K
2K
5M
10G
```

## Usage Examples

### Sorting a file and saving the output

```console
$ sort names.txt > sorted_names.txt
```

### Merging multiple sorted files

```console
$ sort -m sorted1.txt sorted2.txt > merged.txt
```

### Sorting by multiple fields

```console
$ cat data.txt
John Smith 35 Developer
Alice Johnson 28 Designer
Bob Williams 42 Manager
$ sort -k4,4 -k1,1 data.txt
Alice Johnson 28 Designer
John Smith 35 Developer
Bob Williams 42 Manager
```

### Finding unique values in a column

```console
$ cat logs.txt | cut -d' ' -f3 | sort -u
ERROR
INFO
WARNING
```

## Tips

### Stable Sort

Use `sort -s` for a stable sort, which preserves the original order of lines with equal sort keys. This is useful when sorting by multiple criteria in sequence.

### Memory Usage

For very large files, use `sort -S` to specify memory buffer size or `sort -T` to specify a temporary directory with more space. For example: `sort -S 1G -T /tmp bigfile.txt`.

### Check If Already Sorted

Use `sort -c` to check if a file is already sorted without producing any output. The exit status will indicate if the file is sorted (0) or not (1).

### Random Sort

Use `sort -R` to randomize the order of lines, which is useful for selecting random samples from data.

## Frequently Asked Questions

#### Q1. How do I sort a file numerically?
A. Use `sort -n filename` to sort numerically instead of alphabetically.

#### Q2. How can I sort by a specific column?
A. Use `sort -k COLUMN_NUMBER filename`. For example, `sort -k 2 filename` sorts by the second column.

#### Q3. How do I remove duplicate lines while sorting?
A. Use `sort -u filename` to output only unique lines.

#### Q4. How can I sort in reverse order?
A. Use `sort -r filename` to sort in descending order.

#### Q5. How do I sort a CSV file by a specific column?
A. Use `sort -t, -k COLUMN_NUMBER filename.csv` where `-t,` specifies the comma as the field separator.

## References

https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html

## Revisions

- 2025/05/04 First revision