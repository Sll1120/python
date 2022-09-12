#======================================
# file name:max_func.py
# author:liangliangSu
# date of writing:2022-09-12 12:25
# description:
#======================================
#!/usr/bin/env python3
#Python3 max()方法
#Python3 字符串 Python3 字符串
#描述
#max() 方法返回字符串中最大的字母。
#语法
#max()方法语法：
#max(str)
#参数
#str -- 字符串。
#返回值
#返回字符串中最大的字母。
#实例
#以下实例展示了max()函数的使用方法：
#!/usr/bin/python3
str = "runoob"
print ("最大字符: " + max(str))
#以上实例输出结果如下：
#最大字符: u
#在有大小写的字符串中返回的是小写字母的最大值。
#!/usr/bin/python3
str = "rUnoob"
print ("最大字符: " + max(str))
#以上实例输出结果如下：
#最大字符: r
