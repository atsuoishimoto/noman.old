# git rebase command

Reapply commits on top of another base tip, rewriting the commit history.

## Overview

`git rebase` is used to change the base of your branch from one commit to another, making it appear as if you created your branch from a different commit. This rewrites the commit history by creating new commits for each commit in the original branch, resulting in a linear, cleaner project history.

## Options

### **-i, --interactive**

Opens an editor allowing you to edit, squash, reorder, or delete commits before rebasing.

```console
$ git rebase -i HEAD~3
# An editor opens with the last 3 commits listed
# pick f7f3f6d Change feature A
# pick 310154e Fix typo in feature A
# pick a5f4a0d Add feature B
```

### **--onto \<newbase\>**

Specifies the new base commit to reapply your changes onto.

```console
$ git rebase --onto main feature-branch~3 feature-branch
# Moves commits from feature-branch onto main, excluding the first 3 commits
```

### **--continue**

Continues the rebase operation after resolving conflicts.

```console
$ git rebase --continue
# After fixing conflicts and adding the resolved files
```

### **--abort**

Cancels the rebase operation and returns the branch to its original state.

```console
$ git rebase --abort
# Stops the rebase and restores the original branch state
```

## Usage Examples

### Basic Rebasing

```console
$ git checkout feature-branch
$ git rebase main
# Reapplies commits from feature-branch on top of main
```

### Interactive Rebasing to Squash Commits

```console
$ git rebase -i HEAD~4
# In the editor, change some "pick" commands to "squash" or "s"
# pick 01d1124 Add feature X
# squash 6340aaa Fix bug in feature X
# squash ebfd367 Improve feature X
# pick 30e0ccb Add feature Y
```

### Moving a Branch to a Different Base

```console
$ git rebase --onto release-branch old-base feature-branch
# Moves commits between old-base and feature-branch onto release-branch
```

## Tips

### Always Rebase Before Pushing

Rebase your local branch before pushing to avoid creating unnecessary merge commits in the shared repository. However, never rebase commits that have already been pushed to a public repository unless you're absolutely sure no one has based work on them.

### Create a Backup Branch

Before performing a complex rebase, create a backup branch:
```console
$ git branch backup-branch
```

### Resolving Conflicts During Rebase

When conflicts occur, Git pauses the rebase. Resolve conflicts in each file, then:
```console
$ git add <resolved-file>
$ git rebase --continue
```

## Frequently Asked Questions

#### Q1. What's the difference between merge and rebase?
A. Merge preserves history and creates a merge commit, while rebase rewrites history by creating new commits, resulting in a linear history.

#### Q2. When should I avoid using rebase?
A. Avoid rebasing commits that have been pushed to a public repository and might have been pulled by others, as it rewrites history and can cause conflicts for collaborators.

#### Q3. How do I undo a rebase?
A. If you haven't pushed the rebased commits, use `git reflog` to find the commit before the rebase and then `git reset --hard <commit-hash>` to return to that state.

#### Q4. Can I rebase only part of my branch?
A. Yes, using `git rebase -i <commit>` you can select which commits to include and how to handle each one.

## References

https://git-scm.com/docs/git-rebase

## Revisions

- 2025/04/30 First revision