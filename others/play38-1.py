# 第一种方法
for item in 'python': #第一次将p取出来，将p赋值item再打印输出，第二次将Y打印出来。。。。。。
    print(item)
for i in range(10): #range()产生一个整数序列，也是一个可迭代的对象。
    print(i)
for _ in range(3): #如果在循环体中不需要使用自定义变量，可以将自定义变量写成 "_"
    print('人生苦短，我要学python')
sum=0  #用于存储和
for j in range(1,101):
    if j%2==0: #条件执行体（求和）
        sum+=j
print('1-100之间的偶数和是：',sum)

