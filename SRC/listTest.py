def main():
    x = list(range(8))
    print(x,type(x))

    x2 = list(range(3))
    x.extend(x2)
    print(x,type(x))

    x.insert(0,25)
    print(x,type(x))

    x.pop()
    print(x,type(x))
    x.pop(0)
    print(x,type(x))
    x.pop(1)
    print(x,type(x))
    x.remove(0)
    print(x,type(x))
    print(x[0])
    x[0]  = 68
    print(x,type(x))

if __name__ == '__main__':
    main()
