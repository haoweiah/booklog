### Django问题描叙

## Django自带了用户注册

```
调用User.object.create_user()实现保存和加密隐私信息，若报错，
是为integrityerror，用户已存在，或已注册，Django默认激活和用户，要改变为未激活状态
Django如果要在user表中添加字段要继承AbstractUser,可以添加字段，但是要修改原始字段就要重写登录模块
```

## 登录验证

```
验证用户是否登录的是使用的装饰器login_required实现的传入的参数是as_view中的view返回值，要在setting.py 中设置LONGIN_URL='/users/login'
也可以使用request.user.is_authenticated()方法完成
```

## 邮件激活

```
邮件激活使用了Django自带的send_mail方法，因为发送邮件是耗时操作所以使用celery异步执行
```

## celery异步操作

```
celery可以使用redis服务器作为中间人，在项目中创建一个celery_tasks文件夹，在文件夹中创建tasks.py 文件，
实例化celery对象配置连接redis数据库，使用对象.task来装饰send_mail()这样让方法成为了celery任务。
* celery实现，把项目发送一份到celery服务器，导入Django环境，并启动。
* 终端创建celery任务celery -A celery_tasks.tasks worker -l info
客户端调用发送邮件方法要加一个delay延迟
```

## 用户中心三大功能：个人信息、全部订单、收货地址

```
个人信息：登录验证
        next参数作用：用于标记，当用户登录时可以查看next后是否有页面，有可以跳转过去
        用户地址：接受浏览器的post表单请求用orm的create方法保存到数据库
        商品：tinymce使用富文本，富文本需要安装需要在app里应用，还好在总的urls里配置url
 
```

## 页面静态化

```
使用loader.get_template()加载模板，使用template.render(context)把模板变成文件，
把html文件静态化，保存在缓存里，缓存要设置过期时间，当时间过期后会重新查询数据库，
当后台人员增加数据或者删除数据时执行这个方法，使用obj.save(),obj.delete()
用户未登录时访问的静态页面，登录后访问的是动态页面，页面静态写成文件可以使用celery异步实现
```

## Django中间件有五个

- process_request(request)

```
处理请求前：在每个请求上调用，返回None或HttpResponse对象
```

- process_view(request, view_func, view_args, view_kwargs)

```
处理视图前：在每个请求上调用，返回None或HttpResponse对象.
```

- process_template_response(request, response)

```
处理模板响应前：在每个请求上调用，返回实现了render方法的响应对象.
```

- process_response(request, response)

```
处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象.
```

- process_exception(request,exception)

```
 	异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象.
```

## django 中间件应用场景

```
拦截器查看ip访问的频率可以禁止访问、debug关闭后，
报错信息查看可以使用process_exception来返回给超级用户或者特殊ip查看错误页面
```

> https://code.ziqiangxuetang.com/django/django-middleware.html

## Django分页功能

```
Django中有一个Paginator对象可以对一页对象进行分页操作需要传入的参数是object——list，
每页显示的数据，最后一页数量大于多少是才显示最后一页，
默认为0可以不传，如果要获取每页的数据可以用paginator.page(页码)来获取
```

## 商品详情页

```
用户未登录时查询出数据可以保存在
cache缓存中设置过期时间可以使用
```

## 订单页面有一个乐观锁悲观锁

```
一元秒杀时的操作，有一个乐观锁和悲观锁
乐观锁：查询的时候不加锁，更新的时候对比库存和当时查询的库存是否一致，在操作数据库之前先加上事物，如果操作失败rollback
创建事物点：save_point =transaction.savepoint()
回滚：transaction.savepoint_rollback(save_point)
提交：transaction.savepoint_commit(save_point)
悲观锁：查询的时候加锁别人不能查询，当要操作某条记录时，立即将该条记录锁起来，谁也无法操作，直到它操作完
select * from table where id=17 for update;
```

## 支付怎样保证安全

```
设置公钥和私钥保证安全
```