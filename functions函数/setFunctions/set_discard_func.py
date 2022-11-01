#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 11:27
# * Filename : set_discard_func.py
# * Description : 
## **********************************************************
#Python Set discard() 方法
#Python3 列表 Python 集合
#描述
#discard() 方法用于移除指定的集合元素。
#该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
#语法
#discard() 方法语法：
#set.discard(value)
#参数
#value -- 必需，要移除的元素
#返回值
#无。
#实例
#移除集合中的元素 banana：
#实例 1
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") 
print(fruits)
#输出结果为：
#{'cherry', 'apple'}
#Python3 列表 Python 集合
# Python3 字典Python3 编程第一步 
#在集合删除完一个元素，返回新的集合后。再次用 set.discard(value) 删除刚刚已经删除掉的元素，程序不会报错：
a={'123','456','789'}
a.discard('123')
print(a)
#{'456', '789'}
print(a)
#{'456', '789'}
a.discard('123')
print(a)
#{'456', '789'}
