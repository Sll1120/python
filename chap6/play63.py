dic={'张三':100,'李四':99,'王五':98}
print('------第一种获取方法[]---------')
print(dic['张三'])
# print(dic['陈六']) #KeyError: '陈六'
# 获取的第二种方法dic.get()
print(dic.get('张三'))
print(dic.get('陈六')) #None
print(dic.get('陈六',97)) #97在查找对应的'陈六' value时不存在时,打印输出默认值。
