import pickle

#写入列表
list = [1,2,3,4,'youcw', '你是神']
path = r"/home/youcw/PycharmProjects/study/helloworld3.txt"
fp = open(path, 'wb') #必须采用二进制形式
pickle.dump(list, fp)
fp.close()

#读取列表数据
fp = open(path, "rb")
list = pickle.load(fp)
print(list)
fp.close()
