# tr command

Translate or delete characters from standard input, writing to standard output.

## Overview

The `tr` command is a text transformation utility that operates on a character-by-character basis. It reads from standard input, performs substitution or deletion of characters according to specified rules, and writes the result to standard output. It's commonly used for character-based text transformations like case conversion, whitespace removal, or character substitution.

## Options

### **-d, --delete**

Delete characters in SET1 instead of translating them.

```console
$ echo "Hello, World!" | tr -d 'aeiou'
Hll, Wrld!
```

### **-s, --squeeze-repeats**

Replace each sequence of a repeated character in SET1 with a single occurrence of that character.

```console
$ echo "Hello    World!" | tr -s ' '
Hello World!
```

### **-c, --complement**

Use the complement of SET1 (all characters not in SET1).

```console
$ echo "Hello, World!" | tr -cd 'a-zA-Z'
HelloWorld
```

## Usage Examples

### Converting lowercase to uppercase

```console
$ echo "hello world" | tr 'a-z' 'A-Z'
HELLO WORLD
```

### Replacing specific characters

```console
$ echo "Hello, World!" | tr ',' '!'
Hello! World!
```

### Removing all non-printable characters

```console
$ cat file.txt | tr -cd '[:print:]\n' > clean_file.txt
```

### Translating spaces to newlines

```console
$ echo "one two three" | tr ' ' '\n'
one
two
three
```

## Tips

### Character Classes

Use predefined character classes like `[:alnum:]`, `[:alpha:]`, `[:digit:]`, `[:lower:]`, `[:upper:]`, and `[:space:]` for common character sets.

### Combining Options

Combine `-d` and `-c` to delete all characters except those specified. For example, `tr -cd '[:alnum:]'` removes everything except alphanumeric characters.

### Escaping Special Characters

When using special characters like newlines or tabs, escape them with backslashes: `\n` for newline, `\t` for tab.

### Piping with Other Commands

`tr` works best in pipelines with other commands. For example, `cat file.txt | tr 'a-z' 'A-Z' | grep "PATTERN"`.

## Frequently Asked Questions

#### Q1. How do I convert a file to uppercase?
A. Use `cat file.txt | tr 'a-z' 'A-Z' > uppercase_file.txt`.

#### Q2. How can I remove all numbers from a file?
A. Use `tr -d '0-9'` to delete all digits.

#### Q3. Can tr replace strings?
A. No, `tr` operates on individual characters, not strings. For string replacement, use `sed` instead.

#### Q4. How do I remove duplicate spaces?
A. Use `tr -s ' '` to squeeze multiple spaces into a single space.

#### Q5. How do I translate Windows line endings to Unix?
A. Use `tr -d '\r'` to remove carriage returns.

## References

https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html

## Revisions

- 2025/04/30 First revision