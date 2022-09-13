s='苏亮亮'
#编码，定义编码格式
print(s.encode(encoding='GBK')) #gbk编码格式中，一个中文占用两个字节 b'\xcb\xd5\xc1\xc1\xc1\xc1'六个字节
print(s.encode(encoding='UTF-8')) #utf-8编码格式中，一个中文占用三个字节 b'\xe8\x8b\x8f\xe4\xba\xae\xe4\xba\xae'九个字节
#解码
#byte代表就是一个二进制数据（字节类型数据）
byte=s.encode(encoding='GBK') #编码
print(byte.decode(encoding='GBK')) #解码
byte=s.encode(encoding='UTF-8')#编码
print(byte.decode(encoding='UTF-8'))#解码