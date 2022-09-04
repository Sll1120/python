#转义符的作用
print('hello \nworld') #转义功能首字母，n代表newline表示换行的意思
print('hello \tworld') #水平制表符
print('hello \bworld') #退格
print('hello \rworld') #覆盖之前的
print('https:\\\\www.baidu.com')
print(r'hello \nworld') #不希望转义符起作用，就在前面加r或是R
print('hello \nworld')
#打印类型
print(type(1)) #int
print(type(True)) #bool
print(type(1.23)) #float
print(type(1+2j)) #complex 复合的意思

print('----------完美分割线--------')
str='Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('----------完美分割线--------')
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
