# more command

Display file contents one screen at a time.

## Overview

The `more` command is a pager that allows you to view text files one screen at a time. It's particularly useful for examining large files without overwhelming your terminal with text. Unlike its more advanced counterpart `less`, `more` only allows forward navigation through a file.

## Options

### **-d, --silent**

Displays helpful prompts and provides more user-friendly error messages.

```console
$ more -d large_file.txt
--More--(50%) [Press space to continue, 'q' to quit.]
```

### **-f, --logical**

Counts logical lines rather than screen lines (doesn't wrap long lines).

```console
$ more -f wide_content.txt
```

### **-p, --plain**

Disables screen clearing and displays text without processing special characters.

```console
$ more -p script.sh
```

### **-c, --clean-print**

Draws each page by scrolling from the bottom of the screen, providing a cleaner display.

```console
$ more -c document.txt
```

### **-s, --squeeze**

Squeezes multiple blank lines into a single blank line.

```console
$ more -s log_with_gaps.txt
```

### **-u, --plain**

Suppresses underlining and other formatting.

```console
$ more -u formatted_text.txt
```

### **-number**

Specifies the number of lines to display on each screen.

```console
$ more -10 short_file.txt
```

### **+number**

Starts displaying the file at the specified line number.

```console
$ more +100 large_file.txt
```

### **+/pattern**

Starts displaying at the first line containing the specified pattern.

```console
$ more +/ERROR log_file.txt
```

## Usage Examples

### Basic Usage

```console
$ more /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
--More--(28%)
```

### Viewing Multiple Files

```console
$ more file1.txt file2.txt
::::::::::::::
file1.txt
::::::::::::::
This is the content of file1.txt
--More--(75%)
```

### Combining Options

```console
$ more -cs +/important document.txt
[displays from the first occurrence of "important" with clean screen and squeezed blank lines]
```

### Using with Pipes

```console
$ ls -la | more
total 112
drwxr-xr-x  15 user  staff   480 May  4 10:23 .
drwxr-xr-x   5 user  staff   160 Apr 29 09:15 ..
-rw-r--r--   1 user  staff  8196 May  3 14:22 file1.txt
--More--(42%)
```

## Tips

### Navigation Commands

While viewing a file with `more`, you can use these keyboard commands:
- `Space` or `f`: Move forward one screen
- `Enter`: Move forward one line
- `b`: Move back one screen (may not work in all implementations)
- `q` or `Q`: Quit
- `/pattern`: Search for a pattern
- `n`: Repeat the previous search

### Using with Large Files

When examining very large files, `more` loads the file as you view it, making it more memory-efficient than loading the entire file at once.

### Alternative to `more`

Consider using `less` instead of `more` for more advanced features like backward navigation and better search capabilities. The `less` command was designed as an improvement over `more` with the tagline "less is more".

## Frequently Asked Questions

#### Q1. What's the difference between `more` and `less`?
A. `more` only allows forward navigation through a file, while `less` allows both forward and backward navigation and has more advanced features.

#### Q2. How do I exit from `more`?
A. Press `q` or `Q` to exit.

#### Q3. Can I search for text in `more`?
A. Yes, press `/` followed by your search pattern, then press Enter. Use `n` to find the next occurrence.

#### Q4. How can I display line numbers in `more`?
A. Unlike `less`, `more` doesn't have a built-in option to display line numbers.

#### Q5. Why does `more` sometimes clear my screen?
A. By default, `more` clears the screen before displaying each page. Use the `-p` option to prevent this behavior.

## References

https://man7.org/linux/man-pages/man1/more.1.html

## Revisions

- 2025/05/04 First revision