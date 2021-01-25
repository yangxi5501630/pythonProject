'''
列表本质就是一个有序的结果,可以替代定义多个变量存储数据的代码罗嗦问题
格式:列表名=[成员1,...成员N]
注意:成员可以是不同数据类型的
注意:列表成员是可以修改的
'''
#创建空列表
list1 = []
print(list1)

#列表元素的访问
list2 = [1,2,3,4,5]
print(list2[2])

#修改成员
list2[2] = 300
print(list2)

#带有元素的列表
list3 = [1,2,3,4,5]
sum = 0
index = 0
while index < 5:
    sum += list3[index]
    index += 1
    if index == 5:
        print("平均数:%d" %(sum/5))

#不同数据类型
list4 = [1, 2, "hello", True]
print(list4)

#列表组合
list5 = [1,2,3]
list6 = [4,5,6]
print(list5+list6)

#列表重复
print(list5*3)

#判断
print(3 in list5)
print(3 in list6)

#列表截取
list7 = [1,2,3,4,5,6,7,8,9]
print(list7[:3])
print(list7[2:4])
print(list7[4:])

#二维列表
list8 = [[1,2,3],[4,5,6]]
print(list8[1][1])

#列表相关函数
#append:列表末尾追加成员
list9 = [1,2,3]
list9.append(4)
print(list9)

list9.append([5,6])
print(list9)

#extend:一次性追加列表的多个元素值
list10 = [1,2,3]
list10.extend([5,6,7])
print(list10)

#insert:在下标处添加一个元素，不覆盖原数据，原数据向后顺延
list11 = [1,2,3]
list11.insert(1, 250)
list11.insert(1, [251, 252])
print(list11)

#pop:移除列表中指定下标的元素(默认移除最后一个元素)并返回删除的元素
list12 = [1,2,3,4,5,6,7]
list12.pop()
print(list12)

dmem = list12.pop(2)
print(dmem, list12)

#remove  移除列表中的某个元素第一个匹配的结果
list13 = [1,2,3,4,3,4,5]
list13.remove(4)
print(list13)

#清除列表中所有的数据
list13.clear()
print(list13)

#从列表中找出某个值第一个匹配的索引值
list14 = [1,2,3,4,4,5]
indexlist = list14.index(3)
print(indexlist)

indexlist = list14.index(4,4,6)
print(indexlist)

#列表元素个数
print(len(list14))

#获取列表中的最大值
print(max(list14))

#获取列表中的最小值
print(min(list14))

#获取某个元素出现的个数
list15 = [1,2,3,4,4,4,5,3]
print(list15.count(4))

num = 0
cnt = list15.count(4)
while num < cnt:
    list15.remove(4)
    num += 1
print(list15)

#倒需
list15.reverse()
print(list15)

#升顺序
list15.sort()
print(list15)

#浅拷贝,引用拷贝
list16 = [1,2,3,4,5]
list17 = list16
list17[2] = 300
print(list16)
print(list17)
print(id(list16))
print(id(list17))

#深拷贝,内存的拷贝
list18 = [1,2,3,4]
list19 = list18.copy()
list19[2] = 300
print(list18)
print(list19)
print(id(list18))
print(id(list19))

#将元组转成列表
list20 = list((1,2,3,4))
print(list20)

