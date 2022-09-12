#======================================
# file name:isdecimal_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:50
# description:
#======================================
#!/usr/bin/env python3
#Python3 isdecimal()方法
#Python3 字符串 Python3 字符串
#描述
#isdecimal() 方法检查字符串是否只包含十进制字符。
#语法
#isdecimal() 方法语法：
#str.isdecimal()
#参数
#无
#返回值
#True - 如果字符串中的所有字符都是十进制字符。
#False - 至少一个字符不是十进制字符。
#实例
#以下实例展示了 isdecimal() 函数的使用方法：
#实例
#!/usr/bin/python3
str = "runoob2016"
print (str.isdecimal())
str = "23443434"
print (str.isdecimal())
#以上实例输出结果如下：
#False
#True
