#======================================
# file name:count_func.py
# author:liangliangSu
# date of writing:2022-09-11 23:37
# description:
#======================================
#!/usr/bin/env python3
#Python3 count()方法
#Python3 字符串 Python3 字符串
#描述
#count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
#语法
#count()方法语法：
#str.count(sub, start= 0,end=len(string))
#参数
#sub -- 搜索的子字符串
#start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
#end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
#返回值
#该方法返回子字符串在字符串中出现的次数。
#实例
#以下实例展示了count()方法的实例：
#!/usr/bin/python3
str="www.runoob.com.liangliangsu"
sub='o'
print ("str.count('o') : ", str.count(sub))
sub='run'
print ("str.count('run', 0, 10) : ", str.count(sub,0,10))
sub='n'
print ("str.count('n', 0, 27) : ", str.count(sub,0,27))
sub='liang'
print ("str.count('liangliangsu', 0, 10) : ", str.count(sub,0,10))
print ("str.count('liangliangsu', 0, 20) : ", str.count(sub,0,20))
print ("str.count('liangliangsu', 0, 27) : ", str.count(sub,0,27))
#以上实例输出结果如下：
#str.count('o') :  3
#str.count('run', 0, 10) :  1
