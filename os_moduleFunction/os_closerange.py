#!/usr/bin/env python3
#======================================
# file name:os_closerange.py
# author:liangliangSu
# date of writing:2022-09-24 13:06
#======================================
#Python3 os.closerange() 方法
#Python3 OS 文件/目录方法 Python3 OS 文件/目录方法
#概述
#os.closerange() 方法用于关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。
#语法
#closerange()方法语法格式如下：
#os.closerange(fd_low, fd_high);
#参数
#fd_low -- 最小文件描述符
#fd_high -- 最大文件描述符
#该方法类似于：
#for fd in xrange(fd_low, fd_high):
#    try:
#        os.close(fd)
#    except OSError:
#        pass
#返回值
#该方法没有返回值。
#实例
#以下实例演示了 closerange() 方法的使用：
#!/usr/bin/python3
import os, sys
# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
# 写入字符串
os.write(fd, "This is test")
# 关闭文件
os.closerange( fd, fd)
print ("关闭文件成功!!")
#执行以上程序输出结果为：
#关闭文件成功!!
