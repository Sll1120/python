'''1,要求输出1到50之间所有5的倍数，5,10,15,20....
5的倍数的共同点是：除以5的余数为0
不是5的倍数的'''
for item in range (1,41):
    if item%5==0:
        print(item)
print('----------使用continue——-----')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)
