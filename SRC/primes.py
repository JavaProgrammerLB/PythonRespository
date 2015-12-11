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

def is_prime(number):
    """Return True if *number* is prime."""
    if number > 1:
        for element in range(2,number):
            if number % element == 0:
                return False
        return True
    elif number <= 1:
        return False

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)

if __name__ == '__main__' :
    print('start')
    main()
