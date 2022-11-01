# 字符串的查询操作
s = 'hello,hello,hello'
print(s.find('lo'))  # 3
print(s.rfind('lo'))  # 15
print(s.index('lo'))  # 3
print(s.rindex('lo'))  # 15
print(s.find('k'))  # 不存在返回-1
# print(s.index('k')) #不存在返回 ValueError: substring not found
