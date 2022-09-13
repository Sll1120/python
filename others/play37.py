sum=0 #用于存储偶数和
# print(bool(0))
a=1 #初始化变量
'''条件判断'''
while a<=100:
    '''条件执行体（求和）'''
    if a%2==0: #判断是否是偶数 #if not bool(a%2):
        sum+=a
    a+=1 #改变变量
print('1-100之间的偶数和是：',sum)