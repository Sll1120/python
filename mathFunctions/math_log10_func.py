#======================================
# file name:python3_log10_func.py
# author:liangliangSu
# date of writing:2022-09-11 16:36
# description:
#======================================
#!/usr/bin/env python3
#Python3 log10() 函数
#Python3 数字 Python3 数字
#描述
#log10() 方法返回以10为基数的x对数，x>0。
#语法
#以下是 log10() 方法的语法:
#import math
#math.log10( x )
#注意：log10()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#参数
#x -- 数值表达式。
#返回值
#返回以10为基数的x对数，x>0。
#实例
#以下展示了使用 log10() 方法的实例：
#!/usr/bin/python3
import math   # 导入 math 模块
print ("math.log10(100.12) : ", math.log10(100.12))
print ("math.log10(100) : ", math.log10(100))
print ("math.log10(119) : ", math.log10(119))
print ("math.log10(math.pi) : ", math.log10(math.pi))

#以上实例运行后输出结果为：
#math.log10(100.12) :  2.0005208409361854
#math.log10(100.72) :  2.003115717099806
#math.log10(119) :  2.075546961392531
#math.log10(math.pi) :  0.4971498726941338
