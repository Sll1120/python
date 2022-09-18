#======================================
# file name:python3_.py
# author:liangliangSu
# date of writing:2022-09-11 16:17
# description:
#======================================
#!/usr/bin/env python3
#Python3 floor() 函数
#Python3 数字 Python3 数字
#描述
#floor(x) 返回数字的下舍整数，小于或等于 x。
#语法
#以下是 floor() 方法的语法:
#import math
#math.floor( x )
#注意：floor()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#参数
#x -- 数值表达式。
#返回值
#返回小于或等于 x 的整数。
#实例
#以下展示了使用 floor() 方法的实例：
#!/usr/bin/python
import math   # 导入 math 模块
print ("math.floor(-45.17) : ", math.floor(-45.17))
print ("math.floor(100.12) : ", math.floor(100.12))
print ("math.floor(100.72) : ", math.floor(100.72))
print ("math.floor(math.pi) : ", math.floor(math.pi))

#以上实例运行后输出结果为：
#math.floor(-45.17) :  -46
#math.floor(100.12) :  100
#math.floor(100.72) :  100
#math.floor(math.pi) :  3
