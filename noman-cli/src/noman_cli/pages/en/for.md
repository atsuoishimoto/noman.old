# for command

Executes a command or set of commands for each item in a list.

## Overview

The `for` command is a shell loop construct that iterates through a list of values, executing specified commands once for each value. It's commonly used in shell scripts for batch processing, automation, and repetitive tasks. The loop variable takes on each value in the list sequentially, allowing you to perform operations on multiple items with a single command structure.

## Options

The `for` command is a shell built-in and doesn't have traditional command-line options like standalone programs. Instead, it has different syntax variations:

### **Basic Syntax**

The standard form that iterates over a list of words.

```console
$ for i in one two three; do echo "Number: $i"; done
Number: one
Number: two
Number: three
```

### **C-style Syntax**

A C-like syntax available in bash and some other shells for numeric iterations.

```console
$ for ((i=1; i<=3; i++)); do echo "Count: $i"; done
Count: 1
Count: 2
Count: 3
```

## Usage Examples

### Iterating Over Files

```console
$ for file in *.txt; do echo "Processing $file"; cat "$file"; done
Processing notes.txt
This is the content of notes.txt
Processing readme.txt
This is the content of readme.txt
```

### Iterating Over Command Output

```console
$ for user in $(cut -d: -f1 /etc/passwd | head -3); do echo "User: $user"; done
User: root
User: daemon
User: bin
```

### Iterating Over a Range of Numbers

```console
$ for i in {1..5}; do echo "Number $i"; done
Number 1
Number 2
Number 3
Number 4
Number 5
```

### Iterating with Step Values

```console
$ for i in {0..10..2}; do echo "Even number: $i"; done
Even number: 0
Even number: 2
Even number: 4
Even number: 6
Even number: 8
Even number: 10
```

## Tips:

### Use Proper Quoting

Always quote variables within the loop to handle filenames or values with spaces correctly:

```console
$ for file in *.txt; do echo "Processing '$file'"; done
```

### Break and Continue

Use `break` to exit a loop early and `continue` to skip to the next iteration:

```console
$ for i in {1..10}; do
>   if [ $i -eq 5 ]; then continue; fi
>   if [ $i -eq 8 ]; then break; fi
>   echo $i
> done
1
2
3
4
6
7
```

### Nested Loops

You can nest `for` loops for more complex iterations:

```console
$ for i in {1..3}; do
>   for j in a b c; do
>     echo "$i-$j"
>   done
> done
1-a
1-b
1-c
2-a
2-b
2-c
3-a
3-b
3-c
```

## Frequently Asked Questions

#### Q1. How do I iterate over a range of numbers?
A. Use brace expansion: `for i in {1..10}; do echo $i; done` or C-style syntax: `for ((i=1; i<=10; i++)); do echo $i; done`.

#### Q2. How can I process each line of a file?
A. While `for` can be used, it's better to use a `while` loop with `read`: `while read line; do echo "$line"; done < file.txt`.

#### Q3. How do I iterate over array elements?
A. Use `for element in "${array[@]}"; do echo "$element"; done`.

#### Q4. Can I use `for` to iterate over command output?
A. Yes, use command substitution: `for item in $(command); do echo "$item"; done`.

#### Q5. How do I specify a step value in a numeric range?
A. Use extended brace expansion: `for i in {start..end..step}; do echo $i; done`.

## References

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## Revisions

- 2025/05/04 First revision