import os

print('Operate System name:',os.name)
print('Now directory:',os.getcwd())
s = os.getcwd()
print(s)
print(type(s))
l = os.listdir(os.getcwd())
print(l)
print(type(l))
l2 = os.listdir('d:\Music')
print(l2)
va = os.system('dir')
print(type(va))
print(va)
