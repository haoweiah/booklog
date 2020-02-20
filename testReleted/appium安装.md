### appium安装

一、安装npm node
 node安装地址：https://nodejs.org
 根据文档显示最好不要用sudo安装npm和node所以源码安装
 下载好源码后在家目录下新建node文件夹，解压下载好的文件，node-v8.12.0-linux-x64.tar下载好的文件名
解压后把文件中的bin文件夹加到环境变量中，我是写到了.bashrc文件中，运行npm -v 和 node -v查看安装的版本

二、appium的安装 link： https://testerhome.com/topics/5874
 在家里的环境无法通过 npm npm install -g appium进行安装，因为需要下载Google的一些插件，所以安装不成功

所以源码安装：link ：https://testerhome.com/topics/4235
先安装cpnm：npm install -g cnpm --registry=https://registry.npm.taobao.org
克隆appium项目：
 git clone https://github.com/appium/appium.git
进入appium源码文件夹，使用cnpm install安装依赖

安装log：
 ➜ [/home/hw] cnpm install
npminstall WARN package.json not exists: /home/hw/package.json
✔ Installed 0 packages
✔ Linked 0 latest versions
✔ Run 0 scripts
✔ All packages installed (used 27ms(network 15ms), speed 0B/s, json 0(0B), tarball 0B)
➜ [/home/hw] cd appium 
➜ [/home/hw/appium] git:(master) cnpm install
⠇  [26/54] Installing fsevents@1.xplatform unsupported fsevents@1.x  Package require os(darwin) not compatible with your platform(linux)
[fsevents@1.x] optional install error: Package require os(darwin) not compatible with your platform(linux)
✔ Installed 54 packages
✔ Linked 0 latest versions
✔ Run 0 scripts
[20:31:35] Using gulpfile ~/appium/gulpfile.js
[20:31:35] Starting 'prepublish'...
[20:31:35] Starting 'clean'...
[20:31:35] Finished 'clean' after 74 ms
[20:31:35] Starting 'transpile'...
[20:31:38] Finished 'transpile' after 2.66 s
[20:31:38] Starting 'fixShrinkwrap'...
Could not find shrinkwrap; skipping fixing shrinkwrap. (Original error: Cannot find module './npm-shrinkwrap.json')
✔  All packages installed (1 packages installed from npm registry, used  7s(network 726ms), speed 22.64kB/s, json 1(16.43kB), tarball 0B)
➜ [/home/hw/appium] git:(master) 

报错不能安装完成
分析日志可能缺少shrinkwrap
百度得到命令：npm shrinkwrap
继续安装：cnpm install 
继续安装：cnpm link
运行：appium -v
➜ [/home/hw/appium] git:(master) ✗ appium -v
1.9.2-beta.1
➜ [/home/hw/appium] git:(master) ✗ cd ..