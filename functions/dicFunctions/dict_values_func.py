#======================================
# file name:dict_values_func.py
# author:liangliangSu
# date of writing:2022-09-12 22:46
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 values() 方法
#Python3 字典 Python3 字典
#描述
#Python3 字典 values() 方法返回一个视图对象。
#dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
#视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
#我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
#语法
#values()方法语法：
#dict.values()
#参数
#NA。
#返回值
#返回视图对象。
#实例
#以下实例展示了 values() 方法的使用方法：
#实例
dict1 = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dict1.keys()
values = dict1.values()
# 迭代
n = 0
for val in values:
    n += val
print(n)
#504
# keys 和 values 以相同顺序（插入顺序）进行迭代
print(list(keys))    # 使用 list() 转换为列表
#['eggs', 'sausage', 'bacon', 'spam']
print(list(values))
#[2, 1, 1, 500]
# 视图对象是动态的，受字典变化的影响，以下删除了字典的 key，视图对象转为列表后也跟着变化
del dict1['eggs']
del dict1['sausage']
print(list(values))
#[1, 500]
#相同两个 dict.values() 比较返回都是 False
d = {'a': 1}
d.values() == d.values()
#False
