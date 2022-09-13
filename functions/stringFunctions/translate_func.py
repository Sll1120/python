#======================================
# file name:translate_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:58
# description:
#======================================
#!/usr/bin/env python3
#Python3 translate()方法
#Python3 字符串 Python3 字符串
#描述
#translate() 方法根据参数 table 给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。
#语法
#translate()方法语法：
#str.translate(table)
#bytes.translate(table[, delete])    
#bytearray.translate(table[, delete]) 
#参数
#table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
#deletechars -- 字符串中要过滤的字符列表。
#返回值
#返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射 。
#实例
#以下实例展示了 translate() 函数的使用方法：
#实例(Python 3.0+)
#!/usr/bin/python3
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)   # 制作翻译表
str = "this is string example....wow!!!"
print (str.translate(trantab))
#以上实例输出结果如下：
#th3s 3s str3ng 2x1mpl2....w4w!!!
#以下实例演示如何过滤掉的字符 o：
#实例(Python 3.0+)
#!/usr/bin/python
# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))
#以上实例输出结果：
#b'RUNB'
#在 Python3.8 以后，delete 参数确实没有了，不管是 delete= 还是直接写 b'string' 都会返回 translate() 只有一个参数，不能给予两个的错误提示。
#下面这个简单示例可以用:
import string
s = '###ABCD####EFG##'
intab = "ABC"
outab = "123"
tab = str.maketrans(intab, outab)
print(s.translate(tab))
# 返回显示:  '###123D####EFG##'
# --------------------- 或者这个示例: ----------------------
dtab = {ord("#"): "--", ord("B"): "$$"}          # 直接用字典来作为 tab
print(s.translate(dtab))
## 返回显示:  '------A$$CD--------EFG----'
