adb 获取app、时间、流量的命令操作

### adb 获取 启动程序的程序名

    adb shell logcat |grep START
    

### adb 获取 CPU状态值

    adb shell dumpsys cpuinfo | grep packagename
    

### adb 获取 流量值

    adb shell ps | grep packagename         获取到包的id
    adb shell cat /proc/pid/net/dev             通过进程id获取流量
    eg:     adb shell cat /proc/5715/net/dev

### adb 获取 内存信息

    adb shell top
    VSS - Virtual Set Size 虚拟耗用内存
    RSS - Resident Set Size 实际使用物理内存
    