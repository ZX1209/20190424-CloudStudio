#/bin/sh

currentdir=`pwd`


echo "parament is $#\n"

for gitrepo in ~/CloudStudio ~/lady-linemark;
  do
    cd $gitrepo &&
    git pull  &&
    git add --all && echo "$gitrepo:status:\n" ; git status ; echo "\n"     || echo "add failed"
  done

cd $currentdir
