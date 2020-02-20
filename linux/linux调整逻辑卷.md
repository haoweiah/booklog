### linux调整逻辑卷

## 如果硬盘为xfs格式

- 1 lvscan 查看逻辑卷的大小
- 2 lvextend -L 300M /dev/lvm/lo 调整逻辑卷大小到300M
- 3 xfs_growfs /dev/lvm/lo 使逻辑卷同步

## 如果硬盘为ext4格式

- 3 resize2fs /dev/lvm/lo