# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-22 11:45
# * Filename : file_write.py
#!/usr/bin/python3
# **********************************************************
#Python3 File write() 方法
#Python3 File(文件) 方法 Python3 File(文件) 方法
#概述
#write() 方法用于向文件中写入指定字符串。
#在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
#如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。
#语法
#write() 方法语法如下：
#fileObject.write( [ str ])
#参数
#str -- 要写入文件的字符串。
#返回值
#返回的是写入的字符长度。
#实例
#文件 runoob.txt 的内容如下：
#1:www.runoob.com
#2:www.runoob.com
#3:www.runoob.com
#4:www.runoob.com
#5:www.runoob.com
#以下实例演示了 write() 方法的使用：
#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名: ", fo.name)
str = "6:www.runoob.com"
# 在文件末尾写入一行
fo.seek(0, 2)
line = fo.write( str )
# 读取文件所有内容
fo.seek(0,0)
for index in range(6):
    line = next(fo)
    print ("文件行号 %d - %s" % (index, line))
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件行号 0 - 1:www.runoob.com
#文件行号 1 - 2:www.runoob.com
#文件行号 2 - 3:www.runoob.com
#文件行号 3 - 4:www.runoob.com
#文件行号 4 - 5:www.runoob.com
#文件行号 5 - 6:www.runoob.com
#查看文件内容：
#$ cat runoob.txt 
#1:www.runoob.com
#2:www.runoob.com
#3:www.runoob.com
#4:www.runoob.com
#5:www.runoob.com
#6:www.runoob.com
