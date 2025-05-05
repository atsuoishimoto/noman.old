# git-branch command

Lists, creates, or deletes branches in a Git repository.

## Overview

The `git branch` command is used to manage branches in a Git repository. It allows you to list existing branches, create new branches, rename branches, and delete branches. Branches are lightweight movable pointers to commits, making them essential for parallel development workflows.

## Options

### **-a, --all**

List both remote-tracking branches and local branches.

```console
$ git branch -a
* main
  feature-login
  remotes/origin/main
  remotes/origin/feature-login
```

### **-r, --remotes**

List or delete remote-tracking branches.

```console
$ git branch -r
  origin/main
  origin/feature-login
  origin/dev
```

### **-v, --verbose**

Show SHA-1 and commit subject line for each branch.

```console
$ git branch -v
* main        a72f324 Update README.md
  feature-login 8d3e5c1 Implement login functionality
```

### **-d, --delete**

Delete a branch. The branch must be fully merged in its upstream branch.

```console
$ git branch -d feature-login
Deleted branch feature-login (was 8d3e5c1).
```

### **-D**

Force delete a branch even if it's not fully merged.

```console
$ git branch -D unmerged-branch
Deleted branch unmerged-branch (was 7c3a9f2).
```

### **-m, --move**

Move/rename a branch and its reflog.

```console
$ git branch -m old-branch-name new-branch-name
```

### **--list**

List branches. With optional pattern, e.g., `git branch --list 'feature-*'`.

```console
$ git branch --list 'feature-*'
  feature-login
  feature-signup
  feature-dashboard
```

## Usage Examples

### Creating a new branch

```console
$ git branch new-feature
$ git branch
* main
  new-feature
```

### Creating and switching to a new branch

```console
$ git branch new-feature
$ git checkout new-feature
Switched to branch 'new-feature'

# Or more concisely with git checkout -b
$ git checkout -b new-feature
Switched to a new branch 'new-feature'
```

### Viewing all branches with commit information

```console
$ git branch -av
* main                  a72f324 [ahead 2] Update README.md
  feature-login         8d3e5c1 Implement login functionality
  remotes/origin/main   3e4f2a1 Initial commit
  remotes/origin/dev    9c2d1b3 Fix bug in API
```

## Tips:

### Use Branch Descriptions

You can add descriptions to branches using `git branch --edit-description`. This is helpful for documenting the purpose of long-lived branches.

### Clean Up Remote-Tracking Branches

Use `git fetch --prune` to clean up deleted remote branches. This removes remote-tracking branches that no longer exist on the remote.

### Identify Merged Branches

Use `git branch --merged` to list branches that have been merged into the current branch. This helps identify branches that can be safely deleted.

### Branch Naming Conventions

Follow a consistent naming convention for branches, such as `feature/login`, `bugfix/header`, or `hotfix/security-issue`. This helps organize branches by their purpose.

## Frequently Asked Questions

#### Q1. How do I create a new branch?
A. Use `git branch <branch-name>` to create a new branch. Note that this only creates the branch but doesn't switch to it.

#### Q2. How do I delete a branch?
A. Use `git branch -d <branch-name>` to delete a branch that has been fully merged, or `git branch -D <branch-name>` to force delete a branch regardless of its merge status.

#### Q3. How do I rename a branch?
A. Use `git branch -m <old-name> <new-name>` to rename a branch. If you're on the branch you want to rename, you can simply use `git branch -m <new-name>`.

#### Q4. How do I see which branches are merged into the current branch?
A. Use `git branch --merged` to see which branches have been merged into the current branch.

#### Q5. How do I list remote branches?
A. Use `git branch -r` to list remote-tracking branches.

## References

https://git-scm.com/docs/git-branch

## Revisions

- 2025/05/04 First revision