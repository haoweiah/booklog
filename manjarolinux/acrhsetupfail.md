#### archlinux滚动升级失败解决方法
    error: failed to commit transaction (conflicting files)
    python2-setuptools: /usr/lib/python2.7/site-packages/pkg_resources/__init__.pyc exists in filesystem
    python2-setuptools: /usr/lib/python2.7/site-packages/setuptools/windows_support.pyc exists in filesystem
    python2-pip: /usr/lib/python2.7/site-packages/pip/utils/glibc.py exists in filesystem
    python2-pip: /usr/lib/python2.7/site-packages/pip/utils/packaging.py exists in filesystem
    python2-pip: /usr/lib/python2.7/site-packages/pip/utils/packaging.pyc exists in filesystem
    Errors occurred, no packages were upgraded.
### 解决方案

sudo pacman -S python2-setuptools --force
sudo pacman -S python2-pip --force


