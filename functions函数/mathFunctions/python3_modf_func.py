#======================================
# file name:python3_modf_func.py
# author:liangliangSu
# date of writing:2022-09-11 16:47
# description:
#======================================
#!/usr/bin/env python3
#Python3 modf() 函数
#Python3 数字 Python3 数字
#描述
#modf() 方法返回 x 的整数部分与小数部分，两部分的数值符号与 x 相同，整数部分以浮点型表示。
#语法
#以下是 modf() 方法的语法:
#import math
#math.modf( x )
#注意：modf()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#参数
#x -- 数值表达式。
#返回值
#返回x的整数部分与小数部分，
#实例
#以下展示了使用 modf() 方法的实例：
#实例
#!/usr/bin/python3
import math   # 导入 math 模块
print ("math.modf(100.12) : ", math.modf(100.12))
print ("math.modf(-100.12) : ", math.modf(-100.12))
print ("math.modf(100.72) : ", math.modf(100.72))
print ("math.modf(119) : ", math.modf(119))
print ("math.modf(math.pi) : ", math.modf(math.pi))
print(type(math.modf(-9.8)))
#以上实例运行后输出结果为：
#math.modf(100.12) :  (0.12000000000000455, 100.0)
#math.modf(-100.12) :  (-0.12000000000000455, -100.0)
#math.modf(100.72) :  (0.7199999999999989, 100.0)
#math.modf(119) :  (0.0, 119.0)
#math.modf(math.pi) :  (0.14159265358979312, 3.0)
