#from……import语句
#作用：从模块中导入一个指定的部分到当前命名空间
#格式：from module import name1[, name2[, ……namen]]

from add import add,sub
#from add import * #不建议这么用

'''
程序内容的函数可以将模块中的同名函数覆盖
def add(num1, num2):
    print("*********")
    return
'''
print(add(100,200))
print(sub(100,200))