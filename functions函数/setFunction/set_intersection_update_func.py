#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 12:41
# * Filename : set_intersection_update_func.py
# * Description : 
# **********************************************************
#Python Set intersection_update() 方法
#Python3 列表 Python 集合
#描述
#intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。
#intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
#语法
#intersection_update() 方法语法：
#set.intersection_update(set1, set2 ... etc)
#参数
#set1 -- 必需，要查找相同元素的集合
#set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
#返回值
#无。
#实例
#移除 x 集合中不存在于 y 集合中的元素：
#实例 1
x = {"apple", "banana", "cherry"}  # y 集合不包含 banana 和 cherry，被移除 
y = {"google", "runoob", "apple"}
x.intersection_update(y) 
print(x)
#输出结果为：
#{'apple'}
#计算多个集合的并集：
#实例 1
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)
#输出结果为：
#{'c'}
