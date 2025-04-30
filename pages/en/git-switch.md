# git switch command

Switch branches or restore working tree files.

## Overview

The `git switch` command allows you to switch between branches in a Git repository. It was introduced in Git 2.23 as a more user-friendly alternative to certain uses of `git checkout`. While `git checkout` serves multiple purposes, `git switch` is specifically designed for branch operations, making it clearer and less error-prone.

## Options

### **-c, --create \<branch>**

Create a new branch and switch to it.

```console
$ git switch -c feature-login
Switched to a new branch 'feature-login'
```

### **-d, --detach**

Switch to a commit in "detached HEAD" state.

```console
$ git switch --detach HEAD~3
Note: switching to 'HEAD~3'.

You are in 'detached HEAD' state...
HEAD is now at a1b2c3d Previous commit message
```

### **-t, --track**

Set up tracking mode when switching to a remote branch.

```console
$ git switch -t origin/feature
Branch 'feature' set up to track remote branch 'feature' from 'origin'.
Switched to a new branch 'feature'
```

### **--discard-changes**

Throw away local modifications before switching.

```console
$ git switch --discard-changes main
Switched to branch 'main'
```

## Usage Examples

### Switching to an existing branch

```console
$ git switch main
Switched to branch 'main'
```

### Creating and switching to a new branch based on current HEAD

```console
$ git switch -c bugfix/issue-123
Switched to a new branch 'bugfix/issue-123'
```

### Creating a new branch from a specific starting point

```console
$ git switch -c hotfix/security-patch v1.2.3
Switched to a new branch 'hotfix/security-patch'
```

## Tips

### Use `git switch -` to quickly return to the previous branch

Similar to `cd -` in the shell, `git switch -` allows you to toggle between the current and previous branch.

```console
$ git switch feature
Switched to branch 'feature'
$ git switch main
Switched to branch 'main'
$ git switch -
Switched to branch 'feature'
```

### Combine with `git branch` to see available branches

Before switching, you might want to see what branches are available:

```console
$ git branch
  develop
* main
  feature-x
$ git switch develop
Switched to branch 'develop'
```

### Prefer `git switch` over `git checkout` for branch operations

Using `git switch` for branch operations and `git restore` for file operations makes your intentions clearer and helps avoid accidental changes.

## Frequently Asked Questions

#### Q1. What's the difference between `git switch` and `git checkout`?
A. `git switch` is focused solely on branch operations, while `git checkout` has multiple functions including branch switching and file restoration. `git switch` was introduced to provide a clearer, more focused command.

#### Q2. How do I create a new branch without switching to it?
A. Use `git branch <new-branch>` instead of `git switch`. The `switch` command always changes your current branch.

#### Q3. Can I switch to a branch that has uncommitted changes?
A. Yes, if the changes don't conflict with the target branch. If there are conflicts, Git will prevent the switch unless you use `--discard-changes` or stash your changes first.

#### Q4. How do I switch to a remote branch?
A. Use `git switch -t origin/branch-name` to create a local tracking branch and switch to it.

## References

https://git-scm.com/docs/git-switch

## Revisions

- 2025/04/30 First revision