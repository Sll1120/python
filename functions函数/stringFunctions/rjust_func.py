#======================================
# file name:rjust_func.py
# author:liangliangSu
# date of writing:2022-09-12 11:59
# description:
#======================================
#!/usr/bin/env python3
#Python3 rjust()方法
#Python3 字符串 Python3 字符串
#描述
#rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
#语法
#rjust()方法语法：
#str.rjust(width[, fillchar])
#参数
#width -- 指定填充指定字符后中字符串的总长度.
#fillchar -- 填充的字符，默认为空格。
#返回值
#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
#实例
#以下实例展示了rjust()函数的使用方法：
#!/usr/bin/python3
str = "this is string example....wow!!!"
print (str.rjust(50, '*'))
print (str.rjust(50))
#以上实例输出结果如下：
#******************this is string example....wow!!!
#                  this is string example....wow!!!
#以表格的形式输出一个数的平方和立方：
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意在前面一行使用 end
    print(repr(x*x*x).rjust(4))
# 1   1    1
# 2   4    8
# 3   9   27
# 4  16   64
# 5  25  125
# 6  36  216
# 7  49  343
# 8  64  512
# 9  81  729
#10 100 1000
