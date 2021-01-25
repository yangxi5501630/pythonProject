'''
函数格式：
def 函数名(参数列表):
    语句
    return 表达式
'''

#1.定义无参无返回值的函数
def printinfo():
    print("hello,world")

#调用函数
printinfo()


#2.定义有参函数
def printinfo1(name, age):
    print(name, age)

printinfo1("youcw", 18)

#3.函数返回值
def mysum(num1, num2):
    return num1 + num2

sum = mysum(100, 200)
print(sum)

#4.函数传参之:值传递
#值传递的数据类型是不可变的,字符串,元组,数字
#由于不可变性,函数如果同名操作,必然是重新分配的对象
def fun1(num3):
    print(num3)
    print(id(num3))
    num3 = 10
    print(id(num3))

val = 20
print(id(val))
fun1(val)
print(val)

#5.传递参数之:引用传递
#引用传递的数据类型是可变的,列表,字典,集合(分拆搞)
def fun2(list1):
    list1[0] = 100

list0 = [1,2,3,4,5]
fun2(list0)
print(list0)

def fun3(dict1):
    i = 0
    for index, key in enumerate(dict1):
        dict1[key] = i
        i += 1

dict0 = {1:"A", 2:"B"}
fun3(dict0)
print(dict0)

def fun4(set1):
    set1.update([3,4])
    set1.update((5,6))
    set1.update("hello")

set0 = set({1:"A", 2:"B"})
fun4(set0)
print(set0)

a = 10
b = 10
b = 40
print(id(a), id(b))

c = 20
d = 30
print(id(c), id(d))
d = c
print(id(c), id(d))

#6.关键字传递参数:参数的顺序可以不一致
def myprintinfo(name, age):
    print(name, age)

myprintinfo(age=18, name="youcw")

#7.默认参数:如果不传递参数,使用默认参数,最好将默认参数放到最后
def myprintinfo1(name, age=18):
    print(name, age)

myprintinfo1("youcw")

#8.不定长参数
#加了星号(*)的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组
def fun(name, *args):
    print(name)
    print(type(args))
    for i in args:
        print(i)

fun("youcw")
fun("youcw", "zhangsan", "lisi", 123, [1,2,3,4])

def mysum1(*a):
    sum = 0
    for i in a:
        sum += i
    return sum
print(mysum1(1,2,3,4,5))

#**代表键值对的参数字典，和*所代表的意义类似
def fun2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for index, key in enumerate(kwargs):
        print("%s:%d" %(key, kwargs[key]))

fun2(x = 1)
fun2(x=1, y=2, z=3)

#二者结合
def fun3(*args, **kwargs):
    print(args) #元组
    print(kwargs) #字典

print("*****************")
fun3(100)
fun3(x=1,y=2)
fun3(100,x=1,y=2)

'''
概念：不使用def这样的语句定义函数，使用lambda来创建匿名函数

特点：
1、lambda只是一个表达式，函数体比def简单
2、lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3、lambda函数有自己的命名空间,且不能访问自由参数列表之外的或全局命名空间的参数
4、虽然lambda是一个表达式且看起来只能写一行，与C和C++内联函数不同。


格式：lambda 参数1,参数2,……,参数n:expression
'''

sum = lambda num1, num2:num1 + num2
print(sum(1,2))

#函数也是一种数据类型
def sum(a, b):
    return a +b

f = sum
aa = f(2,3)
print(aa)


