'''
    私有属性特点:
    1.通过内部的方法，取修改私有属性
    2.通过自定义的方法实现对私有属性的赋值与取值
    3.如果要让的内部属性不被外部直接访问,在属性前加两个下划线（__）,
      在Python中如果在属性前加两个下划线，那么这个属性就变成了私有属性
    4.在Python中  __XXX__   属于特殊变量，可以直接访问
    5.在Python中  _XXX  变量，这样的实例变量外部是可以访问的,
      但是按照约定的规则，当我们看到这样的变量时，意思是“虽然我可以被访问，
      但是请把我视为私有变量，不要直接访问我”
'''
class student(object):
    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.__age__ = age
        self._height = height
        self.weight = weight
        self.__money = money #___money为私有

    def run(self):
        print("我要跑路了")

    def eat(self, food):
        print("我会吃%s" % (food))

    def play(self):
        print(self.name, self.age, self.height, self.weight)

    #内部方法访问
    def setmoney(self, money):
        self.__money = money

    #内部方法访问
    def getmoney(self):
        return self.__money

A = student("老王", 18, 172, 170, 10000)
#print(A.__money) #不允许外部访问
print(A.getmoney()) #允许内部访问

A.setmoney(500)
print(A.getmoney())

print(A.__age__)
print(A._height)
