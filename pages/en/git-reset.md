# git reset command

Reset current HEAD to the specified state.

## Overview

`git reset` is used to undo changes by moving the current branch pointer to a different commit. It can also modify the staging area (index) and optionally the working directory, depending on the mode used. This command is commonly used to unstage files, undo commits, or completely revert to a previous state in your Git history.

## Options

### **--soft**

Moves HEAD to the specified commit but leaves the index and working directory unchanged. This effectively undoes commits while keeping all changes staged.

```console
$ git reset --soft HEAD~1
```

### **--mixed (default)**

Moves HEAD to the specified commit and updates the index to match, but leaves the working directory unchanged. This unstages changes while preserving them in your working directory.

```console
$ git reset HEAD file.txt
```

### **--hard**

Moves HEAD to the specified commit and updates both the index and working directory to match. This discards all changes in the staging area and working directory.

```console
$ git reset --hard HEAD~2
```

### **--patch (-p)**

Interactively select hunks of changes to reset.

```console
$ git reset -p
```

### **--keep**

Resets index entries but keeps files that are different between the index and working tree.

```console
$ git reset --keep HEAD~1
```

## Usage Examples

### Unstaging a file

```console
$ git add file.txt
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   file.txt

$ git reset file.txt
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
```

### Undoing the last commit but keeping changes

```console
$ git reset --soft HEAD~1
```

### Completely discarding recent commits and changes

```console
$ git reset --hard HEAD~3
HEAD is now at a1b2c3d Message from 3 commits ago
```

### Resetting to a specific commit

```console
$ git reset --mixed 5a78ef2
```

## Tips

### Safely Experiment with Reset

Before using `git reset --hard`, consider creating a backup branch with `git branch backup-branch` so you can recover if needed.

### Recover from Hard Reset

If you accidentally reset too far with `--hard`, you can use `git reflog` to find the commit you want to return to, then `git reset --hard COMMIT_HASH` to go back.

### Unstage All Files

Use `git reset` without arguments to unstage all files while keeping your working directory changes.

### Selective Unstaging

Use `git reset -p` for interactive unstaging, allowing you to select specific parts of files to unstage.

## Frequently Asked Questions

#### Q1. What's the difference between `git reset` and `git revert`?
A. `git reset` changes history by moving the branch pointer, while `git revert` creates a new commit that undoes previous changes, preserving history.

#### Q2. How do I undo a `git reset --hard`?
A. Use `git reflog` to find the commit hash before the reset, then `git reset --hard COMMIT_HASH` to restore to that point.

#### Q3. Can I use `git reset` on a public branch?
A. It's not recommended to use `git reset` on branches you've already pushed to a shared repository, as it rewrites history. Use `git revert` instead.

#### Q4. How do I unstage all files?
A. Run `git reset` without any arguments to unstage all files.

#### Q5. What does `HEAD~1` mean in `git reset HEAD~1`?
A. `HEAD~1` refers to the commit before the current HEAD (one commit back in history).

## References

https://git-scm.com/docs/git-reset

## Revisions

- 2025/05/04 First revision