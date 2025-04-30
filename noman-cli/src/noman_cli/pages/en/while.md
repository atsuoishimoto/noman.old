# while command

Execute commands repeatedly as long as a condition is true.

## Overview

The `while` command is a shell construct that creates a loop, executing a set of commands repeatedly as long as a specified condition evaluates to true. It's commonly used for iterating a fixed number of times, processing input line by line, or running commands until a specific condition changes.

## Options

The `while` command doesn't have traditional command-line options as it's a shell construct rather than a standalone program. Instead, it uses a specific syntax structure.

### **Basic Syntax**

```bash
while [ condition ]
do
  # commands to execute
done
```

## Usage Examples

### Counting with a numeric condition

```console
$ i=1
$ while [ $i -le 5 ]
> do
>   echo "Count: $i"
>   i=$((i+1))
> done
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

### Reading file line by line

```console
$ while read line
> do
>   echo "Line: $line"
> done < file.txt
Line: This is the first line
Line: This is the second line
Line: This is the third line
```

### Running until a condition changes

```console
$ while [ ! -f stop_file.txt ]
> do
>   echo "Waiting for stop file to appear..."
>   sleep 5
> done
Waiting for stop file to appear...
Waiting for stop file to appear...
Waiting for stop file to appear...
```

### Infinite loop with break

```console
$ i=1
$ while true
> do
>   echo "Iteration: $i"
>   if [ $i -eq 3 ]; then
>     echo "Breaking out of loop"
>     break
>   fi
>   i=$((i+1))
> done
Iteration: 1
Iteration: 2
Iteration: 3
Breaking out of loop
```

## Tips

### Use Control-C to Exit Infinite Loops

If your `while` loop becomes stuck in an infinite loop, press Control-C to interrupt and terminate the execution.

### Check Your Condition Carefully

Ensure your condition will eventually become false, or use a `break` statement to exit the loop, otherwise you'll create an infinite loop.

### Use the `continue` Statement

The `continue` statement skips the rest of the current iteration and jumps to the next iteration, useful for filtering or skipping certain cases.

### Combine with Command Substitution

You can use command substitution to process command output in a loop:
```bash
while read line; do echo "Processing: $line"; done < <(ls -1)
```

## Frequently Asked Questions

#### Q1. What's the difference between `while` and `for` loops?
A. `while` loops continue as long as a condition is true, making them suitable for situations where the number of iterations isn't known in advance. `for` loops typically iterate over a predefined list of items.

#### Q2. How do I create an infinite loop?
A. Use `while true` or `while :` to create an infinite loop. Make sure to include a way to exit the loop (like a `break` statement) to avoid having to forcibly terminate it.

#### Q3. How can I read a file line by line?
A. Use `while read line; do commands; done < file.txt` to process each line of a file.

#### Q4. Can I use `while` to wait for a condition?
A. Yes, `while` is often used to wait for conditions like file existence or process completion. For example: `while [ ! -f file.txt ]; do sleep 1; done`

## References

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## Revisions

- 2025/04/30 First revision