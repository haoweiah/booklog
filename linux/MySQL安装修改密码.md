### MySQL安装修改密码

首先，修改mysql配置文:

\```
vim /etc/mysql/mysql.conf.d/mysqld.cnf
\```

\* 1

在skip-external-locking的下一行添加skip-grant-tables，跳过密码校验

\```
user = mysql
pid-file =/var/run/mysqld/mysqld.pid
socket =/var/run/mysqld/mysqld.sock
port = 3306
basedir = /usr
datadir = /var/lib/mysql
tmpdir = /tmp
lc-messages-dir = /usr/share/mysql
skip-external-locking
skip-grant-tables
\```

\* 1
\* 2
\* 3
\* 4
\* 5
\* 6
\* 7
\* 8
\* 9
\* 10

然后重启mysql后，我们直接无密码登陆：

\```
sudo service mysql restartmysql
\```

\* 1
\* 2

登录后，我们来修改密码

\```
mysql>use mysql;
mysql>update user set authentication_string=password('新密码') where user='root';
\```

\* 1
\* 2

注意：可能遇到这样的问题，这个是你的密码强度不够，请修改强度，举例：@ROOT_root_123 
[图片上传失败...(image-5a2d18-1536108943382)]

到这里还没彻底弄好，千万不要退出，这里只是修改而已，还没保存 
继续输入以下命令：

\```
mysql> flush privileges;
mysql> quit;
\```

\* 1
\* 2

好了，大功告成，把配置文件修改回去，注释掉skip-grant-tables，然后重启，

\```
sudo service mysql restart
\```

\* 1

最后输入你的新密码登录。