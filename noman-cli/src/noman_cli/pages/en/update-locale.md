# update-locale command

Configure system-wide locale settings by updating the /etc/default/locale file.

## Overview

The `update-locale` command modifies system-wide locale settings on Debian-based Linux distributions. It updates the `/etc/default/locale` file, which defines environment variables that determine language, character encoding, and regional formatting preferences used by the system and applications.

## Options

### **--reset**

Reset all locale variables by removing the `/etc/default/locale` file

```console
$ sudo update-locale --reset
```

### **VARIABLE=value**

Set a specific locale variable to the specified value

```console
$ sudo update-locale LANG=en_US.UTF-8
```

### **--locale-file=FILE**

Specify an alternative locale file instead of the default `/etc/default/locale`

```console
$ sudo update-locale --locale-file=/path/to/custom/locale
```

## Usage Examples

### Setting the system language to English (US)

```console
$ sudo update-locale LANG=en_US.UTF-8
```

### Setting multiple locale variables at once

```console
$ sudo update-locale LANG=en_GB.UTF-8 LC_TIME=en_GB.UTF-8 LC_PAPER=en_GB.UTF-8
```

### Removing a specific locale variable

```console
$ sudo update-locale LC_PAPER=
```

## Tips:

### Check Current Locale Settings

Before making changes, check your current locale settings with the `locale` command to understand what you're modifying.

```console
$ locale
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
...
```

### Generate Required Locales First

Make sure the locales you want to use are generated on your system. Use `locale -a` to list available locales and `sudo locale-gen <locale>` to generate missing ones.

### System Restart May Be Required

Some changes to locale settings might require a system restart or at least a logout/login to take full effect across all applications.

## Frequently Asked Questions

#### Q1. What's the difference between LANG and LC_ALL?
A. `LANG` is the default locale for all categories when specific `LC_*` variables are not set. `LC_ALL` overrides all other locale variables, including `LANG`.

#### Q2. How do I set the system to use English interface but local formats?
A. Set `LANG` to your preferred English locale (e.g., `en_US.UTF-8`) and set specific `LC_*` variables like `LC_TIME` and `LC_MONETARY` to your local format.

#### Q3. Why do some applications ignore my locale settings?
A. Some applications might have their own language settings that override system locale, or they might not support the locale you've configured.

#### Q4. How do I completely reset all locale settings?
A. Use `sudo update-locale --reset` to remove all locale settings from the system configuration file.

## References

https://manpages.debian.org/bullseye/locales/update-locale.8.en.html

## Revisions

- 2025/05/04 First revision