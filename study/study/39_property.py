'''
#问题场景1:
#缺点:age,name直接暴露,不安全
class student(object):
    def __init__(self, name ,age):
        self.age = age
        self.name = name

A = student("不要脸", -1)
print(A.name, A.age)
'''

'''
#问题2:采用私有方法限制
#缺点需要额外的函数访问
class student(object):
    def __init__(self, name ,age):
        self.__age = age
        self.__name = name

    def setage(self, age):
        if age < 0:
            self.__age = 0
        self.__age = 0

    def getage(self):
        return self.__age

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

A  = student("张三", "-1")
A.setname("李四")
A.setage(-10)
print(A.getage(), A.getname())
'''
#优化:利用property:可以对受限制的成员访问以点.的形式访问
class student(object):
    def __init__(self, name ,age):
        self.__age = age
        self.__name = name

        # 方法名为受限制的变量去掉双下划綫
        @property
        def age(self):
            return self.__age

        # 去掉下划线.setter
        @age.setter
        def age(self, age):
            if age < 0:
                age = 0
            self.__age = age

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, name):
            self.__name = name

A = student("张三", -1)
A.age = 18 #相当调用setage
A.name = "李四" #相当调用了setname
print(A.age, A.name) #相当调用getname和getage



