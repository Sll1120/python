#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 14:40
# * Filename : set_union_func.py
# **********************************************************
#Python Set union() 方法
#描述
#union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
#语法
#union() 方法语法：
#set.union(set1, set2...)
#参数
#set1 -- 必需，合并的目标集合
#set2 -- 可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开。
#返回值
#返回一个新集合。
#实例
#合并两个集合，重复元素只会出现一次：
#实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.union(y) 
print(z)
#输出结果为：
#{'cherry', 'runoob', 'google', 'banana', 'apple'}
#合并多个集合：
#实例 1
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z) 
print(result)
#输出结果为：
#{'c', 'd', 'f', 'e', 'b', 'a'}
