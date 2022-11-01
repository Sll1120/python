#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 14:34
# * Filename : set_symmetric_diff_update_func.py
# **********************************************************
#Python Set symmetric_difference_update() 方法
#Python3 列表 Python 集合
#描述
#symmetric_difference_update() 方法移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
#语法
#symmetric_difference_update() 方法语法：
#set.symmetric_difference_update(set)
#参数
#set -- 要检测的集合
#返回值
#无。
#实例
#在原始集合 x 中移除与 y 集合中的重复元素，并将不重复的元素插入到集合 x 中：
#实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.symmetric_difference(y) 
print(x)
#输出结果为：
#{'cherry', 'apple', 'banana'}
x.symmetric_difference_update(y) 
print(x)
#输出结果为：
#{'google', 'cherry', 'banana', 'runoob'}
