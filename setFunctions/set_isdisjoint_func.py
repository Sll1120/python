#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 13:49
# * Filename : set_isdisjoint_func.py
# **********************************************************
#Python Set isdisjoint() 方法
#Python3 列表 Python 集合
#描述
#isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。。
#语法
#isdisjoint() 方法语法：
#set.isdisjoint(set)
#参数
#set -- 必需，要比较的集合
#返回值
#返回布尔值，如果不包含返回 True，否则返回 False。
#实例
#判断集合 y 中是否有包含 集合 x 的元素：
#实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "facebook"}
z = x.isdisjoint(y) 
print(z)
#输出结果为：
#True
#如果包含返回 False：
#实例 1
y = {"google", "runoob", "apple"}
z = x.isdisjoint(y) 
print(z)
#输出结果为：
#False
