def fun(a,b):
    c=a+b #c就是局部变量，因为c在函数体内进行定义的变量，a,b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)
# print(c) 因为a,c超出了起作用的范围（超出了作用域）
# print(a)
name='sll' #name的作用范围为函数内部和外部都可以使用-->成为全局变量
print(name)
def fun2():
    print(name)
fun2() #调用函数
print('----------------')
def fun3():
    global age #函数内部定义的变量，局部变量，局部变量使用global声明，这个变量才能生效全局变量。
    age=20
    print(age)
fun3()
print(age) 

