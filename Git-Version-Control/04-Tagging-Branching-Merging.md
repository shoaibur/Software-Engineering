# Tagging, Branching and Merging

## Tagging
* `git tag -a v1.0` Add annotated tag v1.0 to the latest commit
* `git tag -a v1.0 SHA` Add annotated tag v1.0 to the SHA commit
* `git tag -d v1.0` Remove tag v1.0 (`-d` refers to `--delete`)
* `git tag` Show available tags

## Branching
* `git branch` Shows local branches, active branch is marked by asterisk
* `git branch sidebar` Creates a branch named sidebar at the latest commit/SHA
* `git branch sidebar SHA` Creates branch at the commit specified by SHA
* `git checkout sidebar` HEAD points to sidebar, i.e. sidebar becomes active branch
* `git checkout -b footer` Create footer branch and switch to it
* `git checkout -b footer master` Create and switch to footer branch, which is in same commit as the master branch
* `git branch -d sidebar` Deletes sidebar
* `git log --oneline --graph --all` Shows all branches together

## Merging
* `git merge OtherBranch` Merge "other branch" with the current branch)
* Two types of merging:
  * Fast-forward
    * The branch being merged in must be ahead of the current branch (checked out branch).
		* Current branch's pointer moves forward to point to the same commit as the other branch.
		* No commit is created.
  * Auto-merging (Regular)
    * Two divergent branches are merged
		* A merge commit is created
