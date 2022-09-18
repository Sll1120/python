#======================================
# file name:center_func.py
# author:liangliangSu
# date of writing:2022-09-11 23:26
# description:
#======================================
#!/usr/bin/env python3
#Python3 center()方法
#Python3 字符串 
#center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
#语法
#center()方法语法：
#str.center(width[, fillchar])
#参数
#width -- 字符串的总宽度。
#fillchar -- 填充字符。
#返回值
#返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
#实例
#以下实例展示了center()方法的实例：
#实例
#!/usr/bin/python3
str = "[runoob]"
print ("str.center(20) : ", str.center(20)) #fillchar 默认是空格
print ("str.center(20, '*') : ", str.center(20, '*')) #如果 width 小于字符串宽度直接返回字符串，不会截断:
print ("str.center(4, '*') : ", str.center(4, '*'))
print ("str.center(20, 'x') : ", str.center(20, 'x'))
#以上实例输出结果如下：
#str.center(40, '*') :  ****************[runoob]****************
#fillchar 只能是单个字符
#>>> str = "[www.runoob.com]"
#>>> print ("str.center(40, '?!') : ", str.center(40, '?!'))
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: The fill character must be exactly one character long

#补充说明一下：
print('123'.center(2, '*'))
# 123
print('123'.center(3, '*'))
# 123
print('123'.center(4, '*'))     # 奇数个字符时优先向右边补*
# 123*
print('123'.center(5, '*'))
# *123*
print('1234'.center(4, '*'))
# 1234
print('1234'.center(5, '*'))    # 偶数个字符时优先向左边补*
# *1234
print('1234'.center(6, '*'))
# *1234*
print('1234'.center(7, '*'))
# **1234*
