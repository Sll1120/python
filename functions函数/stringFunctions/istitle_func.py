#======================================
# file name:istitle_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:29
# description:
#======================================
#!/usr/bin/env python3
#Python3 istitle()方法
#描述
#istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
#语法
#istitle()方法语法：
#str.istitle()
#参数
#无。
#返回值
#如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
#实例
#以下实例展示了istitle()方法的实例：
#实例
#!/usr/bin/python3
str = "This Is String Example...Wow!!!"
print (str.istitle())
str = "This is string example....wow!!!"
print (str.istitle())
#以上实例输出结果如下：
#True
#False
