#======================================
# file name:python3_asin_func.py
# author:liangliangSu
# date of writing:2022-09-11 20:54
# description:
#======================================
#!/usr/bin/env python3
#Python3 asin() 函数
#Python3 数字 Python3 数字
#描述
#asin() 返回x的反正弦弧度值。
#语法
#以下是 asin() 方法的语法:
#import math
#math.asin(x)
#注意：asin()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。
#参数
#x -- -1到1之间的数值。如果x是大于1，会产生一个错误。
#返回值
#返回x的反正弦弧度值。
#实例
#以下展示了使用 asin() 方法的实例：
#!/usr/bin/python3
import math
print ("asin(0.64) : ",  math.asin(0.64))
print ("asin(0) : ",  math.asin(0))
print ("asin(-1) : ",  math.asin(-1))
print ("asin(1) : ",  math.asin(1))
#以上实例运行后输出结果为：
#asin(0.64) :  0.694498265626556
#asin(0) :  0.0
#asin(-1) :  -1.5707963267948966
#asin(1) :  1.5707963267948966
