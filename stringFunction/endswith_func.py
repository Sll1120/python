#======================================
# file name:endswith_func.py
# author:liangliangSu
# date of writing:2022-09-12 00:00
# description:
#======================================
#!/usr/bin/env python3
#Python3 endswith()方法
#Python3 字符串 
#描述
#endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。
#语法
############################################################
#endswith()方法语法：
#str.endswith(suffix[, start[, end]])
#参数
#suffix -- 该参数可以是一个字符串或者是一个元素。
#start -- 字符串中的开始位置。
#end -- 字符中结束位置。
#返回值
#如果字符串含有指定的后缀返回 True，否则返回 False。
###########################################################
#实例
#以下实例展示了endswith()方法的实例：
#实例
#!/usr/bin/python3
Str='Runoob example.wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,10))
print (Str.endswith(suffix,19))
print (Str.endswith(suffix,20))
print('----------------------------')
suffix='!'
print (Str.endswith(suffix,20))
print('----------------------------')
suffix='run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))
#以上实例输出结果如下：
#True
#True
#False
#False
#False
#Python3 字符串 Python3 字符串
# Python3 数字(Number)Python3 列表 
#str.endswith(suffix[, start[, end]])
#start 参数以 0 为第一个字符索引值。
#end 参数以 1 为第一个字符索引值。
print('----------------------------')
print('01234'.endswith('234'))
print('01234'.endswith('234', 0, 5))
print('01234'.endswith('234', 0, 4))
