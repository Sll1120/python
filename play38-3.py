sum=0 #用于存储偶数和
for l in range(1,101):
    if l%2!=0: #条件执行体 if bool(l%2):
        sum+=l
    l+=1
print('1到100之间的奇数之和是：',sum)
