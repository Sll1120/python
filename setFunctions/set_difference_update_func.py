#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 11:25
# * Filename : set_difference_update_func.py
# * Description : 
## **********************************************************
#Python Set difference_update() 方法
#Python3 列表 Python 集合
#描述
#difference_update() 方法用于移除两个集合中都存在的元素。
#difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
#语法
#difference_update() 方法语法：
#set.difference_update(set)
#参数
#set -- 必需，用于计算差集的集合
#返回值
#无。
#实例
#移除两个集合都包含的元素：
#实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) 
print(x)
#输出结果为：
#{'cherry', 'banana'}
