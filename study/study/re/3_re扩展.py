import re

#字符串切割
str = "abc123efg456xyz"
print(str.split("123")) #不支持正则

str1 = "abc123efg456xyz"
print(re.split("\d+",str1)) #可以随意切割

str2 = "hello   world   zhangsan"
print(re.split('\s+', str2))
print(re.split('\s+', str2, 1))

'''
re.finditer函数
原型：finditer(pattern, string, flags=0)
参数：
patter: 匹配的正则表达式
string: 要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
'''
str3 = "hello 1234 world! hello 55555 world!"
d = re.finditer(r"(hello)", str3)
while True:
    try:
        l = next(d)
        print(d)
        print(l.span())
    except StopIteration as e:
        break

'''

字符串的替换和修改
sub(pattern, repl, string, count=0)
subn(pattern, repl, string, count=0)
pattern:  正则表达式(规则)
repl:     指定的用来替换的字符串
string:   目标字符串
count:    最多替换次数
功能：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。可以指定替换的次数,如果不指定，替换所有的匹配字符串

区别：前者返回一个被替换的字符串，后者返回一个元组，第一个元素被替换的字符串，第二个元素表示被替换的次数
'''
str5 = "hello world world world tarena"
print(re.sub(r"hello", "china", str5))
print(type(re.sub(r"(world)", "china", str5)))

print(re.subn(r"(world)", "张三", str5))
print(type(re.subn(r"(good)", "张三", str5)))

'''
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
pattern:要编译的正则表达式

'''
pat = r"^1([3578])\d{9}$"
print(re.match(pat, "13612345678"))
#编译成正则对象
re_telephon = re.compile(pat)
print(re_telephon.match("13612345678"))


'''
group
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
用()表示的就是要提取的分组（Group）。
比如：^(\d{3})-(\d{3,8})$分别定义了两个组，
可以直接从匹配的字符串中提取出区号和本地号码
'''
str6 = "010-66677788"
m = re.match(r'^(\d{3})-(\d{3,8})$', str6)
print(m.group(0)) #永远是源字符串
print(m.group(1)) #第一个字符串
print(m.group(2)) #第二个字符串
print(m.groups()) #打印所有字符元组