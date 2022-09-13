#判定字符串
s='hello python'
r='su'
t='苏亮亮'
print('1:',s.isidentifier()) #False
print('2:',r.isidentifier()) #True #isidentifier判定字符串是否合法的标识符
print('3:',t.isidentifier()) #True
print('4:','zangsan_2'.isidentifier()) #True
print('5:','lisi-1'.isidentifier()) #False
print('6:','\t'.isspace()) # isspace #判定指定的字符串是否全部由空白字符组成（回车，换行，水平制表符等）
print('7:','Abc'.isalpha()) #isalpha #判定指定的字符串是否全部由字母组成
print('9:','129四'.isnumeric()) #判断指定字符串是否全部由数字组成
print('11:','ⅠⅡⅢⅣⅤⅥⅦⅧⅨ'.isnumeric()) #isnumeric判断指定字符串是否全部由数字组成
print('12','adb22'.isalnum()) #isalnum判定指定字符串是否全部由字母和数字组成
print('13','asd23_'.isalnum()) #False
