# awk command

Pattern scanning and processing language for text files.

## Overview

`awk` is a powerful text processing tool that scans files line by line, splits each line into fields, and performs operations on those fields based on patterns and actions. It's particularly useful for extracting specific columns from structured text, generating reports, and transforming data. `awk` treats each line as a record and each word as a field, making it ideal for working with CSV files, logs, and other structured text data.

## Options

### **-F fs, --field-separator fs**

Specify the field separator (default is whitespace)

```console
$ echo "apple,orange,banana" | awk -F, '{print $2}'
orange
```

### **-f file, --file file**

Read the AWK program from a file instead of the command line

```console
$ cat script.awk
{print $1}
$ awk -f script.awk data.txt
[first field of each line in data.txt]
```

### **-v var=val, --assign var=val**

Assign a value to a variable before program execution begins

```console
$ awk -v name="John" '{print "Hello, " name "!"}'
Hello, John!
```

### **-W version, --version**

Display version information and exit

```console
$ awk --version
GNU Awk 5.1.0, API: 3.0 (GNU MPFR 4.1.0, GNU MP 6.2.1)
```

## Usage Examples

### Basic Field Printing

```console
$ echo "John Smith 42" | awk '{print $1, $2}'
John Smith
```

### Filtering Lines with Pattern Matching

```console
$ cat /etc/passwd | awk -F: '/root/ {print $1, $6}'
root /root
```

### Calculating Sums

```console
$ cat numbers.txt
10
20
30
$ awk '{sum += $1} END {print "Sum:", sum}' numbers.txt
Sum: 60
```

### Processing CSV Data

```console
$ cat data.csv
Name,Age,City
John,25,New York
Mary,30,Boston
$ awk -F, 'NR>1 {print "Name: " $1 ", Age: " $2}' data.csv
Name: John, Age: 25
Name: Mary, Age: 30
```

## Tips

### Built-in Variables

`awk` has several built-in variables: `NR` (current record number), `NF` (number of fields in current record), `FS` (field separator), and `OFS` (output field separator). Use them to simplify your scripts.

### Multiple Commands

Separate multiple commands with semicolons: `awk '{count++; sum+=$1} END {print "Average:", sum/count}'`

### Regular Expressions

`awk` supports powerful regular expressions for pattern matching: `awk '/^[0-9]+$/ {print "Number:", $0}'` matches lines containing only numbers.

### BEGIN and END Blocks

Use `BEGIN` for initialization and `END` for final processing: `awk 'BEGIN {print "Start"} {print $1} END {print "Done"}'`

## Frequently Asked Questions

#### Q1. How do I print specific columns from a file?
A. Use `awk '{print $n}'` where n is the column number. For example, `awk '{print $1, $3}'` prints the first and third columns.

#### Q2. How can I change the field separator?
A. Use the `-F` option: `awk -F, '{print $1}'` uses a comma as the field separator.

#### Q3. How do I perform calculations on numeric fields?
A. Use arithmetic operators: `awk '{sum+=$1} END {print sum}'` calculates the sum of the first column.

#### Q4. Can I use if-else statements in awk?
A. Yes, `awk` supports conditional statements: `awk '{if ($1 > 10) print "Large"; else print "Small"}'`

#### Q5. How do I process only certain lines?
A. Use patterns: `awk 'NR > 1 {print}'` skips the first line, or `awk '/pattern/ {print}'` processes only lines matching a pattern.

## References

https://www.gnu.org/software/gawk/manual/gawk.html

## Revisions

- 2025/05/04 First revision