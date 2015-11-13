a=2
print(a**2)
print(a**3)

square=[]
for i in range(10):
    square.append(i**2)

print(square.__len__())
print(len(square))
for a in range(square.__len__()):
    print(str(square[a]))