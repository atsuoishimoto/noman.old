# yes command

Repeatedly output a string until interrupted.

## Overview

The `yes` command continuously outputs a string (by default "y") until it is terminated. It's primarily used to automatically respond to prompts in scripts or commands that require confirmation.

## Options

### **Default (no options)**

Outputs "y" repeatedly until interrupted with Ctrl+C.

```console
$ yes
y
y
y
y
[continues until interrupted]
```

### **Custom string**

Outputs the specified string repeatedly until interrupted.

```console
$ yes "I agree"
I agree
I agree
I agree
[continues until interrupted]
```

## Usage Examples

### Automatically confirming prompts

```console
$ yes | rm -i *.txt
```
This automatically answers "y" to all confirmation prompts when removing text files.

### Creating a test file of repeated content

```console
$ yes "test data" | head -n 100 > testfile.txt
```
This creates a file with "test data" repeated 100 times.

### Stress testing

```console
$ yes > /dev/null
```
This can be used as a simple CPU stress test as it generates continuous output.

## Tips

### Terminating the Command

Always remember to use Ctrl+C to terminate the `yes` command, as it will run indefinitely otherwise.

### Piping with Caution

When piping `yes` to other commands, ensure the receiving command will eventually terminate on its own, or you'll need to manually interrupt the process.

### Resource Usage

The `yes` command can consume significant CPU resources when running for extended periods, as it continuously generates output.

## Frequently Asked Questions

#### Q1. What is the purpose of the `yes` command?
A. The primary purpose is to automatically respond "y" (or a custom string) to commands that require interactive confirmation.

#### Q2. How do I stop the `yes` command?
A. Press Ctrl+C to terminate the command.

#### Q3. Can I use `yes` with multiple words?
A. Yes, just enclose the phrase in quotes: `yes "multiple words here"`.

#### Q4. Does `yes` consume a lot of system resources?
A. It can consume significant CPU if left running, as it continuously generates output.

## References

https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html

## Revisions

- 2025/04/30 First revision