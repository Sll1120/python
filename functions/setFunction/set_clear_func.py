#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 11:18
# * Filename : set_clear_func.py
# * Description : 
## **********************************************************
#Python Set clear()方法
#Python3 列表 Python 集合
#描述
#clear() 方法用于移除集合中的所有元素。
#语法
#clear()方法语法：
#set.clear()
#参数
#无。
#返回值
#无。
#实例
#移除 fruits 集合中的所有元素：
#实例 1
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
#输出结果为：
#set()
#Python3 列表 Python 集合
# Python3 字典Python3 编程第一步 
#1 篇笔记 写笔记
#   上帝也编程
#  717***589@qq.com
#6
#clear() 从内存删除集合与清空集合，但内存地址不删除。
#del() 会从内存中删除。
fruits = {"apple", "banana", "cherry"}
del(fruits) #从内存中删除fruits
fruits = {"apple", "banana", "cherry"}
fruits.clear() #从清空集合fruits的内容，内存地址不删除
