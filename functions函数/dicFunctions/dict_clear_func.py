#!/usr/bin/env python3
#======================================
# file name:dict_clear_func.py
# author:liangliangSu
# date of writing:2022-09-12 20:34
# description:
#======================================
#Python3 字典 clear()方法
#描述
#Python 字典 clear() 函数用于删除字典内所有元素。
#语法
#clear()方法语法：
#dict.clear()
#参数
#NA。
#返回值
#该函数没有任何返回值。
#实例
#以下实例展示了 clear()函数的使用方法：
#实例
#!/usr/bin/python3
tinydict = {'Name': 'Zara', 'Age': 7}
print ("字典长度 : %d" %  len(tinydict))
tinydict.clear()
print ("字典删除后长度 : %d" %  len(tinydict))
#以上实例输出结果为：
#字典长度 : 2
#字典删除后长度 : 0
