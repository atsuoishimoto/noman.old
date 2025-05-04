# xdg-open command

Opens a file or URL in the user's preferred application.

## Overview

`xdg-open` is a desktop-independent tool that opens files or URLs using the default application registered for that file type or URL scheme. It's essentially the Linux equivalent of double-clicking a file in a graphical file manager, automatically selecting the appropriate application based on the file's MIME type.

## Options

### **--help**

Displays help information for the command.

```console
$ xdg-open --help
xdg-open - opens a file or URL in the user's preferred application

Synopsis

xdg-open { file | URL }

xdg-open { --help | --manual | --version }
```

### **--manual**

Displays the manual page for the command.

```console
$ xdg-open --manual
[displays detailed manual page]
```

### **--version**

Displays the version information.

```console
$ xdg-open --version
xdg-open 1.1.3
```

## Usage Examples

### Opening a file with the default application

```console
$ xdg-open document.pdf
[Opens the PDF file with the default PDF viewer]
```

### Opening a URL with the default web browser

```console
$ xdg-open https://www.example.com
[Opens the URL in the default web browser]
```

### Opening a directory with the file manager

```console
$ xdg-open ~/Documents
[Opens the Documents directory in the default file manager]
```

## Tips

### Silent Operation

`xdg-open` runs silently by default. If you want to see any error messages, you can redirect stderr:

```console
$ xdg-open nonexistent-file.txt 2>&1
```

### Using with Different File Types

`xdg-open` works with various file types including documents, images, videos, and directories. The application used depends on your desktop environment's file associations.

### Changing Default Applications

If `xdg-open` isn't opening files with your preferred application, you can change the default application using:
- GNOME: Settings → Apps → Default Apps
- KDE: System Settings → Applications → File Associations
- Or use `xdg-mime default application.desktop mimetype`

## Frequently Asked Questions

#### Q1. What's the difference between `xdg-open` and `open` on macOS?
A. `xdg-open` is the Linux equivalent of macOS's `open` command. They serve the same purpose but work on different operating systems.

#### Q2. Can I use `xdg-open` in scripts?
A. Yes, but be aware that it will launch graphical applications, which might not be suitable for all scripting contexts, especially in headless environments.

#### Q3. Why isn't `xdg-open` opening my file with the correct application?
A. This usually happens when the MIME type association is incorrect. You can fix this by updating your desktop environment's file associations.

#### Q4. Does `xdg-open` work in all Linux distributions?
A. `xdg-open` is part of the xdg-utils package, which is available in most Linux distributions. However, its behavior might vary slightly depending on the desktop environment.

## References

https://www.freedesktop.org/wiki/Software/xdg-utils/

## Revisions

- 2025/05/04 First revision