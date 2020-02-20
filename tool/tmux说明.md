### tmux 说明

***

- session操作

  ```
  //创建制定名称的session
  #tmux new -s ${session}
  ```

  ```
  //创建制定名称的session
  #tmux new -s ${session}
  ```

  ```
  //创建制定名称的session
  #tmux new -s ${session}
  ```

  ```
  //从tmux中脱离
  ^C + a  d
  ```

  ```
  //查看tmux session
  #tmux ls
  ```

  ```
  //查看tmux session
  #tmux ls
  ```

  ```
  //重新接入tmux
  #tmux a  -t ${serssionname}
  ```

  ```
  //删除session
  Ctrl+a :kill-session
  ```

  ```
  //临时退出session
  Ctrl+a d
  ```

  ```
  //删除所有session
  Ctrl+a :kill-server
  ```

  ```
  //删除指定session
  tmux kill-session -t $session_name
  ```

  

- window

  ```
//创建window
  Ctrl+a +c
  
  //删除window
  Ctrl+a &
  
  //下一个window
  Ctrl+a n
  
  //上一个window
  Ctrl+a p
  
  //重命名window
  Ctrl+a ,
  
  //在多个window里搜索关键字
  Ctrl+a f
  
  //在相邻的两个window里切换
  Ctrl+a l
  ```
  
  pane在window里，可以有N个pane，并且pane可以在不同的window里移动、合并、拆分
  
  ```
  //按顺序在pane之间移动
  Ctrl+b o
  
  //上下左右选择pane
  Ctrl+b 方向键上下左右
  
  //调整pane的大小
  Ctrl+b :resize-pane -U #向上
  Ctrl+b :resize-pane -D #向下
  Ctrl+b :resize-pane -L #向左
  Ctrl+b :resize-pane -R #向右
  在上下左右的调整里，最后的参数可以加数字 用以控制移动的大小，例如：
  Ctrl+b :resize-pane -D 50
  
  //在同一个window里左右移动pane
  Ctrl+b { （往左边，往上面）
  Ctrl+b } （往右边，往下面）
  
  //删除pane
  Ctrl+b x
  //更换pane排版
  Ctrl+b “空格”
  
  //移动pane至window
  Ctrl+b !
  
  //移动pane合并至某个window
  Ctrl+b :join-pane -t $window_name
  
  //显示pane编号
  Ctrl+b q
  
  //按顺序移动pane位置
  Ctrl+b Ctrl+o
  
  ```
  
- 其他

  ```
  复制模式
  Ctrl+b [
  空格标记复制开始，回车结束复制。
  
  //粘贴最后一个缓冲区内容
  Ctrl+b ]
  
  //选择性粘贴缓冲区
  Ctrl+b =
  
  //列出缓冲区目标
  Ctrl+b :list-buffer
  
  //查看缓冲区内容
  Ctrl+b :show-buffer
  
  //vi模式
  Ctrl+b :set mode-keys vi
  
  //显示时间
  Ctrl+b t
  
  //快捷键帮助
  Ctrl+b ? (Ctrl+b :list-keys)
  
  //tmux内置命令帮助
  Ctrl+b :list-commands
  ```

- tmux 配置

  ```
  设置Ctrl a 替换 Ctrl b 前缀建
  
  alt + 方向键在pane中跳转
  
  shift + 方向键 在window间跳转
  
  长按shift 可以操作鼠标复制粘贴
  
  滚轮键可以上下滚动，按 q 退出
  ```

  

  ```
  # Send prefix
  set-option -g prefix C-a
  unbind-key C-a
  bind-key C-a send-prefix
  
  # Use Alt-arrow keys to switch panes
  bind -n M-Left select-pane -L
  bind -n M-Right select-pane -R
  bind -n M-Up select-pane -U
  bind -n M-Down select-pane -D
  
  # Shift arrow to switch windows
  bind -n S-Left previous-window
  bind -n S-Right next-window
  
  # Mouse mode
  set -g mouse on
  
  
  # Set easier window split keys
  bind-key v split-window -h
  bind-key h split-window -v
  
  # Easy config reload
  bind-key r source-file ~/.tmux.conf \; display-message "tmux.conf reloaded"
  ```

  

