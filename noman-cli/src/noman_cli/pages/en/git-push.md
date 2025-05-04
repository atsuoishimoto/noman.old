# git push command

Update remote references along with associated objects.

## Overview

`git push` sends local branch commits to the corresponding remote repository. It updates remote references (like branches and tags) and transfers the necessary objects to keep repositories in sync. This command is essential for sharing your work with others or backing up your local changes to a remote repository.

## Options

### **-u, --set-upstream**

Set upstream for the current branch, allowing future pushes to use the same remote branch without specifying it again.

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

### **-f, --force**

Force update the remote branch with your local branch, even if it results in a non-fast-forward update. Use with caution as it can overwrite changes on the remote.

```console
$ git push -f origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
 + a1b2c3d...e4f5g6h main -> main (forced update)
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

Delete the specified branch from the remote repository.

```console
$ git push origin --delete feature-branch
To github.com:username/repository.git
 - [deleted]         feature-branch
```

### **--dry-run**

Show what would be done, without actually pushing anything.

```console
$ git push --dry-run origin main
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  main -> main
```

## Usage Examples

### Pushing to the default remote branch

```console
$ git push
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

### Pushing a specific branch to a specific remote

```console
$ git push origin feature-branch
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  feature-branch -> feature-branch
```

### Pushing a local branch to a differently named remote branch

```console
$ git push origin local-branch:remote-branch
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:username/repository.git
   a1b2c3d..e4f5g6h  local-branch -> remote-branch
```

## Tips

### Set Up Tracking Branches

When creating a new branch, use `git push -u origin branch-name` to set up tracking. This allows you to use `git pull` and `git push` without specifying the remote and branch each time.

### Push All Branches

Use `git push --all origin` to push all your local branches to the remote repository. This is useful when you want to back up all your work.

### Handle Rejected Pushes

If your push is rejected because the remote contains work you don't have locally, use `git pull` to integrate the remote changes before pushing again. Alternatively, if you're certain your changes should take precedence, use `git push --force` (with caution).

### Push Only Specific Commits

To push only specific commits up to a certain point, use `git push origin <commit-hash>:branch-name`. This is useful when you want to share only part of your work.

## Frequently Asked Questions

#### Q1. What's the difference between `git push` and `git push origin main`?
A. `git push` pushes the current branch to its upstream branch if configured. `git push origin main` explicitly pushes the local main branch to the main branch on the origin remote, regardless of which branch you're currently on.

#### Q2. How do I push a new local branch to the remote repository?
A. Use `git push -u origin branch-name` to push the new branch and set up tracking.

#### Q3. How can I undo a push?
A. You can't directly "undo" a push. Instead, you need to revert the changes locally (using `git revert` or `git reset`) and then push the new state with `git push --force`. Be cautious with force pushing as it can overwrite others' work.

#### Q4. Why does my push get rejected?
A. Pushes are typically rejected when the remote branch has commits that your local branch doesn't have. This happens when someone else pushed changes to the same branch. Use `git pull` to integrate their changes before pushing.

#### Q5. How do I push to multiple remotes at once?
A. Git doesn't have a built-in way to push to multiple remotes simultaneously. You need to push to each remote separately, or set up a remote that points to multiple URLs.

## References

https://git-scm.com/docs/git-push

## Revisions

2025/05/04 First revision