# cut command

Extract selected parts of lines from each FILE to standard output.

## Overview

The `cut` command is used to extract sections from each line of input files or standard input. It can cut by character position, byte position, or delimiter-separated fields. This is particularly useful for processing structured text files like CSV or TSV files, or for extracting specific columns from command output.

## Options

### **-b, --bytes=LIST**

Extract specific bytes from each line

```console
$ echo "Hello" | cut -b 1-3
Hel
```

### **-c, --characters=LIST**

Extract specific characters from each line

```console
$ echo "Hello World" | cut -c 1-5
Hello
```

### **-d, --delimiter=DELIM**

Use DELIM as the field delimiter character instead of the default tab

```console
$ echo "name,age,city" | cut -d, -f2
age
```

### **-f, --fields=LIST**

Select only the specified fields on each line

```console
$ echo "name:age:city" | cut -d: -f1,3
name:city
```

### **-s, --only-delimited**

Do not print lines not containing delimiters

```console
$ printf "field1,field2,field3\nno delimiter line\nother,fields,here\n" | cut -d, -f1 -s
field1
other
```

### **--complement**

Complement the set of selected bytes, characters, or fields

```console
$ echo "field1,field2,field3" | cut -d, -f1 --complement
field2,field3
```

### **--output-delimiter=STRING**

Use STRING as the output delimiter instead of the input delimiter

```console
$ echo "field1,field2,field3" | cut -d, -f1,3 --output-delimiter=" | "
field1 | field3
```

## Usage Examples

### Extract specific columns from CSV file

```console
$ cat data.csv
name,age,city,country
John,25,New York,USA
Alice,30,London,UK
$ cut -d, -f1,3 data.csv
name,city
John,New York
Alice,London
```

### Extract characters from fixed-width data

```console
$ cat fixed.txt
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
$ cut -c 5-10 fixed.txt
EFGHIJ
efghij
```

### Process command output

```console
$ ps | cut -c 1-5,27-
  PID COMMAND
    1 /sbin/init
  123 bash
  456 ps
```

## Tips:

### Specify Ranges in LIST

When specifying character or field positions, you can use:
- N: The Nth position
- N-: From the Nth position to the end
- N-M: From the Nth to the Mth position
- -M: From the beginning to the Mth position

### Combine with Other Commands

`cut` works well in pipelines with other commands like `grep`, `sort`, and `uniq` to process and filter text data.

### Handle Missing Delimiters

By default, `cut` outputs the entire line if it doesn't contain the delimiter. Use `-s` to suppress these lines if needed.

### Working with Multi-byte Characters

Be careful when using `-c` with multi-byte characters (like UTF-8). For these cases, consider using `-b` with the appropriate byte ranges.

## Frequently Asked Questions

#### Q1. What's the difference between `-c` and `-b`?
A. `-c` selects by character positions, while `-b` selects by byte positions. They behave differently with multi-byte characters (like in UTF-8 encoding).

#### Q2. How do I extract multiple fields?
A. Use comma-separated values with the `-f` option, like `cut -f1,3,5`.

#### Q3. Can I change the output delimiter?
A. Yes, use `--output-delimiter=STRING` to specify a different output delimiter.

#### Q4. How do I extract everything except certain fields?
A. Use the `--complement` option along with `-f` to select all fields except those specified.

#### Q5. Why doesn't cut work with variable-width fields?
A. `cut` is designed for fixed-width fields or delimiter-separated fields. For variable-width processing, consider using `awk` instead.

## References

https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html

## Revisions

- 2025/05/04 First revision