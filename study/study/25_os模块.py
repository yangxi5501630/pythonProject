import os

#os模块方法
print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get("PATH"))
print(os.curdir)
print(os.getcwd())
print(os.listdir(r"/home/youcw"))
os.mkdir(r"/home/youcw/test1111")
os.rmdir(r"/home/youcw/test1111")
print(os.stat(r"/home/youcw"))
#os.rename(r"/home/youcw/test", r"/home/youcw/test1")
#os.remove(r"/home/youcw/test1/helloworld.txt")
print(os.system("ls /home/youcw"))
#print(os.system("gedit"))

#os.path模块方法
print(os.path.abspath("./25_os模块.py")) #查看绝对路径

p1 = r"/home/youcw/"
p2 = r"test22"
print(os.path.join(p1, p2)) #拼接

p3 = r"/home/youcw/test1/helloworld.txt"
print(os.path.split(p3)) #拆分目录和文件
print(os.path.splitext(p3)) #拆分扩展名
print(os.path.isdir(p3)) #判断是否是目录
print(os.path.isfile(p3)) #判断文件是否存在
print(os.path.exists(r"/home/youcw")) #判断目录是否存在
print(os.path.getsize(p3)) #获取文件大小
print(os.path.dirname(p3)) #获取文件所在目录
print(os.path.basename(p3)) #获取文件


