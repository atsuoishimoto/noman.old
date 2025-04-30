# git add command

Add file contents to the staging area (index) in preparation for the next commit.

## Overview

`git add` updates the Git index with the current content of files in your working directory. It marks new or modified files to be included in your next commit. This command is a crucial step in the Git workflow, as it allows you to selectively choose which changes will be part of your next commit.

## Options

### **-A, --all**

Add all changes (new, modified, and deleted files) to the staging area.

```console
$ git add -A
```

### **-u, --update**

Update only files that Git already knows about (modified or deleted, but not new files).

```console
$ git add -u
```

### **-p, --patch**

Interactively choose parts of files to stage, allowing you to commit specific changes within a file rather than the entire file.

```console
$ git add -p
diff --git a/file.txt b/file.txt
index 1234567..abcdefg 100644
--- a/file.txt
+++ b/file.txt
@@ -10,6 +10,7 @@ Some content
 More content
+New line added
 Final line
Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? 
```

### **-i, --interactive**

Start an interactive staging session to select files and parts of files to add.

```console
$ git add -i
           staged     unstaged path
  1:    unchanged        +2/-0 file1.txt
  2:    unchanged        +1/-1 file2.txt

*** Commands ***
  1: status       2: update       3: revert       4: add untracked
  5: patch        6: diff         7: quit         8: help
What now> 
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

### Adding files by pattern

```console
$ git add *.js
```

### Adding all changes except specific files

```console
$ git add . ':!file_to_exclude.txt' ':!*.log'
```

## Tips

### Stage Changes in Chunks

Use `git add -p` to review and stage specific parts of files. This is useful when you've made multiple unrelated changes to a file but want to commit them separately.

### Check What's Staged

After using `git add`, run `git status` to verify what changes are staged before committing.

### Undo Staging

If you accidentally stage a file, use `git restore --staged <file>` to unstage it.

### Use the Staging Area Strategically

The staging area allows you to create focused, logical commits. Take advantage of this by staging related changes together rather than adding everything at once.

## Frequently Asked Questions

#### Q1. What's the difference between `git add .` and `git add -A`?
A. `git add .` adds all new and modified files in the current directory and its subdirectories, but doesn't stage deleted files unless you're using Git 2.0+. `git add -A` adds all changes including new, modified, and deleted files across the entire repository.

#### Q2. How do I add only part of a file's changes?
A. Use `git add -p` (or `--patch`) to interactively select which changes to stage within each file.

#### Q3. Can I undo a `git add` if I change my mind?
A. Yes, use `git restore --staged <file>` to unstage a file while keeping your changes in the working directory.

#### Q4. What does "Changes to be committed" mean after using `git add`?
A. It means the changes have been staged (added to the index) and will be included in your next commit.

## References

https://git-scm.com/docs/git-add

## Revisions

- 2025/04/30 First revision