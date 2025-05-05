# eval command

Construct and execute commands from arguments.

## Overview

The `eval` command evaluates and executes arguments as a shell command. It combines its arguments into a single string, then executes that string as a command in the current shell environment. This is particularly useful for constructing commands dynamically or executing commands stored in variables.

## Options

The `eval` command itself doesn't have specific options, as it simply takes arguments and executes them as shell commands. Any options provided are passed to the command being evaluated.

## Usage Examples

### Basic Usage

```console
$ eval "echo Hello, World!"
Hello, World!
```

### Using Variables in Commands

```console
$ command="ls -la"
$ eval $command
total 32
drwxr-xr-x  5 user  staff   160 May  4 10:23 .
drwxr-xr-x  3 user  staff    96 May  4 10:20 ..
-rw-r--r--  1 user  staff  1024 May  4 10:22 file1.txt
-rw-r--r--  1 user  staff  2048 May  4 10:23 file2.txt
drwxr-xr-x  2 user  staff    64 May  4 10:21 directory
```

### Dynamic Command Construction

```console
$ file="document.txt"
$ action="cat"
$ eval "$action $file"
This is the content of document.txt
```

### Command with Multiple Arguments

```console
$ options="-l -a"
$ directory="/tmp"
$ eval "ls $options $directory"
total 16
drwxrwxrwt  5 root  wheel   160 May  4 10:30 .
drwxr-xr-x 20 root  wheel   640 May  4 09:15 ..
-rw-r--r--  1 user  wheel  1024 May  4 10:25 temp1.txt
drwxr-xr-x  2 user  wheel    64 May  4 10:28 tempdir
```

## Tips

### Use Quotes Carefully

Always quote your variables when using them with `eval` to prevent word splitting and unexpected behavior:

```console
$ filename="my file.txt"
$ eval "echo $filename"    # Incorrect: will be interpreted as "my" and "file.txt"
my file.txt
$ eval "echo \"$filename\""  # Correct: preserves the space
my file.txt
```

### Security Considerations

Be extremely cautious when using `eval` with user input or untrusted data, as it can lead to command injection vulnerabilities. Avoid using `eval` when simpler alternatives exist.

### Debugging Eval Commands

To see what command `eval` will execute without actually running it, use `echo` first:

```console
$ cmd="ls -la /tmp"
$ echo "$cmd"
ls -la /tmp
$ eval "$cmd"
[output of ls -la /tmp]
```

## Frequently Asked Questions

#### Q1. When should I use `eval`?
A. Use `eval` when you need to construct and execute commands dynamically, especially when the command structure is stored in variables or generated at runtime.

#### Q2. Why is `eval` considered dangerous?
A. `eval` executes its arguments as shell commands, which can lead to security vulnerabilities if those arguments contain untrusted input. This could allow command injection attacks.

#### Q3. Are there alternatives to using `eval`?
A. Yes, depending on your use case. For simple variable expansion, parameter substitution is often sufficient. For more complex cases, consider using functions, arrays, or command substitution instead.

#### Q4. How does `eval` handle errors?
A. `eval` returns the exit status of the last command executed. If the command string is syntactically incorrect, it will return a non-zero exit status.

## References

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/eval.html

## Revisions

- 2025/05/04 First revision