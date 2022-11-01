#======================================
# file name:python3_.py
# author:liangliangSu
# date of writing:2022-09-11 12:10
# description:
#======================================
#!/usr/bin/env python3
#Python3 ceil() 函数
#Python3 数字 Python3 数字
#描述
#ceil(x) 函数返回一个大于或等于 x 的的最小整数。
#语法
#以下是 ceil() 方法的语法:
#import math
#math.ceil( x )
#注意：ceil()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#参数
#x -- 数值表达式。
#返回值
#函数返回返回一个大于或等于 x 的的最小整数。
#实例
#以下展示了使用 ceil() 方法的实例：
#!/usr/bin/python3
import math   # 导入 math 模块

print (math.ceil(-45.17))
print (math.ceil(100.12))
print (math.ceil(100.72))
print (math.ceil(math.pi))
#以上实例运行后输出结果为：
#math.ceil(-45.17) :  -45
#math.ceil(100.12) :  101
#math.ceil(100.72) :  101
#math.ceil(math.pi) :  4
