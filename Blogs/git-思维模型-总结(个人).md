# git 思维模型 总结(个人)



备份或许是最直接的版本管理办法了.想要保存(备份)更改,直接复制文件夹改个名就好了,这样我想回到某一版本就直接打开那个备份的文件夹就好了.但是,对于要备份很多更改,,这个就有点力不从心了..这时git的优势就体现出来了



git init 

初始化.



git add 

添加要跟踪的文件,没有被跟踪的文件,git是不会对它做任何操作于管理的

git reset





git log 

查看版本历史



git checkout 

回到某一版本





look around 

detached HEAD







git pull;git push

云端存储..多人合作..





保证当前工作数记录





git stash

git stash apply 	

git stash list



整个git系统就是管理blob的,但是我只是想管理版本系统而已,,有些东西要么太复杂,要么太危险,,真事的..

我就规定下一些常用模式



git add ,git commit ,存档更改

git log master ,git checkout , 游历



git branch ;git checkout git merge;分支debug之类的



git pull;git push



不要更改HEAD,,

不要reset



用stash 隐藏.



object id













































