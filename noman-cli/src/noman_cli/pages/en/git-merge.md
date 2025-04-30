# git merge command

Combines changes from different branches into the current branch.

## Overview

`git merge` integrates changes from one branch into another. It's commonly used to incorporate completed features into the main branch or to update a feature branch with the latest changes from the main branch. The command creates a new commit that combines the histories of the merged branches.

## Options

### **--no-ff** (No Fast-Forward)

Forces creation of a merge commit even when a fast-forward merge would be possible, preserving branch history

```console
$ git merge --no-ff feature-branch
Merge made by the 'recursive' strategy.
 file.txt | 5 +++++
 1 file changed, 5 insertions(+)
```

### **--ff-only** (Fast-Forward Only)

Refuses to merge unless the current branch can be fast-forwarded to the target branch

```console
$ git merge --ff-only upstream/main
Updating 1234abc..5678def
Fast-forward
 README.md | 10 +++++++---
 1 file changed, 7 insertions(+), 3 deletions(-)
```

### **--squash**

Combines all changes from the target branch into a single commit, without recording the merge history

```console
$ git merge --squash feature-branch
Squash commit -- not updating HEAD
Automatic merge went well; stopped before committing as requested
$ git commit -m "Implement feature X"
[main 1234abc] Implement feature X
 2 files changed, 15 insertions(+), 5 deletions(-)
```

### **--abort**

Aborts the current merge and returns to the state before the merge began

```console
$ git merge feature-branch
Auto-merging file.txt
CONFLICT (content): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.
$ git merge --abort
```

## Usage Examples

### Basic Merge

```console
$ git checkout main
Switched to branch 'main'
$ git merge feature-branch
Updating 1234abc..5678def
Fast-forward
 file.txt | 10 ++++++++--
 1 file changed, 8 insertions(+), 2 deletions(-)
```

### Merging with Conflicts

```console
$ git merge feature-branch
Auto-merging file.txt
CONFLICT (content): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.
$ vim file.txt  # Edit file to resolve conflicts
$ git add file.txt
$ git commit -m "Merge feature-branch, resolve conflicts"
[main 1234abc] Merge feature-branch, resolve conflicts
```

### Merging Remote Branch

```console
$ git fetch origin
remote: Counting objects: 15, done.
remote: Compressing objects: 100% (5/5), done.
Unpacking objects: 100% (10/10), done.
$ git merge origin/feature-branch
Merge made by the 'recursive' strategy.
 file.txt | 7 +++++++
 1 file changed, 7 insertions(+)
```

## Tips

### Preview Merge Results

Use `git merge --no-commit --no-ff branch-name` to see what would happen in a merge without actually committing. You can then either commit with `git commit` or abort with `git merge --abort`.

### Understand Merge Strategies

Git uses different merge strategies depending on the situation. The default "recursive" strategy works well for most cases, but for specific scenarios, you might want to use `--strategy=ours` or `--strategy=theirs` to automatically prefer one side's changes.

### Keep Branches Updated

Regularly merge the main branch into your feature branches to reduce the likelihood of complex merge conflicts later.

### Use Merge Tools for Complex Conflicts

For complex merge conflicts, visual merge tools can be helpful. Configure one with `git config --global merge.tool <toolname>` and invoke it with `git mergetool`.

## Frequently Asked Questions

#### Q1. What's the difference between merge and rebase?
A. Merge creates a new commit that combines histories, preserving the branch structure. Rebase replays your branch's commits on top of the target branch, creating a linear history but altering commit hashes.

#### Q2. How do I undo a merge?
A. If you haven't pushed the merge, use `git reset --hard HEAD~1` to undo the last commit. If you've pushed, consider using `git revert -m 1 <merge-commit-hash>` to create a new commit that undoes the merge.

#### Q3. What does "fast-forward merge" mean?
A. A fast-forward merge occurs when the target branch is a direct descendant of the current branch. Git simply moves the branch pointer forward, without creating a new merge commit.

#### Q4. How do I resolve merge conflicts?
A. Edit the conflicted files manually (look for the `<<<<<<<`, `=======`, and `>>>>>>>` markers), then `git add` the resolved files and complete the merge with `git commit`.

## References

https://git-scm.com/docs/git-merge

## Revisions

- 2025/04/30 First revision