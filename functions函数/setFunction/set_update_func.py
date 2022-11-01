#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 14:44
# * Filename : set_update_func.py
# **********************************************************
#Python Set update() 方法
#Python3 列表 Python 集合
#描述
#update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
#语法
#update() 方法语法：
#set.update(set)
#参数
#set -- 必需，可以是元素或集合
#返回值
#无。
#实例
#合并两个集合，重复元素只会出现一次：
#实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.update(y) 
print(x)
#输出结果为：
#{'banana', 'apple', 'google', 'runoob', 'cherry'}
