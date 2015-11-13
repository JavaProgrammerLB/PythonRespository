#open
file = open('liubei.txt','w')
list = []
s = ' liubei daoci yiyou'
list.append(s)
s2 = 'nihaoma'
list.append(s2)
s3 = 'hello world'
list.append(s3)

print(list)
#write
for i in range(len(list)):
    file.write(list[i])
    file.write('\n')
#close
file.close()
