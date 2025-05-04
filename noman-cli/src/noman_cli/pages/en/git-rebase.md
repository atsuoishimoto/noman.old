# git-rebase command

Reapply commits on top of another base tip.

## Overview

`git rebase` is used to change the base of your branch from one commit to another, making it appear as if you created your branch from a different commit. This rewrites the commit history by creating new commits for each commit in the original branch, resulting in a linear project history.

## Options

### **-i, --interactive**

Allows you to edit commits during the rebase process, including reordering, editing, squashing, or dropping commits.

```console
$ git rebase -i HEAD~3
# An editor will open with something like:
# pick f7f3f6d Change feature A
# pick 310154e Fix typo in feature A
# pick a5f4a0d Add feature B
```

### **--onto \<newbase\>**

Specifies the new base commit onto which the commits will be replayed.

```console
$ git rebase --onto main feature-branch~3 feature-branch
# Moves commits from feature-branch~3 to feature-branch onto main
```

### **--continue**

Continues the rebase operation after resolving conflicts.

```console
$ git rebase --continue
# After resolving conflicts and adding the changes
```

### **--abort**

Aborts the rebase operation and returns the branch to its original state.

```console
$ git rebase --abort
# Cancels the rebase and restores the original branch state
```

### **--skip**

Skips the current commit and continues with the next one.

```console
$ git rebase --skip
# Skips the current problematic commit
```

## Usage Examples

### Basic Rebasing

```console
$ git checkout feature-branch
$ git rebase main
# Rebases feature-branch onto the latest main
```

### Interactive Rebase to Squash Commits

```console
$ git rebase -i HEAD~4
# In the editor, change some "pick" lines to "squash" or "s"
# pick 01d1124 Add feature X
# squash 6340aaa Fix bug in feature X
# squash ebfd367 Improve feature X
# pick 30e0ccb Add feature Y
```

### Moving a Branch to a Different Base

```console
$ git rebase --onto new-base old-base branch-to-move
# Moves commits between old-base and branch-to-move onto new-base
```

## Tips

### Always Rebase Before Pushing

Rebase your local branch before pushing to ensure a clean history. However, never rebase commits that have already been pushed to a shared repository unless you're absolutely sure no one else has based work on them.

### Create a Backup Branch

Before performing a complex rebase, create a backup branch:

```console
$ git branch backup-branch
```

### Resolving Conflicts During Rebase

When conflicts occur, Git pauses the rebase. Resolve conflicts, then:

```console
$ git add <resolved-files>
$ git rebase --continue
```

### Using Autosquash

When making fixup commits, use `--fixup` and later rebase with `--autosquash`:

```console
$ git commit --fixup <commit-hash>
$ git rebase -i --autosquash <base>
```

## Frequently Asked Questions

#### Q1. What's the difference between merge and rebase?
A. Merge preserves history and creates a merge commit, while rebase rewrites history by creating new commits, resulting in a linear history.

#### Q2. When should I avoid using rebase?
A. Avoid rebasing commits that have been pushed to a public repository and might have been pulled by others, as it rewrites history and can cause conflicts for collaborators.

#### Q3. How do I undo a rebase?
A. If you haven't pushed the rebased commits, use `git reflog` to find the commit before the rebase and then `git reset --hard <commit-hash>` to return to that state.

#### Q4. Can I rebase multiple branches at once?
A. No, you need to rebase each branch separately.

#### Q5. How do I resolve complex conflicts during a rebase?
A. Resolve conflicts in each file, `git add` the resolved files, and then use `git rebase --continue`. If a particular commit is too problematic, you can use `git rebase --skip` to skip it.

## References

https://git-scm.com/docs/git-rebase

## Revisions

- 2025/05/04 First revision