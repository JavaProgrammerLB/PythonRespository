def main():
    list = [1,2]
    for i in range(0,100,1):
        list.append(list[i]list[i+1])
        if list[i] > 4000000:
            print(i-1,list[i-1])
            break
    

if __name__ == '__main__':
    main()