'''
self代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象
self.__class__  代表类名_
'''
class student(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def run(self):
        print("我要跑路了")

    def eat(self, food):
        print("我会吃%s" % (food))

    def play(self):
        print(self.name, self.age, self.height, self.weight)

A = student("张三", 18, 170, 173)
B = student("李四", 20, 180, 200)
A.play()
B.play()
