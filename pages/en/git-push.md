# git push command

Send local branch commits to a remote repository.

## Overview

`git push` uploads your local repository content to a remote repository. It transfers commits, branches, and tags from your local repository to update the corresponding remote repository, making your changes available to others.

## Options

### **-u, --set-upstream**

Set up tracking relationship between local and remote branch, allowing future pushes without specifying the remote branch.

```console
$ git push -u origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### **--force, -f**

Force update the remote branch with your local branch, even if it results in a non-fast-forward merge. Use with caution as it can overwrite remote changes.

```console
$ git push --force origin feature
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
 + a1b2c3d...e4f5g6h feature -> feature (forced update)
```

### **--tags**

Push all local tags to the remote repository.

```console
$ git push --tags
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 160 bytes | 160.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:username/repository.git
 * [new tag]         v1.0.0 -> v1.0.0
 * [new tag]         v1.1.0 -> v1.1.0
```

### **--delete**

Delete a remote branch or tag.

```console
$ git push origin --delete old-feature
To github.com:username/repository.git
 - [deleted]         old-feature
```

## Usage Examples

### Basic push to remote

```console
$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  main -> main
```

### Push all branches to remote

```console
$ git push --all origin
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 594 bytes | 594.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  main -> main
   b2c3d4e..f5g6h7i  feature -> feature
```

## Tips

### Use `git push -u` for New Branches

When pushing a new branch for the first time, use `-u` to set up tracking. This allows you to use `git pull` and `git push` without specifying the remote and branch names in the future.

### Check Remote Status Before Pushing

Run `git fetch` followed by `git status` before pushing to see if your local branch is behind the remote. This helps avoid merge conflicts.

### Use `--force-with-lease` Instead of `--force`

`--force-with-lease` is safer than `--force` as it ensures you don't overwrite others' changes that you haven't seen yet.

```console
$ git push --force-with-lease origin feature
```

### Push to Multiple Remotes

You can configure a branch to push to multiple remotes simultaneously by setting up multiple push URLs:

```console
$ git remote set-url --add --push origin git@github.com:username/repository.git
$ git remote set-url --add --push origin git@gitlab.com:username/repository.git
```

## Frequently Asked Questions

#### Q1. What's the difference between `git push` and `git push origin main`?
A. `git push` without arguments pushes the current branch to its upstream branch. `git push origin main` explicitly pushes the local main branch to the main branch on the origin remote.

#### Q2. How do I push a new local branch to a remote repository?
A. Use `git push -u origin branch-name` to push and set up tracking for a new branch.

#### Q3. I get a "non-fast-forward updates were rejected" error. What does it mean?
A. This means the remote branch has commits that your local branch doesn't have. You need to pull the remote changes first with `git pull` or use `--force` if you're sure you want to overwrite remote changes.

#### Q4. How can I push only specific commits?
A. You can't push specific commits directly. Instead, create a new branch at the desired commit with `git checkout -b new-branch commit-hash`, then push that branch.

#### Q5. How do I undo a push?
A. You can revert the changes with `git revert` and push the revert, or use `git reset` to move back to a previous commit and then force push with `git push --force`.

## References

https://git-scm.com/docs/git-push

## Revisions

- 2025/04/30 First revision