https://blog.csdn.net/u013378306/article/details/70146102

在一个类下写logging.basicConfig，在此类中调用其他包的方法都会使用该配置，其他类中无需在配置logging.basicConfig。如果不写默等级为WARN

注意，在logging.basicConfig 之前不要有logging.×××，不然配置会不起作用,如下则不会打印：

```
import logginglogging.debug("aaaaaaaaaaa")logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)logging.debug("wwwwwwwwwwwwww")
```

正确的写法为

```
import logging logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)logging.debug("aaaaaaaaaaa")logging.debug("wwwwwwwwwwwwww")
```

# 1.简单的将日志打印到屏幕

|

`import logging

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')`

`屏幕上打印: WARNING:root:This is warning message`

|

默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

# 2.通过logging.basicConfig函数对日志的输出格式及方式做相关配置

|

`import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')`

`./myapp.log文件中内容为:
Sun, 24 May 2009 21:48:54 demo2.py[line:11] DEBUG This is debug message
Sun, 24 May 2009 21:48:54 demo2.py[line:12] INFO This is info message
Sun, 24 May 2009 21:48:54 demo2.py[line:13] WARNING This is warning message`

|

logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

# 3.将日志同时输出到文件和屏幕

|

`import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')`

`屏幕上打印:
root        : INFO     This is info message
root        : WARNING  This is warning message`

`./myapp.log文件中内容为: Sun, 24 May 2009 21:48:54 demo2.py[line:11] DEBUG This is debug message
Sun, 24 May 2009 21:48:54 demo2.py[line:12] INFO This is info message
Sun, 24 May 2009 21:48:54 demo2.py[line:13] WARNING This is warning message`

|

# 4.logging之日志回滚

|

`import logging
from logging.handlers import RotatingFileHandler

#################################################################################################
#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)
################################################################################################`

|

从上例和本例可以看出，logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的。
logging的几种handle方式如下：

|

logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件
logging.FileHandler: 日志输出到文件

日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
logging.handlers.BaseRotatingHandler
logging.handlers.RotatingFileHandler
logging.handlers.TimedRotatingFileHandler

logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets
logging.handlers.DatagramHandler:  远程输出日志到UDP sockets
logging.handlers.SMTPHandler:  远程输出日志到邮件地址
logging.handlers.SysLogHandler: 日志输出到syslog
logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志
logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer
logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器

|

由于StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中，
上述其它处理方式的使用请参见python2.5手册！

# 5.通过logging.config模块配置日志

|

`#logger.conf`

`###############################################`

`[loggers]
keys=root,example01,example02`

`[logger_root] level=DEBUG
handlers=hand01,hand02`

`[logger_example01] handlers=hand01,hand02
qualname=example01
propagate=0`

`[logger_example02] handlers=hand01,hand03
qualname=example02
propagate=0`

`###############################################`

`[handlers]
keys=hand01,hand02,hand03`

`[handler_hand01] class=StreamHandler
level=INFO
formatter=form02
args=(sys.stderr,)`

`[handler_hand02] class=FileHandler
level=DEBUG
formatter=form01
args=('myapp.log', 'a')`

`[handler_hand03] class=handlers.RotatingFileHandler
level=INFO
formatter=form02
args=('myapp.log', 'a', 10*1024*1024, 5)`

`###############################################`

`[formatters]
keys=form01,form02`

`[formatter_form01] format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s
datefmt=%a, %d %b %Y %H:%M:%S`

`[formatter_form02] format=%(name)-12s: %(levelname)-8s %(message)s
datefmt=`

|

上例3：

|

`import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')`

|

上例4：

|

`import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example02")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')`

|

### 6.logging是线程安全的

# 7 其他有关

1、总体介绍：

(1)Logger：一个界面，程序员在写应用程序时直接使用它来记录日志信息。该类无需自定义重载。

(2)Handler：处理器，它用于将由Logger创建的日志信息发送到相应的目的地;不同的Handler种类(继承自Handler抽象类)发送到不同的目的地，比如：FileHandler将日志写入到文件中，StreamHandler将日志输出到控制台，SMTPHandler将日志以邮件的形式发送出去，SocketHandler将日志用TCP Socket发送出去，而DatagramHandler将日志用UDP数据报发送出去，等等。以上都是logging已经实现的Handler，另外，也可以自己定义自己的Handler，只要继承自Handler抽象类并重载emit方法即可。

(3)Filter：过滤器，表明一个日志信息是否要被过滤掉而不记录;它提供了一个好的、细粒度的日志控制。可以重载Filter来自定义自己的Filter，此时要重载Filter类的filter方法。

(4)Formatter：格式化工具，在Handler处理器把日志信息发送出去之后，会使用该类对象格式日志信息，即该类指定日志信息最终被输出的格式。该类无需自定义重载。

2、相互关系：

(1)Logger可以包含一个或多个Handler和Filter，即Logger与Handler或Fitler是一对多的关系;

(2)Handler可以包含一个或多个Filter，但只能包含一个Formatter，即Handler与Filter是一对多的关系，与Formatter是一对一的关系;

(3)Filter可以多次被包含在Logger和Handler中;

(4)Formatter只能被包含在Handler中，不能被包含在Logger中，并且只能有一个被包含在Handler中。

![Python日志系统Logging](http://upload-images.jianshu.io/upload_images/2676555-44b2b3bf976d2b3d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

说明：不带箭头端是包含者，带箭头端是被包含者;箭头线旁边的1和n表示箭头线两端的对象之间对应关系(一对多或一对一)，此处的“一对多”指的是一个对象可以包含多个另外一个对象，“一对一”指的是一个对象只能包含一个另外一个对象。

3、常用功能：

(1)Logger：可以设置Logger上的日志等级(Logger.setLevel方法)、添加或移除过滤器(Logger.addFilter和Logger.removeFilter方法)、添加或移除处理器(Logger.addHanlder和Logger.removeHandler方法)以及一些日志记录工具(Logger类的debug、info、error、warning、critical、log等方法)。

(2)Handler：可以设置Handler上的日志等级(Handler.setLevel方法)、设置Formatter(Handler.setFormatter方法)、添加或移除过滤器(Handler.addFilter和Handler.removeFilter方法)。

(3)Fitler：默认的Filter类，需要获取一个字符串类型的参数，该参数是用来判断日志信息是否允许被记录。Filter类中有一个filter方法，该方法返回真则表示日志信息被记录，否则将丢弃，不再处理。如果该参数为空字符串，则filter方法返回真;否则，该字符串参数表示着一个Logger(每个Logger对象都有一个用点分隔的字符串名字)，只有当前处理日志信息的Logger对象是该字符串参数指定的Logger对象或子对象，filter方法才返回真，其它情况返回假。

(4)Formatter：Formatter在实例化时，需要传递至少一个参数、至多三个参数。第一个参数代表格式化字符串，第二个参数代表日期格式，第三个参数表示格式化字符串中将要使用哪种占符符(“%”表示旧的Python格式化方式，“{”表示新的Python格式化方式，“$”表示模板格式化方式)。

4、logging工作流程：

(1)第一次导入logging模块或使用reload函数重新导入logging模块，logging模块中的代码将被执行，这个过程中将产生logging日志系统的默认配置。

(2)自定义配置(可选)。logging标准模块支持三种配置方式：dictConfig、fileConfig、listen。其中，dictConfig是通过一个字典进行配置Logger、Handler、Filter、Formatter，fileConfig则是通过一个文件进行配置，而listen则监听一个网络端口，通过接收网络数据来进行配置。当然，除了以上集体化配置外，也可以直接调用Logger、Handler等对象中的方法在代码中来手工进行单独配置。关于字典配置和文件配置的格式，请参见Python logging官方文档。

(3)使用logging模块的全局作用域中的getLogger函数来得到一个Logger对象(其参数即是一个字符串，表示Logger对象的名字，即通过该名字来得到相应的Logger对象)。

(4)使用Logger对象中的debug、info、error、warning、critical、log等方法记录日志信息，其处理流程如下：

1> 判断日志的等级是否大于Logger对象的等级：如果大于，则往下执行;否则，流程结束。

2> 产生日志。第一步，判断是否有异常，如果有，则添加异常信息;第二步，处理日志记录方法(如debug、info等)中的占位符，即一般的字符串格式化处理。

3> 使用注册到Logger对象中的Filters进行过滤。如果有多个过滤器，则依次过滤;只要有一个过滤器返回假，则过滤结束，且该日志信息将丢弃，不再处理，而处理流程也至此结束。否则，处理流程往下执行。

4> 在当前Logger对象中查找Handlers，如果找不到任何Handler，则往上到该Logger对象的父Logger中查找;如果找到一个或多个Handler，则依次用Handler来处理日志信息。但在每个Handler处理日志信息过程中，会首先判断日志信息的等级是否大于该Handler的等级，如果大于，则往下执行(由Logger对象进入Handler对象中);否则，处理流程结束。

5> 执行Handler对象中的filter方法，该方法会依次执行注册到该Handler对象中的Filter。如果有一个Filter判断该日志信息为假，则此后的所有Filter都不再执行，而直接将该日志信息丢弃，处理流程结束。

6> 使用Formatter类格式化最终的输出结果。 注：Formatter同上述第2步(即2>)的字符串格式化不同，它会添加额外的信息，比如：日志产生的时间、产生日志的源代码所在的源文件的路径等等。

7> 真正地输出日志信息(到网络、文件、终端、邮件等)。至于输出到哪个目的地，由Handler的种类来决定。