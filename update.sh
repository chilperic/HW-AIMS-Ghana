git stash save
git fetch origin master
git merge origin/master --no-edit
git stash apply
