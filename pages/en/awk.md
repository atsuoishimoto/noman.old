# awk command

Process text files line by line, applying pattern-matching and transformations.

## Overview

`awk` is a powerful text processing tool that treats each line of input as a record and each word as a field. It allows you to search for specific patterns in files and perform actions on matching lines. `awk` is particularly useful for extracting and manipulating structured data, generating reports, and transforming text files.

## Options

### **-F** (Field Separator)

Specifies the character or regular expression used to separate fields

```console
$ echo "apple,orange,banana" | awk -F, '{print $2}'
orange
```

### **-v** (Variable Assignment)

Assigns a value to an `awk` variable before processing begins

```console
$ awk -v name="John" '{print "Hello, " name "!"}'
Hello, John!
```

### **-f** (File)

Reads the `awk` program from a file instead of from the command line

```console
$ cat script.awk
{print $1}
$ echo "hello world" | awk -f script.awk
hello
```

## Usage Examples

### Basic Field Printing

```console
$ echo "John Smith 42" | awk '{print $1, $2}'
John Smith
```

### Pattern Matching

```console
$ cat /etc/passwd | awk -F: '/root/ {print $1, $6}'
root /root
```

### Calculations with Fields

```console
$ cat data.txt
Item1 10 5
Item2 15 3
Item3 20 8
$ awk '{print $1, $2 * $3}' data.txt
Item1 50
Item2 45
Item3 160
```

### Built-in Variables

```console
$ cat names.txt
Alice
Bob
Charlie
$ awk '{print NR ": " $1}' names.txt
1: Alice
2: Bob
3: Charlie
```

## Tips

### Understanding Field Variables

In `awk`, `$1` refers to the first field, `$2` to the second, and so on. `$0` represents the entire line. This makes extracting specific columns of data very straightforward.

### Using BEGIN and END Blocks

The `BEGIN` block executes before processing any input, and the `END` block executes after all input is processed. These are useful for initialization and summary operations:

```console
$ awk 'BEGIN {sum=0} {sum+=$1} END {print "Sum:", sum}' numbers.txt
Sum: 156
```

### Multiple Commands

Separate multiple commands with semicolons within the action block:

```console
$ awk '{count++; sum+=$1} END {print "Count:", count, "Average:", sum/count}' data.txt
Count: 10 Average: 15.6
```

## Frequently Asked Questions

#### Q1. What's the difference between `awk`, `sed`, and `grep`?
A. While `grep` searches for patterns, and `sed` performs text substitutions, `awk` is designed for structured data processing with fields and records, making it more powerful for complex text manipulation.

#### Q2. How do I use regular expressions in `awk`?
A. Regular expressions are placed between slashes: `awk '/pattern/ {action}'`. For example, `awk '/^[0-9]+/ {print $0}'` prints lines starting with numbers.

#### Q3. Can `awk` read from multiple files?
A. Yes, simply list the files after the `awk` command: `awk '{print $1}' file1.txt file2.txt`.

#### Q4. How do I format output in `awk`?
A. Use `printf` for formatted output: `awk '{printf "%-10s %5d\n", $1, $2}'` creates columns with specific widths.

## References

https://www.gnu.org/software/gawk/manual/gawk.html

## Revisions

- 2025/04/30 First revision