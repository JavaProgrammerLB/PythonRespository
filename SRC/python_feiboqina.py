def main():
    list = [1,2]
    for i in range(0,4000000,1):
        value = list[i] + list[i + 1]
        list.append(value)
        if(list[i] > 4000000):
            print(list[i],i)
            print(list[i - 1], i-1)
            break
if __name__ == '__main__':
    main()
