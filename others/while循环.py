#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-13 13:43
# * Filename : while循环.py
# * Description : 
# **********************************************************
'''
while循环与if条件的 语法格式类型：
if 条件表达式:
	代码块
while 条件表达式:
	代码块
'''
num = 1
while num <= 100:
#    print("num =", num, end=" ")
    print("num =", num)
    num += 1
print("循环结束")
while True:
    user = input("请输入账号:")
    pwd = input("请输入密码:")
    if user == "sll" and pwd == "sll":
        print("登录成功")
        break  #stop
    else:
        print("账号或是密码错误")
print("欢迎")

sum = 0  #初始化一个累计的变量
num = 1  #从1开始
while num < 100:
    sum = sum + num
    num += 1
print("从1开始到100的和是:",sum)

