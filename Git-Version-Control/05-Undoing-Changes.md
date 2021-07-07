# Undoing Changes

### Update the most recent commit
* `git commit --amend` Updates the most recent commit; newly modified files are included in the updates without making a new commit.

### Revert commits
* `git revert SHA` Reverts a specific commit, i.e., deletions, insertion, etc. will be undone.

### Reset commits
* Command: `git reset`
  * `HEAD^` refers to parent of the current commit
    * Used mainly to refer primary/secondary parent in merging
		* `HEAD^` refers to primary/first parent
		* `HEAD^2` refers to secondary/second parent
  * `HEAD~` refers to parent of the current commit
    * Ignore any second parent branch
    * `HEAD~4` refers to 4th parent from current commit considering only first parent branch
* `git reset --mixed HEAD~4` Moves HEAD pointer to 4th parent and move previous 4 commits to working directory (mixed)
* `git reset --soft HEAD~4` Moves HEAD pointer to 4th parent and move previous 4 commits to staging (soft)
* `git reset --hard HEAD~4` Moves HEAD pointer to 4th parent and move previous 4 commits to trash (hard)

* Since reseting could be dangerous, it is better to keep a backup branch before reseting using (git branch backup). To go back to normal, first remove any uncommitted changes in the working directory and then merge backup branch to the master or main (it uses fast-forward merging).
  * `git branch backup`
  * `git checkout master`
  * `git merge backup`
