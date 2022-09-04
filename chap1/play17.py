#数据类型转换
name='sulianglaing'
age=30
age1=str(age)
print(type(name),type(age))
print(age1,type(age1))
print('我叫'+name+'今年，'+age1+'岁')
print('我叫'+name+'今年，'+str(age)+'岁')
# print('我叫'+name+'今年，'+age+'岁')
'''ModuleNotFoundError: No module named 'keyworld'当str和int类型进行组合时，报错，解决方案是类型转化一致'''
print('------str()将其他类型转化成str类型--------')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
print('------int()将其他类型转化成int类型--------')
s1='128'
s2=98.7
s3='76.77'
s4=True
s5='hello'
print(type(s1),type(s2),type(s3),type(s4),type(s5))
print(int(s1)) #str是数字串可转化成int型。
print(int(s2),type(int(s2)))#str是数字串可转化成int型，不然会报错。
print(int(s4),type(int(s4)))
# print(int(s3),type(int(s3))) #将str转化成int类型，报错，因为字符串是小数串

