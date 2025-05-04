# update-alternatives command

Manages symbolic links determining default commands in the alternatives system.

## Overview

`update-alternatives` creates, removes, maintains, and displays information about symbolic links in the alternatives system. This system allows multiple versions of the same program to coexist on a system, with one version designated as the default. It's commonly used in Debian-based Linux distributions to manage which version of a program is executed when a user runs a command.

## Options

### **--install** (`-i`)

Creates a new alternative link group

```console
$ sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 50
update-alternatives: using /usr/bin/vim to provide /usr/bin/editor (editor) in auto mode
```

### **--remove** (`-r`)

Removes an alternative from the system

```console
$ sudo update-alternatives --remove editor /usr/bin/vim
update-alternatives: removing editor (/usr/bin/vim) from auto mode
```

### **--config** (`-c`)

Shows available alternatives for a link group and allows interactive selection

```console
$ sudo update-alternatives --config editor
There are 3 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path              Priority   Status
------------------------------------------------------------
* 0            /usr/bin/vim       50        auto mode
  1            /usr/bin/nano      40        manual mode
  2            /usr/bin/emacs     30        manual mode
  3            /usr/bin/vim       50        manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

### **--display** (`-d`)

Displays information about a link group

```console
$ update-alternatives --display editor
editor - auto mode
  link best version is /usr/bin/vim
  link currently points to /usr/bin/vim
  link editor is /usr/bin/editor
  slave editor.1.gz is /usr/share/man/man1/editor.1.gz
  slave editor.fr.1.gz is /usr/share/man/fr/man1/editor.1.gz
  slave editor.it.1.gz is /usr/share/man/it/man1/editor.1.gz
  slave editor.pl.1.gz is /usr/share/man/pl/man1/editor.1.gz
  slave editor.ru.1.gz is /usr/share/man/ru/man1/editor.1.gz
/usr/bin/vim - priority 50
  slave editor.1.gz: /usr/share/man/man1/vim.1.gz
  slave editor.fr.1.gz: /usr/share/man/fr/man1/vim.1.gz
  slave editor.it.1.gz: /usr/share/man/it/man1/vim.1.gz
  slave editor.pl.1.gz: /usr/share/man/pl/man1/vim.1.gz
  slave editor.ru.1.gz: /usr/share/man/ru/man1/vim.1.gz
```

### **--auto** (`-a`)

Sets the link group to automatic mode (highest priority alternative is used)

```console
$ sudo update-alternatives --auto editor
update-alternatives: using /usr/bin/vim to provide /usr/bin/editor (editor) in auto mode
```

### **--set** (`-s`)

Sets a specific alternative as the selected one for a link group

```console
$ sudo update-alternatives --set editor /usr/bin/nano
update-alternatives: using /usr/bin/nano to provide /usr/bin/editor (editor) in manual mode
```

## Usage Examples

### Adding a new Java version to alternatives

```console
$ sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-11-openjdk/bin/java 1100
update-alternatives: using /usr/lib/jvm/java-11-openjdk/bin/java to provide /usr/bin/java (java) in auto mode
```

### Switching between different Java versions

```console
$ sudo update-alternatives --config java
There are 3 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                           Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk/bin/java          1100      auto mode
  1            /usr/lib/jvm/java-8-openjdk/bin/java           1080      manual mode
  2            /usr/lib/jvm/java-17-openjdk/bin/java          1170      manual mode
  3            /usr/lib/jvm/java-11-openjdk/bin/java          1100      manual mode

Press <enter> to keep the current choice[*], or type selection number: 2
update-alternatives: using /usr/lib/jvm/java-17-openjdk/bin/java to provide /usr/bin/java (java) in manual mode
```

### Listing all alternatives for a specific command

```console
$ update-alternatives --list java
/usr/lib/jvm/java-8-openjdk/bin/java
/usr/lib/jvm/java-11-openjdk/bin/java
/usr/lib/jvm/java-17-openjdk/bin/java
```

## Tips

### Understanding Priority Values

Higher priority values (like 100 vs 50) determine which alternative is selected in automatic mode. When installing a new alternative, assign it a higher priority than existing ones if you want it to become the default.

### Managing Groups of Related Commands

For programs like Java that have multiple related commands (java, javac, jar), you can manage them together using the `--slave` option when installing alternatives.

### Checking Current Default

Before making changes, use `--display` to see the current configuration of an alternatives group. This helps avoid unintended changes to your system.

### Auto vs Manual Mode

In auto mode, the system automatically selects the alternative with the highest priority. In manual mode, the system keeps your manually selected alternative regardless of priority.

## Frequently Asked Questions

#### Q1. What's the difference between update-alternatives and symbolic links?
A. `update-alternatives` is a higher-level system that manages symbolic links in a standardized way. It provides a consistent interface for switching between program versions and tracks which alternatives are available.

#### Q2. How do I know which programs use the alternatives system?
A. You can list all managed alternatives with `update-alternatives --get-selections`.

#### Q3. Can I remove an alternative completely from the system?
A. Yes, use `update-alternatives --remove-all <name>` to remove all alternatives for a specific command.

#### Q4. What happens if I install a new package that provides an alternative?
A. Package managers typically call `update-alternatives` during installation to add the new alternative to the system, usually with a predefined priority.

#### Q5. How do I fix broken alternatives?
A. If an alternative points to a non-existent file, you can remove it with `--remove` and then reinstall the correct alternative.

## References

https://manpages.debian.org/bullseye/dpkg/update-alternatives.1.en.html

## Revisions

2025/05/04 First revision