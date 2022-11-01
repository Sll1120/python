#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 14:20
# * Filename : set_remove_func.py
# **********************************************************
#Python Set remove() 方法
#Python3 列表 Python 集合
#描述
#remove() 方法用于移除集合中的指定元素。
#该方法不同于 discard() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
#语法
#remove() 方法语法：
#set.remove(item)
#参数
#item -- 要移除的元素
#返回值
#没有返回值。
#实例
#移除元素 banana：
#实例 1
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)
#输出结果为：
#{'cherry', 'apple'}
