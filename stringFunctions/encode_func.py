#======================================
# file name:encode_func.py
# author:liangliangSu
# date of writing:2022-09-11 23:57
# description:
#======================================
#!/usr/bin/env python3
#Python3 encode()方法
#Python3 字符串 Python3 字符串
#描述
#encode() 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
#语法
#encode()方法语法：
#str.encode(encoding='UTF-8',errors='strict')
#参数
#encoding -- 要使用的编码，如: UTF-8。
#errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
#返回值
#该方法返回编码后的字符串，它是一个 bytes 对象。
#实例
#以下实例展示了encode()方法的实例：
#实例(Python 3.0+)
#!/usr/bin/python3
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
#以上实例输出结果如下：
#菜鸟教程
#UTF-8 编码： b'\xe8\x8f\x9c\xe9\xb8\x9f\xe6\x95\x99\xe7\xa8\x8b'
#GBK 编码： b'\xb2\xcb\xc4\xf1\xbd\xcc\xb3\xcc'
#UTF-8 解码： 菜鸟教程
#GBK 解码： 菜鸟教程
