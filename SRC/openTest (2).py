fh=open('lines.txt')
for line in fh.readlines():
    print(line)
    print('华丽的分割线','-------------')
    print(line,end="")
print('liubei')
print(type(fh))
