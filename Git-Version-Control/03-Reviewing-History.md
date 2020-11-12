# 3. Review commit history

## Git commands
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


## Difference between a single dashed and double dashed flag
* Single letter parameter: single dash
  * `git log -p`
   * `git log -patch` is equivalent to `git log -p -a -t -c -h`
   * Similar in Linux: `ls -lrt` is equivalent to `ls -l -r -t`
* Multiletter parameter: double dash
  * `git log --patch`
