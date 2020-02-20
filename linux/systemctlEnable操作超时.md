### systemctl enable 操作超时

systemctl enable postfix.service
增加由/usr/lib/systemd/system/到/etc/systemd/system/multi-user.target.wants/下的软链接
ln -s '/usr/lib/systemd/system/postfix.service' '/etc/systemd/system/multi-user.target.wants/postfix.service'