#======================================
# file name:python3_sqrt_func.py
# author:liangliangSu
# date of writing:2022-09-11 17:22
# description:
#======================================
#!/usr/bin/env python3
#Python3 sqrt() 函数
#描述
#sqrt() 方法返回数字x的平方根。
#语法
#以下是 sqrt() 方法的语法:
#import math
#math.sqrt( x )
#注意：sqrt()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。
#参数
#x -- 数值表达式。
#返回值
#返回数字x的平方根。
#实例
#以下展示了使用 sqrt() 方法的实例：
#实例
#!/usr/bin/python3
import math   # 导入 math 模块
print ("math.sqrt(100) : ", math.sqrt(100))
print ("math.sqrt(7) : ", math.sqrt(7))
print ("math.sqrt(math.pi) : ", math.sqrt(math.pi))
print ("math.sqrt(9) : ", math.sqrt(9))
#以上实例运行后输出结果为：
#math.sqrt(100) :  10.0
#math.sqrt(7) :  2.6457513110645907
#math.sqrt(math.pi) :  1.7724538509055159
#math.sqrt(7) :  3
#注意点: 使用此函数返回的永远都是一个 float 类型数据。

#场景1: 判断平方根之后的值是否是整数的判断。
import math
def is_sqr(x):
    a = math.sqrt(x)
    return int(a) == a
print(filter(is_sqr,range(1,101)))

#场景2:利用 for...else... 简化代码:
import math
print("101-200之间的素数是：",end="")
for i in range(100,201):
  for j in range(2,int(math.sqrt(i))+1):
    if(i%j==0):break
  else:
    print("",i,end="")
else:
  print()
