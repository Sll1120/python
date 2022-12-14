#======================================
# file name:python3_tan_func.py
# author:liangliangSu
# date of writing:2022-09-11 22:57
# description:
#======================================
#!/usr/bin/env python3
#Python3 tan() 函数
#Python3 数字 Python3 数字
#描述
#tan() 返回 x 弧度的正切值。
#语法
#以下是 tan() 方法的语法:
#import math
#math.tan(x)
#注意：tan()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。
#参数
#x -- 一个数值。
#返回值
#返回 x 弧度的正切值，数值在 -1 到 1 之间。
#实例
#以下展示了使用 tan() 方法的实例：
#实例(Python 3.0+)
#!/usr/bin/python3
import math
print ("(tan(3) : ",  math.tan(3))
print ("tan(-3) : ",  math.tan(-3))
print ("tan(0) : ",  math.tan(0))
print ("tan(math.pi) : ",  math.tan(math.pi))
print ("tan(math.pi/2) : ",  math.tan(math.pi/2))
print ("tan(math.pi/4) : ",  math.tan(math.pi/4))
#以上实例运行后输出结果为：
#(tan(3) :  -0.1425465430742778
#tan(-3) :  0.1425465430742778
#tan(0) :  0.0
#tan(math.pi) :  -1.2246467991473532e-16
#tan(math.pi/2) :  1.633123935319537e+16
#tan(math.pi/4) :  0.9999999999999999
