#!/usr/bin/env python3
#======================================
# file name:file_isatty方法.py
# author:liangliangSu
# date of writing:2022-09-18 20:18
#======================================
#Python3 File isatty() 方法
#Python3 File(文件) 方法 Python3 File(文件) 方法
#概述
#isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。
#语法
#isatty() 方法语法如下：
#fileObject.isatty(); 
#参数
#返回值
#如果连接到一个终端设备返回 True，否则返回 False。
#实例
#以下实例演示了 isatty() 方法的使用：
#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "wb")
print ("文件名为: ", fo.name)
ret = fo.isatty()
print ("返回值 : ", ret)
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名为:  runoob.txt
#返回值 :  False
