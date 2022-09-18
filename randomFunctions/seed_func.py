#======================================
# file name:seed_func.py
# author:liangliangSu
# date of writing:2022-09-11 18:20
# description:
#======================================
#!/usr/bin/env python3
#Python3 seed() 函数
#Python3 数字 Python3 数字
#描述
#seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
#语法
#以下是 seed() 方法的语法:
#import random
#random.seed ( [x] )
#我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。
#注意：seed()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
#参数
#x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
#返回值
#本函数没有返回值。
#实例
#以下展示了使用 seed(() 方法的实例：
#实例
#!/usr/bin/python3
import random
random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())
#以上实例运行后输出结果为：
#使用默认种子生成随机数： 0.7908102856355441
#使用默认种子生成随机数： 0.81038961519195
#使用整数 10 种子生成随机数： 0.5714025946899135
#使用整数 10 种子生成随机数： 0.5714025946899135
#使用字符串种子生成随机数： 0.3537754404730722
