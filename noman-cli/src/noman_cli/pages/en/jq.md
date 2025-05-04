# jq command

Process and transform JSON data with a lightweight and flexible command-line processor.

## Overview

`jq` is a command-line JSON processor that allows you to slice, filter, map, and transform structured data with ease. It works like `sed` for JSON data – you can use it to extract specific fields, transform values, filter arrays, and much more without writing complex scripts.

## Options

### **-r, --raw-output**

Output strings without quotes for more readable results.

```console
$ echo '{"name": "John"}' | jq -r '.name'
John
```

### **-s, --slurp**

Read multiple JSON objects and combine them into an array.

```console
$ echo '{"id": 1}\n{"id": 2}' | jq -s '.'
[
  {
    "id": 1
  },
  {
    "id": 2
  }
]
```

### **-f, --from-file FILENAME**

Read filter from a file instead of command line.

```console
$ echo '{"name": "John", "age": 30}' | jq -f filter.jq
# Where filter.jq contains: .name
"John"
```

### **-c, --compact-output**

Output compact JSON instead of pretty-printed format.

```console
$ echo '{"name": "John", "age": 30}' | jq -c '.'
{"name":"John","age":30}
```

### **-n, --null-input**

Don't read any input, but generate results based on the filter.

```console
$ jq -n '{"hello": "world"}'
{
  "hello": "world"
}
```

## Usage Examples

### Extracting specific fields

```console
$ echo '{"user": {"name": "John", "age": 30}}' | jq '.user.name'
"John"
```

### Filtering arrays

```console
$ echo '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]' | jq '.[] | select(.age > 28)'
{
  "name": "John",
  "age": 30
}
```

### Transforming data

```console
$ echo '[{"name": "John"}, {"name": "Jane"}]' | jq 'map({username: .name})'
[
  {
    "username": "John"
  },
  {
    "username": "Jane"
  }
]
```

### Working with arrays

```console
$ echo '{"users": ["John", "Jane", "Bob"]}' | jq '.users[1]'
"Jane"
```

## Tips

### Pipe Multiple Filters

Chain multiple filters with pipes to perform complex transformations:

```console
$ echo '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]' | jq '.[] | select(.age > 25) | .name'
"John"
```

### Use Built-in Functions

`jq` has many built-in functions like `length`, `keys`, `has`, and `map` that make data manipulation easier:

```console
$ echo '{"a": 1, "b": 2, "c": 3}' | jq 'keys'
[
  "a",
  "b",
  "c"
]
```

### Create Variables

Use the `as` keyword to create variables for reuse in complex filters:

```console
$ echo '{"items": [{"price": 10}, {"price": 20}]}' | jq '.items | map(.price) | add as $total | {"total": $total, "count": length}'
{
  "total": 30,
  "count": 2
}
```

## Frequently Asked Questions

#### Q1. How do I format JSON with jq?
A. Simply pipe your JSON through `jq '.'` to get pretty-printed output.

#### Q2. How can I extract values without quotes?
A. Use the `-r` or `--raw-output` option to output strings without quotes.

#### Q3. How do I filter an array based on a condition?
A. Use `select()` with a condition: `jq '.[] | select(.field == "value")'`

#### Q4. How do I process multiple JSON files?
A. Use the `-s` (slurp) option to combine multiple inputs into an array.

#### Q5. How can I create new JSON from existing data?
A. Create object literals in your filter: `jq '{new_key: .old_key, calculated: (.value * 2)}'`

## References

https://stedolan.github.io/jq/manual/

## Revisions

- 2025/05/04 First revision