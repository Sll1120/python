s1='hello,Yama,suliangliang'
s2=s1.upper() #把字符串中所有的小写字母转化成大写字母a-A
print(s2,id(s2))
s3=s1.lower() #把字符串中的所有大写字母转化成小写字母A-a
print(s3,id(s3))
s4=s1.swapcase() #把字符串中所有的大写转化成小写A-a,小写转化成大写a-A
print(s4)
s5=s1.capitalize() #打第一个字符转化成大写，其余的字符转化成小写。
print(s5)
s6='hello,liangliang'
s7=s1.title() #把每个单词的第一个字符转化成大写，把每个单词剩余的字符转化成小写。
print(s7)