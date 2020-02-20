# property
#
class Person:

    __slots__ = ('name', 'age')
    """
    我们讲到这里，不知道大家是否已经意识到，Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
    当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
    需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
    """
    def __init__(self, name, age):
        self._name = name
        self._age = age


    @property
    def name(self):
        return self._name


    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age



# 重写父类

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    @property
    def grade(self):
        return self.grade

    @grade.setter
    def grade(self, grade):
        self.grade = grade

    def study(self, course):

        print("{grade} 's {name} now study {course}".format(grade=self.grade, name=self.name, course=self.course))

class Teach(Person):

    def __init__(self, name, age, title):
        super.__init__(name, age)
        self._title = title


    @property
    def title(self):
        return self._title

    def teach(self, course):
        print("{grade} 's {name} now study {course}".format(grade=self._title, name=self.name, course=course))





from abc import ABCMeta, abstractclassmethod

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractclassmethod
    def make_voice(self):
        pass

class Dog(Pet):

    def make_voice(self):
        print("%s: wangwangwang"% self._nickname)


"""在上面的代码中，我们将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，
如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
上面的代码中，Dog和Cat两个子类分别对Pet类中的make_voice抽象方法进行了重写并给出了不同的实现版本，当我们在main函数中调用该方法时，
这个方法就表现出了多态行为（同样的方法做了不同的事情）。"""

"""
zai ci shu xi 
"""
