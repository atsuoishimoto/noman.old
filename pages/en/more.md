# more command

Display file contents one screen at a time.

## Overview

The `more` command is a pager that allows you to view text files one screen at a time. It's particularly useful for viewing large files as it displays content page by page, allowing you to navigate through the file with simple keyboard commands. Unlike its more advanced counterpart `less`, `more` only allows forward navigation through files.

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

Disables screen clearing and control sequences that might interfere with some terminals.

```console
$ more -p script.sh
```

### **-c, --clean-print**

Redraws the screen instead of scrolling, providing a cleaner display.

```console
$ more -c document.txt
```

### **-s, --squeeze**

Squeezes multiple blank lines into one.

```console
$ more -s log_file.txt
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
This is file 1 content
--More--(50%)
```

### Starting at a Specific Pattern

```console
$ more +/important document.txt
Here is the important information you were looking for...
--More--(75%)
```

### Combining Options

```console
$ more -cs +10 large_log.txt
[Displays from line 10 with clean screen redraw and squeezed blank lines]
--More--(15%)
```

## Tips:

### Navigation Commands

While viewing a file with `more`, you can use these keyboard commands:
- `Space` - Move forward one screen
- `Enter` - Move forward one line
- `b` - Move back one screen (may not work in all implementations)
- `q` - Quit and exit
- `/pattern` - Search for a pattern
- `n` - Repeat the previous search

### Pipe Command Output

You can pipe the output of commands to `more` to view large outputs page by page:

```console
$ ls -la /usr/bin | more
```

### Environment Variable

Set the `MORE` environment variable to specify default options:

```console
$ export MORE="-d"
$ more large_file.txt
```

## Frequently Asked Questions

#### Q1. What's the difference between `more` and `less`?
A. `more` only allows forward navigation through a file, while `less` allows both forward and backward navigation and has more features. `less` is generally considered an improvement over `more` (hence the name).

#### Q2. How do I exit `more`?
A. Press the `q` key to quit and return to the command prompt.

#### Q3. Can I search for text in `more`?
A. Yes, press `/` followed by your search pattern and press Enter. Use `n` to find the next occurrence.

#### Q4. How can I display line numbers in `more`?
A. Unlike `less`, `more` doesn't have a built-in option to display line numbers. Consider using `less -N` instead if you need line numbers.

## macOS Considerations

On macOS, the `more` command is slightly different from the GNU/Linux version. Some options like `-d` might behave differently or not be available. For more consistent behavior across platforms, consider using `less` instead, which is more feature-rich and consistent across systems.

## References

https://man7.org/linux/man-pages/man1/more.1.html

## Revisions

- 2025/05/04 First revision