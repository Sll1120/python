#======================================
# file name:zfill_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:51
# description:
#======================================
#!/usr/bin/env python3
#Python3 zfill()方法
#Python3 字符串 Python3 字符串
#描述
#Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
#语法
#zfill()方法语法：
#str.zfill(width)
#参数
#width -- 指定字符串的长度。原字符串右对齐，前面填充0。
#返回值
#返回指定长度的字符串。
#实例
#以下实例展示了 zfill()函数的使用方法：
#!/usr/bin/python3
str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))
#以上实例输出结果如下：
#str.zfill :  this is string example from runoob....wow!!!
#str.zfill :  000000this is string example from runoob....wow!!!
#zfill(width) 作用同 rjust(width,"0")
str = "this is string example from runoob....wow!!!"
print(str.zfill(50));print(str.rjust(50,"0"))
#000000this is string example from runoob....wow!!!
#000000this is string example from runoob....wow!!!
