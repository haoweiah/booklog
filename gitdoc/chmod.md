​        当整个文件夹是root权限，使用 `sudo chmod -R +777 xxx`任然不能git push时，使用 `ls -al`查看 `.git`文件夹任然是属于root的，所以需要修改这个的权限，`sudo chmod -R +777 .git`OK，搞定了

