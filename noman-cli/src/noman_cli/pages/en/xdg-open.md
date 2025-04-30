# xdg-open command

Opens a file or URL in the user's preferred application.

## Overview

`xdg-open` is a command-line tool that opens files or URLs using the default application associated with the file type or URL protocol. It's essentially the Linux equivalent of double-clicking a file in a graphical file manager, letting the system decide which program to use based on the file's type.

## Options

### **--help**

Displays help information about the command.

```console
$ xdg-open --help
Usage: xdg-open [options] {file|URL}

xdg-open opens a file or URL in the user's preferred application.

Options:
  --help      Show this help message
  --manual    Show the manual page
  --version   Show the xdg-open version information
```

### **--version**

Shows the version information of xdg-open.

```console
$ xdg-open --version
xdg-open 1.1.3
```

### **--manual**

Displays the manual page for xdg-open.

```console
$ xdg-open --manual
[displays the full manual page]
```

## Usage Examples

### Opening a file with the default application

```console
$ xdg-open document.pdf
[opens the PDF file with the default PDF viewer]
```

### Opening a URL in the default web browser

```console
$ xdg-open https://www.example.com
[opens the URL in the default web browser]
```

### Opening a directory in the file manager

```console
$ xdg-open ~/Documents
[opens the Documents directory in the default file manager]
```

## Tips

### Use for Cross-Desktop Compatibility

`xdg-open` works across different Linux desktop environments (GNOME, KDE, XFCE, etc.), making it ideal for scripts that need to be desktop-agnostic.

### Redirect Output to Hide Messages

When using `xdg-open` in scripts, redirect output to `/dev/null` to hide any error messages:
```console
$ xdg-open file.txt > /dev/null 2>&1 &
```

### Run in Background

Add an ampersand (`&`) at the end of the command to run it in the background, allowing you to continue using the terminal:
```console
$ xdg-open https://example.com &
```

## Frequently Asked Questions

#### Q1. What is the macOS equivalent of xdg-open?
A. The macOS equivalent is the `open` command, which functions similarly.

#### Q2. How do I change the default application used by xdg-open?
A. Use `xdg-mime default application.desktop mimetype` to set the default application for a specific file type.

#### Q3. Why doesn't xdg-open work in my SSH session?
A. `xdg-open` requires a graphical environment. When connected via SSH, you need X11 forwarding enabled or a similar solution.

#### Q4. Can I use xdg-open in shell scripts?
A. Yes, it's commonly used in scripts to open files with their associated applications, but remember to handle its output and run it in the background if needed.

## References

https://www.freedesktop.org/wiki/Software/xdg-utils/

## Revisions

- 2025/04/30 First revision