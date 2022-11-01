#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 11:06
# * Filename : set_add_func.py
# * Description : 
# **********************************************************
#Python Set add()方法
#Python3 列表 Python 集合
#描述
#add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
#语法
#add()方法语法：
#set.add(elmnt)
#参数
#elmnt -- 必需，要添加的元素。
#返回值
#无。
#实例
#以下实例展示了 add() 方法的使用：
#实例 1
fruits = {"apple", "banana", "cherry"}
fruits.add("orange") 
print(fruits)
#输出结果为：
#{'apple', 'banana', 'orange', 'cherry'}
#已存在的元素，则不执行添加操作：
#实例 2
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)
#输出结果为：
#{'apple', 'banana', 'cherry'}
