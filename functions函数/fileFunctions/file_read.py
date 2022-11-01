# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-21 12:34
# * Filename : file_read.py
#!/usr/bin/python3
# **********************************************************
#Python3 File read() 方法
#Python3 File(文件) 方法 Python3 File(文件) 方法
#概述
#read() 方法用于从文件读取指定的字符数（文本模式 t）或字节数（二进制模式 b），如果未给定参数 size 或 size 为负数则读取文件所有内容。
#语法
#read() 方法语法如下：
#fileObject.read([size]); 
#参数
#size -- 从文件中读取的字符数（文本模式）或字节数（二进制模式），默认为 -1，表示读取整个文件。
#返回值
#返回从字符串中读取的字节。
#实例
#以下实例演示了 read() 方法的使用：
#文件 runoob.txt 的内容如下：
#这是第一行
#这是第二行
#这是第三行
#这是第四行
#这是第五行
#循环读取文件的内容：
#实例
#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)
line = fo.read(-1)
print ("读取的字符串: %s" % (line))
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名为:  runoob.txt
#读取的字符串: 这是第一行
#这是第二
