#第一种集合创建方式
s={'python','hello',1,1,2,3,3} #集合中的元素不允许重复的
print(s)
# 第二种集合创建方式，使用内置函数set()
s1=set(range(6))
print(s1)
print(set([3,4,53,56,3])) #集合中的元素不允许重复的
print(set((30,44,43,435)))
print(set('python')) #集合中的的元素是无序的
print(set({123,34,5,6}))
print(set())