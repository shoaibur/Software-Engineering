# 2. Working with a Repo
## Introduction
  * Working directory
  * Staging index
  * Repository
  * Trash

## Creating a repo
* Create a repo from scratch
  * `git init`
* Clone a repo from a url
  * `git clone url`

## Add commits to a repo
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

## Commit message
  * type: Give a short description of the commit
    * Some examples of type are: feat, fix, docs, style, refactor, test, chore, etc.
  * Blank line
  * Body: Give more detailed description of the commit.
  * Blank line
  * Footer
    * Links, references, etc.
