# git command

Distributed version control system for tracking changes in source code during software development.

## Overview

Git is a distributed version control system that allows multiple developers to work on a project simultaneously. It tracks changes to files, maintains a history of modifications, and facilitates collaboration by enabling users to merge changes from different sources. Git operates primarily through a local repository, with the ability to synchronize with remote repositories.

## Options

### **-v, --version**

Display the version of Git installed

```console
$ git --version
git version 2.39.2
```

### **-h, --help**

Display help information for Git or a specific Git command

```console
$ git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]
```

### **-C, --work-tree=<path>**

Run a command as if git was started in the specified path

```console
$ git -C /path/to/repository status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### **-c, --config-env=<name>=<value>**

Set a configuration variable for a single command

```console
$ git -c user.name="Temporary User" commit -m "One-time commit with different user"
[main 1a2b3c4] One-time commit with different user
 1 file changed, 5 insertions(+)
```

## Usage Examples

### Initializing a new repository

```console
$ git init
Initialized empty Git repository in /path/to/project/.git/
```

### Cloning an existing repository

```console
$ git clone https://github.com/username/repository.git
Cloning into 'repository'...
remote: Enumerating objects: 1463, done.
remote: Counting objects: 100% (1463/1463), done.
remote: Compressing objects: 100% (750/750), done.
remote: Total 1463 (delta 713), reused 1463 (delta 713), pack-reused 0
Receiving objects: 100% (1463/1463), 2.56 MiB | 5.12 MiB/s, done.
Resolving deltas: 100% (713/713), done.
```

### Basic workflow example

```console
$ git add file.txt
$ git commit -m "Add new file"
[main 1a2b3c4] Add new file
 1 file changed, 10 insertions(+)
 create mode 100644 file.txt
$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/username/repository.git
   a1b2c3d..1a2b3c4  main -> main
```

### Checking repository status

```console
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

## Tips

### Configure Your Identity

Set your name and email before making commits:

```console
$ git config --global user.name "Your Name"
$ git config --global user.email "your.email@example.com"
```

### Create Aliases for Common Commands

Save time by creating shortcuts for frequently used commands:

```console
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.st status
```

### Use .gitignore Files

Create a `.gitignore` file in your repository to specify files that Git should ignore, such as build artifacts, temporary files, or sensitive information.

### Commit Atomically

Make small, focused commits that address a single logical change rather than large commits that mix multiple unrelated changes.

## Frequently Asked Questions

#### Q1. How do I undo my last commit?
A. Use `git reset HEAD~1` to undo the commit but keep the changes, or `git reset --hard HEAD~1` to discard the changes completely.

#### Q2. How do I create a new branch?
A. Use `git branch branch-name` to create a branch, then `git checkout branch-name` to switch to it. Alternatively, use `git checkout -b branch-name` to create and switch in one command.

#### Q3. How do I merge changes from one branch to another?
A. First checkout the target branch with `git checkout target-branch`, then merge with `git merge source-branch`.

#### Q4. How do I resolve merge conflicts?
A. When conflicts occur, edit the conflicted files to resolve the differences, then use `git add` to mark them as resolved, and finally `git commit` to complete the merge.

#### Q5. How do I update my local repository with changes from remote?
A. Use `git pull` to fetch and merge changes, or `git fetch` followed by `git merge` for more control.

## References

https://git-scm.com/docs/git

## Revisions

2025/05/04 First revision