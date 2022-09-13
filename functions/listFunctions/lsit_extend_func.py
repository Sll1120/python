#======================================
# file name:lsit_extend_func.py
# author:liangliangSu
# date of writing:2022-09-12 14:22
# description:
#======================================
#!/usr/bin/env python3
#Python3 List extend()方法
#Python3 列表 Python3 列表
#描述
#extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
#语法
#extend()方法语法：
#list.extend(seq)
#参数
#seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
#返回值
#该方法没有返回值，但会在已存在的列表中添加新的列表内容。
#实例
#以下实例展示了 extend()函数的使用方法：
#实例
#!/usr/bin/python3
list1 = ['Google', 'Runoob', 'Taobao']
list2=list(range(5)) # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print ("扩展后的列表：", list1)
#以上实例输出结果如下：
#扩展后的列表： ['Google', 'Runoob', 'Taobao', 0, 1, 2, 3, 4]
#不同数据类型：
#实例
#!/usr/bin/python3
# 语言列表
language = ['French', 'English', 'German']
# 元组
language_tuple = ('Spanish', 'Portuguese')
# 集合
language_set = {'Chinese', 'Japanese'}
# 添加元组元素到列表末尾
language.extend(language_tuple)
print('新列表: ', language)
# 添加集合元素到列表末尾
language.extend(language_set)
print('新列表: ', language)
#新列表:  ['French', 'English', 'German', 'Spanish', 'Portuguese']
#新列表:  ['French', 'English', 'German', 'Spanish', 'Portuguese', 'Chinese', 'Japa
