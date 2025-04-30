# continue command

Resume a suspended job by bringing it to the foreground.

## Overview

The `continue` command is used in shell scripts and programming to skip the rest of the current loop iteration and move to the next iteration. It's commonly used in loops like `for`, `while`, and `until` to bypass certain iterations based on specific conditions.

## Options

The `continue` command doesn't have options like traditional Unix commands. However, it can take a numeric argument to specify which loop level to continue.

### **continue (no argument)**

Skips the rest of the current iteration and starts the next iteration of the innermost loop.

```bash
for i in 1 2 3 4 5; do
  if [ $i -eq 3 ]; then
    continue
  fi
  echo "Processing item $i"
done
```

### **continue n**

Skips the rest of the current iteration and starts the next iteration of the nth enclosing loop.

```bash
for i in 1 2 3; do
  for j in a b c; do
    if [ $j = "b" ]; then
      continue 2  # Continues the outer loop (skips to next i)
    fi
    echo "Processing $i$j"
  done
done
```

## Usage Examples

### Basic continue in a loop

```console
$ for file in *.txt; do
>   if [ -s "$file" ]; then
>     echo "Processing $file"
>   else
>     echo "Skipping empty file $file"
>     continue
>   fi
>   # Further processing commands here
>   echo "Completed processing $file"
> done
Skipping empty file empty.txt
Processing document.txt
Completed processing document.txt
Processing notes.txt
Completed processing notes.txt
```

### Continue with nested loops

```console
$ for dir in */; do
>   echo "Entering directory $dir"
>   for file in "$dir"*.log; do
>     if [[ "$file" == *"error"* ]]; then
>       echo "Skipping error file: $file"
>       continue
>     fi
>     echo "Processing log file: $file"
>   done
> done
Entering directory logs/
Skipping error file: logs/error.log
Processing log file: logs/system.log
Processing log file: logs/access.log
Entering directory backups/
Processing log file: backups/backup.log
```

## Tips:

### Use with Caution in Complex Loops

When using `continue` in nested loops, be careful about which loop you're affecting. Without a numeric argument, `continue` only affects the innermost loop.

### Combine with Conditional Logic

`continue` is most useful when combined with `if` statements to create conditional processing within loops.

### Avoid Overuse

Excessive use of `continue` can make code harder to read. Consider restructuring your loop condition instead if you find yourself using `continue` frequently.

## Frequently Asked Questions

#### Q1. What's the difference between `continue` and `break`?
A. `continue` skips the rest of the current iteration and moves to the next iteration, while `break` exits the loop entirely.

#### Q2. Can I use `continue` outside of a loop?
A. No, using `continue` outside of a loop will result in a syntax error.

#### Q3. How do I continue multiple loop levels?
A. Use `continue n` where n is the number of loop levels you want to continue. For example, `continue 2` will continue the second-innermost loop.

#### Q4. Does `continue` work the same in all shells?
A. The basic functionality is the same across Bash, Zsh, and other common shells, but there might be subtle differences in behavior with complex scripts.

## References

https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#index-continue

## Revisions

- 2025/04/30 First revision