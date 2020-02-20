#### lvm扩盘



```
我有一块硬盘 /dev/sdb

1、 pvcreate /dev/sdb # 使盘支持lvm
2、 vgextend vg0 /dev/sdb # 在盘组中加入/dev/sdb
3、 如果根目录挂载在-- /dev/acrn/root上，可以使用 lvextend -L +2.8T /dev/acrn/root 扩盘
3.1、使用 lsblk检查
4、最后使用resize2fs /dev/acrn/root
4.1、使用df -Th检查
```

