print('applle'>'app') #Ture
print('apple'>'banan') #False
print(ord('a'),ord('b'))
print((ord('苏')))
print(chr(97),chr(98))
print(chr(33487))
'''==与is的区别 
==比较的是value
is比较的是id'''
a=b='python'
c='python'
print(a==b) #True
print(a==c) #True
print(a is b)#True
print(a is c) #True
print(id(a)) #2337643651952
print(id(b)) #2337643651952
print(id(c)) #2337643651952