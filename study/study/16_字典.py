'''
字典使用:key:value进行数据存储,查找速度极快
注意:字典是无序的,也就是元素位置顺序不固定,用{}扩起来
key特点:
1.字典中的key必须是唯一的
2.key必须是不可变对象,字符串,整数等都是不可变的,可以作为key
3.列表list是可变,不能作为key

#和list比较
#1、查找和插入的速度极快，不会随着key-value的增加而变慢
#2、需要占用大量的内存，内存浪费多



#list
#1、查找和插入的速度随着数据量的增多而减慢
#2、占用空间小，浪费内存少
'''
#字典描述人的名字和年龄
dict1 = {"zhangsan":22, "lisi":23, "wanger":21}
print(dict1)

#元素访问:字典名[key名]
print(dict1["zhangsan"])
print(dict1["lisi"])
print(dict1["wanger"])
print(dict1.get("zhangsan"))
print(dict1.get("youcw"))
ret = dict1.get("youcw")
if ret == None:
    print("没有")
else:
    print("有")

#添加元素
dict1["youcw"] = 20
print(dict1)

#修改
dict1["youcw"] = 18
print(dict1)

#删除
dict1.pop("lisi")
print(dict1)

#遍历
for key in dict1:
    print(key, dict1[key])

print(dict1.values()) #列表
for value in dict1.values():
    print(value)

print(dict1.items())
for key, value in dict1.items():
    print(key, value)

#获取下标index,当然是无意义的,因为字典是无序的
for index, key in enumerate(dict1):
    print(index, key, dict1[key])



