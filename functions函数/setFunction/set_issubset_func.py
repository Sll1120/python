#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 13:53
# * Filename : set_issubset_func.py
# **********************************************************
#Python Set issubset() 方法
#Python3 列表 Python 集合
#描述
#issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
#语法
#issubset() 方法语法：
#set.issubset(set)
#参数
#set -- 必需，要比查找的集合
#返回值
#返回布尔值，如果都包含返回 True，否则返回 False。
#实例
#判断集合 x 的所有元素是否都包含在集合 y 中：
#实例 1
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 
print(z)
#输出结果为：
#True
#如果没有全部包含返回 False：
#实例 1
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y) 
print(z)
#输出结果为：
#False
