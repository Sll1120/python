#======================================
# file name:list_len_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:01
# description:
#======================================
#!/usr/bin/env python3
#Python3 List len()方法
#Python3 列表 Python3 列表
#描述
#len() 方法返回列表元素个数。
#语法
#len()方法语法：
#len(list)
#参数
#list -- 要计算元素个数的列表。
#返回值
#返回列表元素个数。
#实例
#以下实例展示了 len()函数的使用方法：
#实例
#!/usr/bin/python3
list1 = ['Google', 'Runoob', 'Taobao']
print (len(list1))
list2=list(range(5)) # 创建一个 0-4 的列表
print (len(list2))
#以上实例输出结果如下：
#3
#5
#这上面前面的例子中定义了 list 变量所以，这时候可能会报错，应该使用 del 方法删掉之前定义的变量 list，才能继续运行：
list1 = ['Google', 'Runoob', 'Taobao']
print (len(list1))
if 'list' in locals().keys(): # 判断一下list这个变量是否被定义了
    del (list)
list2=list(range(5)) # 创建一个 0-4 的列表
print (len(list2))
