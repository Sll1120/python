# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-19 17:18
# * Filename : os.pardir.py
#!/usr/bin/python3
# **********************************************************
#Python3 os.pardir 方法
#Python3 OS 文件/目录方法 Python3 OS 文件/目录方法
#概述
#os.pardir() 获取当前目录的父目录（上一级目录），以字符串形式显示目录名。
#注意: Windows 和 POSIX 返回 ..。
#语法
#pardir()方法语法格式如下：
#os.pardir
#参数
#无。
#返回值
#返回当前目录的父目录，默认值为 ..。
#实例
#以下实例演示了 pardir() 方法的使用：
#实例
import os
# 输出默认值 ..
print(os.pardir)
#执行以上程序输出结果为：
#..
#打印当前目录的父目录：
#实例
import os
# 当前工作目录
path = os.getcwd()
print("当前工作目录: ", path)
# 父目录
parent = os.path.join(path, os.pardir)
# 父目录
print("\n父目录:", os.path.abspath(parent))
#执行以上程序输出结果为：
#当前工作目录:  /Users/runoob/python
#父目录: /Users/runoob
