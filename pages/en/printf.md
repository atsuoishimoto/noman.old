# printf command

Format and print data according to a specified format string.

## Overview

The `printf` command formats and prints data to standard output according to a format specification. It works similarly to the C programming language's printf function, allowing precise control over output formatting including text alignment, number formatting, and string manipulation.

## Options

### **Format String**

The format string controls how subsequent arguments are converted for output. It contains text to be printed directly and conversion specifications that start with `%`.

```console
$ printf "Hello, %s!\n" "World"
Hello, World!
```

### **Escape Sequences**

Special characters can be represented using escape sequences.

```console
$ printf "Line 1\nLine 2\tTabbed\n"
Line 1
Line 2	Tabbed
```

## Usage Examples

### Basic Text Output

```console
$ printf "The current year is 2025.\n"
The current year is 2025.
```

### Formatting Numbers

```console
$ printf "Decimal: %d, Float: %0.2f\n" 42 3.14159
Decimal: 42, Float: 3.14
```

### Multiple Arguments

```console
$ printf "%s is %d years old.\n" "Alice" 30 "Bob" 25
Alice is 30 years old.
Bob is 25 years old.
```

### Field Width and Alignment

```console
$ printf "%-10s %5d\n" "Name" "Age" "Alice" 30 "Bob" 25
Name       Age
Alice        30
Bob          25
```

## Tips:

### Zero Padding Numbers

Use `%0Nd` format to pad numbers with leading zeros, where N is the total width.

```console
$ printf "ID: %04d\n" 42
ID: 0042
```

### Printing Percentages

To print a literal percent sign, use `%%` in the format string.

```console
$ printf "Progress: %d%%\n" 75
Progress: 75%
```

### Repeating Format Strings

If you provide more arguments than format specifiers, the format string will be reused for the remaining arguments.

```console
$ printf "-%s-\n" one two three
-one-
-two-
-three-
```

## Frequently Asked Questions

#### Q1. What's the difference between `printf` and `echo`?
A. `printf` offers more precise formatting control, while `echo` is simpler but less flexible. `printf` doesn't automatically add a newline, so you need to add `\n` explicitly.

#### Q2. How do I format a date with `printf`?
A. You can't directly format dates with `printf`. Use the `date` command to get a formatted date, then pass it to `printf` if needed.

#### Q3. How do I print floating-point numbers with specific precision?
A. Use `%.<precision>f` format, like `%.2f` for 2 decimal places.

#### Q4. Can I use `printf` in shell scripts?
A. Yes, `printf` is commonly used in shell scripts for formatted output and is available in most shells including bash, zsh, and sh.

## References

https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html

## Revisions

- 2025/04/30 First revision