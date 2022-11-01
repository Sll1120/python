#列表的生成公式
list1=[i*i for i in range(10)]
print(list1)
list1.reverse() #列表是有序的，可排序操作。
print(list1)
# 集合生成公式
dict1={j*j for j in range(0,10,1)} #注意默认值缺省的写法，看上面的list1写法
print(dict1) #字典是无需的，没有排序操作，不支持排序函数


