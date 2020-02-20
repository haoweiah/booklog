ubuntu安装maridb

- `sudo apt install maridb-server maridb-client`
 `mysql_secure_installation` (初始化mariadb)
 - 之前不小心把普通用户的访问权限给了 root@localhost
 
 
    `sudo apt-get remove mysql-*`
    `dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P`
    之后最好重启一下
创建一个用户并授权
`grant all privileges on *.* to my@localhost identified by '123456';`
`flush privileges;` 刷新操作

linux 普通用户不用sudo链接数据库方法
解决方法是在/etc/mysql/my.cnf添加点内容
[mysqld]
skip-grant-tables
