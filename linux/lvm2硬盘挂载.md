### 硬盘挂载

1. 插上硬盘

2. vgscan //扫描所有卷组

3. vgdisplay //查看你卷组名是否冲突

   1. vgrename [VG UUID] [新的vgname] //修改vgname

4.  lvscan //查看卷组是否激活

   1. ```
      pi@haowx:~ $ sudo lvscan
        inactive          '/dev/data/v0' [500.00 GiB] inherit
      ```

5. vgchange //激活或不激活卷组

   1. ```
      pi@haowx:~ $ sudo vgchange -an /dev/data
        0 logical volume(s) in volume group "data" now active
      pi@haowx:~ $ sudo lvscan
        inactive          '/dev/data/v0' [500.00 GiB] inherit
      pi@haowx:~ $ sudo vgchange -ay /dev/data
        1 logical volume(s) in volume group "data" now active
      pi@haowx:~ $ sudo lvscan
        ACTIVE            '/dev/data/v0' [500.00 GiB] inherit
      ```

6. 挂载硬盘

   1. ```
      $mkdir ~/data
      先建立lv v0然后挂载
      $sudo mount /dev/data/v0 ~/data 
      ```