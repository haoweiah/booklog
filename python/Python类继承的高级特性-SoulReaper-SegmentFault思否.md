专栏 / SoulReaper / 文章详情 LoftySoul 678 发布于 SoulReaper2014-10-30 发布Python类继承的高级特性  python 13k 次阅读  ·  读完需要 14 分钟昨天在Python类的多重继承那里纠结了好久,在提问版块提了个问题探讨了探讨(链接)才完全搞明白,现在把类的特性整理下,供以后参考正文首先得说明的是,Python的类分为经典类 和 新式类经典类是python2.2之前的东西,但是在2.7还在兼容,但是在3之后的版本就只承认新式类了新式类在python2.2之后的版本中都可以使用经典类和新式类的区别在于:

 1. 经典类是默认没有派生自某个基类的,而新式类是默认派生自object这个基类的:

 2. ```python
    old styleclass A():pass# new styleclass A(obejct):pass2.经典类在类多重继承的时候是采用从左到右深度优先原则匹配方法的..而新式类是采用C3算法(不同于广度优先)进行匹配的3.经典类是没有__MRO__和instance.mro()调用的,而新式类是有的.为什么不用经典类，要更换到新式类因为在经典类中的多重继承会有些问题...可能导致在继承树中的方法查询绕过后面的父类:class A():def foo1(self):print "A"class B(A):def foo2(self):passclass C(A):def foo1(self):print "C"class D(B, C):passd = D()d.foo1()按照经典类的查找顺序从左到右深度优先的规则，在访问d.foo1()的时候,D这个类是没有的..那么往上查找,先找到B,里面没有,深度优先,访问A,找到了foo1(),所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过.所以python引入了新式类的概念,每个基类都继承自object并且,他的匹配规则也从深度优先换到了C3C3算法C3算法是怎么做匹配的呢..在问答版块上面讨论之后,归结如下:C3算法的一个核心是merge.在merge列表中，如果第一个序列mro的第一个类是出现在其它序列，并且也是第一个，或者不出现其它序列，那么这个类就会从这些序列中删除，并合到访问顺序列表中比如:(引用问题中zhuangzebo的回答@zhuangzebo)class A(O):passclass B(O):passclass C(O):passclass D(A,B):passclass E(C,D):pass首先需要知道 O(object)的mro(method resolution order)列表是[O,]那么接下来是:mro(A) = [A, O]mro(B) = [B, O]mro(C) = [C, O]mro(D) = [D] + merge(mro(A), mro(B), [A, B])= [D] + merge([A, O], [B, O], [A, B])= [D, A] + merge([O], [B, O], [B])= [D, A, B] + merge([O], [O])= [D, A, B, O]mro(E) = [E] + merge(mro(C), mro(D), [C, D])= [E] + merge([C, O], [D, A, B, O], [C, D])= [E, C] + merge([O], [D, A, B, O], [D])= [E, C, D] + merge([O], [A, B, O])= [E, C, D, A, B] + merge([O], [O])= [E, C, D, A, B, O]然后还有一种特殊情况:比如：merge(DO,CO,C) 先merge的是Dmerge(DO,CO,C) 先merge的是C意思就是.当出现有 一个类出现在两个序列的头(比如C) 这种情况和 这个类只有在一个序列的头(比如D) 这种情况同时出现的时候,按照顺序方式匹配。新式类生成的访问序列被存储在一个叫MRO的只读列表中..你可以使用instance.__MRO__或者instance.mro()来访问最后匹配的时候就按照MRO序列的顺序去匹配了C3和广度优先的区别:举个例子就完全明白了:class A(object):passclass B(A):passclass C(B):passclass D(A):passclass E(D):passclass F(C, E):pass按照广度优先遍历,F的MRO序列应该是[F,C,E,B,D,A]但是C3是[F,E,D,C,B,A]意思是你可以当做C3是在一条链路上深度遍历到和另外一条链路的交叉点,然后去深度遍历另外一条链路,最后遍历交叉点新式类和经典类的super和按类名访问问题在经典类中,你如果要访问父类的话,是用类名来访问的..class A():def __init__(self):print "A"class B(A):def __init__(self):print "B"A.__init__(self) #python不会默认调用父类的初始化函数的这样子看起来没三问题,但是如果类的继承结构比较复杂，会导致代码的可维护性很差..所以新式类推出了super这个东西...class A():def __init__(self):print "A"class B(A):def __init__(self):print "B"super(B,self).__init__()这时候，又有一个问题:当类是多重继承的时候,super访问的是哪一个类呢?super实际上是通过__MRO__序列来确定访问哪一个类的...实际上就是调用__MRO__中此类后面的一个类的方法.比如序列为[F,E,D,C,B,A]那么F中的super就是E,E的就是Dsuper和按照类名访问 混合使用带来的坑class A(object):def __init__(self):print "enter A"print "leave A"class B(object):def __init__(self):print "enter B"print "leave B"class C(A):def __init__(self):print "enter C"super(C, self).__init__()print "leave C"class D(A):def __init__(self):print "enter D"super(D, self).__init__()print "leave D"class E(B, C):def __init__(self):print "enter E"B.__init__(self)C.__init__(self)print "leave E"class F(E, D):def __init__(self):print "enter F"E.__init__(self)D.__init__(self)print "leave F"这时候打印出来是：enter Fenter Eenter Bleave Benter Center Denter Aleave Aleave Dleave Cleave Eenter Denter Aleave Aleave Dleave F可以看出来D和A的初始化函数被乱入了两次！按类名访问就相当于C语言之前的GOTO语句...乱跳,然后再用super按顺序访问..就有问题了所以建议就是要么一直用super,要么一直用按照类名访问最佳实现:
    ```

	1. 避免多重继承
	2. super使用一致
	3. 不要混用经典类和新式类
	4. 调用父类的时候注意检查类层次

参考资料：
	1. 《python高级编程》
	2. http://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html
	3. http://www.cnblogs.com/i2u9/archive/2013/03/19/pythonmroc3.html

新浪微博微信TwitterFacebook你可能感兴趣的
	* background: radial-gradient径向渐变yuan_yuanxucss
	* Jenkins使用Git Submodule姜家志submodulegitjenkins-cijenkins
	* Laravel学习笔记之Schema Builder 和 Migration System(上)lx1036phplaravelschemamigration
	* 开源的一个java 写的图床关注公众号搜云库java
	* 封装一个FTP工具类Honwhyftpjava
	* Flex入坑指南贾顺名flexboxcss
	* Docker初体验——踩过的那些坑！墨梅docker
	* 【yii2调试神器】yii2-debug能力分析和配置项解析阿北debugyii2yii

