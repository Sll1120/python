#======================================
# file name:python3_fabs函数.py
# author:liangliangSu
# date of writing:2022-09-11 13:45
# description:
#======================================
#!/usr/bin/env python3
#fabs() 方法返回数字的绝对值，如math.fabs(-10) 返回10.0。
#fabs() 函数类似于 abs() 函数，但是他有两点区别:
#abs() 是内置函数。 fabs() 函数在 math 模块中定义。
#fabs() 函数只对浮点型跟整型数值有效。 abs() 还可以运用在复数中。
#语法
#以下是 fabs() 方法的语法:
#import math
#math.fabs( x )
#注意：fabs()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#参数
#x -- 数值表达式。
#返回值
#返回数字的绝对值。
#实例
#以下展示了使用 fabs() 方法的实例：
#!/usr/bin/python3
import math   # 导入 math 模块
print ("math.fabs(-45.17) : ", math.fabs(-45.17))
print ("math.fabs(100.12) : ", math.fabs(100.12))
print ("math.fabs(100.72) : ", math.fabs(100.72))
print ("math.fabs(math.pi) : ", math.fabs(math.pi))

#以上实例运行后输出结果为：
#math.fabs(-45.17) :  45.17
#math.fabs(100.12) :  100.12
#math.fabs(100.72) :  100.72
#math.fabs(math.pi) :  3.141592653589793
