#======================================
# file name:uniform_func.py
# author:liangliangSu
# date of writing:2022-09-11 18:33
# description:
#======================================
#!/usr/bin/env python3
#Python3 uniform() 函数
#Python3 数字 Python3 数字
#描述
#uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内。
#语法
#以下是 uniform() 方法的语法:
#import random
#random.uniform(x, y)
#注意：uniform()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
#参数
#x -- 随机数的最小值，包含该值。
#y -- 随机数的最大值，包含该值。
#返回值
#返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x。
#实例
#以下展示了使用 uniform() 方法的实例：
#实例
#!/usr/bin/python3
import random
print ("uniform(5, 10) 的随机浮点数 : ",  random.uniform(5, 10))
print ("uniform(7, 14) 的随机浮点数 : ",  random.uniform(7, 14))
print ("uniform(5, 10) 的随机浮点数 : ", round(random.uniform(5, 10)))
print ("uniform(5, 10) 的随机浮点数 : ", round(random.uniform(5, 10),1))
print ("uniform(5, 10) 的随机浮点数 : ", round(random.uniform(5, 10),3))
#以上实例运行后输出结果为：
#uniform(5, 10) 的随机浮点数 :  7.054602800254241
#uniform(7, 14) 的随机浮点数 :  12.552229882744296
