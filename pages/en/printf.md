# printf command

Format and print data according to a specified format string.

## Overview

The `printf` command formats and prints data to standard output according to a format specification. It works similarly to the C programming language's printf function, allowing precise control over output formatting including text alignment, number formatting, and string manipulation.

## Options

### **-v VAR**

Assign the output to shell variable VAR instead of displaying it on standard output.

```console
$ printf -v greeting "Hello, %s!" "World"
$ echo $greeting
Hello, World!
```

### **--help**

Display a help message and exit.

```console
$ printf --help
Usage: printf FORMAT [ARGUMENT]...
   or: printf OPTION
Print ARGUMENT(s) according to FORMAT, or execute according to OPTION:
...
```

### **--version**

Output version information and exit.

```console
$ printf --version
printf (GNU coreutils) 9.0
Copyright (C) 2021 Free Software Foundation, Inc.
...
```

## Format Specifiers

### **%s** - String

```console
$ printf "Name: %s\n" "John"
Name: John
```

### **%d** or **%i** - Integer

```console
$ printf "Number: %d\n" 42
Number: 42
```

### **%f** - Floating-point number

```console
$ printf "Price: $%.2f\n" 19.99
Price: $19.99
```

### **%c** - Character

```console
$ printf "First letter: %c\n" "A"
First letter: A
```

### **%x** or **%X** - Hexadecimal

```console
$ printf "Hex: 0x%x\n" 255
Hex: 0xff
$ printf "Hex: 0x%X\n" 255
Hex: 0xFF
```

## Usage Examples

### Basic Text Formatting

```console
$ printf "Hello, %s!\n" "World"
Hello, World!
```

### Multiple Arguments

```console
$ printf "%s is %d years old.\n" "Alice" 30
Alice is 30 years old.
```

### Width and Alignment

```console
$ printf "%-10s | %10s\n" "Left" "Right"
$ printf "%-10s | %10s\n" "aligned" "aligned"
Left       |      Right
aligned    |    aligned
```

### Number Formatting

```console
$ printf "Integer: %d, Float: %.2f, Hex: %x\n" 42 3.14159 255
Integer: 42, Float: 3.14, Hex: ff
```

### Repeating Format

```console
$ printf "%s\n" file1 file2 file3
file1
file2
file3
```

## Tips

### Escape Sequences

Use escape sequences like `\n` (newline), `\t` (tab), and `\\` (backslash) to format output:

```console
$ printf "Line 1\nLine 2\tTabbed\n"
Line 1
Line 2	Tabbed
```

### Padding Numbers with Zeros

Use format specifiers with width to pad numbers with zeros:

```console
$ printf "ID: %04d\n" 42
ID: 0042
```

### Printing Literal % Character

To print a literal % character, use %%:

```console
$ printf "Discount: 25%%\n"
Discount: 25%
```

### Format Reuse

The format string is reused for additional arguments:

```console
$ printf "User: %s\n" Alice Bob Charlie
User: Alice
User: Bob
User: Charlie
```

## Frequently Asked Questions

#### Q1. What's the difference between `printf` and `echo`?
A. `printf` offers more precise formatting control, while `echo` is simpler but less flexible. `printf` doesn't automatically add a newline, requires explicit `\n`, and supports format specifiers for data types.

#### Q2. How do I print a fixed number of decimal places?
A. Use the precision modifier with `%f`: `printf "%.2f" 3.14159` prints `3.14`.

#### Q3. How can I format a date with `printf`?
A. You can't directly format dates with `printf`. Use the `date` command to generate a formatted date string, then pass it to `printf`.

#### Q4. How do I print special characters like tabs or newlines?
A. Use escape sequences: `\t` for tab, `\n` for newline, `\r` for carriage return, and `\\` for backslash.

#### Q5. Can I use `printf` in shell scripts?
A. Yes, `printf` is commonly used in shell scripts for formatted output and variable assignment with the `-v` option.

## References

https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html

## Revisions

- 2025/05/04 First revision