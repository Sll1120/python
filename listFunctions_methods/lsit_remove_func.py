#======================================
# file name:lsit_remove_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:43
# description:
#======================================
#!/usr/bin/env python3
#Python3 List remove()方法
#Python3 列表 Python3 列表
#描述
#remove() 函数用于移除列表中某个值的第一个匹配项。
#语法
#remove()方法语法：
#list.remove(obj)
#参数
#obj -- 列表中要移除的对象。
#返回值
#该方法没有返回值但是会移除列表中的某个值的第一个匹配项。
#实例
#以下实例展示了 remove()函数的使用方法：
#实例
#!/usr/bin/python3
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu','Taobao']
list1.remove('Taobao')
print ("列表现在为 : ", list1)
list1.remove('Baidu')
print ("列表现在为 : ", list1)
#以上实例输出结果如下：
#列表现在为 :  ['Google', 'Runoob', 'Baidu', 'Taobao']
#列表现在为 :  ['Google', 'Runoob', 'Taobao']

