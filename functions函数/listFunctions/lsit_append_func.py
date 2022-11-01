#======================================
# file name:lsit_append_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:14
# description:
#======================================
#!/usr/bin/env python3
#Python3 List append()方法
#Python3 列表 Python3 列表
#描述
#append() 方法用于在列表末尾添加新的对象。
#语法
#append()方法语法：
#list.append(obj)
#参数
#obj -- 添加到列表末尾的对象。
#返回值
#该方法无返回值，但是会修改原来的列表。
#实例
#以下实例展示了 append()函数的使用方法：
#实例
#!/usr/bin/python3
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)
#以上实例输出结果如下：
#更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']
#Python3 列表 Python3 列表
# Python3 字符串Python3 元组 
#2 篇笔记 写笔记
#   Suck My Gun
#  307***101@qq.com
#86
#定义了两个函数一个用了extend（）方法，一个用了append（）方法
##!/usr/bin/python
## -*- coding: UTF-8 -*-
#def changeextend(str):
#    "print string with extend"
#    mylist.extend([40,50,60]);
#    print ("print string mylist:",mylist)
#    return
#def changeappend(str):
#    "print string with append" 
#    mylist.append( [7,8,9] )
#    print("print string mylist:",mylist )
#    return
#mylist = [10,20,30]
#changeextend( mylist );
#print ("print extend mylist:", mylist )
#changeappend( mylist );
#print ("print append mylist:", mylist )
#输出结果：
#print string mylist: [10, 20, 30, 40, 50, 60]
#print extend mylist: [10, 20, 30, 40, 50, 60]
#print string mylist: [10, 20, 30, 40, 50, 60, [7, 8, 9]]
#print append mylist: [10, 20, 30, 40, 50, 60, [7, 8, 9]]
#通过比较可知：
# 列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。
# append() 方法向列表的尾部添加一个新的元素。
# 列表是以类的形式实现的。“创建”列表实际上是将一个类实例化。因此，列表有多种方法可以操作。extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。
#append() 是浅拷贝，如果在 append 一个对象时，需要特别注意：
#>>>alist = []
#>>> num = [2]
#>>> alist.append( num )
#>>> id( num ) == id( alist[0] )
#True
#如果使用 num[0]=3，改变 num 后，alist[0] 也随之改变。
#如不希望，需要使用 alist.append( copy.deepcopy( num ) )
#更多参考文章
# Python append() 与深拷贝、浅拷贝
# Python 直接赋值、浅拷贝和深度拷贝解析
