# yes command

Repeatedly outputs a string until interrupted.

## Overview

The `yes` command continuously outputs a string (by default "y") followed by a newline until it is terminated. It's primarily used to automatically respond to command prompts that require confirmation, allowing scripts to run without manual intervention.

## Options

### **-V, --version**

Display version information and exit.

```console
$ yes --version
yes (GNU coreutils) 9.0
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by David MacKenzie.
```

### **--help**

Display help information and exit.

```console
$ yes --help
Usage: yes [STRING]...
  or:  yes OPTION
Repeatedly output a line with all specified STRING(s), or 'y'.

      --help     display this help and exit
      --version  output version information and exit
```

## Usage Examples

### Default behavior (outputting "y")

```console
$ yes
y
y
y
y
[continues until interrupted with Ctrl+C]
```

### Outputting a custom string

```console
$ yes "I agree"
I agree
I agree
I agree
[continues until interrupted with Ctrl+C]
```

### Automatically answering prompts in scripts

```console
$ yes | rm -i *.txt
rm: remove regular file 'file1.txt'? rm: remove regular file 'file2.txt'?
```

### Providing multiple inputs to a command

```console
$ yes n y | rm -i file1.txt file2.txt
rm: remove regular file 'file1.txt'? rm: remove regular file 'file2.txt'?
```

## Tips

### Stopping the Command

Always remember that `yes` runs indefinitely until you stop it with Ctrl+C. Forgetting to terminate it can consume system resources unnecessarily.

### Limiting Output

If you need to limit the number of outputs, pipe `yes` to `head`:

```console
$ yes | head -n 5
y
y
y
y
y
```

### Performance Testing

The `yes` command can be used for simple performance testing or generating load on a system, as it produces output at maximum speed.

### Caution with Destructive Commands

Be careful when using `yes` with destructive commands like `rm -rf`. Always test with a safe command first to ensure the behavior is as expected.

## Frequently Asked Questions

#### Q1. What is the purpose of the `yes` command?
A. The primary purpose is to automatically respond to interactive prompts in scripts, typically answering "y" to confirmation questions.

#### Q2. How do I stop the `yes` command?
A. Press Ctrl+C to terminate the command.

#### Q3. Can I make `yes` output something other than "y"?
A. Yes, simply provide your desired string as an argument: `yes "custom text"`.

#### Q4. Is there a way to limit how many times `yes` outputs its string?
A. The command itself doesn't have this option, but you can pipe it to `head` with the `-n` option: `yes | head -n 10`.

#### Q5. Does `yes` consume a lot of system resources?
A. It can consume significant CPU resources as it generates output as fast as possible. Always terminate it when no longer needed.

## References

https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html

## Revisions

- 2025/05/04 First revision