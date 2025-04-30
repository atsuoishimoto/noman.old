# jq command

Process and manipulate JSON data from the command line.

## Overview

`jq` is a lightweight and flexible command-line JSON processor. It allows you to slice, filter, map, and transform structured data with the same ease that `sed`, `awk`, and `grep` let you play with text. It works like a filter, taking input from files or stdin, and outputting processed JSON to stdout.

## Options

### **-r, --raw-output**

Outputs raw strings rather than JSON encoded strings (removes quotes)

```console
$ echo '{"name": "John"}' | jq -r '.name'
John
```

### **-c, --compact-output**

Produces compact output without pretty-printing

```console
$ echo '{"name": "John", "age": 30}' | jq -c
{"name":"John","age":30}
```

### **-s, --slurp**

Reads all inputs into an array and applies the filter to it

```console
$ echo '{"id": 1}' | echo '{"id": 2}' | jq -s
[
  {"id": 1},
  {"id": 2}
]
```

### **-f, --from-file**

Reads filter from a file

```console
$ echo '{"name": "John", "age": 30}' | jq -f filter.jq
# Output depends on the content of filter.jq
```

## Usage Examples

### Basic Property Access

```console
$ echo '{"user": {"name": "John", "age": 30}}' | jq '.user.name'
"John"
```

### Array Operations

```console
$ echo '[{"name": "John"}, {"name": "Jane"}]' | jq '.[].name'
"John"
"Jane"
```

### Filtering Arrays

```console
$ echo '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]' | jq '.[] | select(.age > 28)'
{
  "name": "John",
  "age": 30
}
```

### Creating New JSON

```console
$ echo '{"first": "John", "last": "Doe"}' | jq '{full_name: .first + " " + .last}'
{
  "full_name": "John Doe"
}
```

## Tips:

### Pipe Multiple Filters

Chain multiple operations with pipes within jq to perform complex transformations:

```console
$ echo '[{"id": 1, "value": "a"}, {"id": 2, "value": "b"}]' | jq '.[] | {id: .id, upper: (.value | ascii_upcase)}'
{
  "id": 1,
  "upper": "A"
}
{
  "id": 2,
  "upper": "B"
}
```

### Use Built-in Functions

jq has many built-in functions for string manipulation, math operations, and more:

```console
$ echo '["apple", "banana", "cherry"]' | jq 'map(length)'
[
  5,
  6,
  6
]
```

### Format JSON Files

Use jq as a simple JSON formatter/pretty-printer:

```console
$ jq '.' messy.json > formatted.json
```

## Frequently Asked Questions

#### Q1. How do I extract a specific field from JSON?
A. Use the dot notation: `jq '.fieldname'` or for nested fields: `jq '.parent.child'`.

#### Q2. How do I process multiple JSON files?
A. You can use shell loops or the `-s` (slurp) option to combine multiple files into an array.

#### Q3. How do I convert JSON to CSV?
A. Use raw output with string concatenation: `jq -r '.[] | [.field1, .field2] | @csv'`.

#### Q4. How do I handle JSON with special characters?
A. jq handles escaping automatically, but you can use the `-r` flag to get raw output when needed.

#### Q5. Can jq modify JSON files in-place?
A. No, jq doesn't modify files in-place. You need to redirect output to a new file and then replace the original.

## References

https://stedolan.github.io/jq/manual/

## Revisions

- 2025/04/30 First revision