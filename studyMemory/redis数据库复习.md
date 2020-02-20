### redis数据库复习

# 2018-4-19

## redis 复习

### 值的类型分为五种

- 字符串string
- 哈希hash
- 列表
- 集合
- 有序集合

## 键命令

- keys * 查找所有的键

```
keys 'a*' 查找包含a的键

exists a1 判断a1是否存在

type key 查看键对应的类型

del key1 删除键对应的值

flushall 清空所有数据库

flushdb 删除当前数据库内容

ttl key 查看有效时间

hash类型

hset key field value 设置单个属性例：hset user name itheima

一次设置 多个属性 hmset key field1  value1 field2 value2

获取键值 hkeys u2

获取一个属性的值 hget key field

删除 hdel key field1 field2

删除对应的属性值也会被删除
```



# list 类型

```
## list类型的数据有些不一样

## 在左侧插入数据 lpush key value1 value2

## 在右侧插入数据 rpush key value1 value2

# 左右插入数据不同点是lrange读取的时候不一样

## list可以在某一个元素前加入数据 linsert a1 before b 3

## list 查询时用lrange start stop
start、stop为元素的下标索引
索引从左侧开始，第一个元素为0
索引可以是负数，表示从尾部开始计数，如-1表示最后一个元素

## list 的修改 lset a 1 z 把key a中的下标1元素改为z

## list删除 lrem a1 -2 b
```

## 例6.2：从'a2'列表右侧开始删除2个'b'

```
lrem a2 -2 b
```

# 无序和有序不常用知道就好