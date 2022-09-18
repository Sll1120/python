#======================================
# file name:dict_copy_func.py
# author:liangliangSu
# date of writing:2022-09-12 23:03
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 copy()方法
#Python3 字典 Python3 字典
#描述
#Python 字典 copy() 函数返回一个字典的浅复制。
#语法
#copy()方法语法：
#dict.copy()
#参数
#NA。
#返回值
#返回一个字典的浅复制。
#实例
#以下实例展示了 copy()函数的使用方法：
#实例
#!/usr/bin/python3
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)
#以上实例输出结果为：
#新复制的字典为 :  {'Age': 7, 'Name': 'Runoob', 'Class': 'First'}
#直接赋值和 copy 的区别
#可以通过以下实例说明：
#实例
#!/usr/bin/python
# -*- coding: UTF-8 -*-
dict1 =  {'user':'runoob','num':[1,2,3]}
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
# 输出结果
print(dict1)
print(dict2)
print(dict3)
#实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。
#{'user': 'root', 'num': [2, 3]}
#{'user': 'root', 'num': [2, 3]}
#{'user': 'runoob', 'num': [2, 3]}
