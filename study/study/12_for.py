'''
for循环
for 变量名 in 集合:
    语句
'''
for i in [1,2,3,4]:
    print(i)

'''
range([start],end,[step]):列表生成器
'''
list = range(10)
print(list)

for i in range(10):
    print(i)

for j in range(2, 20, 2):
    print(j)

#同时列出下标和元素
for index, m in enumerate([1,2,3,4]):
    print(index, m)

#1+...+100
sum = 0
for n in range(1, 101):
    sum += n
print(sum)
