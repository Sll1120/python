#======================================
# file name:isspace_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:25
# description:
#======================================
#!/usr/bin/env python3
#Python3 isspace()方法
#Python3 字符串 Python3 字符串
#描述
#Python isspace() 方法检测字符串是否只由空白字符组成。
#语法
#isspace() 方法语法：
#str.isspace()
#参数
#无。
#返回值
#如果字符串中只包含空格，则返回 True，否则返回 False.
#实例
#以下实例展示了isspace()方法的实例：
#实例
#!/usr/bin/python3
str = "       " 
print (str.isspace())
str = "Runoob example....wow!!!"
print (str.isspace())
#以上实例输出结果如下：
#True
#False
#空白符包含：空格、制表符(\t)、换行(\n)、回车(\r）等。
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# \t\r\n 都是空白符
print (' \t\r\n'.isspace()) # True
print ('\0'.isspace()) # False
print (' a '.isspace()) # False
