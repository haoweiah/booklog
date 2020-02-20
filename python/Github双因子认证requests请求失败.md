现在github开启了双因子认证造成了
s = requests.Session()
s.auth = (username,userpwd)
登录失败
userpwd如果使用密码则会登录失败
需要使用在github上生成 token
点击右上角头像的下来小三角 => Settings => Personal access tokens
Generate new token => 填写token的描述 => 选择token的权限范围（如果只是为了提交代码只勾选repo就够了） => 点击Generate Token
然后会生成一个160bits（40bytes）的token，并提示你让你记住这个token，之后不会再出现。

userpwd需要使用这个token就可以了

后经过验证github会制止这种行为正在想解决方案