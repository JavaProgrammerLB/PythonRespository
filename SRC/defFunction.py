def main():
    print('hello')
    f1(1,1)
    
def f1(*args):
    print(args[0])
    print(args[1])
    print(type(args))

if __name__ == '__main__':
    main()