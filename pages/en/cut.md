# cut command

Extract selected parts of lines from each FILE to standard output.

## Overview

The `cut` command extracts sections from each line of input files or standard input. It can select portions of text by character position, byte position, or delimiter-separated fields. This makes it useful for parsing and manipulating structured text data like CSV files or command outputs.

## Options

### **-f, --fields=LIST**

Select only the specified fields from each line, using a delimiter to identify fields.

```console
$ echo "name,age,city" | cut -f 1,3 -d ","
name,city
```

### **-d, --delimiter=DELIM**

Use DELIM as the field delimiter character instead of the default tab character.

```console
$ echo "name:age:city" | cut -f 2 -d ":"
age
```

### **-c, --characters=LIST**

Select only these characters from each line.

```console
$ echo "Hello World" | cut -c 1-5
Hello
```

### **-b, --bytes=LIST**

Select only these bytes from each line.

```console
$ echo "Hello World" | cut -b 1-5
Hello
```

### **--complement**

Complement the set of selected bytes, characters, or fields.

```console
$ echo "name,age,city" | cut -f 2 --complement -d ","
name,city
```

## Usage Examples

### Extract specific columns from CSV data

```console
$ cat data.csv
John,25,New York
Alice,30,Chicago
Bob,22,Los Angeles
$ cut -d "," -f 1,3 data.csv
John,New York
Alice,Chicago
Bob,Los Angeles
```

### Extract a range of characters from each line

```console
$ echo "The quick brown fox" | cut -c 5-9
quick
```

### Extract multiple ranges of characters

```console
$ echo "The quick brown fox" | cut -c 1-3,10-14
The brown
```

### Extract everything except a specific field

```console
$ echo "user:password:uid:gid:info:home:shell" | cut -d ":" -f 2 --complement
user:uid:gid:info:home:shell
```

## Tips:

### Handling Missing Delimiters

By default, `cut` outputs lines that don't contain the delimiter. Use `--output-delimiter` to specify what character to use in the output.

### Working with Fixed-Width Data

For data with fixed column widths (not delimiter-separated), use the `-c` option to extract specific character positions.

### Combining with Other Commands

`cut` works well in pipelines with commands like `grep`, `sort`, and `uniq` to filter and process text data.

### Handling Whitespace

When dealing with whitespace-delimited files, consider using `awk` instead, as `cut` only supports single-character delimiters.

## Frequently Asked Questions

#### Q1. What's the difference between `-c` and `-b`?
A. `-c` selects by character position, while `-b` selects by byte position. They behave differently with multi-byte characters (like in UTF-8).

#### Q2. Can I use multiple delimiters with `cut`?
A. No, `cut` only supports a single character as delimiter. For multiple delimiters, consider using tools like `awk` or `sed`.

#### Q3. How do I extract the last field when I don't know how many fields there are?
A. `cut` doesn't have a direct way to select the last field. Consider using `awk` for this purpose: `awk -F, '{print $NF}'`.

#### Q4. Can I change the output delimiter?
A. Yes, use the `--output-delimiter` option to specify a different output delimiter.

## References

https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html

## Revisions

- 2025/04/30 First revision