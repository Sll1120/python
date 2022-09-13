#======================================
# file name:split_func.py
# author:liangliangSu
# date of writing:2022-09-12 11:38
# description:
#======================================
#!/usr/bin/env python3
#Python3 split()方法
#描述
#split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
#语法
#split() 方法语法：
#str.split(str="", num=string.count(str))
#参数
#str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
#num -- 分割次数。默认为 -1, 即分隔所有。
#返回值
#返回分割后的字符串列表。
#实例
#以下实例展示了 split() 函数的使用方法：
#实例(Python 3.0+)
#!/usr/bin/python3
str = "this is string example....wow!!!"
print (str.split( ))       # 以空格为分隔符
print (str.split('i',1))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符
print (str.split(' ',-1 ))       # 默认格式
print ('-----------------------------------------------------------')       
#以上实例输出结果如下：
#['this', 'is', 'string', 'example....wow!!!']
#['th', 's is string example....wow!!!']
#['this is string example....', 'o', '!!!']
#['this', 'is', 'string', 'example....wow!!!']
#以下实例以 # 号为分隔符，指定第二个参数为 1，返回两个参数列表。
#实例(Python 3.0+)
#!/usr/bin/python3
txt = "Google#Runoob#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)
print(x)
#以上实例输出结果如下：
#['Google', 'Runoob#Taobao#Facebook']
#URL 简单分割:
#!/usr/bin/python3
url = "http://www.baidu.com/python/image/123456.jpg"
#以“.” 进行分隔
path =url.split(".")
print(path)
#以上输出结果：我们在学习 python 爬虫的时候例如需要保存图片，图片名称的获取，可以依照下列方法：
#['http://www', 'baidu', 'com/python/image/123456', 'jpg']
#以 / 进行分隔：
path =url.split("/")
print(path)
#['http:', '', 'www.baidu.com', 'python', 'image', '123456.jpg']
#我们在学习 python 爬虫的时候例如需要保存图片，图片名称的获取，可以依照下列方法：
path =url.split("/")[-1]
print(path)
print('-------------------------------------------------------------------')
path =url.split("/")[5]
print(path)
#输出结果：
#'123456.jpg'
