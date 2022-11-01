#======================================
# file name:index_func.py
# author:liangliangSu
# date of writing:2022-09-12 09:29
# description:
#======================================
#!/usr/bin/env python3
#Python3 index()方法
#Python3 字符串 Python3 字符串
#描述
#index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
#语法
#index()方法语法：
#str.index(str, beg=0, end=len(string))
#参数
#    str -- 指定检索的字符串
#    beg -- 开始索引，默认为0。
#    end -- 结束索引，默认为字符串的长度。
#返回值
#如果包含子字符串返回开始的索引值，否则抛出异常。
#实例
#以下实例展示了index()方法的实例：
#!/usr/bin/python3
str1 = "Runoob example....wow!!!"
str2 = "exam";
print (str1.index(str2))
print (str1.index(str2, 5))
print (str1.index(str2, 10))
#以上实例输出结果如下(未发现的会出现异常信息)：
#7
#7
#Traceback (most recent call last):
#  File "/home/sll/git_study/gitpython/stringFunction/index_func.py", line 28, in <module>
#    print (str1.index(str2, 10))
#ValueError: substring not found
