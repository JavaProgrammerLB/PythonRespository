def interval(start,stop=None,step=1):
    print(stop is None)
    if stop is None:
        start,stop = 0 ,start
        print(start,stop)
    result =[]
    print(result)
    i = start
    while i < stop:
        result.append(i)
        i +=step
    print (result)

def main():
    interval(10)

if __name__ == '__main__':
    main()
