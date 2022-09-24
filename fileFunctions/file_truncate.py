# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-22 11:27
# * Filename : file_truncate方法.py
#!/usr/bin/python3
# **********************************************************
#Python3 File truncate() 方法
#Python3 File(文件) 方法 Python3 File(文件) 方法
#概述
#truncate() 方法用于从文件的首行首字节开始截断，截断文件为 size 个字节，无 size 表示从当前位置截断；截断之后 V 后面的所有字节被删除，其中 Widnows 系统下的换行代表2个字节大小。 。
#语法
#truncate() 方法语法如下：
#fileObject.truncate( [ size ])
#参数
#size -- 可选，如果存在则文件截断为 size 字节。
#返回值
#该方法没有返回值。
#实例
#以下实例演示了 truncate() 方法的使用：
#文件 runoob.txt 的内容如下：
#1:www.runoob.com
#2:www.runoob.com
#3:www.runoob.com
#4:www.runoob.com
#5:www.runoob.com
#循环读取文件的内容：
#!/usr/bin/python3
fo = open("runoob.txt", "r+")
print ("文件名: ", fo.name)
line = fo.readline()
print ("读取行: %s" % (line))
fo.truncate()
line = fo.readlines()
print ("读取行: %s" % (line))
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名:  runoob.txt
#读取行: 1:www.runoob.com
#读取行: ['2:www.runoob.com\n', '3:www.runoob.com\n', '4:www.runoob.com\n', '5:www.runoob.com\n']
#以下实例截取 runoob.txt 文件的10个字节：
#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)
# 截取10个字节
fo.truncate(10)
str = fo.read()
print ("读取数据: %s" % (str))
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名为:  runoob.txt
#读取数据: 1:www.runo
