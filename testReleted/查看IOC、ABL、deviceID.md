### 查看IOC、ABL、deviceID

> ioc
>  刷好板子后，按r重启
> 00:00 00s001ms --------------------------------
> 00:00 00s001ms - Intel KC3.0 2014 - 2017 -
> 00:00 00s001ms --------------------------------
> 00:00 00s001ms Branch: On branch release/KC4.0_Base
> 00:00 00s001ms Commit hash: a1c9866e34c1c6a60d2bd240635fe48171625f2e
> 00:00 00s001ms Build Date: 2018-8-24 (22:37)
> 00:00 00s004ms FBL ID: 0xA0E229
> 00:00 00s004ms (Production build)
> 00:00 00s004ms Communication: CBC
> 00:00 00s004ms Reset cause: 0x00
> 00:00 00s004ms WatchDog cause: 0x00
> 00:00 00s004ms Setup: Gordon Peak MRB Mainboard Fab D 
> 00:00 00s004ms GP MRB Mainboard Fab E 
> 00:00 00s005ms Customer feature board with id 9 detected 
> 00:00 00s005ms Customer configuration: INTEL 
> 00:00 00s005ms No IOC error trace available. No issue detected -> OK 
> 00:00 00s006ms Build: 4. 0. 8 
> 日志中的build后的就是IOC 版本
> ABL
>  刷好ABL后，按n1r#开启sos
> abl-APL: rel.1820-Android-HF1
> CPU: APL-D0 [4C @ 1900MHz: premium SKU], ucode rev.32; power-on reset
> CSE: FW 3.1.55.2271, SB: OFF, MB: OFF
> CSE: boot dev #2: SPI
> IPC config: R.<28 bytes> (16ms)
> PCB #B00F: GR MRB (BMP fab.E, 4x16Gb), F:8F; BM:0
> MRC: [v0.56.38/89.19] FB OK(0): 8GB
> CSE: send DID UMA 10000000, 34MB
> auto-boot ...
> image#0 - mmc2:@0: MMC: 16G, boot 0/0 [5.01 HS400 FW 3.5 4e 5/15]: 
> ==> jump to image @6e000010 (setup @0) ...
> ACRN Hypervisor
>
> 日志中第一行就是ABL信息
>
> deviceID 2口按n4回车
>  命令行输入：fastboot devices
> root@inteltop:~# fastboot devices
> R1J56L38b31485 fastboot
> 如果要查看6口id可以先在2口关闭fastboot模式，按n1r#顶替掉,在6口输入n4,再在命令行输入 fastboot devices