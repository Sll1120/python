#======================================
# file name:islower_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:04
# description:
#======================================
#!/usr/bin/env python3
#Python3 islower()方法
#描述
#islower() 方法检测字符串是否由小写字母组成。
#语法
#islower()方法语法：
#str.islower()
#参数
#无。
#返回值
#如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
#实例
#以下实例展示了islower()方法的实例：
#实例
#!/usr/bin/python3
str = "RUNOOB example....wow!!!"
print (str.islower())
str = "runoob example....wow!!!"
print (str.islower())
#以上实例输出结果如下：
#False
#True
#Python3 字符串 Python3 字符串
# Python3 数字(Number)Python3 列表 
#1 篇笔记 写笔记
#   vipkwd
#  ser***e@vipkwd.com
#9
#str.islower() 检测字符串是否不包含大写字母。
#>>> import sys; sys.version
#'3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]'
#>>> 'aaab32'.islower()
#True
#>>> 'aaab32你好'.islower()
#True
#>>> 'aaab'.islower()
#True
#>>> 'aaab32~'.islower()
#True
#>>> 'aaab32~+'.islower()
#True
#>>> 'aaab32~?'.islower()
#True
#>>> 'aaab32...'.islower()
#True
#>>> 'a\nb'.islower()
#True
#>>> r'\b'.islower()
#True
#>>> 'aaB'.islower()
#False
#>>> '\b'.islower()
#False
