dic={'张三':100,'李四':99,'王五':98}
keys=dic.keys()
print(keys) #获取所有的key
print(type(keys))
print(list(keys)) #将所有的key组成视图转成列表
values=dic.values()
print(values) #获取所有的values
print(type(values))
print(list(values))
print('------获取所有的keys-values对------')
items=dic.items()
print(items)
print(type(items))
print(list(items))
