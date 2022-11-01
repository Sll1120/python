#======================================
# file name:dict_setdefault_func.py
# author:liangliangSu
# date of writing:2022-09-12 23:23
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 setdefault() 方法
#描述
#Python 字典 setdefault() 方法和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
#语法
#setdefault()方法语法：
#dict.setdefault(key, default=None)
#参数
#key -- 查找的键值。
#default -- 键不存在时，设置的默认键值。
#返回值
#如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
#实例
#以下实例展示了 setdefault() 方法的使用方法：
#实例
#!/usr/bin/python3
tinydict = {'Name': 'Runoob', 'Age': 7}
print ("Age 键的值为 : %s" %  tinydict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  tinydict.setdefault('Sex', None))
print ("新字典为：", tinydict)
#以上实例输出结果为：
#Age 键的值为 : 7
#Sex 键的值为 : None
#新字典为： {'Age': 7, 'Name': 'Runoob', 'Sex': None}
#Python3 字典 Python3 字典
# Python3 元组Python3 集合 
#1 篇笔记 写笔记
#关于字典中 get() 和 setdefault() 的区别：
#主要在于当查找的键值 key 不存在的时候，setdefault()函数会返回默认值并更新字典，添加键值；而 get() 函数只返回默认值，并不改变原字典。
#get() 例子：
#>>> d={}
#>>> d.get('name','N/A')
#'N/A'
#>>> d
#{}
#>>> print d.get('name')
#None
#>>> d
#{}
#setdefault() 例子：
#>>> d={}  # 设定
#>>> d.setdefault('name','N/A')
#'N/A'
#>>> d
#{'name':'N/A'} 
#>>> d.setdefault('name','Jack')
#'N/A'
#>>> d={}  # 不设定
#>>> d.setdefault('name')
#>>> d
#{'name':'None'}
