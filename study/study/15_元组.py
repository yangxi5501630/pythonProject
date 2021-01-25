'''
tuple下元组本质就是一个有序集合
格式：元组名 = (元组元素1, 元组元素2, ……, 元组元素n)
特点:
1.与列表类似
2.用()
3.一旦初始化就不能修改,这个和字符串一样
'''

#创建空元组
tuple1 = ()
print(tuple1)

#创建带元素的元组
tuple2 = (1,2,"tarena", True)
print(tuple2)

#定义只有一个元素的元组,记得后面带分割符,
tuple3 = (1,)
print(tuple3)
print(type(tuple3))

#访问元组成员
tuple4 = (1,2,3,4)
index = 0
for member in tuple4:
    print("tuple[%d] = %d" %(index, tuple4[index]))
    index += 1

tuple4 = (1,2,3,4)
index = -4
for member in tuple4:
    print("tuple[%d] = %d" %(index, tuple4[index]))
    index += 1

#修改元组的成员
tuple5 = (1,2,3,4,[5,6,7])
#tuple5[2] = 250 #不可修改
tuple5[4][1] = 250 #修改成员列表,没毛病
print(tuple5)

#删除元组
del tuple5
#print(tuple5)

#元组合体
tuple6 = (1,2,3)
tuple7 = (4,5,6)
print(tuple6 + tuple7)

#元组的重复
print(tuple6 * 3)

#判断
print(2 in tuple6)
print(2 in tuple7)

#元组截取
tuple8 = (1,2,3,4,5,6,7,8)
print(tuple8[:3])
print(tuple8[3:])
print(tuple8[3:6])

#二维元组
tuple9 = ((1,2,3),(4,5,6))
print(tuple9[1][1])

#元组的方法

#len()   返回元组中元素的个数
tuple10 = (1,2,3,4,5)
print(len(tuple10))

#max()   返回元组中的最大值
#min()
print(max((5,6,7,8,9)))
print(min((5,6,7,8,9)))

#列表转元组
list = [1,2,3,4]
tuple11 = tuple(list)
print(tuple11)
