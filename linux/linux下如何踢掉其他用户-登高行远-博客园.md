### linux下如何踢掉其他用户 - 登高行远 - 博客园



# [linux下如何踢掉其他用户](https://www.cnblogs.com/fbwfbi/archive/2013/05/06/3063331.html)查看机器中登陆的用户



[root@chengest~]# w

16:29:02 up 2 days, 2:35, 5 users, load average: 0.03, 0.05, 0.01

USER TTY FROM LOGIN@ IDLE JCPU PCPU WHAT

root pts/1 :0.0 Tue15 2days 1:44 0.04s -bash

root pts/2 :0.0 Tue15 46:42m 0.05s 0.05s bash

root pts/3 :0.0 Tue15 2days 0.02s 0.02s bash

root pts/4 172.20.52.114 14:17 58:48 0.16s 0.03s sqlplus

root pts/5 172.20.52.114 15:31 0.00s 0.03s 0.00s w

 

我把pts/1踢掉（只有root才能去踢掉用户）

[root@chengest ~]# pkill -kill -t pts/1

[root@chengest ~]# pkill -kill -t pts/2

[root@chengest ~]# pkill -kill -t pts/3

 

查看是不是踢掉

[root@chengest ~]# w

16:34:16 up 2 days, 2:40, 2 users, load average: 0.00, 0.05, 0.02

USER TTY FROM LOGIN@ IDLE JCPU PCPU WHAT

root pts/4 172.20.52.114 14:17 1:04m 0.16s 0.03s sqlplus

root pts/5 172.20.52.114 15:31 0.00s 0.03s 0.00s w

**root可以踢掉其他用户包括自己**