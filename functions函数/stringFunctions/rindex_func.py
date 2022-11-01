#======================================
# file name:rindex_func.py
# author:liangliangSu
# date of writing:2022-09-12 12:04
# description:
#======================================
#!/usr/bin/env python3
#Python3 rindex()方法
#Python3 字符串 Python3 字符串
#描述
#rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
#语法
#rindex()方法语法：
#str.rindex(str, beg=0 end=len(string))
#参数
#str -- 查找的字符串
#beg -- 开始查找的位置，默认为0
#end -- 结束查找位置，默认为字符串的长度。
#返回值
#返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常。
#实例
#以下实例展示了rindex()函数的使用方法：
#!/usr/bin/python3
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))
print (str1.rindex(str2,5))
print (str1.rindex(str2,10))
#以上实例输出结果如下：
#5
#Traceback (most recent call last):
#  File "test.py", line 6, in <module>
#    print (str1.rindex(str2,10))
#ValueError: substring not found
