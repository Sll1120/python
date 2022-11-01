#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-09 18:57
# * Filename : if2_else_双向分支.py
# * Description : 
# **********************************************************
'''
2 选 1
if...else:如果...否则
if 条件表达式:
	条件成立执行的语句块
else:
	条件不成立执行的语句块
'''
age = int(input('请输入你的年龄:'))
if age < 18:  #双向分支,一定只会执行两条路中的一条路
    print('未成年')
else:
    print('成年')
