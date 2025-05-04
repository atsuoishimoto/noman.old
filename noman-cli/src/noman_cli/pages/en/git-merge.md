# git merge command

Join two or more development histories together.

## Overview

`git merge` combines multiple sequences of commits into one unified history. It's primarily used to integrate changes from one branch into another, typically merging feature branches into the main branch after development is complete. The command incorporates specified branches' changes into the current branch.

## Options

### **-m, --message=\<message\>**

Set the commit message to be used for the merge commit.

```console
$ git merge feature-branch -m "Merge feature branch with new login functionality"
```

### **--no-ff**

Create a merge commit even when the merge resolves as a fast-forward.

```console
$ git merge --no-ff feature-branch
Merge made by the 'recursive' strategy.
 login.js | 75 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 75 insertions(+)
 create mode 100644 login.js
```

### **--ff-only**

Refuse to merge and exit with a non-zero status unless the current HEAD is already up to date or the merge can be resolved as a fast-forward.

```console
$ git merge --ff-only upstream/main
Updating 1234abc..5678def
Fast-forward
 README.md | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)
```

### **--abort**

Abort the current conflict resolution process and try to reconstruct the pre-merge state.

```console
$ git merge feature-branch
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.

$ git merge --abort
```

### **--squash**

Produce the working tree and index state as if a merge happened, but do not actually make a commit or move the HEAD.

```console
$ git merge --squash feature-branch
Updating 1234abc..5678def
Fast-forward
Squash commit -- not updating HEAD
 login.js | 75 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 75 insertions(+)
 create mode 100644 login.js
```

### **-s, --strategy=\<strategy\>**

Use the given merge strategy. Common values are recursive, resolve, octopus, ours, and subtree.

```console
$ git merge -s recursive feature-branch
```

## Usage Examples

### Basic Branch Merge

```console
$ git checkout main
Switched to branch 'main'

$ git merge feature-branch
Updating 1234abc..5678def
Fast-forward
 login.js | 75 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 75 insertions(+)
 create mode 100644 login.js
```

### Merging Multiple Branches

```console
$ git checkout main
Switched to branch 'main'

$ git merge feature1 feature2 feature3
Merge made by the 'octopus' strategy.
 feature1.js | 20 ++++++++++++++++++++
 feature2.js | 15 +++++++++++++++
 feature3.js | 30 ++++++++++++++++++++++++++++++
 3 files changed, 65 insertions(+)
```

### Resolving Merge Conflicts

```console
$ git merge feature-branch
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.

# After manually resolving conflicts in index.html
$ git add index.html
$ git commit
[main 1234abc] Merge branch 'feature-branch'
```

## Tips

### Use `--no-ff` for Feature Branches

When merging feature branches, consider using `--no-ff` to preserve the branch history and make it clear in the commit history that a feature branch was merged.

### Preview Merge Results

Before performing an actual merge, you can preview the changes that would be merged using:
```console
$ git diff ...branch-name
```

### Understand Fast-Forward Merges

A fast-forward merge occurs when the target branch's commits are direct descendants of the current branch. Git simply moves the pointer forward without creating a merge commit. Use `--no-ff` if you want to force a merge commit.

### Squash Merges for Clean History

Use `--squash` when you want to combine all changes from a feature branch into a single commit on the target branch, which can make the commit history cleaner and more readable.

## Frequently Asked Questions

#### Q1. What is the difference between merge and rebase?
A. Merge creates a new commit that combines changes from both branches, preserving the branch history. Rebase replays your branch's commits on top of the target branch, creating a linear history but rewriting commit history.

#### Q2. How do I undo a merge?
A. If you haven't pushed the merge, use `git reset --hard HEAD~1` to undo the last commit. If you've already pushed, consider using `git revert -m 1 <merge-commit-hash>` to create a new commit that undoes the merge.

#### Q3. What does "fast-forward" mean in Git merge?
A. A fast-forward merge occurs when there are no new commits on the base branch since the feature branch was created. Git simply moves the base branch pointer forward to the feature branch pointer without creating a merge commit.

#### Q4. How do I resolve merge conflicts?
A. When Git reports conflicts, edit the conflicted files to resolve the differences, then use `git add` to mark them as resolved, and finally `git commit` to complete the merge.

## References

https://git-scm.com/docs/git-merge

## Revisions

- 2025/05/04 First revision