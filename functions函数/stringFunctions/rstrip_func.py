#======================================
# file name:rstrip_func.py
# author:liangliangSu
# date of writing:2022-09-12 11:52
# description:
#======================================
#!/usr/bin/env python3
#Python3 rstrip() 方法
#Python3 字符串 Python3 字符串
#描述
#rstrip() 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。
#语法
#rstrip()方法语法：
#str.rstrip([chars])
#参数
#chars -- 指定删除的字符（默认为空白符）
#返回值
#返回删除 string 字符串末尾的指定字符后生成的新字符串。
#实例
#以下实例展示了 rstrip() 函数的使用方法：
#实例
#!/usr/bin/python3
random_string = 'this is good    '
# 字符串末尾的空格会被删除
print(random_string.rstrip())
# 'si oo' 不是尾随字符，因此不会删除任何内容
print(random_string.rstrip('si oo'))
# 在 'sid oo' 中 'd oo' 是尾随字符，'ood' 从字符串中删除
print(random_string.rstrip('sid oo'))
# 'm/' 是尾随字符，没有找到 '.' 号的尾随字符, 'm/' 从字符串中删除
website = 'www.runoob.com/'
print(website.rstrip('m/.'))
# 移除逗号(,)、点号(.)、字母 s、q 或 w，这几个都是尾随字符
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)
# 删除尾随字符 *
str = "*****this is string example....wow!!!*****"
print (str.rstrip('*'))
#以上实例输出结果如下：
#this is good
#this is good
#this is g
#www.runoob.co
#banana
#*****this is string example....wow!!!
