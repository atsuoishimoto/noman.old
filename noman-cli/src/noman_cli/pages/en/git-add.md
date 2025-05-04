# git add command

Add file contents to the staging area (index) in preparation for the next commit.

## Overview

The `git add` command updates the Git index with the current content of files in your working directory. It marks changes to be included in the next commit. This is a crucial step in Git's workflow, as it allows you to selectively choose which changes to commit.

## Options

### **-A, --all**

Add changes from all tracked and untracked files

```console
$ git add -A
```

### **-u, --update**

Update only tracked files (doesn't add new files)

```console
$ git add -u
```

### **-p, --patch**

Interactively choose hunks of patch between the index and the work tree

```console
$ git add -p file.txt
diff --git a/file.txt b/file.txt
index 1234567..abcdefg 100644
--- a/file.txt
+++ b/file.txt
@@ -1,5 +1,6 @@
 This is some text.
-This line will be removed.
+This line was changed.
+This is a new line.
 More text here.
Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? 
```

### **-i, --interactive**

Add modified contents interactively

```console
$ git add -i
           staged     unstaged path
  1:    unchanged        +2/-1 file.txt
  2:    unchanged        +4/-0 another.txt

*** Commands ***
  1: status       2: update       3: revert       4: add untracked
  5: patch        6: diff         7: quit         8: help
What now> 
```

### **-n, --dry-run**

Don't actually add files, just show what would happen

```console
$ git add -n *.txt
add 'file.txt'
add 'notes.txt'
```

## Usage Examples

### Adding specific files

```console
$ git add file1.txt file2.txt
```

### Adding all files in a directory

```console
$ git add src/
```

### Adding all files with a specific extension

```console
$ git add *.js
```

### Adding all changes in the repository

```console
$ git add .
```

## Tips:

### Use the Staging Area Strategically

The staging area allows you to create focused commits. Instead of adding everything at once with `git add .`, consider adding related changes together for more meaningful commit history.

### Check What's Staged

After using `git add`, run `git status` to verify what changes are staged for the next commit. This helps prevent accidentally committing unwanted changes.

### Undo Staging

If you accidentally stage a file, you can unstage it with `git restore --staged <file>` (or the older `git reset HEAD <file>` syntax).

### Interactive Mode for Complex Changes

For files with multiple changes, use `git add -p` to stage specific parts of the file. This is useful when you've made several unrelated changes to a single file.

## Frequently Asked Questions

#### Q1. What's the difference between `git add .` and `git add -A`?
A. `git add .` adds all changes in the current directory and its subdirectories, while `git add -A` adds changes from the entire working tree, regardless of your current directory.

#### Q2. How do I add only modified and deleted files but not untracked files?
A. Use `git add -u` or `git add --update`.

#### Q3. Can I add part of a file's changes?
A. Yes, use `git add -p <file>` or `git add --patch <file>` to interactively select which changes to stage.

#### Q4. What happens if I add a file and then modify it again?
A. Only the changes that were present when you ran `git add` will be staged. The newer changes will remain unstaged until you add them.

## References

https://git-scm.com/docs/git-add

## Revisions

- 2025/05/04 First revision