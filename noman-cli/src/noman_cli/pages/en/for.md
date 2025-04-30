# for command

Execute a command for each item in a list.

## Overview

The `for` loop is a shell construct that iterates through a list of values, executing a command or set of commands once for each value. It's commonly used for batch processing files, iterating through command output, or performing repetitive tasks with different inputs.

## Options

The `for` loop isn't a command with traditional options, but rather a shell construct with different syntax variations.

### **Basic Syntax**

The standard syntax for a `for` loop:

```bash
for variable in list
do
    commands
done
```

### **C-style Syntax**

Bash also supports C-style for loops:

```bash
for ((initialization; condition; increment))
do
    commands
done
```

## Usage Examples

### Iterating through a list of values

```console
$ for fruit in apple banana orange
> do
>     echo "I like $fruit"
> done
I like apple
I like banana
I like orange
```

### Processing files in a directory

```console
$ for file in *.txt
> do
>     echo "Processing $file..."
>     wc -l "$file"
> done
Processing notes.txt...
      45 notes.txt
Processing report.txt...
      127 report.txt
```

### Using C-style for loop to count

```console
$ for ((i=1; i<=5; i++))
> do
>     echo "Count: $i"
> done
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

### Iterating through command output

```console
$ for user in $(cut -d: -f1 /etc/passwd | head -5)
> do
>     echo "User: $user"
> done
User: root
User: daemon
User: bin
User: sys
User: sync
```

## Tips:

### Use Proper Quoting

Always quote variables inside the loop to handle filenames with spaces or special characters:

```console
$ for file in *.txt
> do
>     cp "$file" "/backup/folder/"
> done
```

### One-line Syntax

For simple loops, you can use a one-line syntax:

```console
$ for i in {1..5}; do echo "Number $i"; done
Number 1
Number 2
Number 3
Number 4
Number 5
```

### Sequence Generation

Use brace expansion for numeric sequences:

```console
$ for i in {1..5}; do echo $i; done    # Simple sequence
$ for i in {10..50..10}; do echo $i; done  # With step value (10, 20, 30, 40, 50)
```

### Breaking and Continuing

Use `break` to exit a loop early and `continue` to skip to the next iteration.

## Frequently Asked Questions

#### Q1. How do I loop through numbers in a range?
A. Use brace expansion: `for i in {1..10}; do echo $i; done` or C-style: `for ((i=1; i<=10; i++)); do echo $i; done`

#### Q2. How do I loop through files in a directory?
A. Use wildcards: `for file in /path/to/dir/*; do echo "$file"; done`

#### Q3. How do I loop through lines in a file?
A. Use a while loop with read: `while read line; do echo "$line"; done < file.txt`

#### Q4. How do I loop through command output?
A. Use command substitution: `for item in $(command); do echo "$item"; done`

#### Q5. How can I use a for loop with arrays?
A. Use the array syntax: `for item in "${my_array[@]}"; do echo "$item"; done`

## References

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## Revisions

- 2025/04/30 First revision