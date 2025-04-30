# update-locale command

Updates system locale settings by modifying locale configuration files.

## Overview

`update-locale` is a command used to modify system-wide locale settings on Debian-based Linux distributions. It updates the `/etc/default/locale` file, which defines environment variables that determine language, character encoding, and regional formatting preferences for the system.

## Options

### **VARIABLE=value**

Sets a locale variable to the specified value

```console
$ sudo update-locale LANG=en_US.UTF-8
```

### **--reset**

Removes all locale settings, resetting to system defaults

```console
$ sudo update-locale --reset
```

## Usage Examples

### Setting multiple locale variables at once

```console
$ sudo update-locale LANG=en_GB.UTF-8 LC_TIME=en_GB.UTF-8 LC_PAPER=en_GB.UTF-8
```

### Checking current locale settings

First set the locale, then verify the changes:

```console
$ sudo update-locale LANG=de_DE.UTF-8
$ cat /etc/default/locale
LANG=de_DE.UTF-8
```

## Tips

### Available Locales

Before setting a locale, ensure it's available on your system. You can check available locales with:

```console
$ locale -a
```

If your desired locale isn't listed, you may need to generate it using `locale-gen`.

### System-wide vs User Settings

`update-locale` changes system-wide settings. For user-specific locale settings, modify `~/.profile` or `~/.bashrc` instead.

### Applying Changes

Changes made with `update-locale` take effect for new login sessions. To apply changes immediately in the current session, use:

```console
$ source /etc/default/locale
```

## Frequently Asked Questions

#### Q1. What's the difference between LANG and LC_ALL?
A. `LANG` is the default locale for all categories, while `LC_ALL` overrides all other locale settings. Use `LANG` for general settings and specific `LC_*` variables for fine-tuning.

#### Q2. How do I know which locales are available on my system?
A. Use `locale -a` to list all available locales.

#### Q3. Do I need to restart my system after changing locale settings?
A. A full restart isn't necessary, but you need to log out and log back in for the changes to take effect in your user session.

#### Q4. How can I remove a specific locale setting?
A. Use `update-locale VARIABLE=` (with empty value) to remove a specific variable.

## References

https://manpages.debian.org/bullseye/locales/update-locale.8.en.html

## Revisions

- 2025/04/30 First revision