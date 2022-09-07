#1，交集操作
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1&s2) #intersection()与 & 等价为交集功能
#2,并集操作
print(s1.union(s2))
print(s1|s2) #union()与 | 等价为并集功能
#3,差集操作
print(s1.difference(s2))
print(s1-s2) #difference()与 - 等价为差集功能
#4，对称差集
print(s1.symmetric_difference(s2))
print(s1^s2) #symmetric_difference()与 ^ 等价为对称差集功能 即是两个集合不相同的元素
