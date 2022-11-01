print('----可变序列，列表，字典----')
lst=[10,100,20,34] #列表是方括号[]
print(id(lst))
lst.append(300) #向末尾添加一个元素
lst1=[90,70]
lst.extend(lst1) #向末尾添加多个元素
print(id(lst)) #可发现列表的ID是不便的，即内存地址不变

print('----不可变序列，字符串，元组----')
s='hello'
print(id(s))
s=s+'  \bworld' #加入退格转义功能
print(id(s))
print(s)


