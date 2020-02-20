### 前言
python 虚拟环境有很多种，自带的 venv, 与 virtualenv, conda, pipenv, pyenv
这些虚拟环境其实差不多，听说conda 跨平台挺好的。
pipenv 的确是虚拟环境利器，pipenv 比较好用的就是对 pip 依赖包的管理，但是如果不设置 pip 代理 pipenv lock 和 pipenv install 有点慢。pipenv 进入虚拟环境需要输入一些命令，我希望省略掉这一步。
pyenv 的虚拟环境，pyenv 在目录中设置了 python 环境，在进入目录后直接会使用 pyenv 设置的环境， 不需要使用命令进入，我比较喜欢这个，python的版本优先级 `shell > local > global` 
**pyenv会从当前目录开始向上逐级查找.python-version文件，直到根目录为止，若找不到，则使用global版本**

pycharm 设置虚拟环境时, 地址 ~/.pyenv/versions/3.7.4/envs/.../bin/python
### pyenv安装配置
pyenv wiki [https://github.com/pyenv/pyenv/wiki/common-build-problems](https://github.com/pyenv/pyenv/wiki/common-build-problems)


```
$sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```

```
$ curl https://pyenv.run | bash 
在当前sh的~/.bashrc 中添加，如果使用zsh在~/.zshrc 中添加
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
重新加载shell
```
$ exec $SHELL -l
```
安装oh-my-zsh提示更友好
```
$ sudo apt install zsh
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
主题可以百度一下选择一个好看的

### 使用
```
查看当前 python 版本
$ pyenv version 
查看所有python版本
$ pyenv versions
使用python版本创建虚拟环境
$ pyenv virtualenv 3.7.4 py37
在当前目录中使用虚拟环境或者python版本
$ pyenv local 3.7.4 
$ pyenv local py37
查看所有虚拟环境
$ pyenv virtualenvs
设置全局python
$ python global 版本号
设置当前shell窗口使用的python版本为指定版本，设置面向 shell 的 Python 版本，
通过设置当前 shell 的 PYENV_VERSION 环境变量的方式。这个版本的优先级比 local 和 global 都要高。
–-unset 参数可以用于取消当前 shell 设定的版本。
$ python shell 版本号
删除python版本或者虚拟环境
pyenv uninstall 版本号
```

### 使用pyenv设置并启用一个虚拟环境
```
$ pyenv install 3.7.4 # 下载安装python3.7.4
$ pyenv virtualenv 3.7.4 py37 #  pyenv virtualenv 版本号 虚拟环境名
$ mkdir py37
$ cd py37
$ pyenv local py37 # 设置当前文件夹使用py37为虚拟环境
$ python --version # 查看python的版本
$ pyenv uninstall py37 # 删除py37虚拟环境
```
### pyenv升级
使用 curl https://pyenv.run | bash 脚本安装可以使用命令升级
```
$ pyenv update
```
[官方文档](https://github.com/yyuu/pyenv#readme)
*参考资料*
[pyenv Tutorial](http://amaral-lab.org/resources/guides/pyenv-tutorial)
