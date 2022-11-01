# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-23 18:41
# * Filename : os_chroot.py
#!/usr/bin/python3
# **********************************************************
#Python3 os.chroot() 方法
#Python3 OS 文件/目录方法 Python3 OS 文件/目录方法
#概述
#os.chroot() 方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。
#在 unix 中有效。
#语法
#chroot()方法语法格式如下：
#os.chroot(path);
#参数
#path -- 要设置为根目录的目录。
#返回值
#该方法没有返回值。
#实例
#以下实例演示了 chroot() 方法的使用：
#!/usr/bin/python3
import os, sys
# 设置根目录为 /tmp
os.chroot("/tmp")
print ("修改根目录成功!!")
#执行以上程序输出结果为：
#修改根目录成功!!
