s='hello,python,python,python'
print(s.replace('python','java')) #默认替换遍历元素
print((s.replace('python','java',1))) #指定替换第一个
print((s.replace('python','java',2)))
t=['hello','java','python']
print(''.join(t))
print('|'.join(t))
r=('hello','java','python')
print(''.join(r))
print('-'.join(r))


