# git commit command

Record changes to the repository by saving staged content as a new commit.

## Overview

The `git commit` command captures a snapshot of the project's currently staged changes. Committed snapshots are considered "safe" versions of a project and can be viewed, restored, or compared at any time. Commits are the core building blocks in a Git project's timeline.

## Options

### **-m, --message**

Add a commit message directly from the command line, avoiding the text editor prompt.

```console
$ git commit -m "Add new login feature"
[main 5d7e9f4] Add new login feature
 1 file changed, 15 insertions(+), 2 deletions(-)
```

### **-a, --all**

Automatically stage all modified and deleted files before committing (does not include new files).

```console
$ git commit -a -m "Update documentation"
[main 8f3d12c] Update documentation
 2 files changed, 24 insertions(+), 5 deletions(-)
```

### **--amend**

Replace the most recent commit with a new one that includes current staged changes.

```console
$ git commit --amend -m "Fix typo in previous commit"
[main 7a2e9d1] Fix typo in previous commit
 Date: Wed Apr 30 10:15:32 2025 -0700
 1 file changed, 2 insertions(+), 1 deletion(-)
```

### **-v, --verbose**

Show the diff of changes to be committed in the commit message editor.

```console
$ git commit -v
# Opens editor with diff included in the commit message template
```

## Usage Examples

### Basic commit with editor for message

```console
$ git add file.txt
$ git commit
# Opens text editor for commit message
[main 3a4b5c6] Add important file
 1 file changed, 10 insertions(+)
```

### Commit with message and skip staging

```console
$ git commit -am "Fix bug in login form"
[main 1b2c3d4] Fix bug in login form
 2 files changed, 7 insertions(+), 3 deletions(-)
```

### Commit only specific files

```console
$ git add src/login.js src/auth.js
$ git commit -m "Improve authentication flow"
[main 9e8d7f6] Improve authentication flow
 2 files changed, 32 insertions(+), 15 deletions(-)
```

## Tips

### Write Meaningful Commit Messages

Use the present tense ("Add feature" not "Added feature") and keep the first line under 50 characters. Add more detailed explanations after a blank line if needed.

### Use Atomic Commits

Make each commit a logical unit of change. This makes it easier to understand, review, and revert changes if necessary.

### Check What You're Committing

Use `git diff --staged` before committing to review exactly what changes will be included in your commit.

### Sign Your Commits

For security and verification, you can sign commits with your GPG key using `git commit -S`.

## Frequently Asked Questions

#### Q1. How do I undo my last commit?
A. Use `git reset HEAD~1` to undo the commit but keep the changes staged, or `git reset --hard HEAD~1` to discard the changes completely.

#### Q2. How can I change my commit message after committing?
A. Use `git commit --amend` to modify the most recent commit message.

#### Q3. What's the difference between `git commit` and `git push`?
A. `git commit` records changes to your local repository, while `git push` uploads your local commits to a remote repository.

#### Q4. Can I commit directly without staging files first?
A. Yes, using `git commit -a` will automatically stage all modified and deleted files (but not new files) before committing.

## References

https://git-scm.com/docs/git-commit

## Revisions

- 2025/04/30 First revision