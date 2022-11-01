#======================================
# file name:python3_log_func.py
# author:liangliangSu
# date of writing:2022-09-11 16:39
# description:
#======================================
#!/usr/bin/env python3
#Python3 log() 函数
#Python3 数字 Python3 数字
#描述
#log() 方法返回x的自然对数，x > 0。
#语法
#以下是 log() 方法的语法:
#import math
#math.log( x )
#注意：log()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#参数
#x -- 数值表达式。
#返回值
#返回x的自然对数，x>0。
#实例
#以下展示了使用 log() 方法的实例：
#!/usr/bin/python3
import math   # 导入 math 模块
print ("math.log(100.12) : ", math.log(100.12))
print ("math.log(100.72) : ", math.log(100.72))
print ("math.log(math.pi) : ", math.log(math.pi))

#以上实例运行后输出结果为：
#math.log(100.12) :  4.6063694665635735
#math.log(100.72) :  4.612344389736092
#math.log(math.pi) :  1.1447298858494002
