#### ntp 搭建



####  ntp 服务端搭建

​     timedatectl status 查看当前时间时区 

​     timedatectl set-timezone Asia/Shanghai # 设置当前时区     

​     服务端安装：ntp服务 apt install ntp systemctl start ntp systemctl enable ntp 

​     客户端安装：ntpdate ntpdate server #同步时间

​    备份配置：

​         cp /etc/ntp.conf /etc/ntp.conf.bak

​    修改配置：

​         添加 ：server 210.72.145.44 # 写在上面一点这是上游服务器

​          server 127.127.1.0 　　　　 #local clock 如果上面的服务器都无法同步时间，就和本地系统时间同步。127.127.1.0在这里是一个IP地址，不是网段

​         fudge 127.127.1.0 stratum 10 #127.127.1.0 为第10层。ntp 和127.127.1.0同步完后，就变成了11层。 ntp是层次阶级的。同步上层服务器的stratum 大小不能超过或等于16。



\## ntpdate 客户端安装

​    ntpdate no server suitable for synchronization found # 报错

​     



则可采用以下步骤检测：

在NTP服务端执行以下命令检测NTP服务是否运行#service ntpd status

运行[ping命令](https://www.baidu.com/s?wd=ping命令&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)检测NTP客户端与NTP服务端是否连通#ping NTP服务端IP

在NTP客户端执行 ntpdate -d NTP服务端IP：

如果输出结果如下：

6 Nov 10:23:16 ntpdate[3521]: ntpdate 4.2.2p1@1.1570-o Tue Nov 18 07:40:49 UTC 2008 (1)

Looking for host 10.75.80.47 and service ntp

host found : 10.75.80.47

transmit(10.75.80.47)

transmit(10.75.80.47)

transmit(10.75.80.47)

transmit(10.75.80.47)

transmit(10.75.80.47)

10.75.80.47: Server dropped: no data

……

……6 Nov 10:23:20 ntpdate[3521]: no server suitable for synchronization found

如果出现以上情况，请按以下步骤处理：

检查NTP服务端使用的ntp版本：

\#ntpq -c version

如果输出版本是ntp4.2（包括4.2）之后的版本，则请检测是否在restrict的定义中使用了notrust。如果有则删除notrust，再进行[NTP时间同步](https://www.baidu.com/s?wd=NTP时间同步&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)。

b) 检查NTP服务端的防火墙是否开放NTP服务端口：udp 123

\#service iptables stop

执行以上命令关闭NTP服务端的防火墙，然后再进行[NTP时间同步](https://www.baidu.com/s?wd=NTP时间同步&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)，如果成功，则需要修改iptables的设置，以开放NTP服务端口：

\#setup #进入配置界面在配置界面选择Firewall configuration进入防火墙配置界面：在防火墙配置界面中选择Customize进入详细的配置界面：按图中方式加入ntp:udp以运行NTP服务通过防火墙。

9) 如果输出结果如下：

5 Nov 19:02:27 ntpdate[28566]: ntpdate 4.2.2p1@1.1570-o Fri Sep 4 18:54:46 UTC 2009 (1)

Looking for host 10.75.80.55 and service ntp

host found : 10.75.80.55

transmit(10.75.80.55)

receive(10.75.80.55)

transmit(10.75.80.55)

receive(10.75.80.55)

transmit(10.75.80.55)

receive(10.75.80.55)

transmit(10.75.80.55)

receive(10.75.80.55)

transmit(10.75.80.55)

10.75.80.55: Server dropped: strata too high

……

……

5 Nov 19:02:27 ntpdate[28566]: no server suitable for synchronization found

出现以上情况的原因是由于NTP Server还没有和自身或其他NTP Server保持同步，因此需在ntp的配置文件ntp.conf中加入以下语句以保证NTP Server与自身同步：

server 127.127.1.0

fudge 127.127.1.0 stratum 10

注意：在NTP Server重新启动NTP服务后，NTP Server自身或与其他NTP 

Server的同步大概需要5分钟左右，因此NTP客户端在这个时间段运行ntpdate命令时会产生no server suitable for 

synchronization found错误。

gbucks



