#======================================
# file name:replace_func.py
# author:liangliangSu
# date of writing:2022-09-12 12:12
# description:
#======================================
#!/usr/bin/env python3
#Python3 replace()方法
#Python3 字符串 Python3 字符串
#描述
#replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
#语法
#replace()方法语法：
#str.replace(old, new[, max])
#参数
#old -- 将被替换的子字符串。
#new -- 新字符串，用于替换old子字符串。
#max -- 可选字符串, 替换不超过 max 次
#返回值
#返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
#实例
#以下实例展示了replace()函数的使用方法：
#实例
#!/usr/bin/python3
str = "www.w3cschool.cc"
print ("菜鸟教程旧地址：", str)
print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
str = "this is string example....wow!!!"
print (str.replace("is", "was", 3))
#以上实例输出结果如下：
#菜鸟教程旧地址： www.w3cschool.cc
#菜鸟教程新地址： www.runoob.com
#thwas was string example....wow!!!
#利用 for 循环可以更加清楚的理解。
#以下实例只会替换 n 中有的，没有的将会自动跳过：
n = input("")
s = "〇一二三四五六七八九"
for c in "0123456789": 
  n = n.replace(c, s[eval(c)])
print(n)
