### pip使用报错



```
Traceback (most recent call last):
  File "/usr/local/bin/pip3", line 7, in <module>
    from pip._internal import main
ModuleNotFoundError: No module named 'pip._internal'
```

- 看网上信息应该是pip 10的bug
- 解决方法强制升级
- wget https://bootstrap.pypa.io/get-pip.py  --no-check-certificate
- sudo python3 get-pip.py

------

pip 安装

sudo apt install python-pip python-dev

pip3

sudo apt install python3-pip

