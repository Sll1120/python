#======================================
# file name:title_func.py
# author:liangliangSu
# date of writing:2022-09-12 11:13
# description:
#======================================
#!/usr/bin/env python3
#Python3 title()方法
#Python3 字符串 Python3 字符串
#描述
#Python title() 方法返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写(见 istitle())。
#语法
#title()方法语法：
#str.title();
#参数
#NA。
#返回值
#返回"标题化"的字符串,就是说所有单词的首字母都转化为大写。
#实例
#以下实例展示了 title()函数的使用方法：
#实例(Python 3.0+)
#!/usr/bin/python3
str = "this is string example from runoob....wow!!!"
print (str.title())
#以上实例输出结果如下：
#This Is String Example From Runoob....Wow!!!
#请注意，非字母后的第一个字母将转换为大写字母：
#实例(Python 3.0+)
#!/usr/bin/python3
str2 = "hello b2b2b2 and 3g3g3g"
x = str2.title()
print(x)
#输出结果为：
#Hello B2B2B2 And 3G3G3G
