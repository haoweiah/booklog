### Nginx学习



## 学习的命令

```
ss，ab（yum install httpd-tools）
```

## ngx_http_core_module

```
= : 对 URI做精确匹配；
    location = / {
                    }
    http://www.a.com/   匹配
    http://www.a.com
^~:     对URI最左边的部分做匹配检查，不区分字符大小写
~:      对URI做正则表达式模式匹配， 区分字符大小写
~*:     对URI做正则表达式模式匹配，不区分大小写
不带符号：   匹配起始于对uri的所有的uri
匹配优先级从高到底：
    =, ^~, ~/~*, 不带符号
```

## Nginx升级

```
Pre-Built Packages for Mainline version

To set up the yum repository for RHEL/CentOS, create the file named /etc/yum.repos.d/nginx.repo with the following contents:

[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/mainline/OS/OSRELEASE/$basearch/
gpgcheck=0
enabled=1

Replace “OS” with “rhel” or “centos”, depending on the distribution used, and “OSRELEASE” with “6” or “7”, for 6.x or 7.x versions, respectively. 
```

## 如果出现错误

```
[root@localhost modules]# nginx
nginx: [emerg] module "/usr/lib64/nginx/modules/ngx_http_geoip_module.so" version 1012002 instead of 1015006 in /usr/share/nginx/modules/mod-http-geoip.conf:1
```

## 解决方案

```
vim /etc/yum.repo.d/nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/mainline/centos/7/$basearch/
gpgcheck=0
enabled=1

yum remove nginx-mod*
yum install nginx-module-*
解决问题
```