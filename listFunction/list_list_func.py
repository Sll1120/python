#======================================
# file name:list_list_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:10
# description:
#======================================
#!/usr/bin/env python3
#Python3 List list()方法
#Python3 列表 Python3 列表
#描述
#list() 方法用于将元组或字符串转换为列表。
#注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
#语法
#list()方法语法：
#list( seq )
#参数
#seq -- 要转换为列表的元组或字符串。
#返回值
#返回列表。
#实例
#以下实例展示了 list()函数的使用方法：
#!/usr/bin/python3
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print ("列表元素 : ", list1)
str="Hello World"
list2=list(str)
print ("列表元素 : ", list2)
#以上实例输出结果如下：
#列表元素 :  [123, 'Google', 'Runoob', 'Taobao']
#列表元素 :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
