#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 14:28
# * Filename : set_symmetric_diff_func.py
# **********************************************************
#Python Set symmetric_difference() 方法
#Python3 列表 Python 集合
#描述
#symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
#语法
#symmetric_difference() 方法语法：
#set.symmetric_difference(set)
#参数
#set -- 集合
#返回值
#返回一个新的集合。
#实例
#返回两个集合组成的新集合，但会移除两个集合的重复元素：
#实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.symmetric_difference(y)
print(z)
z = y.symmetric_difference(x)
print(z)
#输出结果为：
#{'google', 'cherry', 'banana', 'runoob'}
#Python3 列表 Python 集合
# Python3 字典Python3 编程第一步
#这个用 ^ 比较好记，这个是好像是叫对称差集：
x={1,2,3,4,5}
y={2,5,6,7,9}
print(x^y)
#{1, 3, 4, 6, 7, 9}
print(x.symmetric_difference(y))
#{1, 3, 4, 6, 7, 9}
