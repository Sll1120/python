t=(10,[20,30],9)
print(t,type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

#尝试把[1]修改成100
print(id(100))
# t[1]=100 #元组是不允许修改元素的
t[1].append(100)
print(t,id(t[1]))
