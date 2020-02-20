#### 报错日志
    ~/booklog/manjarolinux >>> git push                                           ±[A1B1][master]
    To github.com:haoweiah/booklog.git
     ! [rejected]        master -> master (non-fast-forward)
    error: failed to push some refs to 'git@github.com:haoweiah/booklog.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Integrate the remote changes (e.g.
    hint: 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.


#### 重现问题的步骤
    git commit --am
    然后不修改任何东西
    就会出现报错

#### 修复方法1：
    git push -f
#### 修复方法2：
    git pull --rebase
