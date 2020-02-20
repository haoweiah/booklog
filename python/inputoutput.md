## 线程  
    python的thread模块是比较底层的模块，python的threading模块是对thread做了一些包装的，可以更加方便的被使用
    

>#coding=utf-8import threading
    from time import sleep,ctime
    def sing():
        for i in range(3):
            print("正在唱歌...%d"%i)
            sleep(1)
    def dance():
        for i in range(3):
            print("正在跳舞...%d"%i)
            sleep(1)
    if __name__ == '__main__':
        print('---开始---:%s'%ctime())
        t1 = threading.Thread(target=sing)
        t2 = threading.Thread(target=dance)
        t1.start()
        t2.start()
        #sleep(5) # 屏蔽此行代码，试试看，程序是否会立马结束？
        print('---结束---:%s'%ctime())

### 多线程的使用
    t1 = threading.Thread(target=函数引用， args=[,])
    t1.start()
    不需要使用join
    线程共享变量所以线程不是很安全
### 进程的使用

    from multiprocessing import Process
    import time


    def run_proc():
        """子进程要执行的代码"""
        while True:
            print("----2----")
            time.sleep(1)


    if __name__=='__main__':
        p = Process(target=run_proc)
        p.start()
        while True:
            print("----1----")
            time.sleep(1)
    进程间不共享全局变量
    进程间的通信使用Queque
### 多进程及进程池的使用   
    p = Process(target=run_proc, args=('test',18), kwargs={"m":20})
        p.start()
        sleep(1)  # 1秒中之后
        p.terminate() #立即结束子进程
        p.join()
    多进程使用需要join到主进程中，不然不会执行
    进程间的通行使用Queque完成
    进程池的使用
    from multiprocessing import Pool
    进程池中的通信使用
    multiprocessing.Manager()Queque()
### 协程
    yield
    协程就是使用yield，协程又称微线程
    gevent
    from gevent import monkey
    import gevent
    import random
    import time
    monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

    def coroutine_work(coroutine_name):
        for i in range(10):
            print(coroutine_name, i)
            time.sleep(random.random())

    gevent.joinall([
            gevent.spawn(coroutine_work, "work1"),
            gevent.spawn(coroutine_work, "work2")
    ])
    
    进程、线程、协程对比请仔细理解如下的通俗描述<u>有一个老板想要开个工厂进行生产某件商品（例如剪子）他需要花一些财力物力制作一条生产线，这个生产线上有很多的器件以及材料这些所有的 为了能够生产剪子而准备的资源称之为：进程只有生产线是不能够进行生产的，所以老板的找个工人来进行生产，这个工人能够利用这些材料最终一步步的将剪子做出来，这个来做事情的工人称之为：线程这个老板为了提高生产率，想到3种办法：
    在这条生产线上多招些工人，一起来做剪子，这样效率是成倍増长，即单进程 多线程方式老板发现这条生产线上的工人不是越多越好，因为一条生产线的资源以及材料毕竟有限，所以老板又花了些财力物力购置了另外一条生产线，然后再招些工人这样效率又再一步提高了，即多进程 多线程方式老板发现，现在已经有了很多条生产线，并且每条生产线上已经有很多工人了（即程序是多进程的，每个进程中又有多个线程），为了再次提高效率，老板想了个损招，规定：如果某个员工在上班时临时没事或者再等待某些条件（比如等待另一个工人生产完谋道工序 之后他才能再次工作） ，那么这个员工就利用这个时间去做其它的事情，那么也就是说：如果一个线程等待某些条件，可以充分利用这个时间去做其它事情，其实这就是：协程方式简单总结进程是资源分配的单位线程是操作系统调度的单位进程切换需要的资源很最大，效率很低线程切换需要的资源一般，效率一般（当然了在不考虑GIL的情况下）协程切换任务资源很小，效率高多进程、多线程根据cpu核数不一样可能是并行的，但是协程是在一个线程中 所以是并发
