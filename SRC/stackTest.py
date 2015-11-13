def printListByElement(list):
    print('list共有%d个元素'%len(list))
    for i in range(len(list)):
        print('list的第%d个元素为：%d' %(i,list[i]))

list = [1,2,3,4]

print('遍历list:')
printListByElement(list)
print('')

print('入栈')
list.append(233)
printListByElement(list)
print()

while len(list) > 0 :
    print('出栈')
    list.pop()
    printListByElement(list)
    print()
