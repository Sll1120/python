#元组的第一种创建方式()
t1=('hello','world','python',100)
print(t1,type(t1))
#元组的第二种创建方式,使用tuple()
t2=tuple(('hello','world','python',200))
print(t2,type(t2))
t3='apple','banan','orange'
print(t3,type(t3))
t4=('red',) #只有一个元组的时候要加上 逗号和小括号，不然打印的类型是字符串型str
print('t4',type(t4))
#空列表的创建
lst1=[]
lst2=list()
print('空列表',lst1,lst2)
#空字典的创建
dic1={}
dic2=dict()
print('空字典',dic1,dic2)
#空元组的创建
tuple1=()
tuple2=tuple()
print('空元组',tuple1,tuple2)

