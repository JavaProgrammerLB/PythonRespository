for i in range(2,100,1):
    for j in range(2,i,1):
        if i % j == 0:
            #print(i,j)
            break
    else:
        print(i)
