'''
set集合的本质就是无序和不重复元素的集合,类似dict,保存key的值,无需value
'''
#创建set需要一个list,tuple,dict作为输入集合
#重复的元素将被过滤
s1 = set([1,2,3,4])
print(s1)

s2 = set([1,2,2,3,3,4])
print(s2)

s3 = set((1,2,3,3,4))
print(s3)

s4 = set({"youcw":18, "zhangsan":20})
print(s4)

#添加元素
s5 = set([1,2,3,4])
s5.add(5)
print(s5)

s5.add("youcw")
print(s5)

s5.add((5,6))
print(s5)

#s5.add([5,6]) #注意:列表是可变的,set成员不能为列表
#s5.add({2:"zhangsan"})#注意:字典是可变的,set成员不能为字典

#插入整个list,tuple,字符串,注意是分拆插入
s6 = set([1,2,3,4])
s6.update([5,6,7])
s6.update((8,9,10))
s6.update("hello")
print(s6)

#删除
s6.remove(10)
s6.remove("h")
print(s6)

#遍历
for i in s6:
    print(i)

#print(s6[1]) #注意由于集合是无序的,没有索引

#利用enumrate来获取
for index, data in enumerate(s6):
    print(index, data)

#求交集和并集
s7 = set([1,2,3])
s8 = set([2,3,4])

ret = s7 & s8
print(ret)
print(type(ret))

ret = s7 | s8
print(ret)
print(type(ret))

#list去重复
l = [1,2,3,4,3,4,5,6]
s = set(l)
l = list(s)
print(l)

#list-->set
l1 = [1,2,3,4,5,3,4,5]
s1 = set(l1)
print(l1, s1)

#tuple-->set
t2 = (1,2,3,4,3,2)
s2 = set(t2)
print(t2,s2)

#set-->list
s3 = {1,2,3,4}
l3 = list(s3)
print(l3)

#set-->tuple
s4 = {2,3,4,5}
t4 = tuple(s4)
print(t4)


