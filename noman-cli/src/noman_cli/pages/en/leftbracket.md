# [ command

Evaluates conditional expressions and returns a status based on the evaluation result.

## Overview

The `[` command (also known as `test`) is a shell builtin that evaluates conditional expressions and returns a status of 0 (true) or 1 (false). It's commonly used in shell scripts for conditional testing of file attributes, string comparisons, and arithmetic operations. The command requires a closing `]` to complete its syntax.

## Options

### **File Tests**

Tests for file properties and attributes

```console
$ [ -f /etc/passwd ] && echo "Regular file exists"
Regular file exists
```

### **String Tests**

Compares strings or checks string properties

```console
$ name="John"
$ [ "$name" = "John" ] && echo "Names match"
Names match
```

### **Integer Tests**

Compares integer values

```console
$ age=25
$ [ $age -gt 18 ] && echo "Adult"
Adult
```

## Usage Examples

### Testing if a file exists

```console
$ [ -e /etc/hosts ] && echo "File exists" || echo "File does not exist"
File exists
```

### Checking if a directory is writable

```console
$ [ -w /tmp ] && echo "Directory is writable" || echo "Directory is not writable"
Directory is writable
```

### Comparing string values in an if statement

```console
$ fruit="apple"
$ if [ "$fruit" = "apple" ]; then
>   echo "It's an apple"
> else
>   echo "It's not an apple"
> fi
It's an apple
```

## Common File Test Operators

| Operator | Description |
|----------|-------------|
| `-e file` | True if file exists |
| `-f file` | True if file is a regular file |
| `-d file` | True if file is a directory |
| `-r file` | True if file is readable |
| `-w file` | True if file is writable |
| `-x file` | True if file is executable |
| `-s file` | True if file exists and has size greater than zero |

## Common String Test Operators

| Operator | Description |
|----------|-------------|
| `-z string` | True if string length is zero |
| `-n string` | True if string length is non-zero |
| `string1 = string2` | True if strings are equal |
| `string1 != string2` | True if strings are not equal |

## Common Integer Comparison Operators

| Operator | Description |
|----------|-------------|
| `int1 -eq int2` | True if integers are equal |
| `int1 -ne int2` | True if integers are not equal |
| `int1 -lt int2` | True if int1 is less than int2 |
| `int1 -le int2` | True if int1 is less than or equal to int2 |
| `int1 -gt int2` | True if int1 is greater than int2 |
| `int1 -ge int2` | True if int1 is greater than or equal to int2 |

## Tips

### Always Quote Variables
Always quote variables in test expressions to prevent word splitting and globbing issues:
```console
$ [ "$variable" = "value" ]  # Correct
```

### Use Double Brackets When Possible
In Bash, consider using `[[` instead of `[` for more advanced features and fewer surprises:
```console
$ [[ $string =~ ^[0-9]+$ ]] && echo "Numeric"
```

### Remember the Spaces
The `[` command requires spaces after the opening bracket and before the closing bracket:
```console
$ [ -f file.txt ]  # Correct
$ [-f file.txt]    # Incorrect - will fail
```

## Frequently Asked Questions

#### Q1. What's the difference between `[` and `[[`?
A. `[` is a command (also known as `test`) available in all POSIX shells, while `[[` is a shell keyword in Bash and other modern shells that offers extended functionality like pattern matching and logical operators.

#### Q2. Why do I need spaces around the brackets?
A. The `[` is actually a command (like `ls` or `grep`), so it needs spaces to separate it from its arguments. The closing `]` is its final argument.

#### Q3. How do I test multiple conditions?
A. Use `-a` (AND) or `-o` (OR) operators:
```console
$ [ -f file.txt -a -r file.txt ] && echo "File exists and is readable"
```
With `[[`, you can use `&&` and `||` instead.

## References

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/test.html

## Revisions

- 2025/05/04 First revision