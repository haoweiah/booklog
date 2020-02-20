### centos安装kvm虚拟机

lsmod | grep kvm

[hw@localhost ~]$ lsmod | grep kvm
kvm_intel 174841 0 
kvm 578518 1 kvm_intel
irqbypass 13503 1 kvm
\# 要显示三行，如果只有两行可能是没有开启虚拟化支持

yum -y install qemu-kvm libvirt virt-install bridge-utils 
\# 安装一些kvm必须的东西
安装之后或者之前可以执行yum update