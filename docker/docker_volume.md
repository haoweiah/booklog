### docker volume
- 1. Docker volume 的几种形态

```
有状态容器都有数据持久化需求。前一篇文章中提到过，Docker 采用 AFUS 分层文件系统时，文件系统的改动都是发生在最上面的容器层。在容器的生命周期内，它是持续的，包括容器在被停止后。但是，当容器被删除后，该数据层也随之被删除了。因此，Docker 采用 volume （卷）的形式来向容器提供持久化存储。Docker volume 有如下几种形态。```
**_ docker run -d -P --name web -v /webapp training/webapp python app.py _**

```
其实，在 web 容器被删除后，/var/lib/docker/volumes/f143b7f379fb6d012a08656fc950bf6df4bf5a5b90c72f310644aa997620122b/_data 目录及其中的内容都还会保留下来，但是，新启动的容器无法再使用这个目录，也就是说，已有的数据不能自动地被重复使用了。```

- 1.1 使用 -v 来挂载一个主机上的目录到容器的目录

**_ docker run -d -P --name web2 -v /src/webapp:/webapp training/webapp python app.py _**
```
主机上的目录可以是一个本地目录，也可以在一个 NFS share 内，或者在一个已经格式化好了的块设备上。

其实这种形式和第一种没有本质的区别，容器内对 /webapp 的操作都会反映到主机上的 /src/webapp 目录内。只是，重新启动容器时，可以再次使用同样的方式来将 /src/webapp 目录挂载到新的容器内，这样就可以实现数据持久化的目标。```

- 1.2 使用 -v 来挂载主机上的一个文件到容器内的一个文件

**_docker run --rm -it -v ~/.bash_history:/root/.bash_history ubuntu /bin/bash _**
- 1.3 使用 data container

```如果要在容器之间共享数据，最好是使用 data container。这种 container 中不会跑应用，而只是挂载一个卷。比如：

创建一个 data container：

<pre>docker create -v /dbdata --name dbstore training/webapp  /bin/true</pre>

启动一个 app container：

<pre>docker run -d -P --name web3 --volumes-from dbstore training/webapp python app.py</pre>

其实，对 web3 这个容器来说，volume 的本质没变，它只是将 dbstore 容器的 /dbdata 目录映射的主机上的目录映射到自身的 /dbdata 目录。
[复制代码](http://upload-images.jianshu.io/upload_images/2676555-eb597a6ea5ef52b0.gif?imageMogr2/auto-orient/strip"复制代码")

"Mounts": [
{ "Name": "5341c03f3b94f13f4c86d88ccb0f3b63487adf30dea7ae6b2d06e947235e7330", "Source": "/var/lib/docker/volumes/5341c03f3b94f13f4c86d88ccb0f3b63487adf30dea7ae6b2d06e947235e7330/_data", "Destination": "/dbdata", "Driver": "local", "Mode": "", "RW": true, "Propagation": "" }
]

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-4dc9f00921e0d337.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

但是，其好处是，可以不管其目录的临时性而不断地重复使用它。```
- 1.4 使用 docker volume 命令

Docker 新版本中引入了 docker volume 命令来管理 Docker volume。

（1）使用默认的 ‘local’ driver 创建一个 volume

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-cf032ed9a0ad11b6.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

<pre>root@docker1:/home/sammy# docker volume create --name vol1
vol1
root@docker1:/home/sammy# docker volume inspect vol1
[
{ "Name": "vol1", "Driver": "local", "Mountpoint": "/var/lib/docker/volumes/vol1/_data", "Labels": {}, "Scope": "local" }
]</pre>

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-d6871b3b07d4a2a8.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

（2）使用这个 volume

<pre>docker run -d -P --name web4 -v vol1:/volume training/webapp python app.p</pre>

结果还是一样的，即将 vol1 对应的主机上的目录挂载给容器内的 /volume 目录。

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-3fcc2185666f9f73.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

<pre>"Mounts": [
{ "Name": "vol1", "Source": "/var/lib/docker/volumes/vol1/_data", "Destination": "/volume", "Driver": "local", "Mode": "z", "RW": true, "Propagation": "rprivate" }
],</pre>

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-12e2dd0eb3644308.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

- 1.5 Volume 删除和孤单 volume 清理

	 1.5.1 在删除容器时删除 volume

可以使用 docker rm -v 命令在删除容器时删除该容器的卷。

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-0eb79831872a692b.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

<pre>root@docker1:/home/sammy# docker run -d -P --name web5 -v /webapp training/webapp python app.py
69199905a74cb360935e32f4e99f7f11319f6aa36033a920aa0bae25874f5c69
root@docker1:/home/sammy# docker volume ls
DRIVER VOLUME NAME
local 5341c03f3b94f13f4c86d88ccb0f3b63487adf30dea7ae6b2d06e947235e7330
local 838f4dd99721a9445be22a6b42d35e04cb43ad145ecf26107a9025f428587f76
local vol1
root@docker1:/home/sammy# docker rm -vf web5
web5
root@docker1:/home/sammy# docker volume ls
DRIVER VOLUME NAME
local 5341c03f3b94f13f4c86d88ccb0f3b63487adf30dea7ae6b2d06e947235e7330
local vol1</pre>

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-b80537afcf23d99d.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

#### 1.5.2 批量删除孤单 volumes

从上面的介绍可以看出，使用 docker run -v 启动的容器被删除以后，在主机上会遗留下来孤单的卷。可以使用下面的简单方法来做清理：

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-2f3d26675bd0df13.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

<pre>root@docker1:/home/sammy# docker volume ls -qf dangling=true 244a23f3ab11f17345a68e77f96bb46a8dbaf445760dd86ab0faa07dfbd84236
c864cfac232e8728b1805abc8c363d324124b38e6297544a8cbbf61d883c7e46
f143b7f379fb6d012a08656fc950bf6df4bf5a5b90c72f310644aa997620122b
root@docker1:/home/sammy# docker volume rm $(docker volume ls -qf dangling=true)
244a23f3ab11f17345a68e77f96bb46a8dbaf445760dd86ab0faa07dfbd84236
c864cfac232e8728b1805abc8c363d324124b38e6297544a8cbbf61d883c7e46
f143b7f379fb6d012a08656fc950bf6df4bf5a5b90c72f310644aa997620122b
root@docker1:/home/sammy# docker volume ls
DRIVER VOLUME NAME
local 5341c03f3b94f13f4c86d88ccb0f3b63487adf30dea7ae6b2d06e947235e7330
local vol1</pre>

[![复制代码](http://upload-images.jianshu.io/upload_images/2676555-6c7567f38f09261a.gif?imageMogr2/auto-orient/strip)](javascript:void(0); "复制代码")

github 上有很多脚本可以自动化地清理孤单卷，比如：

* [https://github.com/chadoe/docker-cleanup-volumes/blob/master/docker-cleanup-volumes.sh](https://github.com/chadoe/docker-cleanup-volumes/blob/master/docker-cleanup-volumes.sh)
* [https://github.com/meltwater/docker-cleanup](https://github.com/meltwater/docker-cleanup) 

1.6 小结

对以上内容的两点小结：

* 容器内的数据是临时性的，它会随着容器生命周期的结束而消失
* 默认的 Docker volume （driver = ‘loclal’）不管是哪种形式，本质上都是将容器所在的主机上的一个目录 mount 到容器内的一个目录，因此，它不具备可移植性。


link :[https://www.cnblogs.com/sammyliu/p/5932996.html](https://www.cnblogs.com/sammyliu/p/5932996.html)