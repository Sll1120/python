#======================================
# file name:isnumeric_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:09
# description:
#======================================
#!/usr/bin/env python3
#Python3 isnumeric()方法
#Python3 字符串 
#描述
#isnumeric() 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。
#指数类似 ² 与分数类似 ½ 也属于数字。
s = '½'
s = '\u00BD'
#语法
#isnumeric()方法语法：
#str.isnumeric()
#参数
#无。
#返回值
#如果字符串中只包含数字字符，则返回 True，否则返回 False
#实例
#以下实例展示了 isnumeric() 方法的实例：
#实例
#!/usr/bin/python3
str = "runoob2016"  
print (str.isnumeric())
str = "23443434"
print (str.isnumeric())
print('-------------------------------------')
#以上实例输出结果如下：
#False
#True
#Unicode 数字：
#实例
#!/usr/bin/python3
#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())
# s = '½'
s = '\u00BD'
print(s.isnumeric())
a = "\u0030" #unicode for 0
print(a.isnumeric())
b = "\u00B2" #unicode for ²
print(b.isnumeric())
c = "10km2"
print(c.isnumeric())
#以上实例输出结果如下：
#True
#True
#True
#True
#False
##############################################
# isdigit、isdecimal 和 isnumeric 区别
#isdigit()
#True: Unicode数字，byte数字（单字节），全角数字（双字节）
#False: 汉字数字，罗马数字，小数
#Error: 无
#isdecimal()
#True: Unicode数字，，全角数字（双字节）
#False: 罗马数字，汉字数字，小数
#Error: byte数字（单字节）
#isnumeric()
#True: Unicode 数字，全角数字（双字节），汉字数字
#False: 小数，罗马数字
#Error: byte数字（单字节）

num = "1"  #unicode
print(num.isdigit())   # True
print(num.isdecimal()) # True
print(num.isnumeric()) # True
num = "1" # 全角
print(num.isdigit())   # True
print(num.isdecimal()) # True
print(num.isnumeric()) # True
num = b"1" # byte
print(num.isdigit())   # True
#print(num.isdecimal()) # AttributeError 'bytes' object has no attribute 'isdecimal'
#print(num.isnumeric()) # AttributeError 'bytes' object has no attribute 'isnumeric'
num = "IV" # 罗马数字
print(num.isdigit())   # False
print(num.isdecimal()) # False
print(num.isnumeric()) # False
num = "四" # 汉字
print(num.isdigit())   # False
print(num.isdecimal()) # False
print(num.isnumeric()) # True
