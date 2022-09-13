#======================================
# file name:shuffle_func.py
# author:liangliangSu
# date of writing:2022-09-11 18:23
# description:
#======================================
#!/usr/bin/env python3
#Python3 shuffle() 函数
#Python3 数字 Pytho_n3 数字
#描述
#shuffle() 方法将序列的所有元素随机排序。
#语法
#以下是 shuffle() 方法的语法:
#import random
#random.shuffle (lst )
#注意：shuffle() 是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
#参数
#lst -- 列表。
#返回值
#返回 None。
#实例
#以下展示了使用 shuffle() 方法的实例：
#实例
#!/usr/bin/python3
import random
list = [20, 16, 10, 5];
random.shuffle(list)
print ("随机排序列表 : ",  list)
random.shuffle(list)
print ("随机排序列表 : ",  list)
#以上实例运行后输出结果为：
#随机排序列表 :  [20, 5, 16, 10]
#随机排序列表 :  [5, 20, 10, 16]
#本来想使用相同种子使得随机排序后结果相同：
#!/usr/bin/python3
import random
list = [20, 16, 10, 5]
random.seed(10)
random.shuffle(list)
print("随机排序列表 : ", list)
random.seed(10)
random.shuffle(list)
print("随机排序列表 : ", list)
#输出结果：
#随机排序列表 :  [5, 10, 16, 20]
#随机排序列表 :  [20, 16, 10, 5]
#查阅得知：因为 random.shuffle 具有破坏性，需要每次都重置列表。
#下列代码才可以得到相同的随机排序列表。
#import random
#SEED = 10
#original_list = ['list', 'elements', 'go', 'here']
#random.seed(SEED)
#my_list = original_list[:]
#random.shuffle(my_list)
#print("RUN1: ", my_list)
#random.seed(SEED)
#my_list = original_list[:]
#random.shuffle(my_list)
#print("RUN2: ", my_list)
#输出结果：
#RUN1:  ['here', 'go', 'elements', 'list']
#RUN2:  ['here', 'go', 'elements', 'list']
#coderge
#   coderge
#  cod***e@foxmail.com
#   参考地址
#2年前 (2020-05-28)
#   vipkwd
#  ser***e@vipkwd.com
#16
#浅谈一下“破坏性”的问题。
#一个函数其最终状态无非以下几种：
# 1、显性 return；
# 2、无return（隐性reutrn None）；
# 3、改变空间下的值(多用于类中），显性return；
# 4、改变空间下的值(多用于类中），无return（隐性reutrn None）；
# 5、改变入参 [，改变空间下的值(多用于类中）]，显性 return;
# 6、改变入参 [，改变空间下的值(多用于类中）]，无 return（隐性reutrn None）;
#其中所有无 return 的结构都是合法，只是我们通常都手动显性给个返回值而已（那怕也是同隐性reutrn一样，返回一个 None。
#这样做的意义在于： 从外部看就知道这个函数他是有返回值的,便于代码理解与维护）关于 5 和 6 的“改变入参”，这个说起来就和PHP的引用传参如出一辙（我猜的, 本想看下底层实现来验证的但没有找到地方）：函数内部改变入参，函数外部也跟着被改变；因为他们（外部变量和入参变量）指向了同一个内存地址。 这样说来应该就好理解为啥是：
#list = [20, 16, 10, 5];
#random.shuffle(list)
#print ("正确 : ",  list)
#而不是：
#list = [20, 16, 10, 5];
#thisIsNone=random.shuffle(list)
#print ("不是 : ",  random.shuffle(list))
#print ("也不是 : ",  thisIsNone)
