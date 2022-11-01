print('两个集合相等，即元素相等。')
s1={10,20,30}
s2={10,20,30}
print(s1==s2) #True
print(s1!=s2) #false
print('一个集合是否是另一个集合的子集')
s3={1,3,4,5,6}
s4={1,4,5,9}
s5={1,2,3,4,5,6}
print(s3.issubset(s5)) #True  说明，is:是  subset:意思是子集
print(s4.issubset(s5)) #false
print(' 一个集合是否是另一个集合的超集')
print(s5.issuperset(s3)) #True  说明，superset:意思是超集，父集
print(s5.issuperset(s4)) #false
print('两个集合是否含有交集')
print(s3.isdisjoint(s4)) #False  说明， disjoint：意思是不相交
s6={100,200,300}
print(s5.isdisjoint(s6)) #True
