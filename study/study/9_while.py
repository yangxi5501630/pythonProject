'''
while 表达式:
    执行语句
else:
    执行语句
'''
num = 1
while num <= 5:
    print(num)
    num+=1

#计算0+....+100
sum = 0
num = 0
while num <= 100:
    sum += num
    num += 1
print(sum)

#打印字符串字符
str = "hello world tarena"
index = 0
while index < len(str):
    print("str[%d] = %s" % (index, str[index]))
    index += 1
else:
    print("over")