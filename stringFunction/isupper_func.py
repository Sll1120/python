#======================================
# file name:isupper_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:31
# description:
#======================================
#!/usr/bin/env python3
#Python3 isupper()方法
#Python3 字符串 Python3 字符串
#描述
#isupper() 方法检测字符串中所有的字母是否都为大写。
#语法
#isupper()方法语法：
#str.isupper()
#参数
#无。
#返回值
#如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
#实例
#以下实例展示了isupper()方法的实例：
#实例
#!/usr/bin/python3
str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.isupper())
str = "THIS is string example....wow!!!"
print (str.isupper())
#以上实例输出结果如下：
#True
#False
