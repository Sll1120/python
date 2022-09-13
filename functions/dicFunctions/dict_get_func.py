#======================================
# file name:dict_get_func.py
# author:liangliangSu
# date of writing:2022-09-12 20:39
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 get() 方法
#描述
#Python 字典 get() 函数返回指定键的值。
#语法
#get()方法语法：
#dict.get(key[, value]) 
#参数
#key -- 字典中要查找的键。
#value -- 可选，如果指定键的值不存在时，返回该默认值。
#返回值
#返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。
#实例
#以下实例展示了 get() 函数的使用方法：
#实例
#!/usr/bin/python
tinydict = {'Name': 'Runoob', 'Age': 27}
print ("Age : ", tinydict.get('Age'))
# 没有设置 Sex，也没有设置默认的值，输出 None
print ("Sex : ", tinydict.get('Sex'))  
# 没有设置 Salary，输出默认的值  0.0
print ('Salary: ', tinydict.get('Salary', 0.0))
#以上实例输出结果为：
#Age : 27
#Sex : None
#Salary: 0.0
#get() 方法 Vs dict[key] 访问元素区别
#get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。
#dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常。
#实例
#>>> runoob = {}
#>>> print('URL: ', runoob.get('url'))     # 返回 None
#URL:  None
#>>> print(runoob['url'])     # 触发 KeyError
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'url'
#>>>
#嵌套字典使用
#get() 方法对嵌套字典的使用方法如下：
#实例
#!/usr/bin/python
tinydict = {'RUNOOB' : {'url' : 'www.runoob.com'}}
res = tinydict.get('RUNOOB', {}).get('url')
# 输出结果
print("RUNOOB url 为 : ", str(res))
#以上实例输出结果为：
#RUNOOB url 为 :  www.runoob.com
