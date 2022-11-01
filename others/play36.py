'''第一种创建方式，只有一个参数（小括号只有一个参数)'''
r=range(10) #[0,1,2,3,4,5,6,7,8,9,] 默认从0开始，默认步长是1
print(r) #range(0,10)
print(list(r)) #list用于查看range对象中的整数序列
'''第二种方式，给两个参数（小括号有两个参数）'''
s=range(1,10) #指定起始值，从1开始，到10结束（不包含10），默认步长是1
print(list(s))

'''第三中创建方式，给了三个参数（小阔号中给是哪个参数'''
t=range(1,10,2)
print(list(t))

'''判定指定的整数 在序列中是否存在，使用 in not in'''
print(10 in r) #False
print(9 in r) #True
print(10 not in s) #True
print(9 not in s) #True
print(list(range(1,20,1)))
print(list(range(1,101,3)))