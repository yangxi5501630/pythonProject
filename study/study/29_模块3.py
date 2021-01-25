'''
__name__属性:不运行模块的代码,只是运行自己的代码
格式:
if __name__ == "__main__"
    pass
'''
import add

if __name__ == "__main__":
    print(add.add(100,200))
    print(add.sub(100,200))

