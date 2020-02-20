### git操作命令

## 第一次连接仓库如果仓库中有文件

```
git push -u origin master 执行这个命令会失败
上面是官方提示的方法，只有仓库是空的时候才可以这样用。
如果在创建仓库时选择了添加 license 文件等操作，按上面来操作就会报错。
git remote add origin https://github.com/logig/wechat-shake.git
git pull
git branch -u/--set-upstream-to origin/master # 下一次 push 就不用带 -u 了
git pull
git push

我第一次直接pull代码下来失败了，不知道为啥，后来使用 git push origin master -r 强制推，这个就把原来的代码删除了慎用
```

## git 命令

- git config --global user.name ''
- git config --global user.email ''
- git config --list
- git init      # 初始化仓库
- git add       # 跟踪新文件
- git commit    # 提交到本地仓库
- git clone ... # 克隆远程仓库
- git status    # 检查当前文件状态
- git diff      # 查看尚未暂存文件更新部分
- git diff --staged # 查看已暂存但未提交的内容
- git commit -a # 可以跳过git add 步骤
- git rm file   # 让该文件不在被git追踪,文件也被删除了
- git rm --cached file # 让文件不被追踪，但是还会存在磁盘上，和配置在.gitignore中效果一样
- git mv nameold namenew # 重命名文件
- git log # 查看提交历史
- git log -p -2 # -p显示每次提交的内容差异，-2仅显示最近2次提交
- git log --stat # 可以查看每次提交的简略统计信息
- git log --pretty=oneline # 让信息在一行显示
- git log --pretty=format："%h - %an , %ar : %s" # 格式化输出信息

**git log 功能很强大**

- 撤销操作
- git commit --amend # 替代上次提交
- git checkout -- file # 文件修改被撤销