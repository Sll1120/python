lst=[103,2,56,90,33]
lst.sort() #调用列表对象的sort函数，默认是升序排列
print(lst)
# 通过指定关键字，指定列表中元素的排序。
lst.sort(reverse=True) #降序排序
print(lst)
lst.sort(reverse=False) #升序排列
print(lst)
