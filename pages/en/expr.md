# expr command

Evaluate expressions and output the result.

## Overview

`expr` is a command-line utility that evaluates expressions and outputs the result. It performs arithmetic operations, string manipulations, and logical comparisons. The command is particularly useful in shell scripts for calculations and string handling.

## Options

### **Basic Arithmetic**

Performs addition, subtraction, multiplication, division, and modulo operations.

```console
$ expr 5 + 3
8
$ expr 10 - 4
6
$ expr 3 \* 4
12
$ expr 20 / 5
4
$ expr 17 % 5
2
```

Note: The multiplication operator (`*`) must be escaped with a backslash to prevent shell interpretation.

### **Comparison Operators**

Compares values and returns 1 for true or 0 for false.

```console
$ expr 5 \> 3
1
$ expr 5 \< 3
0
$ expr 5 = 5
1
$ expr 5 != 4
1
```

### **String Operations**

Manipulates and extracts information from strings.

```console
$ expr length "Hello"
5
$ expr substr "Hello World" 7 5
World
$ expr index "Hello World" "W"
7
```

### **Logical Operators**

Performs logical AND and OR operations.

```console
$ expr 5 \> 3 \& 10 \> 5
1
$ expr 5 \> 3 \| 2 \> 5
1
```

## Usage Examples

### Incrementing a Variable in a Shell Script

```console
$ count=1
$ count=$(expr $count + 1)
$ echo $count
2
```

### Extracting a Substring

```console
$ expr substr "Hello World" 1 5
Hello
```

### Checking String Length

```console
$ filename="document.txt"
$ length=$(expr length "$filename")
$ echo "The filename is $length characters long"
The filename is 12 characters long
```

## Tips:

### Use Proper Spacing

Always put spaces between operators and operands. `expr 5+3` will not work, but `expr 5 + 3` will.

### Escape Special Characters

Remember to escape characters that have special meaning to the shell, such as `*`, `(`, `)`, and `<`.

### Alternative to expr

Modern shell scripts often use bash's built-in arithmetic expansion `$(( ))` instead of `expr` for better performance and readability.

```console
$ echo $((5 + 3))
8
```

### Return Values

`expr` returns 0 if the expression evaluates to a non-zero and non-empty value, 1 if the expression is 0 or empty, and 2 if the expression is invalid.

## Frequently Asked Questions

#### Q1. Why does my multiplication with `expr` fail?
A. You need to escape the asterisk: `expr 5 \* 3`. Otherwise, the shell interprets it as a wildcard.

#### Q2. How do I use `expr` in a shell script?
A. Capture the output using command substitution: `result=$(expr 5 + 3)`.

#### Q3. Is there a limit to the size of numbers `expr` can handle?
A. Yes, `expr` typically handles integer arithmetic within the range of your system's integer limits.

#### Q4. Why use `expr` when bash has built-in arithmetic?
A. `expr` is primarily used for POSIX compatibility in scripts that need to run on various Unix-like systems.

## References

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/expr.html

## Revisions

- 2025/04/30 First revision