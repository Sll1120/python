# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-21 15:51
# * Filename : file_seek方法.py
#!/usr/bin/python3
# **********************************************************
#Python3 File seek() 方法
#Python3 File(文件) 方法 Python3 File(文件) 方法
#概述
#seek() 方法用于移动文件读取指针到指定位置。
#语法
#seek() 方法语法如下：
#fileObject.seek(offset[, whence])
#参数
#offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
#whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
#返回值
#如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
#实例
#以下实例演示了 seek() 方法的使用：
#实例
#>>> f = open('workfile', 'rb+')
#>>> f.write(b'0123456789abcdef')
#16
#>>> f.seek(5)      # 移动到文件的第六个字节
#5
#>>> f.read(1)
#b'5'
#>>> f.seek(-3, 2)  # 移动到文件倒数第三个字节
#13
#>>> f.read(1)
#b'd'
#文件 runoob.txt 的内容如下：
#1:www.runoob.com
#2:www.runoob.com
#3:www.runoob.com
#4:www.runoob.com
#5:www.runoob.com
#循环读取文件的内容：
#实例
#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)
line = fo.readline()
print ("读取的数据为: %s" % (line))
print ('(1)------------------------------------------')
# 重新设置文件读取指针到开头
fo.seek(0, 0)
line = fo.readline()
print ("读取的数据为: %s" % (line))
print ('(2)------------------------------------------')
# 重新设置文件读取指针到开头
fo.seek(1, 0)
line = fo.readline()
print ("读取的数据为: %s" % (line))
print ('(3)------------------------------------------')
# 重新设置文件读取指针到开头
fo.seek(0, 1)
line = fo.readline()
print ("读取的数据为: %s" % (line))
print ('(4)------------------------------------------')
# 重新设置文件读取指针到开头
fo.seek(0, 2)
line = fo.readline()
print ("读取的数据为: %s" % (line))
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名为:  runoob.txt
#读取的数据为: 1:www.runoob.com
#读取的数据为: 1:www.runoob.com
