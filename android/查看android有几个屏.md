查看android 有几个屏
adb  shell dumpsys SurfaceFlinger | grep -i 'Display.*entries.*'