nuc unlock 操作

adb reboot bootloader
fastboot flashing unlock
fastboot erase data （Q上userdata）
fastboot format data （选做）
fastboot reboot

adb remount    faild
adb disable-verity   success

adb reboot bootloader
fastboot erase data
fastboot format data (选做)
fastboot reboot

测试
    adb remount  成功即可