s='hello world python su'
lst=s.split()
print(lst)
print('1----------------------------')
s1='hello|world|python|su'
print(s1.split())
print(s1.split(sep='|')) #sep=''是移除冗繁符号' | '的作用 ————>从左至右
print(s1.split(sep='|',maxsplit=1)) #maxsplit=1 是最大劈分次数1
print(s1.split(sep='|',maxsplit=2))
print('2----------------------------')
print(s1.rsplit(sep='|',maxsplit=1)) #sep=''是移除冗繁符号' | '的作用 ————>从右至左
print(s1.rsplit(sep='|',maxsplit=2))
print(s1.rsplit(sep='|',maxsplit=3))
