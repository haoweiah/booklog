### Linux默认变量问题

今天写shell脚本有一个智障的问题
报错 mkdir command not fond
原因：
 开始我在脚本里定义了path变量小写的后来不爽改成大写的PATH
 PATH是linux的全局环境变量，我重新定义了他，报错，这是变量命名的错误