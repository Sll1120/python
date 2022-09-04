s={10,20,30,40}
print('----元素集合存在判断----')
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
print('-----元素集合新增操作------')
s.add(50) #一次添加一个元素
print(s)
s.update({60,70}) #一次至少添加一个元素
print(s)
s.update([80,90,100])
s.update((110,120,))
print(s)
# 集合元素的删除操作
s.remove(100) #一次删除一个元素
# s.remove(1000) #KeyError: 1000 删除不存在的元素会报错
s.discard(70)
print(s)
s.discard(1000) #一次删除一个，删除不存在的不会报错
s.pop()  #一次只删除一个
s.pop() #一次只删除一个
print('清空之前的元素集合')
print(s)
s.clear()
print('清空之后的集合:',s)
