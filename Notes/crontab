#start cron 
service cron start

usage: crontab [-u user] file
       crontab [ -u user] [ -i ] { -e | -l | -r }
               (default operation is replace, per 1003.2)
       -e      (edit user's crontab)
       -l      (list user's crontab)
       -r      (delete user's crontab)
       -i      (prompt before deleting user's crontab)

参数 说明 
-u user指定用户 
-e 编辑某个用户的计划任务文件，若不指定用户，默认编辑当前用户的计划任务文件 
-l 显示某个用户的计划任务文件，若不指定用户，默认显示当前用户的计划任务文件 
-r 删除某个用户的计划任务文件，若不指定用户，默认删除当前用户的计划任务文件 
-i 在删除之前推送确认提示 

crontab -u foo -e     #编辑用户 foo 的计划任务文件

crontab -e            #编辑当前用户的计划任务文件

crontab -u foo -l     #显示用户 foo 的计划任务文件

crontab -l            #显示当前用户的计划任务文件

crontab -r            #删除当前用户的计划任务文件


任务计划的语法格式如下：

m h dom mon dow   command
0-59 0-23 1-31 1-12 0-7  command

m: 表示分钟
h: 表示小时
dom: 表示日期
mon: 表示月份
dow: 表示星期
command: 预执行的命令
另外需要使用一些特殊符号实现灵活的配置：

* 代表所有值
/ 代表“每”
- 代表范围
, 分割数字





# set a shell
SHELL=/bin/bash

# crontab format
* * * * *  command_to_execute
- - - - -
| | | | |
| | | | +- day of week (0 - 7) (where sunday is 0 and 7)
| | | +--- month (1 - 12)
| | +----- day (1 - 31)
| +------- hour (0 - 23)
+--------- minute (0 - 59)

# example entries
# every 15 min
*/15 * * * * /home/user/command.sh

# every midnight
0 0 * * * /home/user/command.sh

# every Saturday at 8:05 AM
5 8 * * 6 /home/user/command.sh

