#### proxychains

###### 1.manjaro 安装

```linux
$ yay -S proxychains
```

###### 2.配置代理

```linux
$ vim /etc/proxychains.conf
搭建服务，v2ray设置本地端口1080
将配置文件最后一行修改成 socks5  127.0.0.1 1080
```

###### 3.测试

```linux
$proxychains wget http://www.google.com
```

---

###### ubuntu安装

```linux
$sudo apt install proxychains
```

