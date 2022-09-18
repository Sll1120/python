#======================================
# file name:python3_radians_func.py
# author:liangliangSu
# date of writing:2022-09-11 22:54
# description:
#======================================
#!/usr/bin/env python3
#Python3 radians() 函数
#Python3 数字 Python3 数字
#描述
#radians() 方法将角度转换为弧度。
#角度和弧度关系是：2π 弧度 = 360°。从而 1°≈0.0174533 弧度，1 弧度≈57.29578°。
#1) 角度转换为弧度公式：弧度=角度÷180×π
#2)弧度转换为角度公式： 角度=弧度×180÷π
#语法
#以下是 radians() 方法的语法:
#import math
#math.radians(x)
#注意：radians()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。
#参数
#x -- 一个角度数值，默认单位是角度 °。
#返回值
#返回一个角度的弧度值。
#实例
#以下展示了使用 radians() 方法的实例：
#实例
#!/usr/bin/python3
import math
print ("radians(90) : ",  math.radians(90))     # 1 弧度等于大概 57.3°
print ("radians(45) : ",  math.radians(45))
print ("radians(30) : ",  math.radians(30))
print ("radians(180) : ",  math.radians(180))  # 180 度的弧度为 π
print("180 / pi : ", end ="")
print (math.radians(180 / math.pi))
#以上实例运行后输出结果为：
#radians(90) :  1.5707963267948966
#radians(45) :  0.7853981633974483
#radians(30) :  0.5235987755982988
#radians(180) :  3.141592653589793
#180 / pi : 1.0
