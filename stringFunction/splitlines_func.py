#======================================
# file name:splitlines_func.py
# author:liangliangSu
# date of writing:2022-09-12 11:29
# description:
#======================================
#!/usr/bin/env python3
#Python3 splitlines()方法
#Python3 字符串 Python3 字符串
#描述
#Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
#语法
#splitlines()方法语法：
#str.splitlines([keepends])
#参数
#keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
#返回值
#返回一个包含各行作为元素的列表。
#实例
#以下实例展示了splitlines()函数的使用方法：
A = 'ab c\n\nde fg\rkl\r\n'
a = 'ab c\n\nde fg\rkl\r\n'.splitlines()
print(A)
print(a)
print('------------------------------------')
a = 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
print(a)
a = 'ab c\n\nde fg\rkl\r\n'.splitlines(False)    #默认为 False
print(a)
a = 'ab c\n\nde fg\rkl\r\n'.splitlines()         #默认为 False
print(a)
