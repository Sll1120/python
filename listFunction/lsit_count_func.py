#======================================
# file name:lsit_count_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:19
# description:
#======================================
#!/usr/bin/env python3
#Python3 List count()方法
#Python3 列表 Python3 列表
#描述
#count() 方法用于统计某个元素在列表中出现的次数。
#语法
#count()方法语法：
#list.count(obj)
#参数
#obj -- 列表中统计的对象。
#返回值
#返回元素在列表中出现的次数。
#实例
#以下实例展示了 count()函数的使用方法：
#实例
#!/usr/bin/python3
aList = [123, 'Google', 'Runoob', 'Taobao', 123];
print ("123 元素个数 : ", aList.count(123))
print ("Runoob 元素个数 : ", aList.count('Runoob'))
#以上实例输出结果如下：
#123 元素个数 :  2
#Runoob 元素个数 :  1

#统计字符出现的个数或列表内出现的元素次数等也可以用 Counter。
#一个 Counter 是一个 dict 的子类，用于计数可哈希对象。
#from collections import Counter
#c = Counter('sadasfas')
#print(c)
#a=['su','bu','sum','bu','sum','bu']
#c = Counter(a)
#print(c)
#c.update('sadasfas') #添加
#print(c)
#输出结果:
#Counter({'s': 3, 'a': 3, 'd': 1, 'f': 1})
#Counter({'bu': 3, 'sum': 2, 'su': 1})
#Counter({'bu': 3, 's': 3, 'a': 3, 'sum': 2, 'su': 1, 'd': 1, 'f': 1})
