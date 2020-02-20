### flask操作数据库

# flask中使用数据库

## flask中有Flask-SQLAlchemy扩展

flask中连接mysql数据库方式:

### app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test'

## 数据库的基本操作



> db.session.add(role)    添加到数据库的session中
>  db.session.add_all([user1, user2]) 添加多个信息到session中
>  db.session.commit()     提交数据库的修改(包括增/删/改)
>  db.session.rollback()   数据库的回滚操作
>  db.session.delete(user) 删除数据库(需跟上commit)

# Redis连接

## redis扩展

### Redis连接

在config文件中配置
 SESSION_TYPE=True
 SESSION_USE_SIGNER=True
 SESSION_REDIS= redis.StrictRedis(host='',port='',db=)
 PERMANENT_SESSION_LIFETIME = 86400 * 2...过期时间
 redis数据库的操作和操作字典类似，
 是使用session操作，session操作的是cookie中的session，使用flask_Session可以把cookie中的session数据同步到数据库中