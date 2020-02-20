## linux 命令
#### zip 解压到 指定文件夹

`unzip *.zip -d /***`

___
#### ubuntu 更新 vim

```
1、编译安装
2、添加安装源更新
   sudo add-apt-repository ppa:jonathonf/vim
  sudo apt update
  sudo apt install vim
   卸载        
   sudo apt remove vim
  sudo add-apt-repository --remove ppa:jonathonf/vim
```

___
#### 脚本中设置变量

```
如果是要在父环境中使用，在脚本写下设置环境变量 ex： export TEST=“/path”
在shell中执行 source ×××.sh  or  . ***.sh

如果都在shell脚本中执行的命令
exec 需要环境变量的命令可以使用这个来执行，可以参考github中的fetchACStest脚本
```

***
#### xargs cp

```
ls !(cel_kbl-flashfiles-OC0000049.zip) | xargs -i cp {} /media/hw/MJRO1802/

-i 表示 传递给xargs的结果 由{}来代替
```

***
#### apt -f install 报错

```
执行apt-get install 报错：Errors were encountered while processing

解决方式：
清空/var/lib/dpkg/info目录下面的内容
```

***

#### rm 反选删除文件

```
rm -rf !(xxx|xxx)
ls | grep -v xxx | xargs rm -rf
```

***
#### wget操作

```
eg：
url=http://10.239.147.147/acrn_daily_build/ww37.2/MRB/B2/

wget $url -r -R index*,gordon* -nd -np -l1 -P ~/ww37 --no-proxy --no-check-certificate

参数解析:
-r, –recursive 递归下载－－慎用!
-R, –reject=LIST 逗号分隔的不被接受的扩展名的列表
-A, –accept=LIST 逗号分隔的被接受扩展名的列表
-nd 递归下载时不创建一层一层的目录，把所有的文件下载到当前目录
-np 表示不下载旁站连接
-np, –no-parent 不要追溯到父目录
-l, –level=NUMBER 最大递归深度 (inf 或 0 代表无穷)
-P, –directory-prefix=PREFIX 将文件保存到目录 PREFIX/…
这个博客中有些错误如果冲突以我笔记为准
https://www.cnblogs.com/ZhangRuoXu/p/6369332.html
```

#### 重定向没有权限

```
需要互动输入命令时可用这样的方式：
    echo "passwd" | sudo -S commend
    使用sudo -S 提权这样可以不用使用expect来交互


* eg：
    ➜ [/home/hw] cat docker.txt > /etc/docker/daemon.json
    zsh: permission denied: /etc/docker/daemon.json
    原因：> 重定向符也需要权限
    可解决
    解决方案：1、使用bash -c 把命令包起来，当作一条命令来执行

    sudo bash -c 'echo > test.txt'
2、使用tree （这个有时候不太管用）
cat dacker.txt | sudo tree /etc/docker/daemon.json
tree == > tree == >>
3、sudo -s
提权

永久更改
修改：/etc/docker/daemon.json增加如下内容

{
"registry-mirrors": ["https://registry.docker-cn.com"]
}
```

#### 环境变量设置

```
在shell脚本中设置的临时环境变量没有作用，因为脚本执行是fork了一个子shell不是当前的shell所以设置的环境变量没有作用

利用shell脚本添加环境变量

在shell脚本设置了环境变量，如export LIBRARY_PATH=./lib/，执行了此脚本后, 在执行生成的可执行文件，提示错误

error while loading shared libraries: libww.so: cannot open shared object file: No such file or directory

但是如果把export那句话单独在命令行运行，在gcc编译代码后不会出现问题

怎么也想不通，为什么脚本执行了，设置了环境变量，但是运行可执行文件总是失败。

查看大牛博客，终于发现

原因是执行脚本用./test.sh的方式，如果采用source test.sh，则环境变量会生效。

./XXX.sh的时候，脚本里面打印PATH是改了，但是在终端echo $PATH却没有看到变化，因为这样执行等于说不在当前进程

那么。这是为什么呢？

关键：直接执行一个脚本文件是在一个子shell中运行的，而source则是在当前shell环境中运行的。

 
1、执行脚本时是在一个子shell环境运行的，脚本执行完后该子shell自动退出；

 
2、一个shell中的系统环境变量才会被复制到子shell中（用export定义的变量）
3、一个shell中的系统环境变量只对该shell或者它的子shell有效，该shell结束时变量消失（并不能返回到父shell中）。

 
4、不用export定义的变量只对该shell有效，对子shell也是无效的。

另：
---- 在UNIX系统中,我们在运行shell程序或系统命令的过程如下:  

---- 假设在当前的shell环境下,我们运行ps -f命令.  

---- 首先,当前的shell会调用:fork()命令,产生一个subprocess,该子进程完全复制了父进程的所有环境;  

---- 之后,当前的shell会调用:exec ps -f命令,在新的子进程的环境中,运行ps -f 命令.子进程的环境变量会根据新的应用进行调整,并使之运行,当应用完成之后,子进程结束,返回到父进程.  

---- 因此,通过上述过程分析,$cbpsprofile的运行的结果就可以预见,该shell程序的运行,环境变量重新赋值仅仅在子进程中,程序运行完后,返回到父进程,父进程的环境变量是不会受到影响的

参考：
https://blog.csdn.net/xhz_1983/article/details/73250033
https://blog.csdn.net/wgembed/article/details/22385469
https://www.cnblogs.com/fdd566/p/6692595.html
https://blog.csdn.net/moqingxinai2008/article/details/53909464
```

#### vim配置

[http://blog.51cto.com/11555417/2150626](http://blog.51cto.com/11555417/2150626)

