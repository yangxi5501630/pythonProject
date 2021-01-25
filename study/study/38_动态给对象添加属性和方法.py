from types import MethodType

#__slot__声明可以节省内存,应用与大量创建类对象时
#如果动态添加某个成员必须用__slots__修饰
#创建空类
class student(object):
    __slots__ = ("name", "age", "func") #声明将来只能添加name和age成员

#动态添加成员
A = student()
A.name = "张三"
A.age = 18
print(A.name, A.age)

#动态添加函数
def run(self):
    print(self.name, self.age)

A.func = MethodType(run, A)
A.func()
