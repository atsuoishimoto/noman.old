# git commit command

Record changes to the repository by creating a new commit containing the current contents of the index.

## Overview

The `git commit` command captures a snapshot of the project's currently staged changes. Committed snapshots are "safe" versions of a project that Git will never change unless explicitly asked to do so. Before committing, changes must be staged using `git add`.

## Options

### **-m, --message=\<msg\>**

Use the given message as the commit message instead of launching an editor.

```console
$ git commit -m "Add new feature"
[main 5d6e7f8] Add new feature
 1 file changed, 10 insertions(+), 2 deletions(-)
```

### **-a, --all**

Automatically stage all modified and deleted files before committing (does not include untracked files).

```console
$ git commit -a -m "Update existing files"
[main 1a2b3c4] Update existing files
 2 files changed, 5 insertions(+), 3 deletions(-)
```

### **--amend**

Replace the tip of the current branch with a new commit, using the same log message as the previous commit or a new one.

```console
$ git commit --amend -m "Fix typo in previous commit"
[main 8f9g0h1] Fix typo in previous commit
 Date: Mon May 4 10:23:45 2025 -0700
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### **-v, --verbose**

Show the diff of changes to be committed in the commit message editor.

```console
$ git commit -v
# Opens editor with diff included in the commit message template
```

### **--no-verify**

Bypass the pre-commit and commit-msg hooks.

```console
$ git commit --no-verify -m "Emergency fix"
[main 2c3d4e5] Emergency fix
 1 file changed, 3 insertions(+)
```

## Usage Examples

### Creating a standard commit

```console
$ git add file1.txt file2.txt
$ git commit -m "Add new files"
[main 1a2b3c4] Add new files
 2 files changed, 15 insertions(+)
```

### Committing all tracked changes

```console
$ git commit -am "Update documentation"
[main 5e6f7g8] Update documentation
 3 files changed, 25 insertions(+), 10 deletions(-)
```

### Amending the previous commit with new changes

```console
$ git add forgotten_file.txt
$ git commit --amend
[main 1a2b3c4] Add new files
 Date: Mon May 4 09:15:32 2025 -0700
 3 files changed, 18 insertions(+)
```

## Tips

### Write Meaningful Commit Messages

Good commit messages should explain what changes were made and why. Use the present tense ("Add feature" not "Added feature") and keep the first line under 50 characters.

### Use Atomic Commits

Make each commit a logical unit of work. This makes it easier to understand, review, and revert changes if needed.

### Check What You're Committing

Use `git diff --staged` before committing to review exactly what will be included in your commit.

### Sign Your Commits

For security and verification, you can sign commits with your GPG key using `git commit -S`.

## Frequently Asked Questions

#### Q1. How do I undo my last commit?
A. Use `git reset HEAD~1` to undo the commit but keep the changes staged, or `git reset --hard HEAD~1` to discard the changes completely.

#### Q2. How can I change my commit message after committing?
A. If you haven't pushed yet, use `git commit --amend` to modify the most recent commit message.

#### Q3. What's the difference between `git commit` and `git commit -a`?
A. `git commit` only commits changes that have been staged with `git add`, while `git commit -a` automatically stages and commits all modified tracked files.

#### Q4. Can I commit directly without staging first?
A. Yes, using `git commit -a`, but this only works for files that are already tracked (previously added to the repository).

#### Q5. How do I commit only part of a file?
A. Use `git add -p` to interactively select which changes to stage, then commit normally.

## References

https://git-scm.com/docs/git-commit

## Revisions

- 2025/05/04 First revision