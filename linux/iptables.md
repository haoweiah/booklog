### iptables

Ubuntu默认安装是没有开启任何防火墙的。

当使用**service iptables status**时发现提示**iptables:unrecoginzed service**。意思是无法识别的服务。

以下方法来自http://blog.csdn.net/lywzgzl/article/details/39938689，但是测试发现，**此方法已经无法在Ubuntu中使用**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#在ubuntu中由于不存在/etc/init.d/iptales文件，所以无法使用service等命令来启动iptables，需要用modprobe命令。
#启动iptables
modprobe ip_tables
#关闭iptables（关闭命令要比启动复杂）
iptables -F
iptables -X
iptables -Z
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
modprobe -r ip_tables
#依次执行以上命令即可关闭iptables，否则在执行modproble -r ip_tables时将会提示
#FATAL: Module ip_tables is in use.
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

通过以上方法，最终无法解决，通过研究发现，以上的命令已经是旧版，在新版中iptables本身不是一个服务。

 

而如果要继续使用iptables配置，可以通过来自http://www.cnblogs.com/general0878/p/5757377.html的方法去实现：

1、查看系统是否安装防火墙

```
sudo whereis iptables
```

[![img](https://images2015.cnblogs.com/blog/417876/201705/417876-20170513224524566-1701143056.png)](https://images2015.cnblogs.com/blog/417876/201705/417876-20170513224524566-1701143056.png)

出现如上提示表示已经安装iptables，如果没有安装，可以通过以下命令安装

```
sudo apt-get install iptables
```

2、查看防火墙的配置信息

```
sudo iptables -L
```

[![img](https://images2015.cnblogs.com/blog/417876/201705/417876-20170513224720597-1424202403.png)](https://images2015.cnblogs.com/blog/417876/201705/417876-20170513224720597-1424202403.png)

3、新建规则文件

```
mkdir /etc/iptables #先新建目录，本身无此目录
vi /etc/iptables/rules.v4
```

两条合起来的命令可以简化成以下写法

```
mkdir /etc/iptables & vi /etc/iptables/rules.v4
```

添加以下内容（备注：80是指web服务器端口，3306是指MySQL数据库链接端口，22是指SSH远程管理端口）

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
*filter
:INPUT DROP [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:syn-flood - [0:0]
-A INPUT -i lo -j ACCEPT
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT
-A INPUT -p icmp -m limit --limit 100/sec --limit-burst 100 -j ACCEPT
-A INPUT -p icmp -m limit --limit 1/s --limit-burst 10 -j ACCEPT
-A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j syn-flood
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A syn-flood -p tcp -m limit --limit 3/sec --limit-burst 6 -j RETURN
-A syn-flood -j REJECT --reject-with icmp-port-unreachable
COMMIT
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

4、使防火墙生效

```
iptables-restore < /etc/iptables/rules.v4
```

5、创建文件，添加以下内容，使防火墙开机启动

```
vi /etc/network/if-pre-up.d/iptables
#!/bin/bash
iptables-restore < /etc/iptables/rules.v4
```

6、添加执行权限

```
chmod +x /etc/network/if-pre-up.d/iptables
```

7、查看规则是否生效

```
iptables -L -n
```

通过以上方法可以在Ubuntu上正常通过，并且可以清晰的知道其依赖关系。

 

再或者如果要折腾iptables的用法，可以参考以下收集的文章进行配置：

https://serverfault.com/questions/129086/how-to-start-stop-iptables-on-ubuntu

https://help.ubuntu.com/community/IptablesHowTo

 

经过研究发现，在Ubuntu/Debian系统上有一个防火墙的简化版，叫做**UFW**，原理还是iptables，但是由于iptables需要操作的表和关系很多，所以使用**UFW**来简化这些操作。