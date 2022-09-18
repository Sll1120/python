#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 13:56
# * Filename : set_issuperset_func.py
# **********************************************************
#Python Set issuperset() 方法
#Python3 列表 Python 集合
#描述
#issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
#语法
#issuperset() 方法语法：
#set.issuperset(set)
#参数
#set -- 必需，要比查找的集合
#返回值
#返回布尔值，如果都包含返回 True，否则返回 False。
#实例
#判断集合 y 的所有元素是否都包含在集合 x 中：
#实例 1
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z)
#输出结果为：
#True
#如果没有全部包含返回 False：
#实例 1
x = {"f", "e", "d", "c", "b"}
z = x.issuperset(y) 
print(z)
#输出结果为：
#False
