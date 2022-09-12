#======================================
# file name:maketrans_func.py
# author:liangliangSu
# date of writing:2022-09-12 12:34
# description:
#======================================
#!/usr/bin/env python3
#Python3 maketrans()方法
#描述
#maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
#两个字符串的长度必须相同，为一一对应的关系。
#注：Python3.4 已经没有 string.maketrans() 了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans() 。
#语法
#maketrans()方法语法：
#string.maketrans(x[, y[, z]])
#参数
#x -- 必需，字符串中要替代的字符组成的字符串。
#y -- 可选，相应的映射字符的字符串。
#z -- 可选，要删除的字符。
#返回值
#返回字符串转换后生成的新字符串。
#实例
#以下实例展示了使用 maketrans() 方法将所有元音字母转换为指定的数字：
#实例
#!/usr/bin/python3
# 字母 R 替换为 N
txt = "Runoob!"
mytable = txt.maketrans("R", "N")
print(txt.translate(mytable))
# 使用字符串设置要替换的字符，一一对应
intab = "aeiou"
outtab = "一二三四五"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print (str.translate(trantab))
#以上实例输出结果如下：
#Nunoob!
#th三s 三s str三ng 二x一mpl二....w四w!!!
#设置要删除的字符参数：
#实例
#!/usr/bin/python3
txt = "Google Runoob Taobao!"
x = "mSa"
y = "MsA"
z = "onght"   # 设置删除的字符
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
#以上实例输出结果如下：
#Gle Rub TAbA!
#str.maketrans(x[, y[, z]]) 静态方法
#给方法 str.translate() 创建字符映射 dict；只有一个参数时，必须是 Unicode序数（整数）或字符（长度为 1 的 String，会被转换为 Unicode 序数）映射到 Unicode 序数（整数）、任意长度字符串、None 的 dict 字典；如果有两个参数 xy，则必须是等长字符串，x 中字符映射到 y 中相同位置的字符，映射字典中 key 和 value 是单个字符转换的 Unicode 序数，如果 x 中存在重复字符则取用索引较大的字符来映射；第三个参数 z 必须为字符串，其字符都会映射到 None，z 可以不与 xy 等长，如果 z 与 x 中字符重复则优先映射到 None 而不映射到 y。
#补充上面知识点的例子：
#1）一个参数，该参数必须为字典
#>>> d = {'a':'1','b':'2','c':'3','d':'4','e':'5','s':'6'}
#>>> trantab = str.maketrans(d)
#>>> st='just do it'
#>>> print(st.translate(trantab))
#ju6t 4o it
#2）两个参数 x 和 y，x、y 必须是长度相等的字符串，并且 x 中每个字符映射到 y 中相同位置的字符
#>>> x = 'abcdefs'
#>>> y = '1234567'
#>>> st='just do it'
#>>> trantab = str.maketrans(x,y)
#>>> print(st.translate(trantab))
#ju7t 4o it
#三个参数 x、y、z，第三个参数 z 必须是字符串，其字符将被映射为 None，即删除该字符；如果 z 中字符与 x 中字符重复，该重复的字符在最终结果中还是会被删除。也就是无论是否重复，只要有第三个参数 z，z 中的字符都会被删除。
#>>> x = 'abcdefs'
#>>> y='1234567'
#>>> z='ot'
#>>> st='just do it'
#>>> trantab = str.maketrans(x,y,z)
#>>> print(st.translate(trantab))
#ju7 4 i
#>>>x = 'abst'
#>>>y = '1234'
#>>>z = 's'
#>>>st = 'just do it'
#>>>trantab = str.maketrans(x,y,z)
#>>>print(st.translate(trantab))
#ju4 do i4
