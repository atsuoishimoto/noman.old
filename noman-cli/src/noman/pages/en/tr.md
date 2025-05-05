# tr command

Translate or delete characters from standard input, writing to standard output.

## Overview

The `tr` command is a text transformation utility that operates on a character-by-character basis. It reads from standard input, performs character substitution, deletion, or compression operations, and writes the result to standard output. It's commonly used in shell scripts for tasks like case conversion, character removal, and basic text transformations.

## Options

### **-d, --delete**

Delete characters in SET1, do not translate.

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

### **-t, --truncate-set1**

First truncate SET1 to the length of SET2.

```console
$ echo "Hello" | tr -t 'aeiou' '12345'
H2ll4
```

## Usage Examples

### Converting lowercase to uppercase

```console
$ echo "hello world" | tr 'a-z' 'A-Z'
HELLO WORLD
```

### Removing all digits from text

```console
$ echo "Phone: 123-456-7890" | tr -d '0-9'
Phone: --
```

### Translating spaces to newlines

```console
$ echo "one two three" | tr ' ' '\n'
one
two
three
```

### Removing all non-printable characters

```console
$ cat file.txt | tr -cd '[:print:]\n'
[outputs only printable characters and newlines]
```

## Tips

### Character Classes

Use predefined character classes like `[:alnum:]`, `[:alpha:]`, `[:digit:]`, `[:lower:]`, `[:upper:]`, and `[:space:]` for more readable and portable commands.

```console
$ echo "Hello123" | tr '[:lower:]' '[:upper:]'
HELLO123
```

### Combining Options

Combine options for more complex transformations. For example, `-cd` both complements the set and deletes characters.

```console
$ echo "abc123!@#" | tr -cd '[:digit:]'
123
```

### Escaping Special Characters

When using special characters like newlines or tabs, escape them properly with backslashes.

```console
$ echo "one,two,three" | tr ',' '\n'
one
two
three
```

## Frequently Asked Questions

#### Q1. How do I replace multiple spaces with a single space?
A. Use `tr -s ' '` to squeeze multiple spaces into one.

#### Q2. Can tr replace words or phrases?
A. No, `tr` operates only on individual characters, not words or patterns. For word/pattern replacement, use `sed` or `awk`.

#### Q3. How do I remove all non-alphanumeric characters?
A. Use `tr -cd '[:alnum:]'` to keep only alphanumeric characters.

#### Q4. Why doesn't tr work with files directly?
A. `tr` only reads from standard input. To process a file, you need to pipe it: `cat file.txt | tr ...` or use redirection: `tr ... < file.txt`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html

## Revisions

- 2025/05/04 First revision