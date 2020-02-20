## Apache简单配置80端口



```
vim /etc/apache2/sites-available/000-default.conf
```

DocumentRoot **/var/www/html**

```
  <Directory /var/www>                                                                       
      Options Indexes FollowSymLinks MultiViews                                              
      AllowOverride None                                                                     
      Order allow,deny                                                                       
      allow from all                                                                         
  </Directory>
```

可以根据自己的需要修改 DocumentRoot 目录和Directory 目录

Directory 中的/var/www就是80口的目录，/var/ww/html就是网页上显示的那个目录