# while command

Execute commands repeatedly as long as a condition is true.

## Overview

The `while` command is a shell construct that creates a loop, executing a set of commands repeatedly as long as a specified condition evaluates to true. It's commonly used in shell scripts for tasks that need to be repeated until a certain condition is met, such as processing files line by line or implementing countdown timers.

## Options

The `while` command itself doesn't have options like standalone Unix commands. Instead, it's a shell control structure with a specific syntax:

```bash
while CONDITION; do
  COMMANDS
done
```

## Usage Examples

### Basic while loop with a counter

```console
$ i=1
$ while [ $i -le 5 ]; do
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
$ cat names.txt
Alice
Bob
Charlie
$ while read name; do
>   echo "Hello, $name!"
> done < names.txt
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

### Infinite loop with break condition

```console
$ i=1
$ while true; do
>   echo "Iteration $i"
>   if [ $i -eq 3 ]; then
>     echo "Breaking out of loop"
>     break
>   fi
>   i=$((i+1))
> done
Iteration 1
Iteration 2
Iteration 3
Breaking out of loop
```

### Waiting for a condition

```console
$ while [ ! -f /tmp/ready.txt ]; do
>   echo "Waiting for file to appear..."
>   sleep 1
> done
Waiting for file to appear...
Waiting for file to appear...
Waiting for file to appear...
```

## Tips

### Use `break` to Exit Early

The `break` command can be used inside a while loop to exit immediately, regardless of the condition:

```bash
while condition; do
  if [other_condition]; then
    break  # Exit the loop
  fi
  # commands
done
```

### Use `continue` to Skip Iterations

The `continue` command skips the rest of the current iteration and jumps back to the condition check:

```bash
while condition; do
  if [skip_condition]; then
    continue  # Skip to next iteration
  fi
  # commands that won't run if continue is executed
done
```

### Avoid Infinite Loops

Always ensure your while loop has a way to terminate. Include a condition that will eventually become false or use a `break` statement. If you accidentally create an infinite loop, press Ctrl+C to terminate it.

### Use `sleep` for Timed Loops

When polling for a condition, use the `sleep` command to prevent excessive CPU usage:

```bash
while [ condition ]; do
  # commands
  sleep 1  # Wait 1 second before checking again
done
```

## Frequently Asked Questions

#### Q1. What's the difference between `while` and `until`?
A. `while` executes commands as long as the condition is true, whereas `until` executes commands as long as the condition is false (until it becomes true).

#### Q2. How do I read a file line by line with a while loop?
A. Use `while read line; do commands; done < file.txt` to process each line of a file.

#### Q3. How can I create an infinite loop?
A. Use `while true; do commands; done` or `while :; do commands; done` to create an infinite loop. Remember to include a way to exit the loop (like a `break` statement).

#### Q4. Can I nest while loops?
A. Yes, you can nest while loops inside other while loops. Each loop needs its own `do` and `done` keywords.

#### Q5. How do I use while with command output?
A. You can pipe command output to a while loop: `command | while read line; do something; done`

## References

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## Revisions

2025/05/04 First revision