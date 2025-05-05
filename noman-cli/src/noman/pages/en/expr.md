# expr command

Evaluate expressions and output the result.

## Overview

`expr` is a command-line utility that evaluates expressions and outputs the result. It performs arithmetic operations, string manipulations, and logical comparisons. The command is primarily used in shell scripts to perform calculations and string operations that would be difficult to accomplish with shell built-ins alone.

## Options

### **--help**

Display a help message and exit.

```console
$ expr --help
Usage: expr EXPRESSION
  or:  expr OPTION
Print the value of EXPRESSION to standard output.
...
```

### **--version**

Output version information and exit.

```console
$ expr --version
expr (GNU coreutils) 9.0
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

## Usage Examples

### Basic Arithmetic

```console
$ expr 5 + 3
8
$ expr 10 - 4
6
$ expr 3 \* 4
12
$ expr 20 / 5
4
$ expr 20 % 3
2
```

### String Operations

```console
$ expr length "Hello World"
11
$ expr substr "Hello World" 7 5
World
$ expr index "Hello World" "W"
7
```

### Logical Comparisons

```console
$ expr 5 \> 3
1
$ expr 5 \< 3
0
$ expr 5 = 5
1
$ expr 5 != 5
0
```

### Use in Shell Scripts

```console
$ a=5
$ b=3
$ c=$(expr $a + $b)
$ echo $c
8
```

## Tips:

### Escape Special Characters

Always escape multiplication (*), division (/), and other characters that have special meaning in the shell using a backslash (\).

```console
$ expr 5 \* 3
15
```

### Space Requirements

`expr` requires spaces between operators and operands. Without spaces, the command will not work correctly.

```console
$ expr 5+3    # Wrong
5+3
$ expr 5 + 3  # Correct
8
```

### Return Values

`expr` returns 0 if the expression evaluates to a non-zero and non-empty value, 1 if the expression is zero or empty, and 2 if the expression is invalid.

### Use for Incrementing Variables

A common use of `expr` is to increment counters in shell scripts:

```console
$ i=1
$ i=$(expr $i + 1)
$ echo $i
2
```

## Frequently Asked Questions

#### Q1. What's the difference between `expr` and shell arithmetic?
A. While modern shells support arithmetic with `$(( ))`, `expr` is more portable across different shells and provides additional string manipulation functions.

#### Q2. Why does my multiplication with `expr` fail?
A. You need to escape the asterisk with a backslash: `expr 5 \* 3`. Otherwise, the shell interprets it as a wildcard.

#### Q3. How can I use `expr` for string operations?
A. `expr` provides functions like `length`, `substr`, and `index` for string manipulation. For example: `expr length "string"` or `expr substr "string" 1 3`.

#### Q4. Is `expr` still relevant in modern shell scripting?
A. While newer shells have built-in arithmetic capabilities, `expr` remains useful for its string manipulation functions and for scripts that need to be portable across different shell environments.

## References

https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html

## Revisions

- 2025/05/04 First revision