# update-alternatives command

Manage symbolic links determining default commands in the alternatives system.

## Overview

`update-alternatives` creates, removes, maintains, and displays information about symbolic links that determine which commands are run when a user enters a command name. It's part of Debian-based systems (like Ubuntu) and helps manage multiple versions of the same program on a system.

## Options

### **--install**

Create a new alternative link group

```console
$ sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 100
update-alternatives: using /usr/bin/vim to provide /usr/bin/editor (editor) in auto mode
```

### **--config**

Configure which alternative to use for a link group

```console
$ sudo update-alternatives --config editor
There are 3 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path              Priority   Status
------------------------------------------------------------
* 0            /usr/bin/vim       100       auto mode
  1            /usr/bin/emacs     50        manual mode
  2            /usr/bin/nano      40        manual mode
  3            /usr/bin/vim       100       auto mode

Press <enter> to keep the current choice[*], or type selection number:
```

### **--display**

Display information about a link group

```console
$ update-alternatives --display editor
editor - auto mode
  link best version is /usr/bin/vim
  link currently points to /usr/bin/vim
  link editor is /usr/bin/editor
  slave editor.1.gz is /usr/share/man/man1/editor.1.gz
  slave editor.fr.1.gz is /usr/share/man/fr/man1/editor.1.gz
  /usr/bin/emacs - priority 50
  /usr/bin/nano - priority 40
  /usr/bin/vim - priority 100
```

### **--remove**

Remove an alternative from a link group

```console
$ sudo update-alternatives --remove editor /usr/bin/emacs
update-alternatives: removing editor alternative /usr/bin/emacs
```

## Usage Examples

### Setting up Java alternatives

```console
$ sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-11-openjdk/bin/java 1100
update-alternatives: using /usr/lib/jvm/java-11-openjdk/bin/java to provide /usr/bin/java (java) in auto mode
```

### Switching between different Java versions

```console
$ sudo update-alternatives --config java
There are 2 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                           Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk/bin/java          1100      auto mode
  1            /usr/lib/jvm/java-8-openjdk/bin/java           1000      manual mode
  2            /usr/lib/jvm/java-11-openjdk/bin/java          1100      auto mode

Press <enter> to keep the current choice[*], or type selection number: 1
update-alternatives: using /usr/lib/jvm/java-8-openjdk/bin/java to provide /usr/bin/java (java) in manual mode
```

## Tips

### Understanding Priority

Higher priority numbers (like 100) are preferred over lower ones (like 50) in auto mode. When installing alternatives, assign higher numbers to preferred versions.

### Auto vs Manual Mode

In auto mode, the system selects the alternative with the highest priority. In manual mode, the system uses the alternative you explicitly selected, regardless of priority.

### Common Alternative Groups

Common alternative groups include `editor`, `java`, `python`, and `x-terminal-emulator`. Use `--display` to see what's available on your system.

### Check Before Removing

Before removing an alternative, check if other packages depend on it using `--display`. Removing an alternative doesn't delete the actual program, just its entry in the alternatives system.

## Frequently Asked Questions

#### Q1. What's the difference between update-alternatives and symbolic links?
A. `update-alternatives` manages symbolic links in a centralized way, tracking priorities and allowing easy switching between alternatives. Manual symbolic links don't have these management features.

#### Q2. How do I check which alternatives are available on my system?
A. Run `update-alternatives --get-selections` to see all managed alternative groups.

#### Q3. Can I use update-alternatives for my own custom commands?
A. Yes, you can create your own alternative groups for any commands using the `--install` option.

#### Q4. How do I completely remove an alternative group?
A. Use `--remove-all` followed by the link name: `sudo update-alternatives --remove-all editor`

## References

https://manpages.debian.org/buster/dpkg/update-alternatives.1.en.html

## Revisions

- 2025/04/30 First revision