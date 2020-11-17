# Git Version Control Overview

1. [Getting started](#1-getting-started-with-git)
2. [Working with a repo](#2-working-with-a-repo)
3. [Review commit history](#3-review-commit-history)
4. [Tagging, branching and merging](#4-tagging-branching-and-merging)
5. [Undoing changes ](#5-undoing-changes)
6. [Git remote](#6-git-remote)


# 1. Getting started with Git

## 1a. Installation and configuration
* Download and install following instructions.
* Check version
  * `git --version`
* Configuration
  * `git config --global user.name "Full Name"`
  * `git config --global user.email "address@email.com"`
  * `git config --global color.ui auto`
  * `git config --global core.editor "atom --wait"` (or `"code --wait"` for VSCode)
  * `git config --list` (Check config settings)

# 2. Working with a Repo
## 2a. Introduction
  * Working directory
  * Staging index
  * Repository
  * Trash

## 2b. Creating a repo
* Create a repo from scratch
  * `git init` Will create `.git` directory
* Clone a repo from a url
  * `git clone url`

## 2c. Add commits to a repo
* Check status, i.e., display the new/changed/modified files in the working directory.
  * `git status`
* Add modified (new/changed/modified) files to staging index
  * `git add file1` Add only file1
  * `git add file1 file2` Add file1 and file2
  * `git add .` Add all modified files
* Commit files from staging index to repository
  * `git commit -m "Commit message"`
  * `git commit` Will open the editor so write more complext commit message
* Remove file from staging index (send back to working directory)
  * `git rm --cached file1`
* Display changes in modified but uncommitted files
  * `git diff`

## 2d. Ignore tracking specific files
* Create a directory named `.gitignore` at the same directory where `.git` directory is.
  * `touch .gitignore`
* Open `.gitignore` (i.e., `vim .gitignore`) and add file names not to be tracked (each file in separate lines)

## 2e. Commit message
  * type: Give a short description of the commit
    * Some examples of type are: feat, fix, docs, style, refactor, test, chore, etc.
  * Blank line
  * Body: Give more detailed description of the commit.
  * Blank line
  * Footer
    * Links, references, etc.

# 3. Review commit history

## 3a. Git commands
* `git log` Shows commit SHA, Author, Date and commit message.
  * Use the following keys to navigate the commit message:
    * j/k Scroll down/up by a line
    * d/u Scroll down/up by half the page
    * f/b Scroll down/up by whole page screen
    * q to quit
* `git log --oneline` Shows first 7 chars of SHA, commit message, and lists one commit per line
* `git log --stat` Shows number of files changed/modified, number insertion/deletion
* `git log -p` or `git log --patch` Shows modified files, lines where changed, and the actual changes.
* `git show` Shows the most recent commit SHA, Author, Date and patch info.
* `git show abc1234` Shows Author, Date and patch info of the commit with SHA abc1234.

## 3b. Difference between a single dashed and double dashed flag
* Single letter parameter: single dash
  * `git log -p`
   * `git log -patch` is equivalent to `git log -p -a -t -c -h`
   * Similar in Linux: `ls -lrt` is equivalent to `ls -l -r -t`
* Multiletter parameter: double dash
  * `git log --patch`

# 4. Tagging, Branching and Merging

## 4a. Tagging
* `git tag -a v1.0` Add annotated tag v1.0 to the latest commit
* `git tag -a v1.0 SHA` Add annotated tag v1.0 to the SHA commit
* `git tag -d v1.0` Remove tag v1.0 (`-d` refers to `--delete`)
* `git tag` Show available tags

## 4b. Branching
* `git branch` Shows local branches, active branch is marked by asterisk
* `git branch sidebar` Creates a branch named sidebar at the latest commit/SHA
* `git branch sidebar SHA` Creates branch at the commit specified by SHA
* `git checkout sidebar` HEAD points to sidebar, i.e. sidebar becomes active branch
* `git checkout -b footer` Create footer branch and switch to it
* `git checkout -b footer master` Create and switch to footer branch, which is in same commit as the master branch
* `git branch -d sidebar` Deletes sidebar
* `git log --oneline --graph --all` Shows all branches together

## 4c. Merging
* `git merge OtherBranch` Merge "other branch" with the current branch)
* Two types of merging:
  * Fast-forward
    * The branch being merged in must be ahead of the current branch (checked out branch).
		* Current branch's pointer moves forward to point to the same commit as the other branch.
		* No commit is created.
  * Auto-merging (Regular)
    * Two divergent branches are merged
		* A merge commit is created


# 5. Undoing Changes

## 5a. Update the most recent commit
* `git commit --amend` Updates the most recent commit; newly modified files are included in the updates without making a new commit.

## 5b. Revert commits
* `git revert SHA` Reverts a specific commit, i.e., deletions, insertion, etc. will be undone.

## 5c. Reset commits
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

# 6. Git Remote

## 6a. Cloning a repo
* `git clone <url>`
  * `git clone https://github.com/shoaibur/SWE.git`
* After cloning, the url is named as `origin` by default in local machine.
  * Check this with `git remote` or `git remote -v`
* We can use alias to see the whole structure
  * `alias graph = ‘git log --oneline --graph --all’`
  * Then `graph`

## 6b. Syncing Local from Remote (GitHub)
* If folder/files in remote have been updated, but not seen by the local yet, we need sync with two commands:
  * `git fetch origin` *Download* the updates from remote
  * `git merge origin`Merge origin, i.e., remote repo with the local repo
  * These two commands are equivalent to:
    * `git pull origin` i.e., `git pull origin` == `git fetch origin && git merge origin`
 
## 6c. Uploading Local to Remote
* `git status`
* `git add <file name>`
* `git commit -m “Commit message”`
  * Alternatively, `git commit -a -m “Commit message”` can be used to commit all (`-a`) changes. In this case, we do not use `git add` command.
* `git push origin main`
  * If the branch name, i.e., `main` in this case, does not match with the branch name in the remote repo, this will through a reference (refs) error. Use `git show-ref` for the available references.
  * If we want to push anyway with our this branch name, we need to use `HEAD` pointing to the branch name.
    * `git push origin HEAD:main` This will create a pull request at the remote, and this branch could be merged with the remote branch.
* Force push: DANGEROUS! Local will replace remote. If there were any updates in remote but not synced with local, those updates will be lost.
  * `git push -f origin`
  * `git push -f origin HEAD:master`
