# git stash command

Temporarily stores modified, tracked files to save changes without committing.

## Overview

`git stash` allows you to save your current work in progress without committing it, so you can switch to another task (like changing branches) and come back to it later. It's like putting your changes on a shelf temporarily. The stashed changes are stored in a stack, so you can have multiple stashes and retrieve them in any order.

## Options

### **git stash push** (or just **git stash**)

Saves your local modifications and reverts the working directory to match the HEAD commit

```console
$ git stash
Saved working directory and index state WIP on main: abc1234 Previous commit message
```

### **git stash list**

Shows all stashes you've created and their descriptions

```console
$ git stash list
stash@{0}: WIP on main: abc1234 Previous commit message
stash@{1}: WIP on feature: def5678 Another commit message
```

### **git stash apply**

Applies the most recent stash to your working directory without removing it from the stash list

```console
$ git stash apply
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
```

### **git stash pop**

Applies the most recent stash and removes it from the stash list

```console
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
Dropped refs/stash@{0} (abcd1234)
```

### **git stash drop**

Removes a specific stash from the list

```console
$ git stash drop stash@{1}
Dropped stash@{1} (def5678)
```

## Usage Examples

### Stashing with a custom message

```console
$ git stash push -m "Work in progress for feature X"
Saved working directory and index state On main: Work in progress for feature X
```

### Applying a specific stash

```console
$ git stash apply stash@{2}
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
```

### Stashing untracked files

```console
$ git stash -u
Saved working directory and index state WIP on main: abc1234 Previous commit message
```

### Creating a branch from a stash

```console
$ git stash branch new-feature stash@{0}
Switched to a new branch 'new-feature'
On branch new-feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
Dropped refs/stash@{0} (abcd1234)
```

## Tips

### Include a Descriptive Message
Always use `-m` with a descriptive message when stashing to easily identify your stashes later, especially if you have multiple stashes.

### Check for Conflicts
When applying a stash, be aware that conflicts might occur if the current state of your files differs significantly from when you created the stash.

### Clean Up Old Stashes
Regularly use `git stash list` and `git stash drop` to manage and remove old stashes you no longer need, as they can accumulate over time.

### Stash Partial Changes
Use `git stash push -p` for interactive stashing, allowing you to select specific changes to stash while keeping others in your working directory.

## Frequently Asked Questions

#### Q1. What's the difference between `git stash apply` and `git stash pop`?
A. `git stash apply` applies the stash but keeps it in your stash list, while `git stash pop` applies the stash and removes it from the list.

#### Q2. Can I stash untracked files?
A. Yes, use `git stash -u` or `git stash --include-untracked` to include untracked files in your stash.

#### Q3. How do I recover a dropped stash?
A. You can use `git fsck --unreachable` to find the hash of the dropped stash, then `git stash apply <hash>` to recover it, but only if garbage collection hasn't run.

#### Q4. How long do stashes last?
A. Stashes remain until you explicitly remove them with `git stash drop` or `git stash clear`, or until they're removed by Git's garbage collection.

#### Q5. Can I stash changes on one branch and apply them to another?
A. Yes, you can stash changes on one branch, switch to another branch, and then apply the stash there.

## References

https://git-scm.com/docs/git-stash

## Revisions

- 2025/04/30 First revision