uiautomatorviewer安装
网址：https://www.androiddevtools.cn/
android sdk link: https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz?utm_source=androiddevtools&utm_medium=website

安装java
sudo apt-get install openjdk-8-jdk
java -version
platform_tools link: https://developer.android.com/studio/releases/platform-tools
uiautomatorviewer 需要使用这里面的不然会报错
报错为screenshot 截图工具用不了  编辑

在 .bashrc 中设置变量环境

# 添加PATH 环境
export ANDROID_HOME="/home/hw/bin/sdk"
export PATH="$ANDROID_HOME/tools/bin:$ANDROID_HOME:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$PATH"


uiautomatorviewer出现Unable to connect to adb. Check if adb is installed correctly解决方法
修改后的最后一行为：
call "%java_exe%" "-Djava.ext.dirs=%javaextdirs%" "-Dcom.android.uiautomator.bindir=D:\AndroidSDK\platform-tools" -jar %jarpath% %*
将其中的bindir=%prog_dir%修改为 SDK 的 platform-tools 所在路径（我的 SDK 路径为：D:\AndroidSDK\platform-tools）



link:
    https://blog.csdn.net/hust_twj/article/details/68077188