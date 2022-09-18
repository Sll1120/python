#======================================
# file name:random_func.py
# author:liangliangSu
# date of writing:2022-09-11 18:14
# description:
#======================================
#!/usr/bin/env python3
#Python3 random() 函数
#描述
#random() 方法返回随机生成的一个实数，它在半开放区间 [0,1) 范围内。
#语法
#以下是 random() 方法的语法:
#import random
#random.random()
#注意：random() 是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法
#参数
#无
#返回值
##########################################################################
#############返回随机生成的一个实数，它在半开放区间 [0,1) 范围内。#########
##########################################################################
#实例
#以下展示了使用 random() 方法的实例：
#实例
#!/usr/bin/python3
import random
# 第一个随机数
print ("random() : ", random.random())
# 第二个随机数
print ("random() : ", random.random())
#以上实例运行后输出结果为：
#random() :  0.09690599908884856
#random() :  0.8732120512570916
