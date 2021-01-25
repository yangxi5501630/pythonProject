'''
模块类似C程序的多文件之间的函数变量访问
特点:
1、提高代码的可维护性
2、提高了代码的复用度，当一个模块完毕，可以被多个地方引用
3、避免函数名和变量名的冲突

引入模块:
import语句
格式 ：  import module1[, module2[, module3[……,moudeln]]]
#使用模块中的内容
#格式：模块名.函数名/变量名
#引入了自定义模块，不用加.py后缀
#注意：一个模块只会被引入一次，不管你执行了多少次import。防止模块被多次引入
'''
#引用标准模块
import time
c = time.time()
print(c)
b = time.localtime(c)
print(b)
s = time.asctime(b)
print(s)

#引用自定义模块
import add
print(add.add(100,200))
print(add.sub(100,200))
Data = 251
print(add.Data)

