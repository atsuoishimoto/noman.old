# git command

Manage source code and track changes in files with a distributed version control system.

## Overview

Git is a distributed version control system that tracks changes in files, allowing multiple people to collaborate on projects. It maintains a history of file changes, enables branching and merging of code, and facilitates both local and remote repository management. Git helps developers track, compare, and revert changes while working independently or collaboratively.

## Options

### **init**

Creates a new Git repository in the current directory

```console
$ git init
Initialized empty Git repository in /path/to/project/.git/
```

### **clone**

Creates a copy of a remote repository on your local machine

```console
$ git clone https://github.com/username/repository.git
Cloning into 'repository'...
remote: Enumerating objects: 125, done.
remote: Counting objects: 100% (125/125), done.
remote: Compressing objects: 100% (80/80), done.
remote: Total 125 (delta 58), reused 95 (delta 37)
Receiving objects: 100% (125/125), 2.31 MiB | 3.15 MiB/s, done.
Resolving deltas: 100% (58/58), done.
```

### **status**

Shows the current state of your working directory and staging area

```console
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        new-file.txt
```

### **add**

Adds file changes to the staging area for the next commit

```console
$ git add README.md
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```

### **commit**

Records staged changes to the repository with a descriptive message

```console
$ git commit -m "Update README with installation instructions"
[main 5d7e9f4] Update README with installation instructions
 1 file changed, 15 insertions(+), 2 deletions(-)
```

### **log**

Shows the commit history

```console
$ git log
commit 5d7e9f4a9e7d4a7e9f4a9e7d4a7e9f4a9e7d4a7e (HEAD -> main)
Author: Your Name <your.email@example.com>
Date:   Wed Apr 30 10:15:32 2025 -0700

    Update README with installation instructions

commit a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2
Author: Your Name <your.email@example.com>
Date:   Tue Apr 29 15:42:10 2025 -0700

    Initial commit
```

## Usage Examples

### Creating and committing to a new repository

```console
$ mkdir my-project
$ cd my-project
$ git init
Initialized empty Git repository in /path/to/my-project/.git/
$ echo "# My Project" > README.md
$ git add README.md
$ git commit -m "Initial commit"
[main (root-commit) a1b2c3d] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

### Working with branches

```console
$ git branch feature-login
$ git switch feature-login
Switched to branch 'feature-login'
$ echo "function login() {}" > login.js
$ git add login.js
$ git commit -m "Add login functionality"
[feature-login 3e4f5g6] Add login functionality
 1 file changed, 1 insertion(+)
 create mode 100644 login.js
$ git switch main
Switched to branch 'main'
$ git merge feature-login
Updating a1b2c3d..3e4f5g6
Fast-forward
 login.js | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 login.js
```

### Working with remote repositories

```console
$ git remote add origin https://github.com/username/my-project.git
$ git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 253 bytes | 253.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/username/my-project.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

## Tips

### Use Meaningful Commit Messages

Write clear, concise commit messages that explain what changes were made and why. This helps team members understand the history of the project.

### Commit Often

Make small, focused commits rather than large, sweeping changes. This makes it easier to track down issues and understand the evolution of your code.

### Use Branches for Features and Fixes

Create separate branches for new features or bug fixes. This keeps your main branch stable while you work on experimental changes.

### Stash Uncommitted Changes

Use `git stash` to temporarily save changes you're not ready to commit when you need to switch branches or pull updates.

### Configure Global Settings

Set up your identity with `git config --global user.name "Your Name"` and `git config --global user.email "your.email@example.com"` to ensure your commits are properly attributed.

## Frequently Asked Questions

#### Q1. How do I undo my last commit?
A. Use `git reset HEAD~1` to undo the commit but keep the changes in your working directory. Use `git reset --hard HEAD~1` to discard the commit and its changes completely.

#### Q2. How do I resolve merge conflicts?
A. When Git reports a conflict, open the affected files (marked with conflict markers), edit them to resolve the conflicts, then use `git add` to mark them as resolved, and finally `git commit` to complete the merge.

#### Q3. How do I update my local repository with changes from the remote?
A. Use `git pull` to fetch and merge changes from the remote repository, or `git fetch` followed by `git merge` for more control over the process.

#### Q4. How do I create a new branch and switch to it?
A. Use `git switch -c new-branch-name` or the older command `git checkout -b new-branch-name`.

#### Q5. How do I discard local changes to a file?
A. Use `git restore filename` to discard changes in your working directory, or `git restore --staged filename` to unstage changes.

## References

https://git-scm.com/doc

## Revisions

2025/04/30 First revision