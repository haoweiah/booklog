获取包名
adb logcat | grep START
然后打开软件就可以获取包名

adb shell input keyevent 3
# 点击键back效果一样




2019-1-15
uiautomator 
logcat 
dumpsys
adb  shell getprop
adb  shell getprop ro.product.name
查看当前运行应用
    adb shell dumpsys window | grep -i mFocusedwindow
    adb shell dumpsysactivit top | grep ACTIVITY
adb shell settings get global package_verifier_enable
adb command: adb shell settings put global package_verifier_enable 0
adb shell settings get secure install_non_market_apps
adb shell settings put secure install_non_market_apps 1


2019-1-11
logcat
dumpsys
uiautomator
ACS 熟悉
烧录 case code


2019-1-7
morning 
    熟悉库
afternoon
    adb、ui

acs 需要下载的文件放在一个服务器上，需要就去下载

分析完一条case 

python 解析 minicom 数据

import serial
import pynmea2
import time
ser = serial.Serial("/dev/ttyUSB2")
while True:
    line = ser.readline()
    if line.startswith('$GNRMC'):
    rmc = pynmea2.parse(line)
    print "Latitude: ", float(rmc.lat)/100
    print "Longitude: ", float(rmc.lon)/100
    break

uiittest 了解

disable car app
     cmd = "pm disable android.car.cluster.sample"
     cmd_user = "pm disable-user android.car.cluster.sample"

