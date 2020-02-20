### dhcp修改和重启

dhcp修改
 修改192.168.202.131
 文件在：/etc/dhcp/dhcpd.conf
重启dhcp服务
 sudo service isc-dhcp-server restart
查看dhcp是否启动
 sudo netstat -uap