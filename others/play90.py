# print(bool(0)) #False
# print(bool(4)) #True
def fun(num):
    odd=[]
    even=[]
    for i in num:
         if i%2:
             odd.append(i)
         else:
             even.append(i)
    return odd,even
list1=[10,29,34,23,44,53,56]
print(fun(list1))
'''函数的返回值情况
1)，如果函数没有返回值[函数执行完后，不需要给调用处提供数据] return可以省略不写；
2)，函数返回值如果是一个，直接返回类型；
3)，函数返回值如果是多个，返回的结果是元组。
'''
def fun1():
    print('hello') #1)如果函数没有返回值[函数执行完后，不需要给调用处提供数据] return可以省略不写
    return
fun1()
def fun2(): #2)函数返回值如果是一个，直接返回类型；
    return 'word'
print(fun2())
def fun3():
    return 'hello','word'
print(fun3()) #3)函数返回值如果是多个，返回的结果是元组。

