#======================================
# file name:lsit_index_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:27
# description:
#======================================
#!/usr/bin/env python3
#Python3 List index()方法
#Python3 列表 Python3 列表
#描述
#index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
#语法
#index()方法语法：
#list.index(x[, start[, end]])
#参数
#x-- 查找的对象。
#start-- 可选，查找的起始位置。
#end-- 可选，查找的结束位置。
#返回值
#该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
#实例
#以下实例展示了 index()函数的使用方法：
#实例 1
#!/usr/bin/python3
list1 = ['Google', 'Runoob', 'Taobao']
print ('Runoob 索引值为', list1.index('Runoob'))
print ('Taobao 索引值为', list1.index('Taobao'))
#以上实例输出结果如下：
#Runoob 索引值为 1
#Taobao 索引值为 2
#实例 2
#!/usr/bin/python3
list2 = ['Google', 'Runoob', 'Taobao', 'Facebook', 'QQ']
## 从指定位置开始搜索
print ('Runoob 索引值为', list1.index('Runoob',2))
#以上实例输出结果如下：
#Runoob 索引值为 1
