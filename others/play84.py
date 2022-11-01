s='hello,python'
s1=s[:5] #没有指定起始位置，默认起始0
s2=s[6:] #没有指定结束位置，默认到尾
s3='!'
newstr=s1+s2+s3
print(s1,id(s1))
print(s2,id(s2))
print(s3,id(s3))
print(newstr,id(newstr))
print('--------切片[start,end,step]---------')
print(s[1:5:1]) #从一开始截止到五，步长是一
print(s[::2]) #起始默认，默认从0开始，默认到最后一个元素，步长是2
print(s[::-1]) #默认从最后一个元素开始，到一个元素结束，因为步长是负数
print(s[-6::1]) #默认从索引-6开始到最后一个元素，步长是1
