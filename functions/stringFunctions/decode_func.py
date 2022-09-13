#======================================
# file name:bytes.decode_func.py
# author:liangliangSu
# date of writing:2022-09-11 23:53
# description:
#======================================
#!/usr/bin/env python3
#Python3 bytes.decode()方法
#Python3 字符串 Python3 字符串
#描述
#decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
#语法
#decode()方法语法：
#bytes.decode(encoding="utf-8", errors="strict")
#参数
#encoding -- 要使用的编码，如"UTF-8"。
#errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
#返回值
#该方法返回解码后的字符串。
#实例
#以下实例展示了decode()方法的实例：
#实例(Python 3.0+)
#!/usr/bin/python3
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
#以上实例输出结果如下：
#菜鸟教程
#UTF-8 编码： b'\xe8\x8f\x9c\xe9\xb8\x9f\xe6\x95\x99\xe7\xa8\x8b'
#GBK 编码： b'\xb2\xcb\xc4\xf1\xbd\xcc\xb3\xcc'
#UTF-8 解码： 菜鸟教程
#GBK 解码： 菜鸟教程

#UTF-8 和 GBK 的区别
#先给结论：现在基本都用 UTF-8，建议采用这个。
#GB 指代的“国标”，即“国家标准”。
#UTF-8 是一种国际化的编码方式，包含了世界上大部分的语种文字（简体中文字、繁体中文字、英文、日文、韩文等语言），也兼容 ASCII 码。
#GBK 是在国家标准 GB2312 基础上扩容后兼容 GB2312 的标准（好像还不是国家标准），专门用来解决中文编码的，是双字节的，不论中英文都是双字节的。
#UTF－8 编码是用以解决国际上字符的一种多字节编码，它对英文使用 8 位（即一个字节），中文使用 24 位（三个字节）来编码。
#对于英文字符较多的论坛则用 UTF－8 节省空间。
#另外，如果是外国人访问你的 GBK 网页，需要下载中文语言包支持。访问 UTF-8 编码的网页则不出现这问题，可以直接访问。
#GBK 包含全部中文字符。
#UTF-8 则包含全世界所有国家需要用到的字符。
