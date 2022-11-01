#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-13 12:24
# * Filename : if5_pass关键字.py
# * Description : 
# **********************************************************
'''
pass：有时候程序需要占有一个位置，但是又不想做事情，可以通过pass实现
pass什么都不会做，填个坑用的。
'''
age = int(input('请输入你的年龄'))
if age >= 0:
    pass
else:
    print('请输入合法的年龄')
