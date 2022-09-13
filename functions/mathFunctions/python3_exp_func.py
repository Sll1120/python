#======================================
# file name:Python3_exp函数.py
# author:liangliangSu
# date of writing:2022-09-11 12:15
# description:
#======================================
#!/usr/bin/env python3
#Python3 exp() 函数
#Python3 数字 Python3 数字
#
#描述
#exp() 方法返回x的指数,ex。
#
#语法
#以下是 exp() 方法的语法:
#
#import math
#
#math.exp( x )
#注意：exp()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#
#参数
#x -- 数值表达式。
#返回值
#返回x的指数,ex。
#实例
#以下展示了使用 exp() 方法的实例：
#
#!/usr/bin/python3
import math   # 导入 math 模块
print (math.exp(-45.17))
print (math.exp(100.12))
print (math.exp(100.72))
print (math.exp(math.pi))
print (math.exp(2))
#以上实例运行后输出结果为：
#math.exp(-45.17) :  2.4150062132629406e-20
#math.exp(100.12) :  3.0308436140742566e+43
#math.exp(100.72) :  5.522557130248187e+43
#math.exp(math.pi) :  23.140692632779267
