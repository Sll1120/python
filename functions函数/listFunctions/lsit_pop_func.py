#======================================
# file name:lsit_pop_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:39
# description:
#======================================
#!/usr/bin/env python3
#Python3 List pop()方法
#Python3 列表 Python3 列表
#描述
#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
#语法
#pop()方法语法：
#list.pop([index=-1])
#参数
#index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
#返回值
#该方法返回从列表中移除的元素对象。
#实例
#以下实例展示了 pop()函数的使用方法：
#!/usr/bin/python3
list1 = ['Google', 'Runoob', 'Taobao']
list1.pop()
print ("列表现在为 : ", list1)
list1.pop(1)
print ("列表现在为 : ", list1)
#以上实例输出结果如下：
#列表现在为 :  ['Google', 'Runoob']
#列表现在为 :  ['Google']
#可以通过下面这种方法打印 pop() 函数来显示返回值:
#!/usr/bin/python3
list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop(1)
print ("删除的项为 :", list_pop)
print ("列表现在为 : ", list1)
#以上实例输出结果如下：
#删除的元素为 : Runoob
#列表现在为 :  ['Google', 'Taobao']
