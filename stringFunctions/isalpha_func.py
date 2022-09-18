#======================================
# file name:isalpha.py
# author:liangliangSu
# date of writing:2022-09-12 09:55
# description:
#======================================
#!/usr/bin/env python3
#Python3 isalpha()方法
#Python3 字符串 Python3 字符串
#描述
#Python isalpha() 方法检测字符串是否只由字母或文字组成。
#语法
#isalpha()方法语法：
#str.isalpha()
#参数
#无。
#返回值
#如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。
#实例
#以下实例展示了isalpha()方法的实例：
#实例
#!/usr/bin/python3
str = "runoob"
print (str.isalpha())
# 字母和中文文字
str = "runoob菜鸟教程"
print (str.isalpha())
str = "Runoob example....wow!!!"
print (str.isalpha())
#以上实例输出结果如下：
#True
#True
#False
