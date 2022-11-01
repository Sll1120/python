#======================================
# file name:dict_pop_func.py
# author:liangliangSu
# date of writing:2022-09-12 23:26
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 pop() 方法
#Python3 字典 Python3 字典
#描述
#Python 字典 pop() 方法删除字典 key（键）所对应的值，返回被删除的值。
#语法
#pop()方法语法：
#pop(key[,default])
#参数
#key - 要删除的键
#default - 当键 key 不存在时返回的值
#返回值
#返回被删除的值：
#如果 key 存在 - 删除字典中对应的元素
#如果 key 不存在 - 返回设置指定的默认值 default
#如果 key 不存在且默认值 default 没有指定 - 触发 KeyError 异常
#实例
#以下实例展示了 pop() 方法的使用方法：
#实例
##!/usr/bin/python3
#site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
#element = site.pop('name')
#print('删除的元素为:', element)
#print('字典为:', site)
#输出结果为：
#删除的元素为: 菜鸟教程
#字典为: {'alexa': 10000, 'url': 'www.runoob.com'}
#如果删除的键不存在会触发异常：
#实例
##!/usr/bin/python3
#site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
#element = site.pop('nickname')
#print('删除的元素为:', element)
#print('字典为:', site)
#输出结果为：
#File "/Users/RUNOOB/runoob-test/test.py", line 5, in <module>
#    element = site.pop('nickname')
#KeyError: 'nickname'
#可以设置默认值来避免异常：
#实例
#!/usr/bin/python3
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
element = site.pop('nickname', '不存在的 key')
print('删除的元素为:', element)
print('字典为:', site)
#输出结果为：
#删除的元素为: 不存在的 key
#字典为: {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
#Python3 字典 Python3 字典
# Python3 元组Python3 集合 
#如果要删除的 key 不存在，则需要添加默认值，否则会报错：
#!/usr/bin/python3
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
last_day = weekdays.pop() #括号里没有参数，表示删除list数组中最后一个元素
last_day = weekdays.pop(0) #0参数表示删除数组中的第一个元素
print("last_day = ", last_day, "\nweekdays = ", weekdays)
#输出结果：
#last_day =  Monday 
#weekdays =  ['Tuesday', 'Wednesday', 'Thursday']
