#======================================
# file name:python3_choice_func.py
# author:liangliangSu
# date of writing:2022-09-11 17:36
# description:
#======================================
#!/usr/bin/env python3
#Python3 choice() 函数
#描述
#choice() 方法返回一个列表，元组或字符串的随机项。
#语法
#以下是 choice() 方法的语法:
#import random
#random.choice( seq  )
#注意：choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
#参数
#seq -- 可以是一个列表，元组或字符串。
#返回值
#返回随机项。
#实例
#以下展示了使用 choice() 方法的实例：
#实例
#!/usr/bin/python3
import random
print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))
#以上实例运行后输出结果为：
#从 range(100) 返回一个随机数 :  68
#从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 :  2
#从字符串中 'Runoob' 返回一个随机字符 :  u

#创建随机密码组合:
import string #string module里包含了阿拉伯数字,ascii码,特殊符号
import random #需要利用到choice
a = int(input('请输入要求的密码长度: '))
b = string.digits + string.ascii_letters + string.punctuation #构建密码池
password = "" #命名一个字符串
for i in range(0,a):  #for loop 指定重复次数
    password = password + random.choice(b)   #从密码池中随机挑选内容构建密码
print(password)   #输出密码
