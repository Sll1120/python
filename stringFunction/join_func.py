#======================================
# file name:join_func.py
# author:liangliangSu
# date of writing:2022-09-12 10:32
# description:
#======================================
#!/usr/bin/env python3
#Python3 join()方法
#Python3 字符串 Python3 字符串
#描述
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#语法
#join()方法语法：
#str.join(sequence)
#参数
#sequence -- 要连接的元素序列。
#返回值
#返回通过指定字符连接序列中元素后生成的新字符串。
#实例
#以下实例展示了join()的使用方法：
#实例
#!/usr/bin/python3
s1 = "-"
s2 = ""
s3 = "*"
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
seq1 = ("1", "2", "3", "4", "5", "6") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
print (s3.join( seq1 ))
#以上实例输出结果如下：
#r-u-n-o-o-b
#runoob
