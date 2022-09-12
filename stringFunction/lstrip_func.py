#======================================
# file name:lstrip_func.py
# author:liangliangSu
# date of writing:2022-09-12 12:28
# description:
#======================================
#!/usr/bin/env python3
#Python3 lstrip()方法
#描述
#lstrip() 方法用于截掉字符串左边的空格或指定字符。
#语法
#lstrip()方法语法：
#str.lstrip([chars])
#参数
#chars --指定截取的字符。
#返回值
#返回截掉字符串左边的空格或指定字符后生成的新字符串。
#实例
#以下实例展示了lstrip()的使用方法：
#实例
#!/usr/bin/python3
str = "     this is string example....wow!!!     ";
print( str.lstrip() );
str = "88888888this is string example....wow!!!8888888";
print( str.lstrip('8') );
#以上实例输出结果如下：
#this is string example....wow!!!     
#this is string example....wow!!!8888888
#从左到右移除字符串的指定字符，无字符集参数或为 None 时移除空格，str 时移除所有属于字符集子串的字符一旦不属于则停止移除并返回字符串副本。
str = 'www.example.com'
print(str.lstrip('cmowz.'))
#'example.com'
