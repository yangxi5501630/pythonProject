'''
try……except……else...finally
格式：
try:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句3
……
except 错误码 as e:
    语句m
else:
    语句n
finally:
    语句p

作用：语句1无论是否有错误都执行最后的语句p
     用来检测try语句块中的错误，从而让except语句捕获错误信息并处理
执行流程:
1、如果当try“语句1”执行出现错误，会匹配第一个错误码，如果匹配上就执行对应"语句"
2、如果当try“语句1”执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句。或者到程序的最上层
'''
#场景分析,第一条语句错了,程序直接退出,但是还想执行第二条语句,咋办?
#print(1/0)
#print("hello,world")

#搞定:情形1 try...except...finally
try:
    print(1/0)
except ZeroDivisionError as e:
    print("除数为0了")
finally:
    print("hello,world")

#情形2 try...except....else
try:
    print(3/1)
except NameError as e:
    print("变量没有定义")
except ZeroDivisionError as e:
    print("除数为0")
else:
    print("代码没毛病")

try:
    print(3/0)
except NameError as e:
    print("变量没有定义")
except ZeroDivisionError as e:
    print("除数为0")
else:
    print("代码没毛病")

try:
    print(num/0)
except NameError as e:
    print("变量没有定义")
except ZeroDivisionError as e:
    print("除数为0")
else:
    print("代码没毛病")

#情形3:except ,可以不用跟错误马,只要是错误都捕获
try:
    #print(4/0)
    print(num/0)
except:
    print("出错了")
else:
    print("没错")

#情形4:带多种异常
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print("么有定义或者除数为0了")

#情形5:#特殊
#1、错误其实是class(类),所有的错误都继承自BaseException,所以在捕获的时候，它捕获了该类型的错误，
try:
    print(1/0)
except BaseException:
    print("异常1")
except ZeroDivisionError:
    print("除数为0")

#情形6:
#2、跨越多层调用，main调用了func2，func2调用了func1，func1出现了错误
# 这里只要main捕获到就可以处理
def func1(num):
    print(1 / num)
def func2(num):
    func1(num)
def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e:
    print("除数为0")

#断言
def func(num, div):

    assert (div != 0),"div不能为0"
    return  num / div

print(func(10, 0))
