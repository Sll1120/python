#======================================
# file name:dict_items_func.py
# author:liangliangSu
# date of writing:2022-09-12 23:07
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 items() 方法
#Python3 字典 Python3 字典
#描述
#Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。
#dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
#视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
#我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
#语法
#items()方法语法：
#dict.items()
#参数
#NA。
#返回值
#返回可视图对象。
#实例
#以下实例展示了 items() 方法的使用方法：
#实例
#!/usr/bin/python3
tinydict = {'Name': 'Runoob', 'Age': 7}
print ("Value : %s" %  tinydict.items())
#以上实例输出结果为：
#Value : dict_items([('Age', 7), ('Name', 'Runoob')])
#遍历例子：
d = {'Name': 'Runoob', 'Age': 7}
for i,j in d.items():
    print(i, ":\t", j)
#输出：
#Name :   Runoob
#Age :    7
#将字典的 key 和 value 组成一个新的列表：
d={1:"a",2:"b",3:"c"}
result=[]
for k,v in d.items():
    result.append(k)
    result.append(v)
print(result)
#输出：
#[1, 'a', 2, 'b', 3, 'c']
