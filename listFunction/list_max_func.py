#======================================
# file name:list_max_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:04
# description:
#======================================
#!/usr/bin/env python3
#Python3 List max()方法
#Python3 列表 Python3 列表
#描述
#max() 方法返回列表元素中的最大值。
#语法
#max()方法语法：
#max(list)
#参数
#list -- 要返回最大值的列表。
#返回值
#返回列表元素中的最大值。
#实例
#以下实例展示了 max()函数的使用方法：
#实例
#!/usr/bin/python3
list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
print ("list1 最大元素值 : ", max(list1))
print ("list2 最大元素值 : ", max(list2))
#以上实例输出结果如下：
#list1 最大元素值 :  Taobao
#list2 最大元素值 :  700
#当列表中的个元素都是字符串的时候，max 函数的比较原理：
list1 = ['我','爱','python']
list2 = [100, 200, 300]
print( 'list1的最大值:', max(list1) )
print( 'list2的最大值:', max(list2) )
print( id(list1[0]) )
print( id(list1[1]) )
print( id(list1[2]) )
print('我' > '爱')
print('爱' > 'python')
print('我' > 'python')
#输出结果为：
#list1的最大值: 爱
#list2的最大值: 300
#95966224
#100598176
#95751008
#False
#True
#True
#可以看出列表中元素为字符串的时候，
############### max 函数的比较是根据 id 的大小来判断的。##################
#max 函数的其他比较方法可以参考数字章节的 max 函数笔记。
#当用 max() 函数当比较容器类型中的列表或者元组数据类型时，当其中的元素全部为数字类型时，直接根据值的大小比较。当其中的元素全部为字符串类型(string)时，则比较的是每个字符串元素的第一个字符的 ASCII 的大小。如果列表或者元组中的元素为数字类型和字符串类型混杂时，则无法比较。
#list1 = ['我最','爱学习','python']
#print( 'list1 的最大值:', max(list1)) # list1 的最大值: 爱学习
#print(ord(list1[0][0])) # ord('我') >>> 25105
#print(ord(list1[1][0])) # ord('爱') >>> 29233
#print(ord(list1[2][0])) # ord('p') >>> 112
#同理，调用 min() 函数比较时原理也是一样的。
