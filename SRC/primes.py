def main():
    primes()

def primes():
    n = 20
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                print('%d is not primes'%i)
                #print('i // %d = 0'%j)
                #yield
        #else:
                #print('i is a prime')
    print('end')

if __name__ == '__main__' :
    print('start')
    main()