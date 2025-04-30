# seq command

Print a sequence of numbers from FIRST to LAST by INCREMENT.

## Overview

The `seq` command generates a sequence of numbers from a starting value to an ending value, with an optional step size. It's commonly used in shell scripts for creating loops, generating test data, or producing numbered output.

## Options

### **-s, --separator=STRING**

Specify a string to separate numbers (default is newline)

```console
$ seq -s " " 1 5
1 2 3 4 5
```

### **-f, --format=FORMAT**

Use printf style floating-point FORMAT

```console
$ seq -f "Number %g" 1 3
Number 1
Number 2
Number 3
```

### **-w, --equal-width**

Equalize width by padding with leading zeros

```console
$ seq -w 8 10
08
09
10
```

## Usage Examples

### Basic sequence generation

```console
$ seq 5
1
2
3
4
5
```

### Specifying start and end values

```console
$ seq 3 7
3
4
5
6
7
```

### Using a custom increment

```console
$ seq 0 2 10
0
2
4
6
8
10
```

### Counting down

```console
$ seq 5 -1 1
5
4
3
2
1
```

## Tips:

### Use in Bash Loops

Combine `seq` with a for loop to iterate through a range of numbers:

```console
$ for i in $(seq 1 3); do echo "Processing item $i"; done
Processing item 1
Processing item 2
Processing item 3
```

### Create Numbered Files

Generate a series of numbered files quickly:

```console
$ for i in $(seq -w 1 5); do touch file$i.txt; done
$ ls file*.txt
file01.txt file02.txt file03.txt file04.txt file05.txt
```

### Save Memory with Ranges

For very large sequences, use `{start..end}` bash syntax instead of `seq` to avoid storing the entire sequence in memory:

```console
$ for i in {1..5}; do echo $i; done
1
2
3
4
5
```

## Frequently Asked Questions

#### Q1. What's the difference between `seq` and bash's `{start..end}` syntax?
A. While both generate sequences, `seq` offers more formatting options and can use floating-point numbers. Bash's built-in syntax is faster but more limited in features.

#### Q2. Can `seq` generate decimal numbers?
A. Yes, `seq` can handle decimal numbers for start, increment, and end values.

```console
$ seq 0.5 0.5 2.5
0.5
1.0
1.5
2.0
2.5
```

#### Q3. How can I use `seq` output in a command?
A. Use command substitution with `$(seq ...)` or backticks `` `seq ...` `` to use the output in another command.

## References

https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html

## Revisions

- 2025/04/30 First revision