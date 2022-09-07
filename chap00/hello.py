#======================================
# file name:var.py
# author:liangliangSu
# date of writing:2022-09-04 17:28
# description:
#======================================
#!/usr/bin/python3
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
print(artist_intro)

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print(counter)
print(miles)
print(name)

a, b, c = 1, 2, "john"
print(a),print(b),print(c)
