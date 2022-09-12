#======================================
# file name:rfind_func.py
# author:liangliangSu
# date of writing:2022-09-12 12:07
# description:
#======================================
#!/usr/bin/env python3
#Python3 rfind()方法
#Python3 字符串 Python3 字符串
#描述
#Python rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
#语法
#rfind()方法语法：
#str.rfind(str, beg=0 end=len(string))
#参数
#str -- 查找的字符串
#beg -- 开始查找的位置，默认为0
#end -- 结束查找位置，默认为字符串的长度。
#返回值
#返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
#实例
#以下实例展示了rfind()函数的使用方法：
#实例
#!/usr/bin/python3
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))
#以上实例输出结果如下：
#5
#5
#-1
#2
#2
#-1
