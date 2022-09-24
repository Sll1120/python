# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-14 11:31
# * Filename : set_intersection_func.py
# * Description : 
# **********************************************************
#!/usr/bin/python3
#Python Set intersection() 方法
#Python3 列表 Python 集合
#描述
#intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。
#语法
#intersection() 方法语法：
#set.intersection(set1, set2 ... etc)
#参数
#set1 -- 必需，要查找相同元素的集合
#set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
#返回值
#返回一个新的集合。
#实例
#返回一个新集合，该集合的元素既包含在集合 x 又包含在集合 y 中：
#实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.intersection(y) 
print(z)
#输出结果为：
#{'apple'}
#计算多个集合的交集：
#实例 1
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)
#输出结果为：
#{'c'}
#Python3 列表 Python 集合
# Python3 字典Python3 编程第一步 
#intersection(set)，set 参数可以不是集合，可以是任何序列。
y2 = {1, 2, 3, 4, 'a', 5, 56}
#字典之外的序列：
y3 = y2.intersection([2]) # list
print(y3) 
{2}
y3 = y2.intersection((2,)) # tuple
print(y3)
#{2}
y3 = y2.intersection('a') # str
print(y3)
#{'a'}
#而对字典则是与字典的 key 值比较：
y3 = y2.intersection({'a': 2})
print(y3)
#{'a'}
y3 = y2.intersection({1: 2})
print(y3)
#{1}
