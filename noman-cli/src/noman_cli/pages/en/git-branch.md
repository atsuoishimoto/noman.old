# git branch command

List, create, or delete branches in a Git repository.

## Overview

The `git branch` command allows you to manage branches in your Git repository. Branches are independent lines of development that let you work on features or fixes without affecting the main codebase. You can create new branches, list existing ones, rename them, or delete branches that are no longer needed.

## Options

### **-a, --all**

List all branches, including remote-tracking branches

```console
$ git branch -a
* main
  feature/login
  remotes/origin/main
  remotes/origin/feature/login
```

### **-v, --verbose**

Show commit hash and subject line for each branch

```console
$ git branch -v
* main        a72f4e2 Add documentation
  feature/login 8d3e5f1 Implement login form
```

### **-d, --delete**

Delete a branch (safe version that prevents deletion of unmerged branches)

```console
$ git branch -d feature/completed
Deleted branch feature/completed (was 8d3e5f1).
```

### **-D**

Force delete a branch, even if it contains unmerged changes

```console
$ git branch -D feature/abandoned
Deleted branch feature/abandoned (was 7c2d9a3).
```

### **-m, --move**

Rename a branch

```console
$ git branch -m old-name new-name
```

## Usage Examples

### Creating a new branch

```console
$ git branch feature/user-authentication
$ git branch
* main
  feature/user-authentication
```

### Creating and switching to a new branch

```console
$ git checkout -b feature/payment-gateway
Switched to a new branch 'feature/payment-gateway'
```

### Listing branches with more information

```console
$ git branch -vv
* main                a72f4e2 [origin/main] Add documentation
  feature/login       8d3e5f1 [origin/feature/login] Implement login form
  feature/signup      3b2c1a5 Add signup validation
```

### Deleting multiple branches

```console
$ git branch -d feature/completed feature/obsolete
Deleted branch feature/completed (was 8d3e5f1).
Deleted branch feature/obsolete (was 2c4b6a8).
```

## Tips

### Use Descriptive Branch Names

Use meaningful branch names that describe the feature or fix you're working on. Names like `feature/user-authentication` or `bugfix/login-error` are more informative than generic names like `new-stuff`.

### Clean Up Merged Branches

Regularly delete branches that have been merged to keep your repository clean. Use `git branch --merged` to see which branches have been fully merged into your current branch.

### Track Remote Branches

When collaborating with others, use `git branch -r` to see remote branches, and `git checkout -b local-name origin/remote-name` to create a local branch that tracks a remote branch.

### Protect Your Main Branch

Avoid making direct changes to your main branch. Instead, create feature branches for development and merge them back when they're ready.

## Frequently Asked Questions

#### Q1. How do I create a new branch?
A. Use `git branch branch-name` to create a new branch, or `git checkout -b branch-name` to create and switch to it in one command.

#### Q2. How do I delete a branch?
A. Use `git branch -d branch-name` to safely delete a merged branch, or `git branch -D branch-name` to force delete an unmerged branch.

#### Q3. How can I see which branches are already merged?
A. Use `git branch --merged` to see branches that have been merged into your current branch.

#### Q4. How do I rename a branch?
A. Use `git branch -m old-name new-name` to rename a branch. If you want to rename the current branch, you can simply use `git branch -m new-name`.

#### Q5. How do I push a new local branch to the remote repository?
A. After creating a local branch, use `git push -u origin branch-name` to push it to the remote and set up tracking.

## References

https://git-scm.com/docs/git-branch

## Revisions

- 2025/04/30 First revision