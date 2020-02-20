* pip安装文件太慢时可以设置国内源
* exempale
* 在~/.pip/pip.conf文件中加入

[global]

index-url = http://pypi.douban.com/simple

[install]

trusted-host=pypi.douban.com
* Ubuntu添加启动器

 Version=1.0
 
 Type=Application
 
 Name=PyCharm Professional Edition
 
 Icon=/home/hw/Downloads/pycharm-2018.2/bin/pycharm.png
 
 Exec="/home/hw/Downloads/pycharm-2018.2/bin/pycharm.sh" %f
 
 Comment=Python IDE for Professional Developers
 
 Categories=Development;IDE;
 
 Terminal=false
 
 StartupWMClass=jetbrains-pycharm