#格式化字符串
#1, %占位符
name='汤姆'
age=20
print('我叫%s,今年%d岁' %(name,age))
# 2,{}
print('我叫{0},今年{1}岁'.format(name,age))
# 3,f-string
print(f'我叫{name},今年{age}岁')
print('----------完美分割线---------')
print('%10d' %99) #10表示字符的宽度
print('hellohello') #10表示宽度字符
print('%.3f' %3.1415926) #3表示是小数点后三位
print('%10.3f' %3.1415926) #表示字符宽度10，小数点精确到三位。