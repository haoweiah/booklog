### nginx源码安装



## 下载nginx安装包

```
解压
./configure \
--prefix=/app/nginx \ ** 这个目录不能与安装目录在一起 **
--with-http_ssl_module \ *默认模块安装*
--add-module=/第三方安装模块目录

安装
make && make install
```