#!/usr/bin/env python3
#======================================
# file name:os_dup.py
# author:liangliangSu
# date of writing:2022-09-24 13:10
#======================================
#Python3 os.dup() 方法
#Python3 OS 文件/目录方法 Pyth_on3 OS 文件/目录方法
#概述
#os.dup() 方法用于复制文件描述符 fd。
#语法
#dup()方法语法格式如下：
#os.dup(fd);
#参数
#fd -- 文件描述符
#返回值
#返回复制的文件描述符。
#实例
#以下实例演示了 dup() 方法的使用：
#实例(Python 3.0+)
#!/usr/bin/python3
import os, sys
# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
# 复制文件描述符
d_fd = os.dup( fd )
# 使用复制的文件描述符写入文件
os.write(d_fd, "This is test".encode())
# 关闭文件
os.closerange( fd, d_fd)
print ("关闭所有文件成功!!")
#执行以上程序输出结果为：
#关闭所有文件成功!!
