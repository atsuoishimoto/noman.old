# more command

Display file contents one screen at a time.

## Overview

The `more` command is a pager that allows you to view text files one screen at a time. It's particularly useful for examining large files without overwhelming your terminal with text. Unlike its more advanced counterpart `less`, `more` only allows forward navigation through a file.

## Options

### **-d (--display-help)**

Displays a help prompt at the bottom of the screen with basic navigation commands.

```console
$ more -d large_file.txt
[file content appears]
--More--(56%) [Press space to continue, 'q' to quit, 'd' to display help]
```

### **-f (--force)**

Forces `more` to open non-regular files (like directories or device files).

```console
$ more -f /dev/null
[displays content if any]
```

### **-p (--clean-print)**

Clears the screen before displaying each page.

```console
$ more -p large_file.txt
[screen clears and shows first page]
```

### **-s (--squeeze)**

Squeezes multiple blank lines into a single blank line.

```console
$ more -s file_with_many_blanks.txt
[file content with compressed blank lines]
```

### **-number (--lines)**

Specifies the number of lines to display per screen.

```console
$ more -10 large_file.txt
[displays 10 lines at a time]
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

### Combining Options

```console
$ more -ds large_log_file.log
[displays content with squeezed blank lines and help prompt]
--More--(15%) [Press space to continue, 'q' to quit, 'd' to display help]
```

### Viewing Multiple Files

```console
$ more file1.txt file2.txt
::::::::::::::
file1.txt
::::::::::::::
[content of file1.txt]
--More--(75%)
```

## Tips

### Navigation Commands

While viewing a file with `more`, you can use these keyboard shortcuts:
- `Space` or `f`: Move forward one screen
- `Enter`: Move forward one line
- `b`: Move back one screen (may not work in all implementations)
- `q` or `Q`: Quit
- `/pattern`: Search for "pattern" in the file
- `n`: Repeat the previous search

### Using with Pipes

`more` works well with command output piping, making it useful for viewing lengthy command results:

```console
$ ls -la /usr/bin | more
```

### Setting Default Options

You can set default options for `more` by defining the `MORE` environment variable:

```console
$ export MORE="-d"
```

## Frequently Asked Questions

#### Q1. What's the difference between `more` and `less`?
A. `more` only allows forward navigation through a file, while `less` allows both forward and backward movement and has more features. The saying goes: "less is more than more."

#### Q2. How do I search for text in `more`?
A. Type `/` followed by your search pattern and press Enter. Use `n` to find the next occurrence.

#### Q3. How do I exit `more`?
A. Press `q` or `Q` to quit.

#### Q4. Can I customize how many lines `more` displays?
A. Yes, use the `-number` option (e.g., `more -20 file.txt` to display 20 lines at a time).

## macOS Considerations

On macOS, the `more` command is slightly different from the GNU/Linux version. It doesn't support all the same options, and some behaviors may differ. For example, the `-d` option might not work as expected. If you need more advanced features, consider installing GNU coreutils via Homebrew and using `gmore` instead, or simply use the `less` command which is more feature-rich and available by default.

## References

https://www.gnu.org/software/coreutils/manual/html_node/more-invocation.html

## Revisions

- 2025/04/30 First revision