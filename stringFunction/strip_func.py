#======================================
# file name:strip_func.py
# author:liangliangSu
# date of writing:2022-09-12 11:19
# description:
#======================================
#!/usr/bin/env python3
#Python3 strip()方法
#描述
#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
#注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#语法
#strip()方法语法：
#str.strip([chars]);
#参数
#chars -- 移除字符串头尾指定的字符序_列。
#返回值
#返回移除字符串头尾指定的字符序列生成的新字符串。
#实例
#以下实例展示了 strip() 函数的使用方法：
#实例(Python 3.0+)
#!/usr/bin/python3
str = "*****this is **string** example....wow!!!*****"
print (str.strip( '*' ))  # 指定字符串 *
#以上实例输出结果如下：
#this is **string** example....wow!!!
#从结果上看，可以注意到中间部分的字符并未删除。
#以上下例演示了只要头尾包含有指定字符序列中的字符就删除：
#实例(Python 3.0+)
#!/usr/bin/python3
str = "123abcrunoob321"
print (str.strip( '12' ))  # 字符序列为 12
#以上实例输出结果如下：
#3abcrunoob3
