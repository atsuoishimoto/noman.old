# git-stash command

Stash changes in a dirty working directory for later use.

## Overview

`git stash` temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later. Stashing is handy when you need to quickly switch contexts and work on something else, but you're not ready to commit your current work.

## Options

### **-u, --include-untracked**

Include untracked files in the stash.

```console
$ git stash -u
Saved working directory and index state WIP on main: 2d4e15a Add feature X
```

### **-a, --all**

Include both untracked and ignored files in the stash.

```console
$ git stash -a
Saved working directory and index state WIP on main: 2d4e15a Add feature X
```

### **-p, --patch**

Interactively select hunks from the diff between HEAD and the working tree to be stashed.

```console
$ git stash -p
diff --git a/file.txt b/file.txt
index 1234567..abcdefg 100644
--- a/file.txt
+++ b/file.txt
@@ -1,4 +1,4 @@
-Old content
+New content
Stash this hunk [y,n,q,a,d,e,?]? y
Saved working directory and index state WIP on main: 2d4e15a Add feature X
```

### **push [<message>]**

Save your local modifications to a new stash entry and roll them back to HEAD.

```console
$ git stash push -m "WIP: implementing feature Y"
Saved working directory and index state On main: WIP: implementing feature Y
```

### **list**

List all stashes in the stack.

```console
$ git stash list
stash@{0}: WIP on main: 2d4e15a Add feature X
stash@{1}: On main: WIP: implementing feature Y
```

### **show [<stash>]**

Show the changes recorded in the stash as a diff.

```console
$ git stash show stash@{0}
 file.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### **pop [<stash>]**

Apply a stash and remove it from the stack.

```console
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### **apply [<stash>]**

Apply a stash without removing it from the stack.

```console
$ git stash apply stash@{1}
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
```

### **drop [<stash>]**

Remove a stash from the stack.

```console
$ git stash drop stash@{0}
Dropped stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

### **clear**

Remove all stashes from the stack.

```console
$ git stash clear
```

## Usage Examples

### Basic stash workflow

```console
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt

$ git stash
Saved working directory and index state WIP on main: 2d4e15a Add feature X

$ git status
On branch main
nothing to commit, working tree clean

# Do some other work, then come back to your stashed changes
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file.txt
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
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
Dropped refs/stash@{0} (a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9)
```

## Tips:

### Name Your Stashes

Use descriptive messages with your stashes to make them easier to identify later:

```console
$ git stash push -m "halfway through refactoring authentication"
```

### Stash Only Specific Files

You can stash only specific files by listing them after the command:

```console
$ git stash push file1.txt file2.txt
```

### View Stash Contents in Detail

For a more detailed view of a stash's contents:

```console
$ git stash show -p stash@{0}
```

### Create a Branch from a Stash

If you realize your stashed changes should be in their own branch:

```console
$ git stash branch new-feature-branch stash@{0}
```

## Frequently Asked Questions

#### Q1. What happens to my stashed changes if I switch branches?
A. Stashed changes remain available across all branches. You can stash changes on one branch and apply them on another.

#### Q2. Can I recover a stash after I've dropped it?
A. Yes, if you know the commit hash of the stash (shown when dropping). Use `git stash apply <commit-hash>` to recover it, but only if the garbage collector hasn't run.

#### Q3. How long do stashes persist?
A. Stashes persist indefinitely until you explicitly remove them with `git stash drop` or `git stash clear`, or until they're garbage collected (which typically doesn't happen for a long time).

#### Q4. What's the difference between `git stash pop` and `git stash apply`?
A. `git stash pop` applies the stash and then removes it from the stash list, while `git stash apply` only applies the stash but keeps it in the list for potential future use.

#### Q5. Can I stash untracked files?
A. By default, `git stash` only stashes tracked files with changes. Use `git stash -u` to include untracked files or `git stash -a` to include both untracked and ignored files.

## References

https://git-scm.com/docs/git-stash

## Revisions

- 2025/05/04 First revision