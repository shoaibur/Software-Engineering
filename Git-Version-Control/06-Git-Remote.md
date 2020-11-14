# Git Remote

### Cloning a repo
* `git clone <url>`
  * `git clone https://github.com/shoaibur/SWE.git`
* After cloning, the url is named as `origin` by default in local machine.
  * Check this with `git remote` or `git remote -v`
* We can use alias to see the whole structure
  * `alias graph = ‘git log --oneline --graph --all’`
  * Then `graph`

### Syncing Local from Remote (GitHub)
* If folder/files in remote have been updated, but not seen by the local yet, we need sync with two commands:
  * `git fetch origin` *Download* the updates from remote
  * `git merge origin`Merge origin, i.e., remote repo with the local repo
  * These two commands are equivalent to:
    * `git pull origin` i.e., `git pull origin` == `git fetch origin && git merge origin`
 
### Uploading Local to Remote
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
