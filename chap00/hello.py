#======================================
# file name:var.py
# author:liangliangSu
# date of writing:2022-09-04 17:28
# description:
#======================================
#!/usr/bin/python3
print("可打印数字")
print(88)
print(34.4)
print(1.2345e4)
print('可打印字符串')
print('suliangliang')
print('可输出运算符的表达式')
print(3+4)
print(3*2)
print(9-3)
print(9/3)
print('#转义符的作用')
print('hello \nworld') #转义功能首字母，n代表newline表示换行的意思
print('hello \tworld') #水平制表符
print('hello \bworld') #退格
print('hello \rworld') #覆盖之前的
print('https:\\\\www.baidu.com')
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print('打印类型')
print(type(1)) #int
print(type(True)) #bool
print(type(1.23)) #float
print(type(1+2j)) #complex 复合的意思
print('字符串切片&分片')
str='liangliangsu'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
print(str * 2)  # 输出字符串两次
print(str + '你好','\n')  # 连接字符串

i = 5
print (i)
i = i + 1
print (i)
print('hello,world!')
print('# 这里的内容是一个注释')
print('''
这是多行注释，使用单引号。
这是多行注释，使用单引号。''')
print("""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
""" )

what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro,'\n')

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print(counter)
print(miles)
print(name,'\n')

a, b, c = 1, 2, "john"
print(a),print(b),print(c,'\n')

str = 'Hello World!'
print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST",'\n')  # 输出连接的字符串

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)    # 输出完整列表
print(list[0])    # 输出列表的第一个元素
print(list[1:3])    # 输出第二个至第三个元素
print(list[2:])    # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)    # 输出列表两次
print(list + tinylist,'\n')    # 打印组合的列表

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print(tuple)   # 输出完整元组
print(tuple[0])   # 输出元组的第一个元素
print(tuple[1:3])   # 输出第二个至第四个（不包含）的元素
print(tuple[2:])   # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)   # 输出元组两次
print(tuple + tinytuple,'\n')   # 打印组合的元组

#tuple[2] = 1000    # 元组中是非法应用
list[1] = 1000     # 列表中是合法应用
print(list,'\n')

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'liangliangsu','high':170, 'heavy': '55kg'}
print(dict['one']      )    # 输出键为'one' 的值
print(dict[2]          )    # 输出键为 2 的值
print(tinydict         )    # 输出完整的字典
print(tinydict.keys()  )    # 输出所有键
print(tinydict.values(),'\n')    # 输出所有值

a = 21
b = 10
c = 0
c = a + b
print ("1c的值为：", c)
c = a - b
print ("2c的值为：", c)
c = a * b
print ("3c的值为：", c)
c = a / b
print ("4c的值为：",int(c))
print(type(int(c)))
c = a % b
print ("5c的值为：", c)
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print ("6c的值为：", c)
a = 10
b = 5
c = a//b
print ("7c的值为：", c)
