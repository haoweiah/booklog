### 修改Ubuntu网卡信息

Ubuntu中将网卡名称eno16777736改回eth0

vim /etc/default/grub

在”GRUB_CMDLINE_LINUX”中添加参数net.ifnames=0 biosdevname=0，如下图所示

第二步，输入如下命令，更新grub配置文件 
\# update-grub 
执行结果如下图所示
![image.png](https://upload-images.jianshu.io/upload_images/2676555-49cb2882c6b0d81f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

若提示没有此命令，请先输入安装命令 
\# apt-get install grub2-common

第三步，输入如下命令，编辑对应文件 
\# vim /etc/network/interfaces 
将“eno16777736”全部改为“eth0”，如下图所示
![image.png](https://upload-images.jianshu.io/upload_images/2676555-4cbbb8668a63face.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

第四步，重启系统，再一次查看网卡名称已恢复正常，如下图
![image.png](https://upload-images.jianshu.io/upload_images/2676555-c9e9e6faf27815af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)