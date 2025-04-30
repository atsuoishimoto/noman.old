# dpkg command

Manage Debian package files (.deb) on Debian-based Linux distributions.

## Overview

`dpkg` is the package management system for Debian-based Linux distributions (including Ubuntu). It handles the installation, removal, and providing information about .deb packages. Unlike higher-level package managers like `apt`, `dpkg` works directly with .deb files and doesn't automatically resolve dependencies.

## Options

### **-i, --install**

Install a package from a .deb file

```console
$ sudo dpkg -i package.deb
Selecting previously unselected package package.
(Reading database ... 200000 files and directories currently installed.)
Preparing to unpack package.deb ...
Unpacking package (1.0-1) ...
Setting up package (1.0-1) ...
```

### **-r, --remove**

Remove an installed package (keeps configuration files)

```console
$ sudo dpkg -r package
(Reading database ... 200000 files and directories currently installed.)
Removing package (1.0-1) ...
```

### **-P, --purge**

Remove an installed package completely (including configuration files)

```console
$ sudo dpkg -P package
(Reading database ... 200000 files and directories currently installed.)
Purging configuration files for package (1.0-1) ...
```

### **-l, --list**

List all installed packages with their status

```console
$ dpkg -l
| Status | Name      | Version      | Architecture | Description                |
|--------|-----------|--------------|--------------|----------------------------|
| ii     | bash      | 5.1-6ubuntu1 | amd64        | GNU Bourne Again SHell     |
| ii     | coreutils | 8.32-4.1     | amd64        | GNU core utilities         |
```

### **-s, --status**

Display detailed status information about a specific package

```console
$ dpkg -s bash
Package: bash
Status: install ok installed
Priority: required
Section: shells
Installed-Size: 6470
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Version: 5.1-6ubuntu1
```

### **-L, --listfiles**

List all files installed by a package

```console
$ dpkg -L bash
/.
/etc
/etc/bash.bashrc
/etc/skel
/etc/skel/.bash_logout
/etc/skel/.bashrc
/etc/skel/.profile
/bin
/bin/bash
...
```

## Usage Examples

### Installing a downloaded .deb package

```console
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
[output showing installation progress]
```

### Fixing broken dependencies after installation

```console
$ sudo apt-get install -f
Reading package lists... Done
Building dependency tree... Done
Correcting dependencies... Done
[output showing dependency resolution]
```

### Listing all installed packages matching a pattern

```console
$ dpkg -l | grep python
ii  python3                          3.10.4-0ubuntu2        amd64        Interactive high-level object-oriented language
ii  python3-minimal                  3.10.4-0ubuntu2        amd64        Minimal subset of the Python language
```

## Tips

### Handling Dependencies

`dpkg` doesn't automatically resolve dependencies. If you encounter dependency errors, run `sudo apt-get install -f` to fix them.

### Checking if a Package is Installed

Use `dpkg -l | grep package-name` to quickly check if a package is installed.

### Understanding Package Status Codes

In the output of `dpkg -l`, the first column shows status codes:
- `ii`: package is installed and configured
- `rc`: package was removed but config files remain
- `un`: package is unknown/not installed

### Backing Up Package List

Before major system changes, back up your package list with `dpkg --get-selections > packages.list`

## Frequently Asked Questions

#### Q1. What's the difference between `dpkg` and `apt`?
A. `dpkg` works directly with .deb files and doesn't handle dependencies automatically. `apt` is a higher-level tool that resolves dependencies and can download packages from repositories.

#### Q2. How do I fix "dependency problems" errors?
A. Run `sudo apt-get install -f` to fix dependency issues after a `dpkg` installation.

#### Q3. How can I see what files a package will install before installing it?
A. Use `dpkg-deb --contents package.deb` to view the contents of a .deb file before installation.

#### Q4. How do I reinstall a package?
A. Use `sudo dpkg -i --force-reinstall package.deb` to reinstall a package.

## References

https://man7.org/linux/man-pages/man1/dpkg.1.html

## Revisions

- 2025/04/30 First revision