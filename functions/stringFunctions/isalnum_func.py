#======================================
# file name:isalnum_func.py
# author:liangliangSu
# date of writing:2022-09-12 09:04
# description:
#======================================
#!/usr/bin/env python3
#Python3 isalnum()方法
#Python3 字符串 Python3 字符串
#描述
#isalnum() 方法检测字符串是否由字母和数字组成。
#语法
#isalnum()方法语法：
#str.isalnum()
#参数
#    无。
#返回值
#如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
#实例
#以下实例展示了isalnum()方法的实例：
#实例(Python 2.0+)
#!/usr/bin/python3
str = "runoob2016"  # 字符串没有空格
print (str.isalnum())
str = "www.runoob.com"
print (str.isalnum())
str = "wwwrunoobcom"
print (str.isalnum())
string = "w3"
print (string.isalnum())
string = "12"
print (string.isalnum())
#以上实例输出结果如下：
#True
#False
#True
#True
#True
