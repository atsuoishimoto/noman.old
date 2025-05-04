# seq command

Print a sequence of numbers from FIRST to LAST by INCREMENT steps.

## Overview

The `seq` command generates a sequence of numbers from a starting value to an ending value, with an optional step increment. It's commonly used in shell scripts for creating loops, generating test data, or producing evenly spaced numerical sequences.

## Options

### **-f, --format=FORMAT**

Use printf-style floating-point FORMAT to print each number

```console
$ seq -f "Number: %.2f" 1 3
Number: 1.00
Number: 2.00
Number: 3.00
```

### **-s, --separator=STRING**

Use STRING to separate numbers (default is newline)

```console
$ seq -s ", " 1 5
1, 2, 3, 4, 5
```

### **-w, --equal-width**

Equalize width by padding with leading zeros

```console
$ seq -w 8 10
08
09
10
```

### **-t, --terminator=CHAR**

Use CHAR as output terminator instead of newline

```console
$ seq -t " " 1 3
1 2 3 
```

## Usage Examples

### Basic Usage

```console
$ seq 5
1
2
3
4
5
```

### Specifying Start, Increment, and End

```console
$ seq 2 2 10
2
4
6
8
10
```

### Using Negative Numbers

```console
$ seq 5 -1 1
5
4
3
2
1
```

### Creating a Range for Loops

```console
$ for i in $(seq 1 3); do echo "Processing item $i"; done
Processing item 1
Processing item 2
Processing item 3
```

## Tips:

### Use with xargs for Parallel Processing

Combine `seq` with `xargs` to process multiple tasks in parallel:

```console
$ seq 1 10 | xargs -P 4 -I{} echo "Processing job {}"
```

### Generate File Names with Leading Zeros

Create sequentially numbered files with consistent width:

```console
$ for i in $(seq -w 1 5); do touch file_$i.txt; done
$ ls
file_01.txt file_02.txt file_03.txt file_04.txt file_05.txt
```

### Use Floating Point Numbers

`seq` supports decimal numbers for more precise sequences:

```console
$ seq 0.5 0.5 2.5
0.5
1.0
1.5
2.0
2.5
```

## Frequently Asked Questions

#### Q1. How do I create a sequence with a specific increment?
A. Use the format `seq START INCREMENT END`. For example, `seq 0 0.5 2` creates a sequence from 0 to 2 with 0.5 increments.

#### Q2. Can seq handle negative numbers?
A. Yes, `seq` can work with negative numbers for start, increment, and end values. For example, `seq 5 -1 1` counts down from 5 to 1.

#### Q3. How do I prevent seq from printing each number on a new line?
A. Use the `-s` option to specify a separator: `seq -s ", " 1 5` outputs "1, 2, 3, 4, 5".

#### Q4. Can seq format numbers with leading zeros?
A. Yes, use the `-w` option: `seq -w 8 12` outputs "08", "09", "10", "11", "12".

## References

https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html

## Revisions

- 2025/05/04 First revision