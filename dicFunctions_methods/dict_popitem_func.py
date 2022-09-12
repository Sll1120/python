#======================================
# file name:dict_popitem_func.py
# author:liangliangSu
# date of writing:2022-09-12 22:43
# description:
#======================================
#!/usr/bin/env python3
#Python3 字典 popitem() 方法
#Python3 字典 Python3 字典
#描述
#Python 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。
#如果字典已经为空，却调用了此方法，就报出 KeyError 异常。
#语法
#popitem()方法语法：
#popitem()
#参数
#无
#返回值
#返回最后插入键值对(key, value 形式)，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。
#注意：在 Python3.7 之前，popitem() 方法删除并返回任意插入字典的键值对。
#实例
#以下实例展示了 popitem() 方法的使用方法：
#实例
#!/usr/bin/python3
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# ('url': 'www.runoob.com') 最后插入会被删除
result = site.popitem()
print('返回值 = ', result)
print('site = ', site)
## 插入新元素
site['nickname'] = 'Runoob'
print('site = ', site)
# 现在 ('nickname', 'Runoob') 是最后插入的元素
result = site.popitem()
print('返回值 = ', result)
print('site = ', site)
#输出结果为：
#返回值 =  ('url', 'www.runoob.com')
#site =  {'name': '菜鸟教程', 'alexa': 10000}
#site =  {'name': '菜鸟教程', 'alexa': 10000, 'nickname': 'Runoob'}
#返回值 =  ('nickname', 'Runoob')
#site =  {'name': '菜鸟教程', 'alexa': 10000}
