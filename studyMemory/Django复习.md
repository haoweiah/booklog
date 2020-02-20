### Django复习

## 迁移数据库的命令

```
python manage.py makemigrations 创建
python manage.py migrate 迁移
```

- 有两个注意点 
  - 1 、要兼容python2 的缘故，要在setting的__init__中导入import pymysql 然后pymysql.install_as_mysqldb()
  - 2、如果User模型继承了AbstractUser这个类，必须到setting中AUTH_USER_MODEL= 'users.USER'这个注册一下，不然迁移时会报E304错误，如果加了还报错就把pycharm重启一下

## celery 异步

- pip install celery

- 有一个celery类导入一下 
  - app = celery('',broker='redis://127.0.0.1:6379/3')

**celery说明：pip安装celery,实例化celery对象，并配置broker可以配置redis数据库，把redis的密码ip端口数据库号配置好，然后用装饰器让方法成为celery的任务，把所有代码拷贝到work服务器中，然后在tasks。py中导入Django环境，在项目文件夹中开启celery任务  celery -A celery_tasks.tasks worker -l info,在Django端调用时方法要加上delay**

## restful风格

```
比较重点的是路径问题：路径是API的具体地址，一般要用名词不使用动词，名词要用复数，
2、使用标准的http方法：get、post、put、delete四个动词，意思是获取、新建、更新删除，
3、状态码：服务器想浏览器返回状态码 常出现的状态码200 OK，404 请求地址不存在，500 服务器错误
```