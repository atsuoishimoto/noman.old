# git reset command

Reset current HEAD to the specified state, allowing you to undo changes or move between commits.

## Overview

`git reset` is a powerful command that adjusts the current branch by moving the HEAD pointer to a different commit. It can be used to undo commits, unstage changes, or completely discard work. The command operates at different levels of aggressiveness, from preserving your working directory changes to completely removing them.

## Options

### **--soft**

Moves HEAD to the specified commit but keeps all changes staged, allowing you to recommit with adjustments.

```console
$ git reset --soft HEAD~1
```

### **--mixed (default)**

Moves HEAD to the specified commit and unstages changes, but preserves modifications in your working directory.

```console
$ git reset HEAD~1
```

### **--hard**

Moves HEAD to the specified commit and discards all changes, reverting both the staging area and working directory to match the target commit.

```console
$ git reset --hard HEAD~1
```

### **<path>**

Unstages specific files without changing HEAD, effectively undoing `git add`.

```console
$ git reset -- filename.txt
```

## Usage Examples

### Undoing the last commit but keeping changes staged

```console
$ git reset --soft HEAD~1
# The changes from the last commit are now staged and ready to be recommitted
```

### Undoing multiple commits

```console
$ git reset HEAD~3
# Moves HEAD back 3 commits, keeping changes in working directory
```

### Completely discarding recent commits and their changes

```console
$ git reset --hard origin/main
# Resets to match the remote main branch, discarding all local changes
```

### Unstaging a specific file

```console
$ git add *.txt
$ git reset -- unwanted.txt
# Unstages unwanted.txt while keeping other .txt files staged
```

## Tips

### Understanding the Reset Levels

Think of the three reset modes as levels of aggressiveness: `--soft` (gentlest, keeps changes staged), `--mixed` (default, keeps changes but unstaged), and `--hard` (most aggressive, discards all changes).

### Creating Backup Branches

Before performing a hard reset, create a backup branch with `git branch backup-branch` to ensure you can recover your work if needed.

### Recovering from Hard Reset

If you accidentally perform a hard reset, you can often recover using `git reflog` to find the commit hash of your previous state, then `git reset --hard <commit-hash>` to return to it.

### Combining with Other Commands

`git reset` works well with `git stash` when you need to temporarily set aside changes before resetting.

## Frequently Asked Questions

#### Q1. What's the difference between `git reset` and `git revert`?
A. `git reset` changes history by moving HEAD to a previous state, while `git revert` creates a new commit that undoes previous changes, preserving history.

#### Q2. How can I undo a `git reset --hard`?
A. Use `git reflog` to find the commit hash before the reset, then `git reset --hard <commit-hash>` to restore that state.

#### Q3. Can I reset to a specific commit?
A. Yes, use `git reset <commit-hash>` to move HEAD to any specific commit.

#### Q4. How do I unstage all files?
A. Use `git reset` without any arguments to unstage all changes.

#### Q5. Is it safe to use `git reset --hard` on a shared branch?
A. No, avoid using `git reset --hard` on branches that others are working on, as it rewrites history and can cause conflicts for collaborators.

## References

https://git-scm.com/docs/git-reset

## Revisions

- 2025/04/30 First revision