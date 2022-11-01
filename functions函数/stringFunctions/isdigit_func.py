#======================================
# file name:isdigit_func.py
# author:liangliangSu
# date of writing:2022-09-12 09:58
# description:
#======================================
#!/usr/bin/env python3
#Python3 isdigit()方法
#Python3 字符串 Python3 字符串
#描述
#Python isdigit() 方法检测字符串是否只由数字组成。
#语法
#isdigit()方法语法：
#str.isdigit()
#参数
#无。
#返回值
#如果字符串只包含数字则返回 True 否则返回 False。
#实例
#以下实例展示了isdigit()方法的实例：
#实例
#!/usr/bin/python3
str = "123456";
print (str.isdigit())
str = "Runoob example....wow!!!"
print (str.isdigit())
print ('-------------------------------------------')
#以上实例输出结果如下：
#True
#False
#isdigit() 方法只对正整数有效，负数及小数均返回不正确。
#可以使用以下函数来解决：
#实例
## 判断是否为数字
def is_number(s):    
    try:    # 如果能运⾏ float(s) 语句，返回 True（字符串 s 是浮点数）        
        float(s)        
        return True    
    except ValueError:  # ValueError 为 Python 的⼀种标准异常，表⽰"传⼊⽆效的参数"        
        pass  # 如果引发了 ValueError 这种异常，不做任何事情（pass：不做任何事情，⼀般⽤做占位语句）    
    try:        
        import unicodedata  # 处理 ASCII 码的包        
        unicodedata.numeric(s)  # 把⼀个表⽰数字的字符串转换为浮点数返回的函数        
        return True    
    except (TypeError, ValueError):        
        pass    
        return False
print(is_number(1))
print(is_number(1.0))
print(is_number(0))
print(is_number(-2))
print(is_number(-2.0))
print(is_number("abc"))
#输出结果为：
#True
#True
#True
#True
#True
#False

#str.isdigit() 检测字符串是否只包含数字（即不接受其他一切非 [0-9] 元素）。
#>>> import sys
#>>> sys.version
#'3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]'
#>>> '777'.isdigit()
#True
#>>> '33d'.isdigit()
#False
#>>> '33在'.isdigit()
#False
#>>> '-23'.isdigit()
#False
#>>> '0.32'.isdigit()
#False
#>>> (2>3).isdigit() #入参类型不合法
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'bool' object has no attribute 'isdigit'
