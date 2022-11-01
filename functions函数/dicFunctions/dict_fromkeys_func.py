#======================================
# file name:dict_fromkeys_func.py
# author:liangliangSu
# date of writing:2022-09-12 20:36
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 fromkeys() 方法
#Python3 字典 Python3 字典
#描述
#Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
#语法
#fromkeys() 方法语法：
#dict.fromkeys(seq[, value])
#参数
#seq -- 字典键值列表。
#value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
#返回值
#该方法返回一个新字典。
#实例
#以下实例展示了 fromkeys()函数的使用方法：
#实例
#!/usr/bin/python3
seq = ('name', 'age', 'sex')
tinydict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(tinydict))
tinydict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(tinydict))
#以上实例输出结果为：
#新的字典为 : {'age': None, 'name': None, 'sex': None}
#新的字典为 : {'age': 10, 'name': 10, 'sex': 10}
#不指定值：
#实例
#!/usr/bin/python3
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)
#以上实例输出结果为：
#{'key1': None, 'key2': None, 'key3': None}
