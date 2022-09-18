#======================================
# file name:dict_in_func.py
# author:liangliangSu
# date of writing:2022-09-12 23:00
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 in 操作符
#Python3 字典 Python3 字典
#描述
#Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
#而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
#语法
#in 操作符语法：
#key in dict
#参数
#key -- 要在字典中查找的键。
#返回值
#如果键在字典里返回true，否则返回false。
#实例
#以下实例展示了 in 操作符在字典中的使用方法：
#实例(Python 3.0+)
#!/usr/bin/python3
dict1 = {'Name': 'Runoob', 'Age': 7}
# 检测键 Age 是否存在
if  'Age' in dict1:
    print("键 Age 存在")
else :
    print("键 Age 不存在")
# 检测键 Sex 是否存在
if  'Sex' in dict1:
    print("键 Sex 存在")
else :
    print("键 Sex 不存在")
# not in
# 检测键 Age 是否存在
if  'Age' not in dict1:
    print("键 Age 不存在")
else :
    print("键 Age 存在")
#以上实例输出结果为：
#键 Age 存在
#键 Sex 不存在
#键 Age 存在
