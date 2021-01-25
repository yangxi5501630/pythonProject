#模拟栈结构
stack = []

#压栈(向栈里存数据)
stack.append("A")
print(stack)
stack.append("B")
print(stack)
stack.append("C")
print(stack)



#出栈(在栈里取数据)
res1 = stack.pop()
print("res1 =", res1)
print(stack)
res2 = stack.pop()
print("res2 =", res2)
print(stack)
res3 = stack.pop()
print("res3 =", res3)
print(stack)


#队列实现
import collections

#创建一个队列
queue = collections.deque()
print(queue)

#进队(存数据)
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)


#出队(取数据)
res1 = queue.popleft()
print("res1 =", res1)
print(queue)
res2 = queue.popleft()
print("res2 =", res2)
print(queue)
res3 = queue.popleft()
print("res3 =", res3)
print(queue)
