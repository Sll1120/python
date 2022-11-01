# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-22 10:54
# * Filename : file_tell.py
#!/usr/bin/python3
# **********************************************************
#Python3 File tell() 方法
#Python3 File(文件) 方法 Python3 File(文件) 方法
#概述
#tell() 方法返回文件的当前位置，即文件指针当前位置。
#语法
#tell() 方法语法如下：
#fileObject.tell()
#参数
#无
#返回值
#返回文件的当前位置。
#实例
#以下实例演示了 tell() 方法的使用：
#文件 runoob.txt 的内容如下：
#1:www.runoob.com
#2:www.runoob.com
#3:www.runoob.com
#4:www.runoob.com
#5:www.runoob.com
#循环读取文件的内容：
#实例(Python 3.0+)
#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)
line = fo.readline()
print ("读取的数据为: %s" % (line))
# 获取当前文件位置
pos = fo.tell()
print ("当前位置: %d" % (pos))
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名为:  runoob.txt
#读取的数据为: 1:www.runoob.com
#当前位置: 17
