## 烧录ioc
    
sudo /opt/intel/platformflashtool/bin/ioc_flash_server_app -s /dev/ttyUSB2 -t <ioc_firmware_gp_mrb_fab_xxx>.ias_ioc
## 烧录 spl
    在2口开启rn1#
     sudo /opt/intel/platformflashtool/bin/ias-spi-programmer --write <ifwi-apl-spi-xxx >.bin