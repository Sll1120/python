#!/usr/bin/python3
# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-13 10:40
# * Filename : if3_if语句嵌套.py
# * Description : 
# **********************************************************
'''
if条件语句的嵌套方式一：
if 条件1:
    条件1满足执行的动作
    if 满足条件1的基础上的条件2:
        ...
    else:
    条件2不满足的情况下
else:
    条件1不满足时，执行的动作
'''
#age = int(input('请输入你的年龄:'))
#if age > 0:
#    if 0 <= age <= 6:
#        print("~~正在童年阶段~~")
#    if 7 <= age <= 17:
#        print("~~正在少年阶段~~")
#    if 18 <= age <= 40:
#        print("~~正在青年阶段~~")
#    if 41 <= age <= 65:
#        print("~~正在中年阶段~~")
#    else:
#        print("~~正在老年阶段~~")
#else:
#    print("~~请输入合法的数字~~")

'''
if条件语句的嵌套方式二：
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
'''

age = int(input('请输入你的年龄:'))
if 0 < age <= 6:
    print("~~正在童年阶段~~")
elif 7 <= age <= 17:
    print("~~正在少年阶段~~")
elif 18 <= age <= 40:
    print("~~正在青年阶段~~")
elif 41 <= age <= 65:
    print("~~正在中年阶段~~")
elif 66 <= age <=100:
    print("~~正在老年阶段~~")
elif 101 <= age <=150:
    print("~~正在超长寿阶段~~")
elif 151 <= age :
    print("~~请再次确认你活到这个年龄阶段~~")
else:
    print("~~请输入合法的数字~~")
