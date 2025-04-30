# [ command

Evaluates conditional expressions and returns a status based on the evaluation.

## Overview

The `[` command (also known as `test`) is used to check file types, compare strings, and evaluate arithmetic expressions. It's commonly used in shell scripts for conditional operations like `if` statements. The command returns a status of 0 (true) or 1 (false) based on the evaluation of the expression.

## Options

### **File Tests**

Tests for file properties and characteristics

```console
$ [ -f file.txt ] && echo "Regular file exists"
Regular file exists

$ [ -d /tmp ] && echo "Directory exists"
Directory exists
```

### **String Tests**

Compares strings or checks string properties

```console
$ [ "hello" = "hello" ] && echo "Strings are equal"
Strings are equal

$ [ -z "" ] && echo "String is empty"
String is empty
```

### **Integer Comparison**

Compares integer values

```console
$ [ 5 -eq 5 ] && echo "Numbers are equal"
Numbers are equal

$ [ 10 -gt 5 ] && echo "10 is greater than 5"
10 is greater than 5
```

## Usage Examples

### In if statements

```console
$ if [ -f /etc/passwd ]; then
>   echo "The passwd file exists"
> fi
The passwd file exists
```

### With logical operators

```console
$ [ -d /tmp ] && [ -w /tmp ] && echo "tmp directory exists and is writable"
tmp directory exists and is writable
```

### Checking command-line arguments

```console
$ [ $# -eq 0 ] && echo "No arguments provided"
No arguments provided
```

## Tips:

### Always Use Spaces

Always put spaces around the brackets and operators. `[ -f file.txt ]` works, but `[-f file.txt]` will fail.

### Remember the Closing Bracket

The `[` command requires a closing `]` at the end of the expression. Forgetting it will cause syntax errors.

### Use Double Brackets in Bash

In Bash scripts, consider using `[[` instead of `[` for more features and fewer quirks with string comparisons and pattern matching.

### Quote Variables

Always quote variables to prevent word splitting: `[ -f "$filename" ]` instead of `[ -f $filename ]`.

## Frequently Asked Questions

#### Q1. What's the difference between `[` and `test`?
A. They are functionally equivalent. `[` is just another name for the `test` command, but requires a closing `]` at the end.

#### Q2. Can I use `[` for mathematical operations?
A. It's limited to basic integer comparisons. For complex math, use `(( ))` in Bash or the `expr` command.

#### Q3. How do I check if a file doesn't exist?
A. Use the negation operator: `[ ! -f filename ]`

#### Q4. What's the difference between `[` and `[[`?
A. `[[` is a Bash-specific extension with more features like pattern matching and better handling of empty variables, while `[` is POSIX-compliant and works in all shells.

## References

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/test.html

## Revisions

- 2025/04/30 First revision