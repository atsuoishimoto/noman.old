# xdg-mime command

Query or modify MIME type associations in desktop environments.

## Overview

`xdg-mime` is a command-line tool for managing MIME type associations on Linux systems. It allows users to query which application is set to open a specific file type, set default applications for file types, and add new MIME type information to the system.

## Options

### **query default**

Determines which application is registered to open a specific MIME type

```console
$ xdg-mime query default text/plain
org.gnome.gedit.desktop
```

### **query filetype**

Determines the MIME type of a file

```console
$ xdg-mime query filetype document.pdf
application/pdf
```

### **default**

Sets the default application for a specific MIME type

```console
$ xdg-mime default firefox.desktop text/html
```

### **install**

Installs new MIME type information from an XML file

```console
$ xdg-mime install myapp-mime.xml
```

## Usage Examples

### Finding which application opens PDF files

```console
$ xdg-mime query default application/pdf
org.gnome.evince.desktop
```

### Setting Firefox as the default browser

```console
$ xdg-mime default firefox.desktop x-scheme-handler/http
$ xdg-mime default firefox.desktop x-scheme-handler/https
```

### Checking the MIME type of a file

```console
$ xdg-mime query filetype ~/Downloads/presentation.pptx
application/vnd.openxmlformats-officedocument.presentationml.presentation
```

## Tips:

### Use with Desktop Files

When setting default applications, you need to use the .desktop file name (like `firefox.desktop`), not just the application name. These files are typically located in `/usr/share/applications/`.

### Finding MIME Types

If you're unsure about a MIME type, use `xdg-mime query filetype` on an example file to determine the correct MIME type string.

### System vs. User Configuration

`xdg-mime` modifies user preferences by default. System-wide changes require root privileges and may involve editing files in `/usr/share/applications/`.

## Frequently Asked Questions

#### Q1. What is a MIME type?
A. MIME (Multipurpose Internet Mail Extensions) types identify file formats and content types. For example, `text/plain` for text files or `image/jpeg` for JPEG images.

#### Q2. How do I reset file associations to system defaults?
A. There's no direct command in `xdg-mime` to reset associations. You can remove user overrides by deleting entries in `~/.config/mimeapps.list`.

#### Q3. Why isn't my new default application being used?
A. Some desktop environments cache MIME associations. Try logging out and back in, or restart the file manager.

#### Q4. Can I associate multiple file types at once?
A. No, you need to run the `xdg-mime default` command separately for each MIME type.

## References

https://portland.freedesktop.org/doc/xdg-mime.html

## Revisions

- 2025/04/30 First revision