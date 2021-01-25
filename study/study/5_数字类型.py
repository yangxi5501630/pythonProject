import math
import random

'''
数字类型分为:整数,浮点数和复数
'''

'''
整数类型:
'''

num1 = 10
num2 = num1
print(num1, num2)
#对象num1和num2的地址一样
print(id(num1), id(num2))

#连续定义多个变量,这三个对象指向同一块内存区域
num3 = num4 = num5 = 1
print(num3, num4, num5)
print(id(num3), id(num4), id(num5))

#交互式赋值变量,地址不一样
num6, num7 = 1, 2
print(num6, num7)
print(id(num6), id(num7))

'''
浮点数,可能涉及四舍五入精度问题
'''
f1 = 1.1
f2 = 2.2
f3 = f1 + f2
print(f3)

'''
数字类型转换
'''
print(int(1.2))
print(float(1))
print(int("123"))
print(float("12.3"))

#如果有其他无效字符报错
#print(int("abc"))
#print(int("123abc456"))

#只有作为正负号才有效
print(int("+250"))
print(int("-250"))
#print(int("250+250"))
#print(int("250-250"))

#相关方法
num8 = -10
num9 = abs(num8)
print(num9)

#比较两个数的大小
num10 = 250
num11 = 251
print((num10>num11)-(num10 < num11))

#求最大/小数
print(max(1,2,3,4))
print(min(1,2,3,4))

#求x^y次放
print(pow(2,5))

#返回浮点数四舍五入后的值,如果后面跟n表示保留小数点的位数
print(round(3.3))
print(round(3.5))
print(round(3.515111, 2))

#向上取整
print(math.ceil(18.1))
print(math.ceil(18.5))

#向下取整
print(math.floor(18.1))
print(math.floor(18.5))

#返回整数部分和小数部分
print(math.modf(22.3))

#随机从以下数据中选择一个数据
print(random.choice([1,2,3,4,5]))
print(random.choice(range(5))) #range(5) = [1,2,3,4]
print(random.choice("youcw")) #"youcw" = ['y','o','u','c','w']

#产生1~100的一个随机数
r1 = random.choice(range(100)) + 1
print(r1)

#按照指定的基数step递增:start,stop,step
r2 = random.randrange(1, 10, 2) #1,3,5,7,9
print(r2)

r3 = random.randrange(1, 10, 3) #1, 4, 7
print(r3)

print(random.randrange(100))

#产生[0~1)的随机浮点数
print(random.random())

#随机排列数据
list = [1,2,3,4]
random.shuffle(list)
print(list)
