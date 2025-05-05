# dpkg command

Manage Debian package files (.deb) on Debian-based systems like Ubuntu.

## Overview

`dpkg` is the package management system for Debian-based Linux distributions. It handles the installation, removal, and providing information about .deb packages. Unlike higher-level package managers like `apt`, `dpkg` works directly with .deb files and doesn't automatically resolve dependencies.

## Options

### **-i, --install**

Install a package from a .deb file

```console
$ sudo dpkg -i firefox_115.0+build2-0ubuntu0.20.04.1_amd64.deb
Selecting previously unselected package firefox.
(Reading database ... 186342 files and directories currently installed.)
Preparing to unpack firefox_115.0+build2-0ubuntu0.20.04.1_amd64.deb ...
Unpacking firefox (115.0+build2-0ubuntu0.20.04.1) ...
Setting up firefox (115.0+build2-0ubuntu0.20.04.1) ...
Processing triggers for mime-support (3.64ubuntu1) ...
```

### **-r, --remove**

Remove an installed package (keeps configuration files)

```console
$ sudo dpkg -r firefox
(Reading database ... 186342 files and directories currently installed.)
Removing firefox (115.0+build2-0ubuntu0.20.04.1) ...
```

### **-P, --purge**

Remove an installed package completely (including configuration files)

```console
$ sudo dpkg -P firefox
(Reading database ... 186342 files and directories currently installed.)
Removing firefox (115.0+build2-0ubuntu0.20.04.1) ...
Purging configuration files for firefox ...
```

### **-l, --list [pattern]**

List installed packages matching an optional pattern

```console
$ dpkg -l firefox
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version      Architecture Description
+++-==============-============-============-=================================
ii  firefox        115.0+build2 amd64        Safe and easy web browser from Mozilla
```

### **-L, --listfiles**

List files installed by a package

```console
$ dpkg -L firefox
/.
/usr
/usr/bin
/usr/bin/firefox
/usr/lib
/usr/lib/firefox
...
```

### **-s, --status**

Display detailed status information about a package

```console
$ dpkg -s firefox
Package: firefox
Status: install ok installed
Priority: optional
Section: web
Installed-Size: 256348
Maintainer: Ubuntu Mozilla Team <ubuntu-mozillateam@lists.ubuntu.com>
Architecture: amd64
Version: 115.0+build2-0ubuntu0.20.04.1
Depends: lsb-release, libatk1.0-0 (>= 1.12.4), libc6 (>= 2.28), ...
Description: Safe and easy web browser from Mozilla
 Firefox delivers safe, easy web browsing. A familiar user interface,
 enhanced security features including protection from online identity theft,
 and integrated search let you get the most out of the web.
```

### **-S, --search**

Search for packages that own a specific file

```console
$ dpkg -S /usr/bin/firefox
firefox: /usr/bin/firefox
```

### **--configure**

Configure an unpacked package that needs setup

```console
$ sudo dpkg --configure firefox
Setting up firefox (115.0+build2-0ubuntu0.20.04.1) ...
```

## Usage Examples

### Installing a package and fixing dependencies

```console
$ sudo dpkg -i package.deb
$ sudo apt-get install -f
```

### Listing all installed packages

```console
$ dpkg -l
```

### Finding which package a file belongs to

```console
$ dpkg -S /usr/bin/python3
python3-minimal: /usr/bin/python3
```

## Tips

### Fix Broken Dependencies

When `dpkg` fails due to missing dependencies, run `sudo apt-get install -f` to resolve them. This is a common workflow when installing .deb files directly.

### Backup Package List

Before major system changes, save a list of installed packages with `dpkg --get-selections > packages.list`. You can later restore with `sudo dpkg --set-selections < packages.list && sudo apt-get dselect-upgrade`.

### Verify Package Integrity

Use `dpkg-deb --info package.deb` to inspect a package before installation, and `dpkg -V packagename` to verify installed files against the package database.

### Reconfigure Packages

If you need to reconfigure a package (e.g., to change settings), use `sudo dpkg-reconfigure packagename` which runs the configuration scripts again.

## Frequently Asked Questions

#### Q1. What's the difference between `dpkg` and `apt`?
A. `dpkg` works directly with .deb files and doesn't handle dependencies automatically. `apt` is a higher-level tool that resolves dependencies and can download packages from repositories.

#### Q2. How do I fix "dependency problems" errors?
A. Run `sudo apt-get install -f` after a failed `dpkg -i` to resolve missing dependencies.

#### Q3. How can I see what files a .deb package will install before installing it?
A. Use `dpkg-deb --contents package.deb` to list the files contained in the package.

#### Q4. How do I reinstall a package?
A. Use `sudo dpkg -i --force-reinstall package.deb` or with apt: `sudo apt-get install --reinstall packagename`.

#### Q5. How do I prevent a package from being upgraded?
A. Use `sudo apt-mark hold packagename` to prevent automatic upgrades.

## References

https://manpages.debian.org/buster/dpkg/dpkg.1.en.html

## Revisions

- 2025/05/04 First revision