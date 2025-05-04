# xdg-mime command

Query and set file type associations in desktop environments.

## Overview

`xdg-mime` is a command-line tool that helps manage file type associations in Linux desktop environments. It allows users to query which application is associated with a specific file type (MIME type), set default applications for file types, and add new MIME type information to the system.

## Options

### **query default [mimetype]**

Queries the default application for a specific MIME type.

```console
$ xdg-mime query default text/plain
gedit.desktop
```

### **query filetype [file]**

Determines the MIME type of a file.

```console
$ xdg-mime query filetype document.pdf
application/pdf
```

### **default [application.desktop] [mimetype(s)]**

Sets the default application for one or more MIME types.

```console
$ xdg-mime default firefox.desktop text/html
```

### **install [--mode mode] [--novendor] mimetypes-file**

Installs new MIME type information from a file.

```console
$ xdg-mime install --mode user myapplication-mime.xml
```

## Usage Examples

### Finding which application opens PDF files

```console
$ xdg-mime query default application/pdf
evince.desktop
```

### Setting Firefox as the default browser

```console
$ xdg-mime default firefox.desktop x-scheme-handler/http x-scheme-handler/https
```

### Checking the MIME type of a file

```console
$ xdg-mime query filetype myimage.jpg
image/jpeg
```

### Setting a different text editor for text files

```console
$ xdg-mime default code.desktop text/plain
```

## Tips:

### Desktop Entry Files Location

Desktop entry files (`.desktop`) are typically located in `/usr/share/applications/` or `~/.local/share/applications/`. You need to reference these files when setting default applications.

### System-wide vs. User-specific Settings

Use `--mode system` to make system-wide changes (requires root privileges) or `--mode user` (default) for user-specific settings.

### Finding Available Desktop Files

To see available desktop files for setting defaults, you can list them with:
```console
$ ls /usr/share/applications/*.desktop
```

### MIME Type Reference

Common MIME types include `text/plain` for text files, `application/pdf` for PDFs, `image/jpeg` for JPEG images, and `video/mp4` for MP4 videos.

## Frequently Asked Questions

#### Q1. How do I find out what application will open a specific file?
A. Use `xdg-mime query default $(xdg-mime query filetype filename)` to first determine the file's MIME type and then query which application is associated with it.

#### Q2. How do I reset file associations to system defaults?
A. There's no direct reset command in xdg-mime. You would need to delete the relevant entries in `~/.config/mimeapps.list` or set them to the desired defaults manually.

#### Q3. Why isn't my new file association working?
A. Some desktop environments cache MIME associations. Try logging out and back in, or restart the file manager. Also ensure the `.desktop` file exists and is properly formatted.

#### Q4. Can I associate multiple applications with one file type?
A. `xdg-mime` only sets the default application. Alternative applications can be configured through your desktop environment's file properties dialog.

## References

https://portland.freedesktop.org/doc/xdg-mime.html

## Revisions

- 2025/05/04 First revision