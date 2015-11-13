import re
s = 'which foot or hand fall fastest'
#print(type(re.findall(r'\bf[a-z]*',s)))
list = re.findall(r'\bfoot[a-z]*',s)
if len(list) == 0 :
    print('list为空')
else :
    print('s是：',s)
    print(list)
    s2 = s.replace('foot ','print(')
    print('s2是',s2)
    print('s是',s)
