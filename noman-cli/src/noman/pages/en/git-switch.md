# git switch command

Switch branches or restore working tree files.

## Overview

The `git switch` command is used to switch between branches in a Git repository. It was introduced in Git 2.23 as a more user-friendly alternative to certain uses of `git checkout`. While `git checkout` serves multiple purposes, `git switch` is specifically designed for branch operations, making it clearer and less error-prone.

## Options

### **-c, --create \<branch>**

Create a new branch and switch to it.

```console
$ git switch -c feature-login
Switched to a new branch 'feature-login'
```

### **-d, --detach**

Switch to a commit in detached HEAD state.

```console
$ git switch --detach HEAD~3
Note: switching to 'HEAD~3'.

You are in 'detached HEAD' state...
HEAD is now at a1b2c3d Previous commit message
```

### **-t, --track**

When creating a new branch, set up "upstream" configuration.

```console
$ git switch -c feature-auth --track origin/feature-auth
Branch 'feature-auth' set up to track remote branch 'feature-auth' from 'origin'.
Switched to a new branch 'feature-auth'
```

### **--discard-changes**

Throw away local modifications before switching.

```console
$ git switch --discard-changes main
Switched to branch 'main'
```

### **-m, --merge**

Merge local modifications into the new branch.

```console
$ git switch -m feature-branch
Switched to branch 'feature-branch'
```

### **-**

Switch to the previous branch.

```console
$ git switch -
Switched to branch 'main'
```

## Usage Examples

### Basic Branch Switching

```console
$ git switch main
Switched to branch 'main'
```

### Creating and Switching to a New Branch

```console
$ git switch -c new-feature
Switched to a new branch 'new-feature'
```

### Switching to a Remote Branch

```console
$ git switch feature-branch
Branch 'feature-branch' set up to track remote branch 'feature-branch' from 'origin'.
Switched to a new branch 'feature-branch'
```

## Tips:

### Use `git switch -` to Toggle Between Branches

Similar to `cd -` in Unix, `git switch -` allows you to quickly toggle between the current and previous branch, which is useful during development when you need to frequently switch contexts.

### Prefer `git switch` Over `git checkout` for Branch Operations

`git switch` is more explicit and safer than `git checkout` when working with branches, as it avoids the confusion of `checkout`'s dual purpose (switching branches and restoring files).

### Use `--discard-changes` with Caution

The `--discard-changes` option will discard all local modifications. Make sure you don't need those changes before using this option, as they cannot be recovered.

### Create Tracking Branches Automatically

When switching to a remote branch that doesn't exist locally, Git will automatically create a tracking branch. This saves you from having to use the `-c` and `--track` options explicitly.

## Frequently Asked Questions

#### Q1. What's the difference between `git switch` and `git checkout`?
A. `git switch` focuses solely on branch operations, while `git checkout` has multiple purposes including branch switching and file restoration. `git switch` was introduced to provide clearer, more focused commands.

#### Q2. How do I create a new branch from a specific commit?
A. Use `git switch -c <new-branch> <commit-hash>` to create and switch to a new branch starting from a specific commit.

#### Q3. Can I switch branches with uncommitted changes?
A. Yes, if the changes don't conflict with the target branch. If there are conflicts, Git will prevent the switch. You can use `--discard-changes` to discard modifications or `--merge` to merge them into the target branch.

#### Q4. How do I switch to a remote branch?
A. Simply use `git switch branch-name`. If the branch exists on a remote but not locally, Git will create a tracking branch automatically.

#### Q5. How can I switch to a specific tag?
A. Use `git switch --detach tag-name` to switch to the commit that the tag points to in a detached HEAD state.

## References

https://git-scm.com/docs/git-switch

## Revisions

- 2025/05/04 First revision